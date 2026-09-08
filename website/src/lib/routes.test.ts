import { describe, expect, it } from "vitest";
import { cleanSiteUrl, GITHUB_PAGES_BASE, pageForPath, sitePages } from "./routes";

describe.each(["/", GITHUB_PAGES_BASE])("clean URLs under %s", (base) => {
  const origin = "https://example.org";

  it.each(sitePages)("preserves the clean $path URL", ({ path }) => {
    expect(cleanSiteUrl(`${origin}${base}${path.slice(1)}`, base)).toBeNull();
  });

  it.each(sitePages)("migrates a bookmarked hash route for $path", ({ path }) => {
    expect(cleanSiteUrl(`${origin}${base}#${path}?record=E01`, base)).toBe(
      `${base}${path.slice(1)}?record=E01`,
    );
  });

  it("preserves encoded graph IDs, repeated filters, pins, and an ordinary fragment", () => {
    const query = "node=Papers%2FAlpha+%26+Beta&type=Papers&type=Datasets&pin=a&pin=b&view=local";
    expect(cleanSiteUrl(`${origin}${base}?utm_source=paper#/?${query}#evidence-graph`, base)).toBe(
      `${base}?utm_source=paper&${query}#evidence-graph`,
    );
  });

  it("lets bookmarked route filters replace outer query values", () => {
    expect(
      cleanSiteUrl(`${origin}${base}?type=Methods#/datasets?type=Papers&type=Datasets`, base),
    ).toBe(`${base}datasets/?type=Papers&type=Datasets`);
  });

  it("normalizes slashless and explicit index paths while retaining queries", () => {
    for (const path of ["evidence", "evidence/index.html"]) {
      expect(cleanSiteUrl(`${origin}${base}${path}?record=E39#details`, base)).toBe(
        `${base}evidence/?record=E39#details`,
      );
    }
  });

  it("leaves document fragments, unknown routes, and external-looking hashes alone", () => {
    for (const suffix of [
      "#main-content",
      "missing/",
      "#/missing",
      "#//other.example/review/",
      "#//",
      "#//[",
    ]) {
      expect(cleanSiteUrl(`${origin}${base}${suffix}`, base)).toBeNull();
    }
  });
});

it("does not rewrite a URL outside the repository base", () => {
  expect(cleanSiteUrl("https://example.org/another-site/#/review", GITHUB_PAGES_BASE)).toBeNull();
});

it.each(sitePages)("recognizes trailing slashes and index.html for $label", (page) => {
  expect(pageForPath(page.path)).toBe(page);
  expect(pageForPath(`${page.path}index.html`)).toBe(page);
  if (page.path !== "/") expect(pageForPath(page.path.slice(0, -1))).toBe(page);
});
