(() => {
  const siteRoot = new URL(import.meta.env.BASE_URL, window.location.origin);
  const siteUrl = (path) => new URL(path, siteRoot).href;

  const header = `
    <header id="masthead" class="site-header" role="banner">
      <div class="col-full">
        <a class="skip-link screen-reader-text" href="#site-navigation">Przejdź do nawigacji</a>
        <a class="skip-link screen-reader-text" href="#content">Przejdź do treści</a>
        <div class="site-branding">
          <a href="${siteUrl("index.html")}" class="custom-logo-link" rel="home">
            <img width="472" height="110" src="${new URL("./assets/psychogra.pl/wp-content/uploads/2017/10/cropped-psychogra-wide-purple.png", import.meta.url).href}" class="custom-logo" alt="Psychogra" decoding="async" fetchpriority="high" srcset="${new URL("./assets/psychogra.pl/wp-content/uploads/2017/10/cropped-psychogra-wide-purple.png", import.meta.url).href} 472w, ${new URL("./assets/psychogra.pl/wp-content/uploads/2017/10/cropped-psychogra-wide-purple-300x70.png", import.meta.url).href} 300w" sizes="(max-width: 472px) 100vw, 472px">
          </a>
        </div>
      </div>
      <div class="storefront-primary-navigation">
        <div class="col-full">
          <nav id="site-navigation" class="main-navigation" role="navigation" aria-label="Główne menu">
            <button class="menu-toggle" aria-controls="site-navigation" aria-expanded="false"><span>Menu</span></button>
            <div class="primary-navigation">
              <ul id="menu-menu-glowne" class="menu">
                <li class="menu-item"><a href="${siteUrl("blog/index.html")}">Blog</a></li>
                <li class="menu-item menu-item-has-children"><a href="${siteUrl("index.html")}">Gry</a>
                  <ul class="sub-menu">
                    <li class="menu-item"><a href="${siteUrl("index.html")}">Teoria Umysłu &#8211; 2018</a></li>
                    <li class="menu-item"><a href="${siteUrl("gra-o-slon-v2/gry-v2/index.html")}">Gry &#8211; wrzesień 2017</a></li>
                    <li class="menu-item"><a href="${siteUrl("gra-o-slon/gry/index.html")}">Gry &#8211; marzec 2017</a></li>
                  </ul>
                </li>
                <li class="menu-item menu-item-has-children"><a href="${siteUrl("index.html")}">Teoria Umysłu</a>
                  <ul class="sub-menu"><li class="menu-item"><a href="${siteUrl("o-nas-ptu/index.html")}">O nas</a></li></ul>
                </li>
                <li class="menu-item menu-item-has-children"><a href="${siteUrl("home/index.html")}">Gra o Słoń</a>
                  <ul class="sub-menu">
                    <li class="menu-item"><a href="${siteUrl("gra-o-slon-v2/o-nas/index.html")}">O nas</a></li>
                    <li class="menu-item menu-item-has-children"><a href="${siteUrl("gra-o-slon-v2/index.html")}">Game Jam v2</a>
                      <ul class="sub-menu">
                        <li class="menu-item"><a href="${siteUrl("gra-o-slon-v2/index.html")}">Game Jam we wrześniu 2017</a></li>
                        <li class="menu-item"><a href="${siteUrl("gra-o-slon-v2/zespoly-v2/index.html")}">Zespoły</a></li>
                        <li class="menu-item"><a href="${siteUrl("gra-o-slon-v2/gry-v2/index.html")}">Gry</a></li>
                        <li class="menu-item"><a href="${siteUrl("gra-o-slon-v2/o-nas/index.html")}">Organizatorzy</a></li>
                        <li class="menu-item"><a href="${new URL("./assets/psychogra.pl/wp-content/uploads/2017/09/plakat-v2.png", import.meta.url).href}">Plakat</a></li>
                      </ul>
                    </li>
                    <li class="menu-item menu-item-has-children"><a href="${siteUrl("gra-o-slon/index.html")}">Game Jam v1</a>
                      <ul class="sub-menu">
                        <li class="menu-item"><a href="${siteUrl("gra-o-slon/index.html")}">Game Jam w marcu 2017</a></li>
                        <li class="menu-item"><a href="${siteUrl("gra-o-slon/zespoly/index.html")}">Zespoły</a></li>
                        <li class="menu-item"><a href="${siteUrl("gra-o-slon/gry/index.html")}">Gry</a></li>
                        <li class="menu-item"><a href="${siteUrl("gra-o-slon/organizatorzy-v1/index.html")}">Organizatorzy</a></li>
                        <li class="menu-item"><a href="${new URL("./assets/psychogra.pl/wp-content/uploads/2017/09/plakat-finalny.jpg", import.meta.url).href}">Plakat</a></li>
                      </ul>
                    </li>
                    <li class="menu-item"><a href="${siteUrl("gra-o-slon/autyzm/index.html")}">Autyzm</a></li>
                    <li class="menu-item"><a href="${siteUrl("gra-o-slon-v2/tworzenie-gier/index.html")}">Tworzenie Gier</a></li>
                    <li class="menu-item"><a href="${siteUrl("gra-o-slon-v2/regulamin/index.html")}">Regulamin</a></li>
                    <li class="menu-item"><a href="${siteUrl("gra-o-slon-v2/pytania-i-odpowiedzi/index.html")}">Pytania i Odpowiedzi</a></li>
                  </ul>
                </li>
                <li class="menu-item"><a href="${siteUrl("kontakt/index.html")}">Kontakt</a></li>
                <li class="menu-item"><a href="${siteUrl("regulamin-serwisu/index.html")}">Regulamin serwisu</a></li>
                <li class="menu-item"><a href="https://www.facebook.com/psychogra">Fanpage</a></li>
              </ul>
            </div>
          </nav>
        </div>
      </div>
    </header>`;

  const sidebar = `
    <div id="secondary" class="widget-area" role="complementary">
      <div id="block-4" class="widget widget_block"><h2 class="wp-block-heading">Wpisy</h2></div>
      <div id="block-3" class="widget widget_block widget_recent_entries">
        <ul class="wp-block-latest-posts__list wp-block-latest-posts">
          <li><a class="wp-block-latest-posts__post-title" href="${siteUrl("jesli-jestes-placowka-i-sciagnales-gre-koniecznie-wyslij-formularz/index.html")}">Jeśli jesteś placówką i ściągnąłeś grę, koniecznie wyślij formularz!</a></li>
          <li><a class="wp-block-latest-posts__post-title" href="${siteUrl("wyklady-dyskusja-i-prezentacja-gry-juz-12-05-18-we-wroclawiu/index.html")}">Wykłady, dyskusja i prezentacja gry! Już 12.05.18 we Wrocławiu.</a></li>
          <li><a class="wp-block-latest-posts__post-title" href="${siteUrl("1000-2/index.html")}">Premiera &#8222;Psychogra: teoria umysłu&#8221;</a></li>
          <li><a class="wp-block-latest-posts__post-title" href="${siteUrl("tworzenie-gry-1/index.html")}">Tworzenie gry #1</a></li>
          <li><a class="wp-block-latest-posts__post-title" href="${siteUrl("projektujemy-nowa-gre/index.html")}">Projektujemy nową grę</a></li>
          <li><a class="wp-block-latest-posts__post-title" href="${siteUrl("gra-o-slon-game-jam/index.html")}">Gra o Słoń &#8211; Game Jam</a></li>
        </ul>
      </div>
    </div>`;

  const footer = `
    <footer id="colophon" class="site-footer col-full" role="contentinfo">
      <div class="partners">
        <a href="http://magicvr.co/" target="_blank" rel="noopener"><img src="${new URL("./assets/psychogra.pl/wp-content/uploads/2017/09/magicvr.png", import.meta.url).href}" alt="MagicVR"></a>
        <a href="https://soundcloud.com/pmmestudio" target="_blank" rel="noopener"><img src="${new URL("./assets/psychogra.pl/wp-content/uploads/2017/09/pmme.png", import.meta.url).href}" alt="PMME Studio"></a>
        <a href="http://techland.pl/" target="_blank" rel="noopener"><img src="${new URL("./assets/psychogra.pl/wp-content/uploads/2017/09/techland.png", import.meta.url).href}" alt="Techland"></a>
        <a href="https://superhotgame.com/" target="_blank" rel="noopener"><img src="${new URL("./assets/psychogra.pl/wp-content/uploads/2017/09/superhot.png", import.meta.url).href}" alt="SUPERHOT"></a>
        <a href="https://www.facebook.com/pwrtkgames/" target="_blank" rel="noopener"><img src="${new URL("./assets/psychogra.pl/wp-content/uploads/2017/09/tk.png", import.meta.url).href}" alt="PwrTk Games"></a>
        <a href="http://mokronosek2.mokronosek.pl/" target="_blank" rel="noopener"><img src="${new URL("./assets/psychogra.pl/wp-content/uploads/2017/09/mokronosek.png", import.meta.url).href}" alt="Mokronosek"></a>
        <a href="http://fundacja-umbrella.org.pl/" target="_blank" rel="noopener"><img src="${new URL("./assets/psychogra.pl/wp-content/uploads/2017/09/umbrella.png", import.meta.url).href}" alt="Fundacja Umbrella"></a>
        <a href="http://wfmi.pl/" target="_blank" rel="noopener"><img src="${new URL("./assets/psychogra.pl/wp-content/uploads/2017/09/wfmi.png", import.meta.url).href}" alt="Wrocławski Fundusz Małych Inicjatyw"></a>
        <a href="http://www.wroclaw.pl/" target="_blank" rel="noopener"><img src="${new URL("./assets/psychogra.pl/wp-content/uploads/2017/09/wroclaw.png", import.meta.url).href}" alt="Wrocław"></a>
        <a href="https://www.facebook.com/szufladamart/" target="_blank" rel="noopener"><img src="${new URL("./assets/psychogra.pl/wp-content/uploads/2018/04/mart2.png", import.meta.url).href}" alt="Szuflada m_art"></a>
      </div>
      <p>Projekt pt. „Gra o Słoń – Edycja II” jest dofinansowany w ramach projektu „Wrocławski Fundusz Małych Inicjatyw” realizowanego ze środków Gminy Wrocław.</p>
      <div class="col-full"></div>
    </footer>`;

  const page = document.querySelector("#page");
  const content = document.querySelector("#content");
  const primary = document.querySelector("#primary");
  if (!page || !content || !primary) {
    throw new Error("Could not find the page content containers for shared site components.");
  }

  page.insertAdjacentHTML("afterbegin", header);
  primary.insertAdjacentHTML("afterend", sidebar);
  page.insertAdjacentHTML("beforeend", footer);

  const mobileNavigation = document.createElement("style");
  mobileNavigation.textContent = `
    @media screen and (max-width: 768px) {
      #site-navigation .menu-toggle { display: block; }
      #site-navigation .primary-navigation { display: none; }
      #site-navigation.toggled .primary-navigation { display: block; }
      #site-navigation .primary-navigation > ul,
      #site-navigation .primary-navigation > ul > li,
      #site-navigation .primary-navigation ul ul { display: block; }
      #site-navigation .primary-navigation ul ul {
        position: static;
        float: none;
        width: auto;
        box-shadow: none;
      }
    }`;
  document.head.append(mobileNavigation);

  const navigation = document.querySelector("#site-navigation");
  const menuToggle = navigation?.querySelector(".menu-toggle");
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && navigation.classList.contains("toggled")) {
      navigation.classList.remove("toggled");
      menuToggle?.setAttribute("aria-expanded", "false");
      menuToggle?.focus();
    }
  });

  const normalizePath = (path) => path.replace(/index\.html$/, "");
  const updateActiveNavigation = () => {
    const currentPath = normalizePath(window.location.pathname);
    document.querySelectorAll("#site-navigation a[href]").forEach((link) => {
      const linkPath = normalizePath(new URL(link.href).pathname);
      if (linkPath === currentPath) {
        link.setAttribute("aria-current", "page");
      } else {
        link.removeAttribute("aria-current");
      }
    });
  };

  const updateMetadata = (nextPage) => {
    document.title = nextPage.title;
    document.documentElement.lang = nextPage.documentElement.lang;
    document.body.className = nextPage.body.className;

    const metadataSelector = 'meta[name="description"], meta[name^="twitter:"], meta[property^="og:"], link[rel="canonical"]';
    document.head.querySelectorAll(metadataSelector).forEach((element) => element.remove());
    nextPage.head.querySelectorAll(metadataSelector).forEach((element) => {
      document.head.append(element.cloneNode(true));
    });
  };

  const canRenderPage = (nextPage) => {
    const nextPrimary = nextPage.querySelector("#primary");
    return Boolean(
      nextPage.querySelector("#page #content") &&
        nextPrimary &&
        !nextPrimary.querySelector("form, script"),
    );
  };

  let navigationController;
  const loadPage = async (url, { addHistory = true, scrollY = 0 } = {}) => {
    navigationController?.abort();
    const controller = new AbortController();
    navigationController = controller;

    try {
      const response = await fetch(url, {
        headers: { Accept: "text/html" },
        signal: controller.signal,
      });
      if (!response.ok) {
        throw new Error(`Page request failed with status ${response.status}: ${url.href}`);
      }

      const nextPage = new DOMParser().parseFromString(await response.text(), "text/html");
      if (!canRenderPage(nextPage)) {
        return false;
      }

      const nextPrimary = nextPage.querySelector("#primary");
      const currentPrimary = document.querySelector("#primary");
      if (!currentPrimary || !nextPrimary) {
        return false;
      }

      if (addHistory) {
        history.replaceState({ spa: true, scrollY: window.scrollY }, "");
        history.pushState({ spa: true, scrollY: 0 }, "", url);
      }
      currentPrimary.replaceWith(nextPrimary);
      updateMetadata(nextPage);
      updateActiveNavigation();

      const navigation = document.querySelector("#site-navigation");
      navigation?.classList.remove("toggled");
      navigation?.querySelector(".menu-toggle")?.setAttribute("aria-expanded", "false");

      requestAnimationFrame(() => {
        if (url.hash) {
          document.getElementById(decodeURIComponent(url.hash.slice(1)))?.scrollIntoView();
          return;
        }
        window.scrollTo(0, scrollY);
        if (addHistory) {
          document.querySelector("#main")?.focus({ preventScroll: true });
        }
      });
      return true;
    } catch (error) {
      if (error instanceof DOMException && error.name === "AbortError") {
        return true;
      }
      console.error("SPA navigation failed; loading the page normally.", error);
      return false;
    }
  };

  const isEligibleLink = (event, link, url) =>
    event.button === 0 &&
    !event.defaultPrevented &&
    !event.metaKey &&
    !event.ctrlKey &&
    !event.shiftKey &&
    !event.altKey &&
    (!link.target || link.target === "_self") &&
    !link.hasAttribute("download") &&
    url.origin === window.location.origin &&
    url.pathname.endsWith(".html") &&
    !(url.pathname === window.location.pathname && url.search === window.location.search);

  history.replaceState({ spa: true, scrollY: window.scrollY }, "");
  updateActiveNavigation();

  document.addEventListener("click", (event) => {
    if (!(event.target instanceof Element)) {
      return;
    }
    const link = event.target.closest("a[href]");
    if (!link) {
      return;
    }
    const url = new URL(link.href, window.location.href);
    if (!isEligibleLink(event, link, url)) {
      return;
    }

    event.preventDefault();
    void loadPage(url).then((loaded) => {
      if (!loaded) {
        window.location.assign(url.href);
      }
    });
  });

  window.addEventListener("popstate", (event) => {
    void loadPage(new URL(window.location.href), {
      addHistory: false,
      scrollY: event.state?.scrollY ?? 0,
    }).then((loaded) => {
      if (!loaded) {
        window.location.reload();
      }
    });
  });
})();
