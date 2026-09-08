// @vitest-environment jsdom
import { act, cleanup, fireEvent, render, screen, waitFor } from "@testing-library/react";
import type { DirectedGraph } from "graphology";
import type { ReactNode } from "react";
import { MemoryRouter } from "react-router-dom";
import Sigma from "sigma";
import { afterAll, afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import GraphExplorer from "./GraphExplorer";

const runtime = vi.hoisted(() => {
  // Sigma reads WebGL enums at import time; these tests never create a WebGL context.
  const enums = {
    BOOL: 0x8b56,
    BYTE: 0x1400,
    UNSIGNED_BYTE: 0x1401,
    SHORT: 0x1402,
    UNSIGNED_SHORT: 0x1403,
    INT: 0x1404,
    UNSIGNED_INT: 0x1405,
    FLOAT: 0x1406,
    TRIANGLES: 4,
  };
  vi.stubGlobal("WebGLRenderingContext", enums);
  vi.stubGlobal("WebGL2RenderingContext", enums);
  const listeners = new Set<() => void>();
  const camera = {
    ratio: 1,
    on: vi.fn((_event: string, listener: () => void) => listeners.add(listener)),
    off: vi.fn((_event: string, listener: () => void) => listeners.delete(listener)),
    getBoundedRatio: (ratio: number) => Math.max(0.025, Math.min(8, ratio)),
    getState: () => ({ x: 0.5, y: 0.5, angle: 0, ratio: camera.ratio }),
    setState: vi.fn((state: { ratio: number }) => {
      camera.ratio = state.ratio;
      listeners.forEach((listener) => listener());
    }),
  };
  return {
    camera,
    listeners,
    graph: null as DirectedGraph | null,
    settings: {} as Record<string, unknown>,
    initialized: false,
    registerEvents: vi.fn(),
  };
});
const sigma = vi.hoisted(() => ({
  getGraph: () => runtime.graph,
  getCamera: () => runtime.camera,
  refresh: vi.fn(),
  getSetting: (key: string) => runtime.settings[key],
  setSetting: vi.fn((key: string, value: unknown) => {
    runtime.settings[key] = value;
  }),
  setSettings: vi.fn((settings: Record<string, unknown>) => {
    Object.assign(runtime.settings, settings);
  }),
  getDimensions: () => ({ width: 800, height: 600 }),
  framedGraphToViewport: ({ x, y }: { x: number; y: number }) => ({ x: x * 800, y: y * 600 }),
  getNodeDisplayData: (id: string) =>
    ({
      a: { x: 0.45, y: 0.5 },
      b: { x: 0.48, y: 0.5 },
      c: { x: 0.5, y: 0.9 },
      d: { x: 0, y: 0 },
      e: { x: 1, y: 1 },
    })[id],
}));

vi.mock("@react-sigma/core", () => ({
  SigmaContainer: ({
    children,
    graph,
    settings,
  }: {
    children: ReactNode;
    graph: DirectedGraph;
    settings: Record<string, unknown>;
  }) => {
    runtime.graph = graph;
    if (!runtime.initialized) {
      runtime.settings = { ...settings };
      runtime.initialized = true;
    }
    return <div data-testid="sigma-canvas">{children}</div>;
  },
  useSigma: () => sigma,
  useRegisterEvents: () => runtime.registerEvents,
}));
vi.mock("sigma/rendering", () => ({ createEdgeArrowProgram: () => class ArrowProgram {} }));

const graph = {
  nodes: [
    { id: "a", title: "Alpha", type: "Datasets" },
    { id: "b", title: "Beta", type: "Papers" },
    { id: "c", title: "Gamma", type: "Methods" },
    { id: "d", title: "Delta", type: "Papers" },
    { id: "e", title: "Epsilon", type: "Methods" },
  ],
  edges: [
    { source: "a", target: "b" },
    { source: "b", target: "c" },
  ],
};

beforeEach(() => {
  vi.clearAllMocks();
  runtime.graph = null;
  runtime.settings = {};
  runtime.initialized = false;
  runtime.camera.ratio = 1;
  runtime.listeners.clear();
  window.history.replaceState(null, "", "/");
  window.matchMedia = vi.fn().mockReturnValue({ matches: true });
  HTMLElement.prototype.scrollIntoView = vi.fn();
});
afterEach(cleanup);
afterAll(() => vi.unstubAllGlobals());

function openGraph() {
  return render(
    <MemoryRouter>
      <GraphExplorer graph={graph} />
    </MemoryRouter>,
  );
}

describe("graph camera and labels", () => {
  it("resets the camera repeatedly and clears hover, selection, and pins", async () => {
    openGraph();
    const events = runtime.registerEvents.mock.lastCall?.[0] as {
      enterNode: (event: { node: string }) => void;
    };
    act(() => events.enterNode({ node: "d" }));
    const reduceNode = (id: string) =>
      (
        runtime.settings.nodeReducer as (
          id: string,
          data: Record<string, unknown>,
        ) => { forceLabel: boolean; highlighted: boolean; hidden: boolean }
      )(id, { color: "#60777d" });
    expect(reduceNode("d").highlighted).toBe(true);
    fireEvent.click(screen.getByRole("button", { name: "Reset view" }));
    await waitFor(() =>
      expect(runtime.camera.setState).toHaveBeenLastCalledWith(
        expect.objectContaining({ x: 0.5, y: 0.5, angle: 0 }),
      ),
    );
    expect(reduceNode("d").highlighted).toBe(false);
    const fullRatio = runtime.camera.ratio;
    fireEvent.click(screen.getByRole("button", { name: "Zoom in" }));
    expect(runtime.camera.ratio).toBeLessThan(fullRatio);
    fireEvent.click(screen.getByRole("button", { name: "Reset view" }));
    await waitFor(() => expect(runtime.camera.ratio).toBeCloseTo(fullRatio));
    fireEvent.click(screen.getByRole("button", { name: "Local neighborhood" }));
    fireEvent.click(screen.getByRole("button", { name: "Pin selected record" }));
    fireEvent.click(screen.getByRole("button", { name: "Reset view" }));
    await waitFor(() => expect(runtime.camera.ratio).toBeCloseTo(fullRatio));
    for (const node of graph.nodes) {
      expect(reduceNode(node.id)).toMatchObject({
        forceLabel: false,
        highlighted: false,
        hidden: false,
      });
    }
  });

  it("clears a full-view selection without moving the camera", async () => {
    window.history.replaceState(null, "", "/?node=b");
    openGraph();
    await waitFor(() => expect(runtime.camera.setState).toHaveBeenCalled());
    runtime.camera.setState.mockClear();
    fireEvent.click(screen.getByRole("button", { name: "Clear selection" }));
    expect(screen.getByText("Select a graph record.")).toBeDefined();
    expect(runtime.camera.setState).not.toHaveBeenCalled();
    fireEvent.click(screen.getByRole("checkbox", { name: /^Papers/ }));
    expect(runtime.camera.setState).not.toHaveBeenCalled();
  });
  it("refits the local neighborhood, two-hop scope, and full graph", async () => {
    openGraph();
    expect(runtime.camera.setState).not.toHaveBeenCalled();
    fireEvent.click(screen.getByRole("button", { name: "Local neighborhood" }));
    await waitFor(() =>
      expect(runtime.camera.setState).toHaveBeenLastCalledWith({
        x: expect.closeTo(0.465),
        y: 0.5,
        angle: 0,
        ratio: 0.16,
      }),
    );
    fireEvent.click(screen.getByRole("button", { name: "2 hops" }));
    await waitFor(() =>
      expect(runtime.camera.setState).toHaveBeenLastCalledWith(
        expect.objectContaining({ x: 0.475, y: 0.7 }),
      ),
    );
    const neighborhoodRatio = runtime.camera.ratio;
    fireEvent.click(screen.getByRole("button", { name: "Full graph" }));
    await waitFor(() =>
      expect(runtime.camera.setState).toHaveBeenLastCalledWith(
        expect.objectContaining({ x: 0.5, y: 0.5 }),
      ),
    );
    expect(runtime.camera.ratio).toBeGreaterThan(neighborhoodRatio);
  });

  it("removes the label quota at close zoom and restores it on zooming out", () => {
    openGraph();
    expect(runtime.settings.labelDensity).toBe(0.12);
    for (let step = 0; step < 4; step++) {
      fireEvent.click(screen.getByRole("button", { name: "Zoom in" }));
    }
    expect(runtime.settings.labelDensity).toBe(Infinity);
    expect(sigma.setSetting).toHaveBeenCalledTimes(1);
    fireEvent.click(screen.getByRole("button", { name: "Zoom in" }));
    expect(sigma.setSetting).toHaveBeenCalledTimes(1);
    fireEvent.click(screen.getByRole("button", { name: "Zoom out" }));
    fireEvent.click(screen.getByRole("button", { name: "Zoom out" }));
    expect(runtime.settings.labelDensity).toBe(0.12);
    expect(sigma.setSetting).toHaveBeenCalledTimes(2);
  });

  it("responds to camera updates at the exact threshold and removes its listener on unmount", () => {
    const { unmount } = openGraph();
    act(() => runtime.camera.setState({ ratio: 0.2 }));
    expect(runtime.settings.labelDensity).toBe(Infinity);
    act(() => runtime.camera.setState({ ratio: 0.21 }));
    expect(runtime.settings.labelDensity).toBe(0.12);
    expect(runtime.listeners.size).toBe(1);
    unmount();
    expect(runtime.listeners.size).toBe(0);
  });

  it("continues forcing labels for the selected record and every direct neighbor", () => {
    window.history.replaceState(null, "", "/?node=b");
    openGraph();
    const reduce = runtime.settings.nodeReducer as (
      id: string,
      data: Record<string, unknown>,
    ) => { forceLabel: boolean };
    for (const id of ["a", "b", "c"]) {
      expect(reduce(id, { color: "#60777d" }).forceLabel).toBe(true);
    }
    expect(reduce("d", { color: "#60777d" }).forceLabel).toBe(false);
  });

  it("renders ordinary on-screen labels with Sigma at close zoom without drawing hidden or offscreen labels", () => {
    openGraph();
    const draw = vi.fn();
    const node = {
      label: "Ordinary label",
      size: 5,
      x: 100,
      y: 100,
      type: "circle",
      forceLabel: false,
    };
    const renderer = {
      settings: { ...runtime.settings, defaultDrawNodeLabel: draw },
      camera: runtime.camera,
      labelGrid: { getLabelsToDisplay: vi.fn(() => ["visible", "hidden", "offscreen"]) },
      nodesWithForcedLabels: new Set(),
      displayedNodeLabels: new Set(),
      nodeDataCache: {
        visible: node,
        hidden: { ...node, hidden: true },
        offscreen: { ...node, x: -1000 },
      },
      canvasContexts: { labels: {} },
      framedGraphToViewport: ({ x, y }: { x: number; y: number }) => ({ x, y }),
      scaleSize: (size: number) => size / Math.sqrt(runtime.camera.ratio),
      width: 800,
      height: 600,
      nodePrograms: {},
    };
    // Exercise Sigma's real label-rendering method without a browser or WebGL context.
    const renderLabels = Reflect.get(Sigma.prototype, "renderLabels");
    renderLabels.call(renderer);
    expect(draw).not.toHaveBeenCalled();
    act(() => runtime.camera.setState({ ratio: 0.2 }));
    Object.assign(renderer.settings, runtime.settings);
    renderLabels.call(renderer);
    expect(renderer.labelGrid.getLabelsToDisplay).toHaveBeenLastCalledWith(0.2, Infinity);
    expect(draw).toHaveBeenCalledTimes(1);
    expect(draw.mock.calls[0][1]).toMatchObject({ key: "visible", label: "Ordinary label" });
  });
});
