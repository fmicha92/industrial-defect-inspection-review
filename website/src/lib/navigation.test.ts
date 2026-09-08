import { readFileSync } from "node:fs";
import { describe, expect, it } from "vitest";
import type { SiteData } from "../types";
import {
  directedPath,
  matchesSearch,
  publicationUrl,
  relatedDatasets,
  safeUrl,
  studyGraphNode,
} from "./navigation";

const datasets = JSON.parse(
  readFileSync(new URL("../../public/data/datasets.json", import.meta.url), "utf8"),
) as SiteData["datasets"];
const evidence = JSON.parse(
  readFileSync(new URL("../../public/data/evidence.json", import.meta.url), "utf8"),
) as SiteData["evidence"];

describe("existing-record navigation", () => {
  it("resolves every retained comparison to a registry record", () => {
    evidence.items.forEach((item) =>
      expect(relatedDatasets(item, datasets.datasets).length).toBeGreaterThan(0),
    );
  });
  it("preserves documented subset associations", () => {
    const expected: Record<string, string> = {
      E06: "WM-811K",
      E09: "ELPV Solar Cell Dataset",
      E16: "NEU-DET",
      E24: "AITEX",
      E27: "MVTec AD",
    };
    Object.entries(expected).forEach(([id, name]) => {
      const item = evidence.items.find((row) => row.id === id);
      expect(item).toBeDefined();
      expect(relatedDatasets(item!, datasets.datasets).map((dataset) => dataset.name)).toEqual([
        name,
      ]);
    });
  });
  it("separates multi-dataset records without matching similar names", () => {
    const item = evidence.items.find((row) => row.id === "E37")!;
    expect(
      relatedDatasets(item, datasets.datasets)
        .map((dataset) => dataset.name)
        .sort(),
    ).toEqual(["KolektorSDD2", "MVTec AD", "VisA"]);
    const mvtec = evidence.items.find((row) => row.id === "E29")!;
    expect(relatedDatasets(mvtec, datasets.datasets).map((dataset) => dataset.name)).toEqual([
      "MVTec AD",
    ]);
  });
  it("does not infer a link for unknown dataset text", () => {
    const item = evidence.items[0];
    expect(
      relatedDatasets(
        { ...item, sourceLabels: { ...item.sourceLabels, normalizedDataset: "MVTec" } },
        datasets.datasets,
      ),
    ).toEqual([]);
  });
  it("requires a unique study identifier match", () => {
    const item = {
      ...evidence.items[0],
      study: { ...evidence.items[0].study, doi: "10.1234/example", title: "Study" },
    };
    const node = {
      id: "paper-a",
      title: "Study",
      type: "Papers",
      doi: "https://doi.org/10.1234/EXAMPLE",
    };
    expect(studyGraphNode(item, [node])?.id).toBe("paper-a");
    expect(studyGraphNode(item, [node, { ...node, id: "paper-b" }])).toBeUndefined();
  });
});

describe("literal search and publication links", () => {
  it("matches multiple literal terms across visible fields", () => {
    expect(matchesSearch("  GAN García  ", ["GAN", "Ana Garcia"])).toBe(true);
    expect(matchesSearch("1024 gray", ["1024 × 1024", "Grayscale"])).toBe(true);
    expect(matchesSearch("wm-811k", ["WM 811K"])).toBe(false);
    expect(matchesSearch("", [])).toBe(true);
  });
  it.each(["javascript:alert(1)", "data:text/html,test", "file:///private", "not a URL"])(
    "rejects unsafe source URL %s",
    (url) => expect(safeUrl(url)).toBeNull(),
  );
  it("uses a DOI when no safe publication URL is available", () => {
    expect(publicationUrl(null, "10.1234/EXAMPLE")).toBe("https://doi.org/10.1234/example");
    expect(publicationUrl("javascript:alert(1)", "not-a-doi")).toBeNull();
  });
});

describe("directed paths", () => {
  const outgoing = new Map([
    ["a", new Set(["b", "d"])],
    ["b", new Set(["c"])],
    ["c", new Set(["a"])],
    ["d", new Set(["c"])],
    ["isolated", new Set<string>()],
  ]);
  it("finds a shortest directed path through cycles", () =>
    expect(directedPath(outgoing, "a", "c")).toEqual(["a", "b", "c"]));
  it("handles identical endpoints", () => expect(directedPath(outgoing, "a", "a")).toEqual(["a"]));
  it("does not invent links to disconnected or unknown records", () => {
    expect(directedPath(outgoing, "a", "isolated")).toBeNull();
    expect(directedPath(outgoing, "unknown", "unknown")).toBeNull();
  });
  it("respects direction", () => {
    const oneWay = new Map([
      ["source", new Set(["target"])],
      ["target", new Set<string>()],
    ]);
    expect(directedPath(oneWay, "source", "target")).toEqual(["source", "target"]);
    expect(directedPath(oneWay, "target", "source")).toBeNull();
  });
});
