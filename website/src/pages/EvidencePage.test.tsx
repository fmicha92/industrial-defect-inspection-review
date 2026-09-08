// @vitest-environment jsdom
import { cleanup, fireEvent, render, screen, within } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import datasetBundle from "../../public/data/datasets.json";
import evidenceBundle from "../../public/data/evidence.json";
import type { SiteData } from "../types";
import EvidencePage from "./EvidencePage";

const data = {
  datasets: datasetBundle,
  evidence: evidenceBundle,
  graph: { nodes: [], edges: [] },
} as unknown as SiteData;

beforeEach(() => {
  vi.stubGlobal(
    "IntersectionObserver",
    class {
      observe() {}
      disconnect() {}
    },
  );
  window.matchMedia = vi.fn().mockReturnValue({ matches: true });
  HTMLElement.prototype.scrollIntoView = vi.fn();
});
afterEach(() => {
  cleanup();
  vi.unstubAllGlobals();
});
function openEvidence(path = "/evidence") {
  return render(
    <MemoryRouter initialEntries={[path]}>
      <EvidencePage data={data} />
    </MemoryRouter>,
  );
}
function comparisonTable() {
  return screen.getByRole("table", {
    name: /^Synthesis-supported evidence comparisons matching/,
  });
}

describe("complete evidence page", () => {
  it.each(["/evidence", "/evidence?page=4"])("shows every comparison on %s", (path) => {
    openEvidence(path);
    const table = comparisonTable();
    expect(within(table).getAllByRole("row")).toHaveLength(40);
    for (const item of evidenceBundle.items) {
      expect(within(table).getByRole("button", { name: `Open ${item.id}` })).toBeDefined();
    }
    expect(screen.queryByRole("navigation", { name: "Results pages" })).toBeNull();
  });

  it("shows the distribution without a collapsed disclosure", () => {
    openEvidence();
    const distribution = screen.getByRole("group", {
      name: "Distribution of 39 positive representative normalized-change values",
    });
    expect(distribution.closest("details")).toBeNull();
    expect(within(distribution).getAllByRole("button")).toHaveLength(39);
    expect(screen.getByText("Normalized change distribution")).toBeDefined();
  });

  it("filters all records without changing the review-wide distribution", () => {
    openEvidence();
    fireEvent.change(screen.getByRole("textbox", { name: "Search evidence" }), {
      target: { value: "E39" },
    });
    const table = comparisonTable();
    expect(within(table).getAllByRole("row")).toHaveLength(2);
    expect(within(table).getByRole("button", { name: "Open E39" })).toBeDefined();
    const distribution = screen.getByRole("group", {
      name: "Distribution of 39 positive representative normalized-change values",
    });
    expect(within(distribution).getAllByRole("button")).toHaveLength(39);
    fireEvent.click(screen.getByRole("button", { name: "Reset" }));
    expect(within(comparisonTable()).getAllByRole("row")).toHaveLength(40);
  });

  it("sorts the entire collection by dataset", () => {
    openEvidence("/evidence?sort=dataset");
    const rows = within(comparisonTable()).getAllByRole("row").slice(1);
    const expected = [...evidenceBundle.items].sort(
      (a, b) => a.dataset.localeCompare(b.dataset) || a.ordinal - b.ordinal,
    );
    expect(rows).toHaveLength(expected.length);
    rows.forEach((row, index) => {
      expect(within(row).getByRole("button", { name: `Open ${expected[index].id}` })).toBeDefined();
    });
  });

  it("opens a study from the visible distribution", () => {
    openEvidence();
    const distribution = screen.getByRole("group", {
      name: "Distribution of 39 positive representative normalized-change values",
    });
    fireEvent.click(within(distribution).getByRole("button", { name: /^E39:/ }));
    expect(screen.getByRole("dialog")).toBeDefined();
    expect(within(screen.getByRole("dialog")).getByText("E39")).toBeDefined();
  });

  it("retains the original dashboard and table arrangement", () => {
    const view = openEvidence();
    const dashboard = view.container.querySelector(".evidence-dashboard");
    const filters = view.container.querySelector(".filter-bar");
    const distribution = view.container.querySelector("#change-distribution");
    expect(dashboard).not.toBeNull();
    expect(filters).not.toBeNull();
    expect(dashboard?.contains(distribution)).toBe(true);
    expect(
      dashboard!.compareDocumentPosition(filters!) & Node.DOCUMENT_POSITION_FOLLOWING,
    ).toBeTruthy();
    expect(view.container.querySelector(".summary-disclosure")).toBeNull();
    expect(view.container.querySelector(".section-nav")).toBeNull();
  });
});
