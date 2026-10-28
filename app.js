(function () {
  "use strict";

  const content = window.siteContent;
  if (!content) return;

  const profileColumn = document.querySelector(".profile-column");
  const contentColumn = document.querySelector(".content-column");
  const navigation = document.querySelector(".site-navigation");
  const footer = document.querySelector(".site-footer");
  const menuToggle = document.querySelector("#menu-toggle");
  const themeToggle = document.querySelector("#theme-toggle");

  const escapeHtml = (value = "") =>
    String(value)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");

  const safeUrl = (url = "") => {
    try {
      const parsed = new URL(url, window.location.href);
      if (["http:", "https:", "mailto:"].includes(parsed.protocol)) return parsed.href;
    } catch (_) {
      return "";
    }
    return "";
  };

  const renderAboutParagraph = (paragraph) => {
    if (typeof paragraph === "string") return `<p>${escapeHtml(paragraph)}</p>`;

    const linkUrl = safeUrl(paragraph?.linkUrl);
    const linkedText = linkUrl
      ? `<a href="${escapeHtml(linkUrl)}" target="_blank" rel="noreferrer">${escapeHtml(
          paragraph.linkLabel,
        )}</a>`
      : escapeHtml(paragraph?.linkLabel);

    return `<p>${escapeHtml(paragraph?.prefix)}${linkedText}${escapeHtml(paragraph?.suffix)}</p>`;
  };

  const icon = (name) => {
    const icons = {
      github:
        '<svg class="icon-fill" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-3.16 19.49c.5.09.68-.22.68-.48v-1.7c-2.78.61-3.37-1.18-3.37-1.18-.45-1.16-1.11-1.47-1.11-1.47-.91-.62.07-.61.07-.61 1 .07 1.53 1.03 1.53 1.03.9 1.53 2.34 1.09 2.91.83.09-.65.35-1.09.64-1.34-2.22-.25-4.55-1.11-4.55-4.94 0-1.09.39-1.98 1.03-2.68-.1-.25-.45-1.27.1-2.64 0 0 .84-.27 2.75 1.03A9.58 9.58 0 0 1 12 7c.85 0 1.71.11 2.51.34 1.91-1.3 2.75-1.03 2.75-1.03.55 1.37.2 2.39.1 2.64.64.7 1.03 1.59 1.03 2.68 0 3.84-2.34 4.68-4.57 4.93.36.31.68.92.68 1.85v2.6c0 .27.18.58.69.48A10 10 0 0 0 12 2Z"/></svg>',
      mail:
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5h18v14H3z"/><path d="m3 6 9 7 9-7"/></svg>',
      file:
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 2h8l4 4v16H6z"/><path d="M14 2v5h5M9 13h6M9 17h6"/></svg>',
      scholar:
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m2 9 10-5 10 5-10 5z"/><path d="M6 11v5c2.8 2.7 9.2 2.7 12 0v-5M22 9v7"/></svg>',
      arrow:
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M14 7l5 5-5 5"/></svg>',
      location:
        '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 10c0 5-8 12-8 12S4 15 4 10a8 8 0 1 1 16 0Z"/><circle cx="12" cy="10" r="2.5"/></svg>',
    };
    return icons[name] || "";
  };

  const p = content.profile;
  const profileLinks = [
    p.email && {
      label: "Email",
      url: `mailto:${p.email}`,
      icon: "mail",
    },
    p.github && { label: "GitHub", url: p.github, icon: "github" },
    p.scholar && { label: "Google Scholar", url: p.scholar, icon: "scholar" },
    p.cv && { label: "Curriculum vitae", url: p.cv, icon: "file" },
  ].filter(Boolean);

  const avatar = safeUrl(p.avatar);
  profileColumn.innerHTML = `
    <div class="profile-card reveal">
      <div class="avatar-wrap">
        ${
          avatar
            ? `<img class="avatar" src="${escapeHtml(avatar)}" alt="${escapeHtml(
                p.avatarAlt || `Portrait of ${p.name}`,
              )}" />`
            : ""
        }
        <div class="avatar-fallback" aria-hidden="true">${escapeHtml(
          p.name
            .split(" ")
            .map((part) => part[0])
            .join("")
            .slice(0, 2),
        )}</div>
      </div>
      <div class="identity">
        <h1>${escapeHtml(p.name)}</h1>
        ${p.title ? `<p class="profile-title">${escapeHtml(p.title)}</p>` : ""}
        ${p.affiliation ? `<p class="affiliation">${escapeHtml(p.affiliation)}</p>` : ""}
        ${
          p.location
            ? `<p class="location">${icon("location")}<span>${escapeHtml(p.location)}</span></p>`
            : ""
        }
      </div>
      ${
        profileLinks.length
          ? `<div class="profile-links" aria-label="Profile links">
              ${profileLinks
                .map(
                  (link) => `<a href="${escapeHtml(safeUrl(link.url))}" aria-label="${escapeHtml(
                    link.label,
                  )}" ${link.url.startsWith("http") ? 'target="_blank" rel="noreferrer"' : ""}>
                    ${icon(link.icon)}<span>${escapeHtml(link.label)}</span>
                  </a>`,
                )
                .join("")}
            </div>`
          : ""
      }
      ${
        p.interests?.length
          ? `<div class="interests-card">
              <h2>Research interests</h2>
              <ul>${p.interests.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}</ul>
            </div>`
          : ""
      }
    </div>
  `;

  const sections = [];

  if (content.about?.length) {
    sections.push({
      id: "about",
      label: "About",
      html: `
        <section class="content-section reveal" id="about">
          <p class="section-kicker">A brief introduction</p>
          <h2>About</h2>
          <div class="prose">
            ${content.about.map(renderAboutParagraph).join("")}
          </div>
        </section>`,
    });
  }

  if (content.work?.length) {
    sections.push({
      id: "work",
      label: "Work",
      html: `
        <section class="content-section reveal" id="work">
          <div class="section-heading-row">
            <div>
              <p class="section-kicker">Selected work</p>
              <h2>Research & projects</h2>
            </div>
          </div>
          <div class="work-list">
            ${content.work
              .map(
                (item, index) => `
                <article class="work-card">
                  <div class="work-index">${String(index + 1).padStart(2, "0")}</div>
                  <div class="work-body">
                    ${item.eyebrow ? `<p class="work-eyebrow">${escapeHtml(item.eyebrow)}</p>` : ""}
                    <h3>${escapeHtml(item.title)}</h3>
                    ${item.authors ? `<p class="authors">${escapeHtml(item.authors)}</p>` : ""}
                    ${item.venue ? `<p class="venue">${escapeHtml(item.venue)}</p>` : ""}
                    <p>${escapeHtml(item.description)}</p>
                    ${
                      item.tags?.length
                        ? `<ul class="tag-list" aria-label="Topics">${item.tags
                            .map((tag) => `<li>${escapeHtml(tag)}</li>`)
                            .join("")}</ul>`
                        : ""
                    }
                    ${
                      item.links?.length
                        ? `<div class="work-links">${item.links
                            .map(
                              (link) => `<a href="${escapeHtml(
                                safeUrl(link.url),
                              )}" target="_blank" rel="noreferrer">${escapeHtml(
                                link.label,
                              )}${icon("arrow")}</a>`,
                            )
                            .join("")}</div>`
                        : ""
                    }
                  </div>
                </article>`,
              )
              .join("")}
          </div>
        </section>`,
    });
  }

  if (content.news?.length) {
    sections.push({
      id: "news",
      label: "News",
      html: `
        <section class="content-section reveal" id="news">
          <p class="section-kicker">Recent notes</p>
          <h2>News</h2>
          <ol class="timeline">
            ${content.news
              .map(
                (item) => `<li>
                  <time>${escapeHtml(item.date)}</time>
                  <span>${
                    item.url
                      ? `<a href="${escapeHtml(safeUrl(item.url))}" target="_blank" rel="noreferrer">${escapeHtml(
                          item.text,
                        )}</a>`
                      : escapeHtml(item.text)
                  }</span>
                </li>`,
              )
              .join("")}
          </ol>
        </section>`,
    });
  }

  const listSection = (id, label, kicker, heading, items) => {
    if (!items?.length) return;
    sections.push({
      id,
      label,
      html: `
        <section class="content-section reveal" id="${id}">
          <p class="section-kicker">${escapeHtml(kicker)}</p>
          <h2>${escapeHtml(heading)}</h2>
          <ul class="credential-list">
            ${items
              .map(
                (item) => `<li><span>${escapeHtml(item.date || item.year || "")}</span><p>${escapeHtml(
                  item.text || item.title || "",
                )}</p></li>`,
              )
              .join("")}
          </ul>
        </section>`,
    });
  };

  listSection("awards", "Awards", "Recognition", "Awards", content.awards);
  listSection("services", "Services", "Community", "Services", content.services);

  contentColumn.innerHTML = sections.map((section) => section.html).join("");
  navigation.innerHTML = sections
    .map((section) => `<a href="#${section.id}">${escapeHtml(section.label)}</a>`)
    .join("");

  footer.innerHTML = `
    <div class="footer-inner">
      <p>© ${new Date().getFullYear()} ${escapeHtml(p.name)}</p>
      <p>${escapeHtml(content.footer?.note || "")}</p>
      <p>Last updated: ${escapeHtml(content.footer?.lastUpdated || "")}</p>
    </div>`;

  const avatarImage = document.querySelector(".avatar");
  if (avatarImage) {
    avatarImage.addEventListener("load", () => avatarImage.parentElement.classList.add("has-image"));
    avatarImage.addEventListener("error", () => avatarImage.remove());
  }

  const closeMenu = () => {
    navigation.classList.remove("is-open");
    menuToggle.setAttribute("aria-expanded", "false");
    menuToggle.setAttribute("aria-label", "Open navigation");
  };

  menuToggle.addEventListener("click", () => {
    const isOpen = navigation.classList.toggle("is-open");
    menuToggle.setAttribute("aria-expanded", String(isOpen));
    menuToggle.setAttribute("aria-label", isOpen ? "Close navigation" : "Open navigation");
  });

  navigation.addEventListener("click", (event) => {
    if (event.target.closest("a")) closeMenu();
  });

  const applyTheme = (theme) => {
    document.documentElement.dataset.theme = theme;
    const dark = theme === "dark";
    themeToggle.setAttribute("aria-label", dark ? "Use light theme" : "Use dark theme");
    document.querySelector('meta[name="theme-color"]').content = dark ? "#12171d" : "#f7f4ee";
  };

  const savedTheme = localStorage.getItem("theme");
  const initialTheme =
    savedTheme || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
  applyTheme(initialTheme);

  themeToggle.addEventListener("click", () => {
    const nextTheme = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
    localStorage.setItem("theme", nextTheme);
    applyTheme(nextTheme);
  });

  const reveals = document.querySelectorAll(".reveal");
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    reveals.forEach((element) => element.classList.add("is-visible"));
  } else {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { rootMargin: "0px 0px -8%", threshold: 0.08 },
    );
    reveals.forEach((element) => observer.observe(element));
  }
})();
