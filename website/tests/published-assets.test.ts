import { existsSync, readdirSync, readFileSync } from "node:fs";
import { resolve } from "node:path";
import { describe, expect, it } from "vitest";

const site = resolve(import.meta.dirname, "..");
function filesIn(directory: string): string[] {
  return readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const path = resolve(directory, entry.name);
    return entry.isDirectory() ? filesIn(path) : [path];
  });
}
describe("website publication assets", () => {
  it("ships no LaTeX source files as public assets", () => {
    expect(
      filesIn(resolve(site, "public")).filter((path) => /\.(tex|bib|sty|cls)$/i.test(path)),
    ).toEqual([]);
  });
  it("keeps all advertised reference downloads available", () => {
    for (const path of [
      "data/datasets.json",
      "data/evidence.json",
      "downloads/synthesis_impact_normalized_change.csv",
      "downloads/table3_baseline_after_synthesis.csv",
      "downloads/dataset_citation_counts_wide_2020_2025_all_domains.csv",
    ]) {
      expect(existsSync(resolve(site, "public", path)), path).toBe(true);
    }
  });
  it("does not link or copy LaTeX sources into website downloads", () => {
    for (const page of ["DatasetsPage.tsx", "ReviewPage.tsx", "EvidencePage.tsx"]) {
      const source = readFileSync(resolve(site, "src/pages", page), "utf8");
      expect(source).not.toMatch(/downloads\/[^\s"`]*\.tex/);
    }
    const prepare = readFileSync(resolve(site, "scripts/prepare-data.ts"), "utf8");
    expect(prepare).not.toMatch(/copyDownload\(sourcePaths\.(registry|evidence)\)/);
  });
});
