// @vitest-environment jsdom
import { cleanup, fireEvent, render, screen, within } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import GraphExplorer from "./GraphExplorer";

vi.mock("@react-sigma/core", () => ({
  SigmaContainer: () => <div data-testid="sigma-canvas" />,
  useSigma: vi.fn(),
  useRegisterEvents: vi.fn(),
}));
vi.mock("sigma/rendering", () => ({ createEdgeArrowProgram: () => class ArrowProgram {} }));

const graph = {
  nodes: [
    { id: "a", title: "Alpha", type: "Datasets" },
    { id: "b", title: "Alpha extended", type: "Papers", aliases: ["Extended paper"] },
    { id: "c", title: "Gamma", type: "Methods" },
    { id: "d", title: "Shared title", type: "Papers" },
    { id: "e", title: "Shared title", type: "Methods" },
  ],
  edges: [
    { source: "a", target: "b" },
    { source: "b", target: "c" },
  ],
};
beforeEach(() => {
  window.history.replaceState(null, "", "/");
  window.matchMedia = vi.fn().mockReturnValue({ matches: true });
  HTMLElement.prototype.scrollIntoView = vi.fn();
});
afterEach(cleanup);
function openGraph() {
  render(
    <MemoryRouter>
      <GraphExplorer graph={graph} />
    </MemoryRouter>,
  );
}

describe("path endpoint interaction", () => {
  it("does not replace a typed title with a longer option label", () => {
    openGraph();
    const source = screen.getByRole("combobox", { name: "Source" }) as HTMLInputElement;
    fireEvent.change(source, { target: { value: "Alpha" } });
    expect(source.value).toBe("Alpha");
    fireEvent.change(source, { target: { value: "Alpha extended" } });
    expect(source.value).toBe("Alpha extended");
  });
  it("finds paths using stable IDs and exact aliases", () => {
    openGraph();
    fireEvent.change(screen.getByRole("combobox", { name: "Source" }), { target: { value: "a" } });
    fireEvent.change(screen.getByRole("combobox", { name: "Target" }), {
      target: { value: "Gamma" },
    });
    fireEvent.click(screen.getByRole("button", { name: "Find path" }));
    expect(screen.getByText("Path found.")).toBeDefined();
    expect(screen.getByRole("button", { name: /Alpha extended · Papers/ })).toBeDefined();
    expect(screen.getByRole("button", { name: /Show path in graph/ })).toBeDefined();
  });
  it("allows reversing direction without implying a reverse link", () => {
    openGraph();
    fireEvent.change(screen.getByRole("combobox", { name: "Source" }), {
      target: { value: "Alpha" },
    });
    fireEvent.change(screen.getByRole("combobox", { name: "Target" }), {
      target: { value: "Gamma" },
    });
    fireEvent.click(screen.getByRole("button", { name: "Reverse direction" }));
    fireEvent.click(screen.getByRole("button", { name: "Find path" }));
    expect(screen.getByText("No directed path found.")).toBeDefined();
  });
  it("requires an unambiguous endpoint", () => {
    openGraph();
    fireEvent.change(screen.getByRole("combobox", { name: "Source" }), {
      target: { value: "Shared title" },
    });
    fireEvent.change(screen.getByRole("combobox", { name: "Target" }), {
      target: { value: "Gamma" },
    });
    expect((screen.getByRole("button", { name: "Find path" }) as HTMLButtonElement).disabled).toBe(
      true,
    );
  });
  it("supports identical source and target", () => {
    openGraph();
    fireEvent.change(screen.getByRole("combobox", { name: "Source" }), {
      target: { value: "Extended paper" },
    });
    fireEvent.change(screen.getByRole("combobox", { name: "Target" }), { target: { value: "b" } });
    fireEvent.click(screen.getByRole("button", { name: "Find path" }));
    expect(screen.getByText("Same record selected.")).toBeDefined();
  });
});

describe("graph reset controls", () => {
  it("resets the complete view, search, filters, pins, path, and URL", () => {
    window.history.replaceState(
      null,
      "",
      "/?node=a&view=local&depth=2&type=Papers&from=2020&to=2025&flag=public&pin=d",
    );
    openGraph();
    fireEvent.change(screen.getByRole("combobox", { name: "Target" }), {
      target: { value: "Gamma" },
    });
    fireEvent.click(screen.getByRole("button", { name: "Find path" }));
    expect(screen.getByText("Path found.")).toBeDefined();
    fireEvent.change(screen.getByRole("searchbox", { name: "Find a title, alias, or node ID" }), {
      target: { value: "Shared" },
    });
    fireEvent.click(screen.getByRole("button", { name: "Table" }));
    fireEvent.click(screen.getByRole("button", { name: "Reset view" }));
    expect(window.location.search).toBe("");
    expect(screen.getByRole("button", { name: "Full graph" }).getAttribute("aria-pressed")).toBe(
      "true",
    );
    expect(screen.getByRole("button", { name: /^Graph$/ }).getAttribute("aria-pressed")).toBe(
      "true",
    );
    expect(screen.getByRole("region", { name: /graph showing 5 records/ })).toBeDefined();
    expect(screen.getByText("Select a graph record.")).toBeDefined();
    expect((screen.getByRole("combobox", { name: "Source" }) as HTMLInputElement).value).toBe("");
    expect((screen.getByRole("combobox", { name: "Target" }) as HTMLInputElement).value).toBe("");
    expect(
      (
        screen.getByRole("searchbox", {
          name: "Find a title, alias, or node ID",
        }) as HTMLInputElement
      ).value,
    ).toBe("");
    expect(screen.queryByText("Path found.")).toBeNull();
    expect(screen.queryByRole("button", { name: "Reset graph filters" })).toBeNull();
    for (const type of [/^Datasets/, /^Papers/, /^Methods/]) {
      expect((screen.getByRole("checkbox", { name: type }) as HTMLInputElement).checked).toBe(true);
    }
    cleanup();
    openGraph();
    expect(window.location.search).toBe("");
    expect(screen.getByText("Select a graph record.")).toBeDefined();
    fireEvent.click(screen.getByRole("button", { name: "Local neighborhood" }));
    expect(screen.getByRole("button", { name: "1 hop" }).getAttribute("aria-pressed")).toBe("true");
  });

  it("clears selection without reselecting or discarding filters, pins, and path work", () => {
    window.history.replaceState(null, "", "/?node=a&view=local&depth=2&type=Papers&pin=d");
    openGraph();
    fireEvent.change(screen.getByRole("combobox", { name: "Target" }), {
      target: { value: "Gamma" },
    });
    fireEvent.click(screen.getByRole("button", { name: "Find path" }));
    const sourceText = (screen.getByRole("combobox", { name: "Source" }) as HTMLInputElement).value;
    fireEvent.click(screen.getByRole("button", { name: "Table" }));
    fireEvent.click(screen.getByRole("button", { name: "Clear selection" }));
    expect(window.location.search).toBe("?depth=2&type=Papers&pin=d");
    expect(screen.getByText("Select a graph record.")).toBeDefined();
    expect(screen.getByText("Path found.")).toBeDefined();
    expect((screen.getByRole("combobox", { name: "Source" }) as HTMLInputElement).value).toBe(
      sourceText,
    );
    expect((screen.getByRole("combobox", { name: "Target" }) as HTMLInputElement).value).toBe(
      "Gamma",
    );
    expect(screen.getByRole("button", { name: "Table" }).getAttribute("aria-pressed")).toBe("true");
    expect(document.activeElement).toBe(screen.getByRole("button", { name: "Full graph" }));
    fireEvent.click(screen.getByRole("checkbox", { name: /^Papers/ }));
    expect(window.location.search).not.toContain("node=");
    cleanup();
    openGraph();
    expect(screen.getByText("Select a graph record.")).toBeDefined();
    expect(window.location.search).not.toContain("node=");
  });

  it("resets an empty filtered view and invalid path inputs", () => {
    openGraph();
    fireEvent.click(screen.getByRole("button", { name: "None" }));
    fireEvent.change(screen.getByRole("combobox", { name: "Source" }), {
      target: { value: "not a record" },
    });
    fireEvent.click(screen.getByRole("button", { name: "Reset view" }));
    expect(screen.getByRole("region", { name: /graph showing 5 records/ })).toBeDefined();
    expect((screen.getByRole("combobox", { name: "Source" }) as HTMLInputElement).value).toBe("");
    expect(window.location.search).toBe("");
  });
});

describe("graph scope defaults", () => {
  it("places Full graph before Local neighborhood", () => {
    openGraph();
    expect(
      within(screen.getByRole("toolbar", { name: "Graph scope" }))
        .getAllByRole("button")
        .map((button) => button.textContent),
    ).toEqual(["Full graph", "Local neighborhood"]);
  });
  it("starts with the complete graph and no implicit selection", () => {
    openGraph();
    expect(screen.getByRole("button", { name: "Full graph" }).getAttribute("aria-pressed")).toBe(
      "true",
    );
    expect((screen.getByRole("combobox", { name: "Source" }) as HTMLInputElement).value).toBe("");
    expect(window.location.search).not.toContain("node=");
    fireEvent.click(screen.getByRole("button", { name: "Table" }));
    expect(screen.getByRole("row", { name: /Gamma c Methods/ })).toBeDefined();
    expect(screen.getAllByRole("row", { name: /Shared title/ })).toHaveLength(2);
    expect(screen.getAllByRole("row")).toHaveLength(graph.nodes.length + 1);
  });
  it.each(["/?type=Papers", "/?view=invalid"])("defaults to full scope for %s", (url) => {
    window.history.replaceState(null, "", url);
    openGraph();
    expect(screen.getByRole("button", { name: "Full graph" }).getAttribute("aria-pressed")).toBe(
      "true",
    );
  });
  it("preserves an explicit local neighborhood on reload", () => {
    window.history.replaceState(null, "", "/?node=a&view=local");
    openGraph();
    expect(
      screen.getByRole("button", { name: "Local neighborhood" }).getAttribute("aria-pressed"),
    ).toBe("true");
    expect(window.location.search).toContain("view=local");
    cleanup();
    openGraph();
    expect(
      screen.getByRole("button", { name: "Local neighborhood" }).getAttribute("aria-pressed"),
    ).toBe("true");
    expect((screen.getByRole("combobox", { name: "Source" }) as HTMLInputElement).value).toBe(
      "Alpha — Datasets — a",
    );
  });
  it("serializes a manually selected local scope", () => {
    openGraph();
    fireEvent.click(screen.getByRole("button", { name: "Local neighborhood" }));
    expect(window.location.search).toContain("view=local");
    fireEvent.click(screen.getByRole("button", { name: "Full graph" }));
    expect(window.location.search).not.toContain("view=local");
  });
  it("opens a real neighborhood without requiring a previous selection", () => {
    openGraph();
    fireEvent.click(screen.getByRole("button", { name: "Local neighborhood" }));
    expect(window.location.search).toContain("node=a");
    expect(screen.getByText(/neighborhood of Alpha/)).toBeDefined();
    fireEvent.click(screen.getByRole("button", { name: "Table" }));
    expect(screen.getAllByRole("row")).toHaveLength(3);
    expect(screen.getByRole("row", { name: /Alpha extended b Papers/ })).toBeDefined();
    expect(screen.queryByRole("row", { name: /Gamma c Methods/ })).toBeNull();
    fireEvent.click(screen.getByRole("button", { name: "2 hops" }));
    expect(screen.getAllByRole("row")).toHaveLength(4);
    expect(screen.getByRole("row", { name: /Gamma c Methods/ })).toBeDefined();
    fireEvent.click(screen.getByRole("button", { name: "1 hop" }));
    expect(screen.getAllByRole("row")).toHaveLength(3);
    fireEvent.click(screen.getByRole("button", { name: "Full graph" }));
    expect(screen.getAllByRole("row")).toHaveLength(graph.nodes.length + 1);
  });
  it("centers the local view on an existing selection and follows both link directions", () => {
    window.history.replaceState(null, "", "/?node=b");
    openGraph();
    fireEvent.click(screen.getByRole("button", { name: "Local neighborhood" }));
    fireEvent.click(screen.getByRole("button", { name: "Table" }));
    expect(window.location.search).toContain("node=b");
    expect(screen.getAllByRole("row")).toHaveLength(4);
    expect(screen.getByRole("row", { name: /Alpha a Datasets/ })).toBeDefined();
    expect(screen.getByRole("row", { name: /Gamma c Methods/ })).toBeDefined();
  });
  it.each(["/?view=local", "/?view=local&node=missing"])(
    "recovers a local URL without a valid center: %s",
    (url) => {
      window.history.replaceState(null, "", url);
      openGraph();
      expect(window.location.search).toContain("node=a");
      expect(screen.getByRole("region", { name: /graph showing 2 records/ })).toBeDefined();
    },
  );
  it("chooses a center within the active filters", () => {
    openGraph();
    fireEvent.click(screen.getByRole("checkbox", { name: /^Datasets/ }));
    fireEvent.click(screen.getByRole("button", { name: "Local neighborhood" }));
    expect(window.location.search).toContain("node=b");
    fireEvent.click(screen.getByRole("button", { name: "Table" }));
    expect(screen.getAllByRole("row")).toHaveLength(3);
    expect(screen.queryByRole("row", { name: /Alpha a Datasets/ })).toBeNull();
  });
  it("keeps empty filters empty and initializes a neighborhood after resetting them", () => {
    openGraph();
    fireEvent.click(screen.getByRole("button", { name: "None" }));
    fireEvent.click(screen.getByRole("button", { name: "Local neighborhood" }));
    expect(screen.getByText("No records match these filters.")).toBeDefined();
    expect(window.location.search).not.toContain("node=");
    fireEvent.click(screen.getByRole("button", { name: "Reset graph filters" }));
    expect(screen.getByRole("region", { name: /graph showing 2 records/ })).toBeDefined();
  });
});
