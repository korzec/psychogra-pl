import { cpSync, existsSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import { extname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { defineConfig } from "vite";

const root = fileURLToPath(new URL(".", import.meta.url));
const ignoredDirectories = new Set([".git", ".github", "dist", "node_modules"]);

function findHtmlEntries(directory = root) {
  return readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const path = join(directory, entry.name);
    if (entry.isDirectory()) {
      return ignoredDirectories.has(entry.name) ? [] : findHtmlEntries(path);
    }
    return extname(entry.name).toLowerCase() === ".html" ? [path] : [];
  });
}

function copyStaticAssets() {
  return {
    name: "copy-static-site-assets",
    closeBundle() {
      const assets = resolve(root, "assets");
      const output = resolve(root, "dist");
      if (existsSync(assets)) {
        cpSync(assets, resolve(output, "assets"), {
          recursive: true,
          filter: (path) => {
            const normalized = path.split("\\").join("/");
            return (
              !/\.(apk|zip)$/i.test(path) &&
              !/^.*\/assets\/psychogra\.pl\/download\/[^/]+\.bin$/i.test(normalized)
            );
          },
        });
      }

      // Vite flattens CSS into dist/assets, while this legacy mirror keeps
      // CSS-relative files below dist/assets/psychogra.pl/.
      const outputAssets = resolve(output, "assets");
      for (const file of readdirSync(outputAssets)) {
        if (!file.endsWith(".css")) continue;
        const cssPath = resolve(outputAssets, file);
        const css = readFileSync(cssPath, "utf8");
        const fixedCss = css.replace(/url\((['"]?)wp-content\//g, "url($1psychogra.pl/wp-content/");
        if (fixedCss !== css) writeFileSync(cssPath, fixedCss);
      }
      writeFileSync(resolve(output, ".nojekyll"), "");
    },
  };
}

export default defineConfig({
  // Keep generated URLs relative so the same build works at both the
  // GitHub Pages project path and the root of the reverse-proxied domain.
  base: "./",
  publicDir: false,
  plugins: [copyStaticAssets()],
  server: {
    host: "127.0.0.1",
  },
  build: {
    outDir: "dist",
    emptyOutDir: true,
    rollupOptions: {
      input: findHtmlEntries(),
    },
  },
});
