import { CircleHelp, Filter, Menu, X } from "lucide-react";
import { type ReactNode, useEffect, useRef, useState } from "react";
import { NavLink, useLocation } from "react-router-dom";
import { pageForPath, sitePages } from "../lib/routes";
import type { MetaData } from "../types";

export function LoadingScreen() {
  return (
    <main className="state-screen" aria-live="polite">
      <div className="loading-mark">
        <span />
        <span />
        <span />
      </div>
      <p className="eyebrow">Opening the evidence base</p>
      <h1>Linking datasets, studies, and methods…</h1>
    </main>
  );
}

export function ErrorScreen({ message }: { message: string }) {
  return (
    <main className="state-screen error-state">
      <CircleHelp size={34} />
      <h1>The evidence could not be loaded.</h1>
      <p>Check your connection and reload the page to try again.</p>
      <button className="primary-action" type="button" onClick={() => window.location.reload()}>
        Reload page
      </button>
      <details>
        <summary>Technical details</summary>
        <p>{message}</p>
      </details>
    </main>
  );
}

export function SiteLayout({ children, meta }: { children: ReactNode; meta: MetaData }) {
  const [menuOpen, setMenuOpen] = useState(false);
  const { pathname } = useLocation();
  const previousPath = useRef(pathname);
  useEffect(() => {
    document.title = (pageForPath(pathname) ?? sitePages[0]).title;
    if (previousPath.current !== pathname) {
      previousPath.current = pathname;
      window.requestAnimationFrame(() => {
        window.scrollTo({ top: 0, behavior: "auto" });
        document.querySelector<HTMLElement>("#main-content h1")?.focus({ preventScroll: true });
      });
    }
  }, [pathname]);

  const backToTop = () => {
    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    document.querySelector<HTMLElement>("#main-content h1")?.focus({ preventScroll: true });
    window.scrollTo({ top: 0, behavior: reduceMotion ? "auto" : "smooth" });
  };
  return (
    <div className="app-shell">
      <a
        className="skip-link"
        href="#main-content"
        onClick={(event) => {
          event.preventDefault();
          document.getElementById("main-content")?.focus();
        }}
      >
        Skip to content
      </a>
      <header className="topbar">
        <NavLink className="brand" to="/" aria-label="Industrial Inspection Evidence Explorer home">
          <span className="brand-mark" aria-hidden="true">
            <span />
            <span />
            <span />
          </span>
          <span>
            <strong>Industrial Inspection</strong>
            <small>Evidence explorer</small>
          </span>
        </NavLink>
        <button
          className="menu-button"
          type="button"
          aria-label={menuOpen ? "Close navigation" : "Open navigation"}
          aria-controls="primary-navigation"
          aria-expanded={menuOpen}
          onClick={() => setMenuOpen(!menuOpen)}
        >
          {menuOpen ? <X /> : <Menu />}
        </button>
        <nav
          id="primary-navigation"
          className={menuOpen ? "open" : ""}
          aria-label="Primary navigation"
        >
          {sitePages.map(({ path, label }) => (
            <NavLink
              key={path}
              onClick={() => setMenuOpen(false)}
              to={path}
              className={({ isActive }) => (isActive ? "active" : "")}
            >
              {label}
            </NavLink>
          ))}
        </nav>
      </header>
      <main id="main-content" tabIndex={-1}>
        {children}
      </main>
      <footer className="site-footer">
        <div>
          <span className="brand-mark small" aria-hidden="true">
            <span />
            <span />
            <span />
          </span>
          <p>
            <strong>Dataset-centered evidence, kept conditional.</strong>
            <br />
            An interactive companion to the related review manuscript.
          </p>
        </div>
        <div className="footer-paper">
          <span>Related work</span>
          <p>{meta.title}</p>
          <small>{meta.authors.join(" · ")}</small>
        </div>
        <div className="footer-links">
          <NavLink to="/review/">Methods & provenance</NavLink>
          <a href={`${import.meta.env.BASE_URL}data/provenance.json`} download>
            Data manifest
          </a>
          <button type="button" onClick={backToTop}>
            Back to top ↑
          </button>
        </div>
      </footer>
    </div>
  );
}

export function SectionHeading({
  index,
  eyebrow,
  title,
  aside,
}: {
  index: string;
  eyebrow: string;
  title: string;
  aside: string;
}) {
  return (
    <div className="section-heading">
      <div className="heading-title">
        <span>{index}</span>
        <div>
          <p className="kicker">{eyebrow}</p>
          <h2>{title}</h2>
        </div>
      </div>
      <p>{aside}</p>
    </div>
  );
}

export function PageHero({
  eyebrow,
  title,
  lede,
  stat,
  statLabel,
}: {
  eyebrow: string;
  title: string;
  lede: string;
  stat: string;
  statLabel: string;
}) {
  return (
    <section className="page-hero">
      <div>
        <p className="eyebrow">{eyebrow}</p>
        <h1 tabIndex={-1}>{title}</h1>
        <p>{lede}</p>
      </div>
      <div className="page-stat">
        <strong>{stat}</strong>
        <span>{statLabel}</span>
      </div>
    </section>
  );
}

export function EmptyState({ title, copy }: { title: string; copy: string }) {
  return (
    <div className="empty-state" role="status" aria-live="polite">
      <Filter />
      <h3>{title}</h3>
      <p>{copy}</p>
    </div>
  );
}
