#!/usr/bin/env python3
"""Mirror the public pages and static files of psychogra.pl."""

from __future__ import annotations

import hashlib
import html
import html.parser
import json
import mimetypes
import os
import posixpath
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import deque


BASE_URL = "https://psychogra.pl/"
ROOT = os.path.dirname(os.path.abspath(__file__))
ASSET_HOSTS = {"fonts.googleapis.com", "fonts.gstatic.com", "psychogra.s3.amazonaws.com"}
IGNORED_PATHS = (
    "/wp-admin/",
    "/wp-login.php",
    "/wp-json/",
    "/xmlrpc.php",
    "/feed/",
    "/comments/feed/",
)
IGNORED_QUERY_KEYS = {
    "add-to-cart",
    "preview",
    "preview_id",
    "preview_nonce",
    "replytocom",
    "s",
}
TRACKING_QUERY_KEYS = {"cb", "cache", "nocache", "ver", "version", "x"}
MAX_URLS = 5000
USER_AGENT = "Mozilla/5.0 (compatible; PsychograStaticMirror/1.0)"


class PageParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.references: list[tuple[str, str]] = []
        self.css: list[tuple[str, str]] = []
        self.base_url: str | None = None
        self.in_style = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "base" and values.get("href"):
            self.base_url = values["href"]
        for name in ("href", "src", "poster", "action", "formaction", "data"):
            value = values.get(name)
            if value:
                self.references.append((name, value))
        if values.get("srcset"):
            self.references.append(("srcset", values["srcset"]))
        if values.get("style"):
            self.css.append(("inline", values["style"]))
        if tag == "style":
            self.in_style = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "style":
            self.in_style = False

    def handle_data(self, data: str) -> None:
        if self.in_style:
            self.css.append(("inline", data))


def normalize_url(url: str, base: str = BASE_URL) -> str | None:
    value = url.strip().replace('\\"', '"').replace("\\'", "'").replace("\\", "").strip().strip("\"'")
    if value.lower().startswith("%22") and value.lower().endswith("%22"):
        value = value[3:-3]
    resolved = urllib.parse.urljoin(base, value)
    parsed = urllib.parse.urlsplit(resolved)
    host = (parsed.hostname or "").lower()
    if parsed.scheme not in {"http", "https"} or not host:
        return None
    if host not in {"psychogra.pl", "www.psychogra.pl"} | ASSET_HOSTS:
        return None
    scheme = "https" if host in {"psychogra.pl", "www.psychogra.pl"} else parsed.scheme

    path = urllib.parse.quote(urllib.parse.unquote(parsed.path or "/"), safe="/%:@!$&'()*+,;=-._~")
    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    query = [
        (key, value)
        for key, value in query
        if key.lower() not in TRACKING_QUERY_KEYS
        and not (
            host in {"psychogra.pl", "www.psychogra.pl"}
            and re.fullmatch(r"x\d+", key.lower())
        )
    ]
    if any(key.lower() in IGNORED_QUERY_KEYS for key, _ in query):
        return None
    query.sort()
    netloc = host
    if parsed.port and parsed.port not in {80, 443}:
        netloc += f":{parsed.port}"
    return urllib.parse.urlunsplit((scheme, netloc, path, urllib.parse.urlencode(query), ""))


def is_site_url(url: str) -> bool:
    host = urllib.parse.urlsplit(url).hostname
    return host in {"psychogra.pl", "www.psychogra.pl"}


def is_asset_url(url: str, reference_kind: str = "") -> bool:
    parsed = urllib.parse.urlsplit(url)
    path = parsed.path.lower()
    ext = posixpath.splitext(path)[1]
    if is_site_url(url):
        return not any(path.startswith(prefix) for prefix in IGNORED_PATHS)
    return parsed.hostname in ASSET_HOSTS and path not in {"", "/"} and (
        reference_kind in {"href", "src", "poster", "data"}
        or ext in {
            ".css", ".eot", ".gif", ".ico", ".jpeg", ".jpg", ".js", ".png",
            ".svg", ".ttf", ".webp", ".woff", ".woff2",
        }
    )


def should_skip(url: str) -> bool:
    parsed = urllib.parse.urlsplit(url)
    path = parsed.path.lower()
    return any(path.startswith(prefix) for prefix in IGNORED_PATHS) or path.endswith(
        ("/trackback/", "/wp-comments-post.php")
    )


def fetch(url: str) -> tuple[bytes, str, str]:
    last_error: Exception | None = None
    for attempt in range(3):
        request = urllib.request.Request(
            url,
            headers={"User-Agent": USER_AGENT, "Accept": "*/*"},
        )
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                final_url = normalize_url(response.geturl())
                if not final_url:
                    raise RuntimeError(f"Unexpected redirect outside allowed hosts: {response.geturl()}")
                return response.read(), response.headers.get_content_type(), final_url
        except urllib.error.HTTPError as error:
            if error.code in {404, 410}:
                raise
            last_error = error
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            last_error = error
        if attempt < 2:
            time.sleep(1 + attempt)
    assert last_error is not None
    raise last_error


def discover_sitemaps() -> list[str]:
    sitemap_queue = deque([urllib.parse.urljoin(BASE_URL, "/wp-sitemap.xml")])
    pages: list[str] = []
    visited: set[str] = set()
    while sitemap_queue:
        sitemap = sitemap_queue.popleft()
        if sitemap in visited:
            continue
        visited.add(sitemap)
        try:
            content, _, _ = fetch(sitemap)
            root = ET.fromstring(content)
        except (urllib.error.HTTPError, ET.ParseError) as error:
            print(f"Could not read sitemap {sitemap}: {error}")
            continue
        for node in root.iter():
            if node.tag.rsplit("}", 1)[-1] != "loc" or not node.text:
                continue
            target = normalize_url(node.text)
            if not target:
                continue
            if target.endswith(".xml") and is_site_url(target):
                sitemap_queue.append(target)
            elif is_site_url(target) and not should_skip(target):
                pages.append(target)
    return pages


def resource_urls(value: str, base: str) -> list[str]:
    result: list[str] = []
    for candidate in value.split(","):
        url_part = candidate.strip().split()
        if url_part:
            target = normalize_url(url_part[0], base)
            if target:
                result.append(target)
    return result


def css_urls(css: str, base: str) -> list[str]:
    found: list[str] = []
    for match in re.finditer(r"url\(\s*(?:['\"](.*?)['\"]|([^)]*?))\s*\)", css, re.I):
        raw = match.group(1) if match.group(1) is not None else match.group(2)
        target = normalize_url(raw.strip(), base)
        if target:
            found.append(target)
    for match in re.finditer(r"@import\s+['\"](.*?)['\"]", css, re.I):
        target = normalize_url(match.group(1), base)
        if target:
            found.append(target)
    return found


def meaningful_query(url: str) -> list[tuple[str, str]]:
    return urllib.parse.parse_qsl(urllib.parse.urlsplit(url).query, keep_blank_values=True)


def local_file_path(url: str, content_type: str, is_page: bool = False) -> str:
    parsed = urllib.parse.urlsplit(url)
    host = (parsed.hostname or "").lower()
    path = urllib.parse.unquote(parsed.path).lstrip("/")
    if is_page:
        if not path:
            path = "index.html"
        elif path.endswith("/"):
            path += "index.html"
        elif not posixpath.splitext(path)[1]:
            path += "/index.html"
        query = meaningful_query(url)
        if query:
            stem, ext = posixpath.splitext(path)
            digest = hashlib.sha256(urllib.parse.urlencode(query).encode()).hexdigest()[:10]
            path = f"{stem}-{digest}{ext}"
    else:
        path = path or "index"
        if path.endswith("/"):
            path += "index"
        stem, ext = posixpath.splitext(path)
        if not ext:
            ext = mimetypes.guess_extension(content_type) or ".bin"
            path = stem + ext
        query = meaningful_query(url)
        if query:
            digest = hashlib.sha256(urllib.parse.urlencode(query).encode()).hexdigest()[:10]
            stem, ext = posixpath.splitext(path)
            path = f"{stem}-{digest}{ext}"
        path = posixpath.join("assets", host, path)
    safe_path = posixpath.normpath(path).lstrip("/")
    if safe_path == ".." or safe_path.startswith("../"):
        raise ValueError(f"Unsafe local path for {url}")
    return safe_path


def relative_reference(target: str, from_file: str) -> str:
    relative = posixpath.relpath(target, posixpath.dirname(from_file) or ".")
    return urllib.parse.quote(relative, safe="/:@!$&'()*+,;=-._~")


def rewrite_css(css: str, base: str, from_file: str, url_map: dict[str, str]) -> str:
    def replace_url(match: re.Match[str]) -> str:
        raw = match.group(1) if match.group(1) is not None else match.group(2)
        target_url = normalize_url(raw.strip(), base)
        if not target_url:
            return match.group(0)
        target_file = url_map.get(target_url)
        if not target_file:
            return match.group(0)
        quote = match.group(0)[match.group(0).find("(") + 1 :].lstrip()[:1]
        quote = quote if quote in {"'", '"'} else ""
        return f"url({quote}{relative_reference(target_file, from_file)}{quote})"

    css = re.sub(r"url\(\s*(?:['\"](.*?)['\"]|([^)]*?))\s*\)", replace_url, css, flags=re.I)

    def replace_import(match: re.Match[str]) -> str:
        target_url = normalize_url(match.group(2), base)
        target_file = url_map.get(target_url or "")
        if not target_file:
            return match.group(0)
        return f"@import {match.group(1)}{relative_reference(target_file, from_file)}{match.group(1)}"

    return re.sub(r"@import\s+(['\"])(.*?)\1", replace_import, css, flags=re.I)


def localize_reference(value: str, base: str, from_file: str, url_map: dict[str, str], kind: str) -> str:
    if kind == "srcset":
        pieces = []
        for candidate in value.split(","):
            tokens = candidate.strip().split()
            if not tokens:
                continue
            target_url = normalize_url(tokens[0], base)
            target_file = url_map.get(target_url or "")
            tokens[0] = relative_reference(target_file, from_file) if target_file else tokens[0]
            pieces.append(" ".join(tokens))
        return ", ".join(pieces)

    target_url = normalize_url(value, base)
    if not target_url:
        return value
    if should_skip(target_url):
        return value
    target_file = url_map.get(target_url)
    if target_file:
        local = relative_reference(target_file, from_file)
    elif is_site_url(target_url):
        guessed_type = mimetypes.guess_type(urllib.parse.urlsplit(target_url).path)[0] or "text/html"
        target_file = local_file_path(target_url, guessed_type, is_page=kind == "href" and guessed_type == "text/html")
        local = relative_reference(target_file, from_file)
    else:
        return value
    fragment = urllib.parse.urlsplit(value).fragment
    return local + (f"#{fragment}" if fragment else "")


def rewrite_html(source: str, source_url: str, page_file: str, url_map: dict[str, str]) -> str:
    scanner = PageParser()
    scanner.feed(source)
    base_url = normalize_url(scanner.base_url, source_url) if scanner.base_url else source_url
    edits: list[tuple[int, int, str]] = []
    line_starts = [0]
    line_starts.extend(match.end() for match in re.finditer("\n", source))

    def position(index: tuple[int, int]) -> int:
        line, column = index
        return line_starts[line - 1] + column

    class Rewriter(PageParser):
        def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
            raw = self.get_starttag_text()
            start = position(self.getpos())
            self._record_tag_edit(raw, start)
            super().handle_starttag(tag, attrs)

        def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
            self.handle_starttag(tag, attrs)

        def handle_data(self, data: str) -> None:
            if self.in_style:
                start = position(self.getpos())
                rewritten = rewrite_css(data, base_url or source_url, page_file, url_map)
                if rewritten != data:
                    edits.append((start, start + len(data), rewritten))
            super().handle_data(data)

        def _record_tag_edit(self, raw: str, start: int) -> None:
            attribute_pattern = re.compile(
                r"(?P<prefix>\s+(?P<name>href|src|poster|action|formaction|data|srcset|style)\s*=\s*)"
                r"(?:(?P<quote>['\"])(?P<quoted>.*?)(?P=quote)|(?P<bare>[^\s>]+))",
                re.I | re.S,
            )

            def replace_attribute(match: re.Match[str]) -> str:
                kind = match.group("name").lower()
                quoted = match.group("quote") is not None
                value = match.group("quoted") if quoted else match.group("bare")
                decoded = html.unescape(value)
                if kind == "style":
                    replacement = rewrite_css(decoded, base_url or source_url, page_file, url_map)
                else:
                    replacement = localize_reference(decoded, base_url or source_url, page_file, url_map, kind)
                if replacement == decoded:
                    return match.group(0)
                escaped = html.escape(replacement, quote=True) if quoted else replacement
                quote = match.group("quote") or ""
                return match.group("prefix") + quote + escaped + quote

            rewritten = attribute_pattern.sub(replace_attribute, raw)
            if rewritten != raw:
                edits.append((start, start + len(raw), rewritten))

    parser = Rewriter()
    parser.feed(source)
    for start, end, replacement in sorted(edits, reverse=True):
        source = source[:start] + replacement + source[end:]
    return source


def save_file(relative_path: str, content: bytes) -> None:
    target = os.path.join(ROOT, *relative_path.split("/"))
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "wb") as output:
        output.write(content)


def cached_asset_path(url: str) -> str | None:
    parsed = urllib.parse.urlsplit(url)
    host = (parsed.hostname or "").lower()
    path = urllib.parse.unquote(parsed.path).lstrip("/") or "index"
    query = meaningful_query(url)
    directory = os.path.join(ROOT, "assets", host, *path.split("/")[:-1])
    basename = path.split("/")[-1]
    stem, ext = posixpath.splitext(basename)

    candidates: list[str] = []
    if basename and ext:
        candidates.append(os.path.join(ROOT, "assets", host, *path.split("/")))
    if query:
        digest = hashlib.sha256(urllib.parse.urlencode(query).encode()).hexdigest()[:10]
        prefix = (stem or "index") + "-" + digest + "."
        if os.path.isdir(directory):
            candidates.extend(
                os.path.join(directory, name)
                for name in os.listdir(directory)
                if name.startswith(prefix)
            )
    if path.endswith("/") or not ext:
        index_dir = os.path.join(ROOT, "assets", host, *path.rstrip("/").split("/"))
        if os.path.isdir(index_dir):
            candidates.extend(
                os.path.join(index_dir, name)
                for name in os.listdir(index_dir)
                if name.startswith("index.")
            )
    for candidate in candidates:
        if os.path.isfile(candidate) and mimetypes.guess_type(candidate)[0] != "text/css":
            return os.path.relpath(candidate, ROOT).replace(os.sep, "/")
    return None


def cached_redirect(url: str, cached_urls: set[str], url_map: dict[str, str]) -> tuple[bytes, str, str] | None:
    class StopRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, request, response, code, message, headers, new_url):
            return None

    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "*/*"})
    try:
        with urllib.request.build_opener(StopRedirect).open(request, timeout=20):
            return None
    except urllib.error.HTTPError as error:
        if error.code not in {301, 302, 303, 307, 308}:
            return None
        location = error.headers.get("Location")
        target = normalize_url(location, url) if location else None
        if not target or target not in cached_urls or target not in url_map:
            return None
        local_path = url_map[target]
        with open(os.path.join(ROOT, *local_path.split("/")), "rb") as cached:
            content = cached.read()
        content_type = mimetypes.guess_type(local_path)[0] or "application/octet-stream"
        return content, content_type, target
    except (urllib.error.URLError, TimeoutError, OSError):
        return None


def main() -> None:
    queue: deque[str] = deque([normalize_url(BASE_URL) or BASE_URL])
    queue.extend(discover_sitemaps())
    seen: set[str] = set()
    url_map: dict[str, str] = {}
    pages: dict[str, tuple[str, str]] = {}
    css_assets: dict[str, tuple[str, str]] = {}
    asset_urls: set[str] = set()
    failures: list[dict[str, str]] = []
    counts = {"pages": 0, "assets": 0, "bytes": 0}
    cached_urls: set[str] = set()
    previous_manifest = os.path.join(ROOT, "mirror-manifest.json")
    if os.path.isfile(previous_manifest):
        with open(previous_manifest, encoding="utf-8") as source:
            previous = json.load(source)
        for old_url, old_path in previous.get("url_map", {}).items():
            cached_url = normalize_url(old_url)
            local_path = os.path.join(ROOT, *old_path.split("/"))
            if (
                cached_url
                and old_path.startswith("assets/")
                and os.path.isfile(local_path)
                and mimetypes.guess_type(local_path)[0] != "text/css"
            ):
                url_map[cached_url] = old_path
                cached_urls.add(cached_url)
        for old_url in previous.get("assets", []):
            cached_url = normalize_url(old_url)
            if cached_url and is_asset_url(cached_url):
                cached_path = cached_asset_path(cached_url)
                if cached_path:
                    url_map[cached_url] = cached_path
                    cached_urls.add(cached_url)
        print(f"Reusing {len(cached_urls)} previously downloaded assets.")

    while queue:
        url = queue.popleft()
        normalized = normalize_url(url)
        if not normalized or normalized in seen or should_skip(normalized):
            continue
        if len(seen) >= MAX_URLS:
            failures.append({"url": normalized, "error": f"Stopped at MAX_URLS={MAX_URLS}"})
            break
        seen.add(normalized)
        try:
            cached_path = url_map.get(normalized) if normalized in cached_urls else None
            if cached_path:
                with open(os.path.join(ROOT, *cached_path.split("/")), "rb") as cached:
                    content = cached.read()
                content_type = mimetypes.guess_type(cached_path)[0] or "application/octet-stream"
                final_url = normalized
            else:
                cached_response = cached_redirect(normalized, cached_urls, url_map)
                if cached_response:
                    content, content_type, final_url = cached_response
                else:
                    content, content_type, final_url = fetch(normalized)
        except urllib.error.HTTPError as error:
            failures.append({"url": normalized, "error": f"HTTP {error.code}"})
            print(f"Failed {normalized}: HTTP {error.code}")
            continue
        except Exception as error:
            failures.append({"url": normalized, "error": str(error)})
            print(f"Failed {normalized}: {error}")
            continue

        canonical = normalize_url(final_url) or normalized
        is_html = content_type in {"text/html", "application/xhtml+xml"}
        relative_path = local_file_path(canonical, content_type, is_page=is_html)
        url_map[normalized] = relative_path
        url_map[canonical] = relative_path
        counts["bytes"] += len(content)
        if is_html:
            text = content.decode("utf-8", errors="replace")
            pages[canonical] = (relative_path, text)
            counts["pages"] += 1
            parser = PageParser()
            parser.feed(text)
            page_base = normalize_url(parser.base_url, canonical) if parser.base_url else canonical
            for kind, value in parser.references:
                refs = resource_urls(value, page_base or canonical) if kind == "srcset" else [normalize_url(value, page_base or canonical)]
                for target in refs:
                    if target and not should_skip(target) and (is_site_url(target) or is_asset_url(target, kind)):
                        queue.append(target)
            for _, css in parser.css:
                queue.extend(css_urls(css, page_base or canonical))
        elif content_type == "text/css" or urllib.parse.urlsplit(canonical).path.lower().endswith(".css"):
            css_assets[canonical] = (relative_path, content.decode("utf-8", errors="replace"))
            asset_urls.add(canonical)
            counts["assets"] += 1
            queue.extend(css_urls(content.decode("utf-8", errors="replace"), canonical))
            save_file(relative_path, content)
        else:
            counts["assets"] += 1
            asset_urls.add(canonical)
            save_file(relative_path, content)
        if counts["pages"] and counts["pages"] % 25 == 0 and is_html:
            print(f"Fetched {counts['pages']} pages and {counts['assets']} assets...")

    sprite_dir = "assets/psychogra.pl/wp-content/plugins/wp-file-upload/vendor/jquery/images"
    if os.path.isdir(os.path.join(ROOT, sprite_dir)):
        for name in os.listdir(os.path.join(ROOT, sprite_dir)):
            if name.startswith("ui-icons_") and name.endswith(".png"):
                missing_url = normalize_url("/images/" + name)
                if missing_url:
                    url_map[missing_url] = f"{sprite_dir}/{name}"
    url_map["https://psychogra.pl/index/index.html"] = "index.html"

    for source_url, (relative_path, content) in css_assets.items():
        save_file(relative_path, rewrite_css(content, source_url, relative_path, url_map).encode("utf-8"))

    for source_url, (relative_path, content) in pages.items():
        save_file(relative_path, rewrite_html(content, source_url, relative_path, url_map).encode("utf-8"))

    failures = [
        failure
        for failure in failures
        if normalize_url(failure["url"]) not in url_map
    ]
    manifest = {
        "source": BASE_URL,
        "pages": sorted(pages),
        "assets": sorted(asset_urls),
        "url_map": url_map,
        "counts": counts,
        "failures": failures,
    }
    save_file("mirror-manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2).encode("utf-8"))
    print(
        f"Mirror complete: {counts['pages']} pages, {counts['assets']} assets, "
        f"{counts['bytes']:,} downloaded bytes, {len(failures)} failed URLs."
    )
    if failures:
        print("See mirror-manifest.json for the failed URL list.")


if __name__ == "__main__":
    main()
