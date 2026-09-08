export const GITHUB_PAGES_BASE = "/industrial-defect-inspection-review/";

export const sitePages = [
  {
    path: "/",
    label: "Explorer",
    title: "Evidence Explorer · Industrial Visual Defect Inspection",
  },
  {
    path: "/datasets/",
    label: "Datasets",
    title: "Public Dataset Registry · Industrial Inspection Evidence",
  },
  {
    path: "/evidence/",
    label: "Evidence",
    title: "Synthesis Evidence Atlas · Industrial Inspection Evidence",
  },
  {
    path: "/review/",
    label: "Review logic",
    title: "Review Logic & Provenance · Industrial Inspection Evidence",
  },
] as const;

export function pageForPath(pathname: string) {
  const path = pathname.replace(/\/index\.html$/, "/").replace(/\/?$/, "/");
  return sitePages.find((page) => page.path === path);
}

// Resolve only known routes; fragments can never redirect to another origin.
export function cleanSiteUrl(href: string, base: string): string | null {
  const url = new URL(href);
  if (!url.pathname.startsWith(base) && url.pathname !== base.slice(0, -1)) return null;

  if (url.hash.startsWith("#/")) {
    let legacy: URL;
    try {
      legacy = new URL(url.hash.slice(1), url.origin);
    } catch {
      return null;
    }
    const page = legacy.origin === url.origin ? pageForPath(legacy.pathname) : undefined;
    if (!page) return null;
    url.pathname = base + page.path.slice(1);
    for (const key of new Set(legacy.searchParams.keys())) url.searchParams.delete(key);
    for (const [key, value] of legacy.searchParams) url.searchParams.append(key, value);
    url.hash = legacy.hash;
  } else {
    const path = url.pathname === base.slice(0, -1) ? "/" : `/${url.pathname.slice(base.length)}`;
    const page = pageForPath(path);
    if (!page) return null;
    url.pathname = base + page.path.slice(1);
  }
  return url.href === href ? null : `${url.pathname}${url.search}${url.hash}`;
}
