// @vitest-environment jsdom
import { act, cleanup, fireEvent, render, screen, waitFor, within } from "@testing-library/react";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import citations from "../public/data/citation-trends.json";
import datasets from "../public/data/datasets.json";
import evidence from "../public/data/evidence.json";
import meta from "../public/data/meta.json";
import provenance from "../public/data/provenance.json";
import coverage from "../public/data/task-coverage.json";
import App from "./App";
import { cleanSiteUrl, GITHUB_PAGES_BASE, sitePages } from "./lib/routes";
import { useSiteData } from "./lib/site-data";
import type { SiteData } from "./types";

vi.mock("./lib/site-data", async (importOriginal) => ({
  ...(await importOriginal<typeof import("./lib/site-data")>()),
  useSiteData: vi.fn(),
}));
vi.mock("@react-sigma/core", () => ({
  SigmaContainer: () => <div data-testid="sigma-canvas" />,
  useSigma: vi.fn(),
  useRegisterEvents: vi.fn(),
}));
vi.mock("sigma/rendering", () => ({ createEdgeArrowProgram: () => class ArrowProgram {} }));

const datasetNode = datasets.datasets.find((record) => record.graphNodeId)?.graphNodeId;
const data = {
  citations,
  datasets,
  evidence,
  meta,
  provenance,
  coverage,
  graph: {
    nodes: [
      { id: "a", title: "Alpha", type: "Datasets" },
      { id: "b", title: "Beta", type: "Papers" },
      { id: datasetNode, title: "Registry node", type: "Datasets" },
    ],
    edges: [{ source: "a", target: "b" }],
  },
} as unknown as SiteData;

beforeEach(() => {
  vi.stubEnv("BASE_URL", GITHUB_PAGES_BASE);
  vi.mocked(useSiteData).mockReturnValue({ status: "ready", data });
  vi.stubGlobal(
    "IntersectionObserver",
    class {
      observe() {}
      disconnect() {}
    },
  );
  window.matchMedia = vi.fn().mockReturnValue({ matches: true });
  window.scrollTo = vi.fn();
  HTMLElement.prototype.scrollIntoView = vi.fn();
});
afterEach(() => {
  cleanup();
  vi.unstubAllEnvs();
  vi.unstubAllGlobals();
});

function openApp(path = "") {
  window.history.replaceState(null, "", `${GITHUB_PAGES_BASE}${path}`);
  const clean = cleanSiteUrl(window.location.href, GITHUB_PAGES_BASE);
  if (clean) window.history.replaceState(window.history.state, "", clean);
  return render(<App />);
}
function navigation() {
  return within(screen.getByRole("navigation", { name: "Primary navigation" }));
}

describe("GitHub Pages clean navigation", () => {
  it.each(sitePages)("opens $label directly under the repository path", async (page) => {
    openApp(page.path.slice(1));
    expect(document.title).toBe(page.title);
    expect(navigation().getByRole("link", { name: page.label }).getAttribute("aria-current")).toBe(
      "page",
    );
    for (const target of sitePages) {
      expect(navigation().getByRole("link", { name: target.label }).getAttribute("href")).toBe(
        `${GITHUB_PAGES_BASE}${target.path.slice(1)}`,
      );
    }
    expect(window.location.hash).toBe("");
    if (page.path === "/") await screen.findByTestId("sigma-canvas");
  });

  it("keeps old evidence bookmarks and nested downloads functional", () => {
    openApp("#/evidence?record=E39");
    expect(window.location.pathname).toBe(`${GITHUB_PAGES_BASE}evidence/`);
    expect(window.location.search).toBe("?record=E39");
    expect(window.location.hash).toBe("");
    expect(screen.getByRole("dialog")).toBeDefined();
    const download = document.querySelector<HTMLAnchorElement>("a[download][href$='.csv']");
    expect(download?.pathname).toBe(
      `${GITHUB_PAGES_BASE}downloads/synthesis_impact_normalized_change.csv`,
    );
  });

  it("opens graph records from a dataset without a hash or a second query update", async () => {
    const record = datasets.datasets.find((item) => item.graphNodeId === datasetNode);
    openApp(`datasets/?record=${record?.id}`);
    const link = screen.getByRole("link", { name: /Open in evidence graph/ });
    expect(link.getAttribute("href")).toBe(
      `${GITHUB_PAGES_BASE}?node=${encodeURIComponent(datasetNode ?? "")}`,
    );
    fireEvent.click(link);
    await screen.findByTestId("sigma-canvas");
    expect(window.location.pathname).toBe(GITHUB_PAGES_BASE);
    expect(new URLSearchParams(window.location.search).get("node")).toBe(datasetNode);
    expect(window.location.hash).toBe("");
  });

  it("retains graph state and canvas identity, then restores state with Back and Forward", async () => {
    openApp("#/?node=a&view=local&pin=b");
    const canvas = await screen.findByTestId("sigma-canvas");
    const state = window.history.state;
    fireEvent.click(screen.getByRole("button", { name: "2 hops" }));
    expect(screen.getByTestId("sigma-canvas")).toBe(canvas);
    expect(window.history.state).toEqual(state);
    const query = window.location.search;
    expect(query).toContain("depth=2");
    fireEvent.click(navigation().getByRole("link", { name: "Evidence" }));
    expect(window.location.pathname).toBe(`${GITHUB_PAGES_BASE}evidence/`);
    act(() => window.history.back());
    await screen.findByTestId("sigma-canvas");
    expect(window.location.search).toBe(query);
    expect(screen.getByRole("button", { name: "2 hops" }).getAttribute("aria-pressed")).toBe(
      "true",
    );
    expect((screen.getByRole("combobox", { name: "Source" }) as HTMLInputElement).value).toBe(
      "Alpha — Datasets — a",
    );
    act(() => window.history.forward());
    await waitFor(() => expect(window.location.pathname).toBe(`${GITHUB_PAGES_BASE}evidence/`));
    await waitFor(() => expect(screen.queryByTestId("sigma-canvas")).toBeNull());
  });
});
