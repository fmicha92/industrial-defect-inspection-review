import "@react-sigma/core/lib/style.css";
import "./GraphExplorer.css";

import { SigmaContainer, useRegisterEvents, useSigma } from "@react-sigma/core";
import { DirectedGraph } from "graphology";
import {
  ArrowRight,
  ChevronLeft,
  ChevronRight,
  ExternalLink,
  List,
  Network,
  Pin,
  PinOff,
  RotateCcw,
  Search,
  X,
  ZoomIn,
  ZoomOut,
} from "lucide-react";
import {
  Component,
  type CSSProperties,
  type ErrorInfo,
  type KeyboardEvent,
  type ReactNode,
  useCallback,
  useEffect,
  useId,
  useMemo,
  useRef,
  useState,
} from "react";
import { Link } from "react-router-dom";
import { createEdgeArrowProgram } from "sigma/rendering";
import type { Settings } from "sigma/settings";
import { directedPath, studyGraphNode } from "../lib/navigation";
import type { Dataset, EvidenceItem } from "../types";

export interface GraphNode {
  id: string;
  title: string;
  type: string;
  aliases?: string[];
  year?: number;
  paperType?: string;
  availability?: string;
  doi?: string;
  url?: string;
  sourceNote?: string;
  isManufacturingDataset?: boolean;
  isPublicDataset?: boolean;
  isSynthesisCandidate?: boolean;
}

export interface GraphEdge {
  source: string;
  target: string;
}

export interface GraphBundle {
  nodes: GraphNode[];
  edges: GraphEdge[];
}

export interface GraphExplorerProps {
  graph: GraphBundle;
  headingId?: string;
  datasets?: Dataset[];
  evidence?: EvidenceItem[];
}

type ViewMode = "local" | "full";
type PresentationMode = "graph" | "table";
type CandidateFlag = "manufacturing" | "public" | "synthesis";

type SigmaNodeAttributes = Record<string, unknown> & {
  label: string;
  x: number;
  y: number;
  size: number;
  color: string;
  nodeType: string;
  record: GraphNode;
  zIndex: number;
};

type SigmaEdgeAttributes = Record<string, unknown> & {
  sourceId: string;
  targetId: string;
  size: number;
  color: string;
  type: "arrow";
  zIndex: number;
};

interface GraphModel {
  graph: DirectedGraph<SigmaNodeAttributes, SigmaEdgeAttributes>;
  nodes: GraphNode[];
  nodeById: Map<string, GraphNode>;
  incoming: Map<string, Set<string>>;
  outgoing: Map<string, Set<string>>;
  types: string[];
  years: number[];
  warnings: string[];
  error: string | null;
}

interface UrlState {
  nodeId: string | null;
  viewMode: ViewMode;
  depth: 1 | 2;
  typeMode: "all" | "none" | "some";
  types: string[];
  yearFrom: string;
  yearTo: string;
  flags: CandidateFlag[];
  pins: string[];
}

type FocusRequest = {
  token: number;
} & ({ scope: "visible" } | { scope: "selection"; id: string; ids?: string[] });

interface PathResult {
  kind: "idle" | "found" | "missing";
  nodes: string[];
}

const BASE_NODE_SIZE = 5;
const LABEL_DETAIL_RATIO = 0.2;
const OVERVIEW_LABEL_DENSITY = 0.12;
const CLOSE_FOCUS_RATIO = 0.16;
const NEIGHBORHOOD_FIT_MARGIN = 1.08;
const TABLE_PAGE_SIZE = 40;
const EDGE_COLOR = "#aebdc0";
const MUTED_NODE_COLOR = "#c8d4d5";
const MUTED_EDGE_COLOR = "#d9e1e2";
const OUTGOING_EDGE_COLOR = "#2d7182";
const INCOMING_EDGE_COLOR = "#fa994a";

const TYPE_COLORS: Record<string, string> = {
  bases: "#60777d",
  benchmarks: "#12333e",
  concepts: "#2f9578",
  datasets: "#41b8aa",
  domains: "#f03630",
  "learning paradigms": "#80629a",
  methods: "#fa994a",
  metrics: "#f2c658",
  papers: "#194454",
  tasks: "#2d7182",
};

const CANDIDATE_LABELS: Record<CandidateFlag, string> = {
  manufacturing: "Manufacturing dataset screen",
  public: "Documented public dataset",
  synthesis: "Synthesis pre-screen candidate",
};

const SIGMA_SETTINGS: Partial<Settings<SigmaNodeAttributes, SigmaEdgeAttributes>> = {
  defaultNodeColor: "#60777d",
  defaultEdgeColor: EDGE_COLOR,
  defaultEdgeType: "arrow",
  edgeProgramClasses: {
    arrow: createEdgeArrowProgram<SigmaNodeAttributes, SigmaEdgeAttributes>(),
  },
  enableEdgeEvents: false,
  hideEdgesOnMove: true,
  hideLabelsOnMove: true,
  labelColor: { color: "#12333e" },
  labelDensity: OVERVIEW_LABEL_DENSITY,
  labelFont: '"Segoe UI Variable", "Aptos", system-ui, sans-serif',
  labelGridCellSize: 120,
  labelRenderedSizeThreshold: 8,
  labelSize: 12,
  labelWeight: "600",
  maxCameraRatio: 8,
  minCameraRatio: 0.025,
  minEdgeThickness: 0.4,
  renderEdgeLabels: false,
  renderLabels: true,
  stagePadding: 34,
  zIndex: true,
};

function normalizeText(value: string): string {
  return value
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLocaleLowerCase()
    .trim();
}

function stableHash(value: string): number {
  let hash = 2166136261;
  for (let index = 0; index < value.length; index += 1) {
    hash ^= value.charCodeAt(index);
    hash = Math.imul(hash, 16777619);
  }
  return hash >>> 0;
}

function positionForNode(id: string): { x: number; y: number } {
  const angle = (stableHash(`${id}:angle`) / 0xffffffff) * Math.PI * 2;
  const radius = 8 + Math.sqrt(stableHash(`${id}:radius`) / 0xffffffff) * 92;
  return { x: Math.cos(angle) * radius, y: Math.sin(angle) * radius };
}

function colorForType(type: string): string {
  return TYPE_COLORS[type.toLocaleLowerCase()] ?? "#60777d";
}

function buildModel(bundle: GraphBundle): GraphModel {
  const graph = new DirectedGraph<SigmaNodeAttributes, SigmaEdgeAttributes>({
    allowSelfLoops: true,
    multi: false,
  });
  const empty: GraphModel = {
    graph,
    nodes: [],
    nodeById: new Map(),
    incoming: new Map(),
    outgoing: new Map(),
    types: [],
    years: [],
    warnings: [],
    error: null,
  };
  if (!bundle || !Array.isArray(bundle.nodes) || !Array.isArray(bundle.edges)) {
    return { ...empty, error: "The graph bundle is missing its nodes or edges array." };
  }

  const nodeById = new Map<string, GraphNode>();
  const incoming = new Map<string, Set<string>>();
  const outgoing = new Map<string, Set<string>>();
  const nodes: GraphNode[] = [];
  for (const candidate of bundle.nodes) {
    if (
      !candidate ||
      typeof candidate.id !== "string" ||
      candidate.id.length === 0 ||
      typeof candidate.title !== "string" ||
      candidate.title.length === 0 ||
      typeof candidate.type !== "string" ||
      candidate.type.length === 0
    ) {
      return { ...empty, error: "At least one node is missing a non-empty id, title, or type." };
    }
    if (nodeById.has(candidate.id))
      return { ...empty, error: `Duplicate node id: ${candidate.id}` };
    const node = {
      ...candidate,
      aliases: Array.isArray(candidate.aliases)
        ? candidate.aliases.filter((alias): alias is string => typeof alias === "string")
        : [],
    };
    nodes.push(node);
    nodeById.set(node.id, node);
    incoming.set(node.id, new Set());
    outgoing.set(node.id, new Set());
    graph.addNode(node.id, {
      ...positionForNode(node.id),
      color: colorForType(node.type),
      label: node.title,
      nodeType: node.type,
      record: node,
      size: BASE_NODE_SIZE,
      zIndex: 0,
    });
  }

  let invalidEdges = 0;
  let duplicateEdges = 0;
  const pairs = new Set<string>();
  bundle.edges.forEach((edge, index) => {
    if (
      !edge ||
      typeof edge.source !== "string" ||
      typeof edge.target !== "string" ||
      !nodeById.has(edge.source) ||
      !nodeById.has(edge.target)
    ) {
      invalidEdges += 1;
      return;
    }
    const pair = JSON.stringify([edge.source, edge.target]);
    if (pairs.has(pair)) {
      duplicateEdges += 1;
      return;
    }
    pairs.add(pair);
    outgoing.get(edge.source)?.add(edge.target);
    incoming.get(edge.target)?.add(edge.source);
    graph.addDirectedEdgeWithKey(`graph-edge-${index}`, edge.source, edge.target, {
      color: EDGE_COLOR,
      size: 0.65,
      sourceId: edge.source,
      targetId: edge.target,
      type: "arrow",
      zIndex: 0,
    });
  });

  const warnings: string[] = [];
  if (invalidEdges) warnings.push(`${invalidEdges} edge(s) with unknown endpoints were omitted`);
  if (duplicateEdges) warnings.push(`${duplicateEdges} duplicate directed edge(s) were omitted`);
  return {
    graph,
    incoming,
    nodeById,
    nodes,
    outgoing,
    types: [...new Set(nodes.map((node) => node.type))].sort((a, b) => a.localeCompare(b)),
    years: [...new Set(nodes.flatMap((node) => (node.year === undefined ? [] : [node.year])))].sort(
      (a, b) => a - b,
    ),
    warnings,
    error: null,
  };
}

function readUrlState(): UrlState {
  const defaults: UrlState = {
    nodeId: null,
    viewMode: "full",
    depth: 1,
    typeMode: "all",
    types: [],
    yearFrom: "",
    yearTo: "",
    flags: [],
    pins: [],
  };
  if (typeof window === "undefined") return defaults;
  const params = new URLSearchParams(window.location.search);
  const flags = params
    .getAll("flag")
    .filter((flag): flag is CandidateFlag =>
      (["manufacturing", "public", "synthesis"] as string[]).includes(flag),
    );
  const types = params.getAll("type");
  return {
    nodeId: params.get("node"),
    viewMode: params.get("view") === "local" ? "local" : "full",
    depth: params.get("depth") === "2" ? 2 : 1,
    typeMode: params.get("types") === "none" ? "none" : types.length ? "some" : "all",
    types,
    yearFrom: params.get("from") ?? "",
    yearTo: params.get("to") ?? "",
    flags,
    pins: params.getAll("pin"),
  };
}

function writeUrlState(state: UrlState, allTypes: string[]): void {
  if (typeof window === "undefined") return;
  const params = new URLSearchParams(window.location.search);
  for (const key of ["node", "view", "depth", "types", "type", "from", "to", "flag", "pin"]) {
    params.delete(key);
  }
  if (state.nodeId) params.set("node", state.nodeId);
  if (state.viewMode === "local") params.set("view", "local");
  if (state.depth === 2) params.set("depth", "2");
  if (state.typeMode === "none") params.set("types", "none");
  if (state.typeMode === "some") {
    state.types
      .filter((type) => allTypes.includes(type))
      .sort((a, b) => a.localeCompare(b))
      .forEach((type) => {
        params.append("type", type);
      });
  }
  if (state.yearFrom) params.set("from", state.yearFrom);
  if (state.yearTo) params.set("to", state.yearTo);
  state.flags.forEach((flag) => {
    params.append("flag", flag);
  });
  state.pins.forEach((pin) => {
    params.append("pin", pin);
  });
  const query = params.toString();
  const nextSearch = query ? `?${query}` : "";
  if (nextSearch !== window.location.search) {
    // Preserve router history and the mounted canvas while editing graph state.
    window.history.replaceState(
      window.history.state,
      "",
      `${window.location.pathname}${nextSearch}${window.location.hash}`,
    );
  }
}

function neighborhood(
  model: GraphModel,
  center: string,
  depth: 1 | 2,
  allowed: Set<string>,
): Set<string> {
  const visited = new Set([center]);
  let frontier = new Set([center]);
  for (let level = 0; level < depth; level += 1) {
    const next = new Set<string>();
    frontier.forEach((id) => {
      model.outgoing.get(id)?.forEach((neighbor) => {
        if (allowed.has(neighbor) && !visited.has(neighbor)) next.add(neighbor);
      });
      model.incoming.get(id)?.forEach((neighbor) => {
        if (allowed.has(neighbor) && !visited.has(neighbor)) next.add(neighbor);
      });
    });
    next.forEach((id) => {
      visited.add(id);
    });
    frontier = next;
  }
  return visited;
}

function directNeighbors(model: GraphModel, id: string | null): Set<string> {
  if (!id) return new Set();
  return new Set([...(model.incoming.get(id) ?? []), ...(model.outgoing.get(id) ?? [])]);
}

function safeExternalUrl(value?: string): string | null {
  if (!value) return null;
  try {
    const url = new URL(value);
    return url.protocol === "http:" || url.protocol === "https:" ? url.href : null;
  } catch {
    return null;
  }
}

function doiUrl(value?: string): string | null {
  if (!value) return null;
  const doi = value.replace(/^https?:\/\/(?:dx\.)?doi\.org\//i, "").trim();
  return safeExternalUrl(`https://doi.org/${encodeURI(doi)}`);
}

function searchRank(node: GraphNode, query: string): number | null {
  const title = normalizeText(node.title);
  const id = normalizeText(node.id);
  const aliases = (node.aliases ?? []).map(normalizeText);
  if (title === query) return 0;
  if (id === query) return 1;
  if (aliases.includes(query)) return 2;
  if (title.startsWith(query)) return 3;
  if (aliases.some((alias) => alias.startsWith(query))) return 4;
  if (title.includes(query)) return 5;
  if (aliases.some((alias) => alias.includes(query))) return 6;
  return id.includes(query) ? 7 : null;
}

function pathOptionLabel(node: GraphNode): string {
  return `${node.title} — ${node.type} — ${node.id}`;
}

function matchesFlag(node: GraphNode, flags: Set<CandidateFlag>): boolean {
  if (!flags.size) return true;
  return (
    (flags.has("manufacturing") && node.isManufacturingDataset === true) ||
    (flags.has("public") && node.isPublicDataset === true) ||
    (flags.has("synthesis") && node.isSynthesisCandidate === true)
  );
}

function relationLabel(model: GraphModel, selected: string | null, node: string): string {
  if (!selected) return "Filtered graph record";
  if (selected === node) return "Selected record";
  const outgoing = model.outgoing.get(selected)?.has(node) ?? false;
  const incoming = model.incoming.get(selected)?.has(node) ?? false;
  if (outgoing && incoming) return "Incoming and outgoing wikilinks";
  if (outgoing) return "Outgoing wikilink from selection";
  if (incoming) return "Incoming wikilink to selection";
  return "Visible filtered record";
}

function reducedMotion(): boolean {
  return (
    typeof window !== "undefined" && window.matchMedia("(prefers-reduced-motion: reduce)").matches
  );
}

interface CanvasControllerProps {
  focus: FocusRequest | null;
  incoming: Map<string, Set<string>>;
  outgoing: Map<string, Set<string>>;
  pathNodes: string[];
  onSelect: (id: string) => void;
  pinned: Set<string>;
  selected: string | null;
  selectedNeighbors: Set<string>;
  visible: Set<string>;
}

function CanvasController({
  focus,
  incoming,
  outgoing,
  pathNodes,
  onSelect,
  pinned,
  selected,
  selectedNeighbors,
  visible,
}: CanvasControllerProps) {
  const sigma = useSigma<SigmaNodeAttributes, SigmaEdgeAttributes>();
  const registerEvents = useRegisterEvents<SigmaNodeAttributes, SigmaEdgeAttributes>();
  const [hovered, setHovered] = useState<string | null>(null);
  useEffect(() => {
    const camera = sigma.getCamera();
    const updateLabelDensity = () => {
      // At close zoom, off-screen candidates must not consume the label grid quota.
      const density = camera.ratio <= LABEL_DETAIL_RATIO ? Infinity : OVERVIEW_LABEL_DENSITY;
      if (sigma.getSetting("labelDensity") !== density) sigma.setSetting("labelDensity", density);
    };
    updateLabelDensity();
    camera.on("updated", updateLabelDensity);
    return () => {
      camera.off("updated", updateLabelDensity);
    };
  }, [sigma]);
  useEffect(() => {
    const graph = sigma.getGraph();
    graph.forEachNode((id) => graph.mergeNodeAttributes(id, positionForNode(id)));
    sigma.refresh();
  }, [sigma]);
  const active = hovered ?? selected;
  const neighbors = useMemo(
    () => new Set(active ? [...(incoming.get(active) ?? []), ...(outgoing.get(active) ?? [])] : []),
    [active, incoming, outgoing],
  );
  const pathNodeSet = useMemo(() => new Set(pathNodes), [pathNodes]);
  const pathEdges = useMemo(
    () => new Set(pathNodes.slice(1).map((id, index) => JSON.stringify([pathNodes[index], id]))),
    [pathNodes],
  );
  useEffect(() => setHovered(null), [selected, focus]);

  useEffect(() => {
    registerEvents({
      clickNode: ({ node }) => onSelect(node),
      clickStage: () => setHovered(null),
      enterNode: ({ node }) => setHovered(node),
      leaveNode: () => setHovered(null),
    });
  }, [onSelect, registerEvents]);

  useEffect(() => {
    sigma.setSettings({
      edgeReducer: (_edge, data) => {
        if (
          data.sourceId === data.targetId ||
          !visible.has(data.sourceId) ||
          !visible.has(data.targetId)
        ) {
          return { ...data, hidden: true };
        }
        if (pathEdges.has(JSON.stringify([data.sourceId, data.targetId]))) {
          return { ...data, color: "#cc7926", hidden: false, size: 2.8, zIndex: 4 };
        }
        if (data.sourceId === active) {
          return { ...data, color: OUTGOING_EDGE_COLOR, hidden: false, size: 1.45, zIndex: 2 };
        }
        if (data.targetId === active) {
          return { ...data, color: INCOMING_EDGE_COLOR, hidden: false, size: 1.45, zIndex: 2 };
        }
        return {
          ...data,
          color: active ? MUTED_EDGE_COLOR : EDGE_COLOR,
          hidden: false,
          size: active ? 0.4 : 0.65,
          zIndex: 0,
        };
      },
      nodeReducer: (node, data) => {
        if (!visible.has(node)) return { ...data, hidden: true };
        const isActive = node === active;
        const isNeighbor = active ? neighbors.has(node) : true;
        const isPinned = pinned.has(node);
        const isPath = pathNodeSet.has(node);
        const isSelected = node === selected;
        const isSelectedNeighbor = selected !== null && selectedNeighbors.has(node);
        return {
          ...data,
          color: isPath
            ? "#cc7926"
            : active && !isActive && !isNeighbor && !isPinned
              ? MUTED_NODE_COLOR
              : data.color,
          forceLabel: isPath || isActive || isPinned || isSelected || isSelectedNeighbor,
          hidden: false,
          highlighted: isActive,
          size: isPath || isActive ? 7.5 : isPinned ? 6 : BASE_NODE_SIZE,
          zIndex: isPath ? 5 : isActive ? 3 : isPinned ? 2 : isNeighbor ? 1 : 0,
        };
      },
    });
  }, [
    active,
    neighbors,
    pathEdges,
    pathNodeSet,
    pinned,
    selected,
    selectedNeighbors,
    sigma,
    visible,
  ]);

  const fitNodes = useCallback(
    (ids: Iterable<string>) => {
      const focusIds = new Set(ids);
      const points = [...focusIds]
        .filter((id) => visible.has(id))
        .map((id) => sigma.getNodeDisplayData(id))
        .filter((data): data is NonNullable<typeof data> => data !== undefined);
      if (!points.length) return;

      const camera = sigma.getCamera();
      const minX = Math.min(...points.map(({ x }) => x));
      const maxX = Math.max(...points.map(({ x }) => x));
      const minY = Math.min(...points.map(({ y }) => y));
      const maxY = Math.max(...points.map(({ y }) => y));
      const center = { x: (minX + maxX) / 2, y: (minY + maxY) / 2 };

      let ratio = CLOSE_FOCUS_RATIO;
      if (points.length > 1) {
        const dimensions = sigma.getDimensions();
        const referenceState = { ...center, angle: 0, ratio: 1 };
        const firstCorner = sigma.framedGraphToViewport(
          { x: minX, y: minY },
          { cameraState: referenceState },
        );
        const secondCorner = sigma.framedGraphToViewport(
          { x: maxX, y: maxY },
          { cameraState: referenceState },
        );
        const horizontalPadding = Math.min(112, Math.max(48, dimensions.width * 0.13));
        const verticalPadding = Math.min(92, Math.max(58, dimensions.height * 0.12));
        const availableWidth = Math.max(80, dimensions.width - horizontalPadding * 2);
        const availableHeight = Math.max(80, dimensions.height - verticalPadding * 2);
        const requiredRatio = Math.max(
          Math.abs(secondCorner.x - firstCorner.x) / availableWidth,
          Math.abs(secondCorner.y - firstCorner.y) / availableHeight,
        );
        ratio = Math.max(CLOSE_FOCUS_RATIO, requiredRatio * NEIGHBORHOOD_FIT_MARGIN);
      }

      const state = {
        ...center,
        angle: 0,
        ratio: camera.getBoundedRatio(ratio),
      };
      if (reducedMotion()) camera.setState(state);
      else void camera.animate(state, { duration: 320 });
    },
    [sigma, visible],
  );
  useEffect(() => {
    if (!focus || (focus.scope === "selection" && !visible.has(focus.id))) return;
    const frame = window.requestAnimationFrame(() =>
      fitNodes(
        focus.scope === "visible" ? visible : (focus.ids ?? [focus.id, ...selectedNeighbors]),
      ),
    );
    return () => window.cancelAnimationFrame(frame);
  }, [fitNodes, focus, selectedNeighbors, visible]);

  const zoomIn = () => {
    const camera = sigma.getCamera();
    if (reducedMotion()) camera.setState({ ratio: camera.getBoundedRatio(camera.ratio / 1.5) });
    else void camera.animatedZoom({ duration: 180, factor: 1.5 });
  };
  const zoomOut = () => {
    const camera = sigma.getCamera();
    if (reducedMotion()) camera.setState({ ratio: camera.getBoundedRatio(camera.ratio * 1.5) });
    else void camera.animatedUnzoom({ duration: 180, factor: 1.5 });
  };
  const reset = () => fitNodes(visible);

  return (
    <>
      <p className="graph-canvas-caption">
        {hovered
          ? sigma.getGraph().getNodeAttribute(hovered, "label")
          : "Select a record to explore its connections. Zoom in to reveal node labels, or hover for a full title."}
      </p>
      <div className="graph-canvas-controls" role="toolbar" aria-label="Graph camera controls">
        <button className="graph-icon-button" type="button" onClick={zoomIn} aria-label="Zoom in">
          <ZoomIn size={18} aria-hidden="true" />
        </button>
        <button className="graph-icon-button" type="button" onClick={zoomOut} aria-label="Zoom out">
          <ZoomOut size={18} aria-hidden="true" />
        </button>
        <button className="graph-icon-button" type="button" onClick={reset} aria-label="Fit graph">
          <RotateCcw size={17} aria-hidden="true" />
        </button>
      </div>
      <div className="graph-direction-key" aria-hidden="true">
        <span>
          <span className="graph-direction-out">→</span> link from active record
        </span>
        <span>
          <span className="graph-direction-in">→</span> link to active record
        </span>
      </div>
    </>
  );
}

interface RuntimeBoundaryProps {
  children: ReactNode;
  resetKey: string;
}

class RuntimeBoundary extends Component<RuntimeBoundaryProps, { failed: boolean }> {
  state = { failed: false };

  static getDerivedStateFromError() {
    return { failed: true };
  }

  componentDidCatch(_error: Error, _info: ErrorInfo): void {
    // The table view remains the complete non-WebGL representation.
  }

  componentDidUpdate(previous: RuntimeBoundaryProps): void {
    if (previous.resetKey !== this.props.resetKey && this.state.failed)
      this.setState({ failed: false });
  }

  render() {
    if (this.state.failed) {
      return (
        <div className="graph-runtime-error" role="alert">
          <strong>The interactive canvas is unavailable.</strong>
          <p>Use the table view to search, select, and inspect the same graph records.</p>
        </div>
      );
    }
    return this.props.children;
  }
}

function GraphExplorer({
  graph: bundle,
  headingId,
  datasets = [],
  evidence = [],
}: GraphExplorerProps) {
  const suffix = useId().replace(/:/g, "");
  const titleId = headingId ?? `graph-title-${suffix}`;
  const searchId = `graph-search-${suffix}`;
  const resultsId = `graph-results-${suffix}`;
  const pathOptionsId = `graph-path-options-${suffix}`;
  const model = useMemo(() => buildModel(bundle), [bundle]);
  const initialState = useRef(readUrlState()).current;

  const [selected, setSelected] = useState<string | null>(() =>
    initialState.nodeId && model.nodeById.has(initialState.nodeId) ? initialState.nodeId : null,
  );
  const [view, setView] = useState<ViewMode>(initialState.viewMode);
  const [depth, setDepth] = useState<1 | 2>(initialState.depth);
  const [presentation, setPresentation] = useState<PresentationMode>("graph");
  const [types, setTypes] = useState<Set<string>>(() => {
    if (initialState.typeMode === "none") return new Set();
    if (initialState.typeMode === "some") {
      return new Set(initialState.types.filter((type) => model.types.includes(type)));
    }
    return new Set(model.types);
  });
  const [yearFrom, setYearFrom] = useState(initialState.yearFrom);
  const [yearTo, setYearTo] = useState(initialState.yearTo);
  const [flags, setFlags] = useState<Set<CandidateFlag>>(() => new Set(initialState.flags));
  const [pinned, setPinned] = useState<Set<string>>(
    () => new Set(initialState.pins.filter((id) => model.nodeById.has(id))),
  );
  const [focus, setFocus] = useState<FocusRequest | null>(() =>
    initialState.viewMode === "local"
      ? { scope: "visible", token: 1 }
      : selected
        ? { scope: "selection", id: selected, token: 1 }
        : null,
  );
  const [filtersOpen, setFiltersOpen] = useState(false);
  const [query, setQuery] = useState("");
  const [searchOpen, setSearchOpen] = useState(false);
  const [page, setPage] = useState(0);
  const [pathSource, setPathSource] = useState(selected ?? "");
  const [pathSourceQuery, setPathSourceQuery] = useState(() => {
    const node = selected ? model.nodeById.get(selected) : null;
    return node ? pathOptionLabel(node) : "";
  });
  const [pathTarget, setPathTarget] = useState("");
  const [pathTargetQuery, setPathTargetQuery] = useState("");
  const [path, setPath] = useState<PathResult>({ kind: "idle", nodes: [] });
  const searchButtons = useRef<Array<HTMLButtonElement | null>>([]);
  const detailsHeading = useRef<HTMLHeadingElement | null>(null);
  const fullViewButton = useRef<HTMLButtonElement | null>(null);
  const [detailsFocusToken, setDetailsFocusToken] = useState(0);
  const pathResult = useRef<HTMLDivElement | null>(null);
  const [pathResultFocusToken, setPathResultFocusToken] = useState(0);

  useEffect(() => {
    if (selected && !model.nodeById.has(selected)) setSelected(null);
    setPinned((current) => new Set([...current].filter((id) => model.nodeById.has(id))));
  }, [model.nodeById, selected]);

  useEffect(() => {
    const typeMode = types.size === 0 ? "none" : types.size === model.types.length ? "all" : "some";
    writeUrlState(
      {
        nodeId: selected,
        viewMode: view,
        depth,
        typeMode,
        types: [...types],
        yearFrom,
        yearTo,
        flags: [...flags].sort(),
        pins: [...pinned].sort(),
      },
      model.types,
    );
  }, [depth, flags, model.types, pinned, selected, types, view, yearFrom, yearTo]);

  useEffect(() => {
    if (detailsFocusToken === 0) return;
    const frame = window.requestAnimationFrame(() => detailsHeading.current?.focus());
    return () => window.cancelAnimationFrame(frame);
  }, [detailsFocusToken]);

  useEffect(() => {
    if (pathResultFocusToken === 0) return;
    const frame = window.requestAnimationFrame(() => {
      const result = pathResult.current;
      if (!result) return;
      result.focus({ preventScroll: true });
      result.scrollIntoView({
        behavior: reducedMotion() ? "auto" : "smooth",
        block: "nearest",
      });
    });
    return () => window.cancelAnimationFrame(frame);
  }, [pathResultFocusToken]);

  const typeCounts = useMemo(() => {
    const counts = new Map<string, number>();
    model.nodes.forEach((node) => {
      counts.set(node.type, (counts.get(node.type) ?? 0) + 1);
    });
    return counts;
  }, [model.nodes]);
  const from = yearFrom ? Number(yearFrom) : null;
  const to = yearTo ? Number(yearTo) : null;
  const reversedYears = from !== null && to !== null && from > to;

  const filtered = useMemo(() => {
    const result = new Set<string>();
    if (reversedYears) return result;
    model.nodes.forEach((node) => {
      if (!types.has(node.type)) return;
      if (from !== null && (node.year === undefined || node.year < from)) return;
      if (to !== null && (node.year === undefined || node.year > to)) return;
      if (!matchesFlag(node, flags)) return;
      result.add(node.id);
    });
    return result;
  }, [flags, from, model.nodes, reversedYears, to, types]);

  const visible = useMemo(() => {
    let result: Set<string>;
    if (view === "local") {
      result =
        selected && model.nodeById.has(selected)
          ? neighborhood(model, selected, depth, filtered)
          : new Set();
    } else {
      result = new Set(filtered);
    }
    if (selected && model.nodeById.has(selected)) result.add(selected);
    if (path.kind === "found") path.nodes.forEach((id) => result.add(id));
    pinned.forEach((id) => {
      if (model.nodeById.has(id)) result.add(id);
    });
    return result;
  }, [depth, filtered, model, path, pinned, selected, view]);

  const selectedNode = selected ? (model.nodeById.get(selected) ?? null) : null;
  const registryRecord = datasets.find((dataset) => dataset.graphNodeId === selected);
  const linkedEvidence = useMemo(
    () => evidence.filter((item) => studyGraphNode(item, model.nodes)?.id === selected),
    [evidence, model.nodes, selected],
  );
  useEffect(() => setPage(0), [types, flags, yearFrom, yearTo, view, depth]);

  const selectedNeighbors = useMemo(() => directNeighbors(model, selected), [model, selected]);
  const visibleNodes = useMemo(
    () =>
      [...visible]
        .map((id) => model.nodeById.get(id))
        .filter((node): node is GraphNode => node !== undefined)
        .sort((a, b) => {
          if (a.id === selected) return -1;
          if (b.id === selected) return 1;
          return a.title.localeCompare(b.title) || a.id.localeCompare(b.id);
        }),
    [model.nodeById, selected, visible],
  );
  const normalizedQuery = normalizeText(query);
  const searchResults = useMemo(() => {
    if (!normalizedQuery) return [];
    return model.nodes
      .map((node) => ({ node, rank: searchRank(node, normalizedQuery) }))
      .filter((entry): entry is { node: GraphNode; rank: number } => entry.rank !== null)
      .sort(
        (a, b) =>
          a.rank - b.rank ||
          a.node.title.localeCompare(b.node.title) ||
          a.node.id.localeCompare(b.node.id),
      )
      .slice(0, 12);
  }, [model.nodes, normalizedQuery]);
  const allNodes = useMemo(
    () =>
      [...model.nodes].sort(
        (a, b) =>
          a.title.localeCompare(b.title) ||
          a.type.localeCompare(b.type) ||
          a.id.localeCompare(b.id),
      ),
    [model.nodes],
  );
  const pathNodeByTerm = useMemo(() => {
    const index = new Map<string, GraphNode | null>();
    const addTerm = (term: string, node: GraphNode) => {
      const normalized = normalizeText(term);
      if (!normalized) return;
      const current = index.get(normalized);
      if (current === undefined) index.set(normalized, node);
      else if (current?.id !== node.id) index.set(normalized, null);
    };
    allNodes.forEach((node) => {
      addTerm(pathOptionLabel(node), node);
      addTerm(node.title, node);
      node.aliases?.forEach((alias) => addTerm(alias, node));
    });
    return index;
  }, [allNodes]);
  const incoming = useMemo(
    () =>
      [...(selected ? (model.incoming.get(selected) ?? []) : [])]
        .map((id) => model.nodeById.get(id))
        .filter((node): node is GraphNode => node !== undefined)
        .sort((a, b) => a.title.localeCompare(b.title) || a.id.localeCompare(b.id)),
    [model, selected],
  );
  const outgoing = useMemo(
    () =>
      [...(selected ? (model.outgoing.get(selected) ?? []) : [])]
        .map((id) => model.nodeById.get(id))
        .filter((node): node is GraphNode => node !== undefined)
        .sort((a, b) => a.title.localeCompare(b.title) || a.id.localeCompare(b.id)),
    [model, selected],
  );

  const totalPages = Math.max(1, Math.ceil(visibleNodes.length / TABLE_PAGE_SIZE));
  const currentPage = Math.min(page, totalPages - 1);
  const tableNodes = visibleNodes.slice(
    currentPage * TABLE_PAGE_SIZE,
    (currentPage + 1) * TABLE_PAGE_SIZE,
  );
  const selectedMatches = selected ? filtered.has(selected) : true;
  const filtersActive =
    types.size !== model.types.length || yearFrom !== "" || yearTo !== "" || flags.size > 0;

  const resolvePathEntry = useCallback(
    (entry: string) =>
      model.nodeById.get(entry.trim()) ?? pathNodeByTerm.get(normalizeText(entry)) ?? null,
    [model.nodeById, pathNodeByTerm],
  );

  const selectAndFocus = useCallback(
    (id: string, local = false, preservePath = false) => {
      setSelected(id);
      setPage(0);
      if (!preservePath) {
        const node = model.nodeById.get(id);
        setPathSource(id);
        setPathSourceQuery(node ? pathOptionLabel(node) : id);
        setPath({ kind: "idle", nodes: [] });
      }
      if (local) setView("local");
      setFocus((current) =>
        local || view === "local"
          ? { scope: "visible", token: (current?.token ?? 0) + 1 }
          : { scope: "selection", id, token: (current?.token ?? 0) + 1 },
      );
    },
    [model.nodeById, view],
  );
  useEffect(() => {
    if (view !== "local" || selected) return;
    const center =
      allNodes.find((node) => filtered.has(node.id) && normalizeText(node.type) === "datasets") ??
      allNodes.find((node) => filtered.has(node.id));
    if (center) selectAndFocus(center.id, true);
  }, [allNodes, filtered, selectAndFocus, selected, view]);

  const changeView = (next: ViewMode) => {
    setView(next);
    setFocus((current) => ({ scope: "visible", token: (current?.token ?? 0) + 1 }));
  };
  const changeDepth = (next: 1 | 2) => {
    setDepth(next);
    setFocus((current) => ({ scope: "visible", token: (current?.token ?? 0) + 1 }));
  };
  const selectAndFocusDetails = useCallback(
    (id: string, local = false) => {
      selectAndFocus(id, local);
      setDetailsFocusToken((current) => current + 1);
    },
    [selectAndFocus],
  );
  const chooseSearchResult = useCallback(
    (id: string) => {
      selectAndFocusDetails(id, true);
      setSearchOpen(false);
    },
    [selectAndFocusDetails],
  );
  const toggleType = (type: string) => {
    setTypes((current) => {
      const next = new Set(current);
      if (next.has(type)) next.delete(type);
      else next.add(type);
      return next;
    });
  };
  const toggleFlag = (flag: CandidateFlag) => {
    setFlags((current) => {
      const next = new Set(current);
      if (next.has(flag)) next.delete(flag);
      else next.add(flag);
      return next;
    });
  };
  const togglePin = (id: string) => {
    setPinned((current) => {
      const next = new Set(current);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  };
  const resetFilters = () => {
    setTypes(new Set(model.types));
    setYearFrom("");
    setYearTo("");
    setFlags(new Set());
  };
  const clearSelection = () => {
    setSelected(null);
    setDetailsFocusToken(0);
    setPage(0);
    if (view === "local") changeView("full");
    else setFocus(null);
    fullViewButton.current?.focus({ preventScroll: true });
  };
  const resetView = () => {
    setSelected(null);
    setPinned(new Set());
    resetFilters();
    setDepth(1);
    setPresentation("graph");
    setQuery("");
    setSearchOpen(false);
    setFiltersOpen(false);
    setPage(0);
    setPathSource("");
    setPathSourceQuery("");
    setPathTarget("");
    setPathTargetQuery("");
    setPath({ kind: "idle", nodes: [] });
    setDetailsFocusToken(0);
    setPathResultFocusToken(0);
    changeView("full");
  };
  const searchKeyDown = (event: KeyboardEvent<HTMLInputElement>) => {
    if (event.key === "ArrowDown" && searchResults.length) {
      event.preventDefault();
      searchButtons.current[0]?.focus();
    } else if (event.key === "Enter" && searchResults.length) {
      event.preventDefault();
      chooseSearchResult(searchResults[0].node.id);
    } else if (event.key === "Escape") {
      setSearchOpen(false);
    }
  };
  const resultKeyDown = (event: KeyboardEvent<HTMLButtonElement>, index: number) => {
    if (event.key === "ArrowDown") {
      event.preventDefault();
      searchButtons.current[Math.min(index + 1, searchResults.length - 1)]?.focus();
    } else if (event.key === "ArrowUp") {
      event.preventDefault();
      if (index) searchButtons.current[index - 1]?.focus();
      else document.getElementById(searchId)?.focus();
    } else if (event.key === "Escape") {
      setSearchOpen(false);
      document.getElementById(searchId)?.focus();
    }
  };
  const findPath = () => {
    if (!pathSource || !pathTarget) return;
    const result = directedPath(model.outgoing, pathSource, pathTarget);
    setPath(result ? { kind: "found", nodes: result } : { kind: "missing", nodes: [] });
    setPathResultFocusToken((current) => current + 1);
  };

  const pathSourceNode = pathSource ? (model.nodeById.get(pathSource) ?? null) : null;
  const pathTargetNode = pathTarget ? (model.nodeById.get(pathTarget) ?? null) : null;
  const pathSourceEntryInvalid = pathSourceQuery.trim().length > 0 && !pathSource;
  const pathTargetEntryInvalid = pathTargetQuery.trim().length > 0 && !pathTarget;

  const sourceUrl = safeExternalUrl(selectedNode?.url);
  const selectedDoi = doiUrl(selectedNode?.doi);
  const selectedFlags: CandidateFlag[] = selectedNode
    ? [
        ...(selectedNode.isManufacturingDataset ? (["manufacturing"] as CandidateFlag[]) : []),
        ...(selectedNode.isPublicDataset ? (["public"] as CandidateFlag[]) : []),
        ...(selectedNode.isSynthesisCandidate ? (["synthesis"] as CandidateFlag[]) : []),
      ]
    : [];

  if (model.error) {
    return (
      <section className="graph-root" aria-labelledby={titleId}>
        <header className="graph-header">
          <div className="graph-heading">
            <p className="graph-kicker">Knowledge structure</p>
            <h2 className="graph-title" id={titleId}>
              Evidence graph
            </h2>
          </div>
        </header>
        <div className="graph-data-error" role="alert">
          <strong>The graph data could not be loaded safely.</strong>
          <p>{model.error}</p>
        </div>
      </section>
    );
  }

  if (!model.nodes.length) {
    return (
      <section className="graph-root" aria-labelledby={titleId}>
        <header className="graph-header">
          <div className="graph-heading">
            <p className="graph-kicker">Knowledge structure</p>
            <h2 className="graph-title" id={titleId}>
              Evidence graph
            </h2>
          </div>
        </header>
        <div className="graph-empty" role="status">
          <strong>No graph records are available.</strong>
          <p>The explorer will appear when the canonical graph bundle has been prepared.</p>
        </div>
      </section>
    );
  }

  return (
    <section
      className="graph-root"
      aria-labelledby={titleId}
      style={
        {
          "--graph-mobile-height": `${view === "local" && visibleNodes.length <= 180 ? Math.max(430, Math.min(960, Math.ceil((visibleNodes.length - 1) / 2) * 19 + 150)) : 430}px`,
        } as CSSProperties
      }
    >
      <header className="graph-header">
        <div className="graph-heading">
          <p className="graph-kicker">Knowledge structure</p>
          <h2 className="graph-title" id={titleId}>
            Evidence graph
          </h2>
        </div>
        <div className="graph-header-actions">
          <div className="graph-segmented" role="toolbar" aria-label="Graph scope">
            <button
              className="graph-segmented-button"
              type="button"
              aria-pressed={view === "full"}
              ref={fullViewButton}
              onClick={() => changeView("full")}
            >
              Full graph
            </button>
            <button
              className="graph-segmented-button"
              type="button"
              aria-pressed={view === "local"}
              onClick={() => changeView("local")}
            >
              Local neighborhood
            </button>
          </div>
          {view === "local" && (
            <div className="graph-segmented" role="toolbar" aria-label="Neighborhood depth">
              <button
                className="graph-segmented-button"
                type="button"
                aria-pressed={depth === 1}
                onClick={() => changeDepth(1)}
              >
                1 hop
              </button>
              <button
                className="graph-segmented-button"
                type="button"
                aria-pressed={depth === 2}
                onClick={() => changeDepth(2)}
              >
                2 hops
              </button>
            </div>
          )}
          <button
            className="graph-mode-button"
            type="button"
            aria-pressed={presentation === "graph"}
            onClick={() => setPresentation("graph")}
          >
            <Network size={15} aria-hidden="true" /> Graph
          </button>
          <button
            className="graph-mode-button"
            type="button"
            aria-pressed={presentation === "table"}
            onClick={() => setPresentation("table")}
          >
            <List size={15} aria-hidden="true" /> Table
          </button>
          <button
            className="graph-mode-button"
            type="button"
            onClick={resetView}
            title="Restore the full graph and clear selections, pins, filters, and paths"
          >
            <RotateCcw size={15} aria-hidden="true" /> Reset view
          </button>
        </div>
      </header>

      <div className="graph-status" aria-live="polite">
        <span>
          <strong>{visibleNodes.length.toLocaleString()}</strong> visible of{" "}
          {model.nodes.length.toLocaleString()} records
          {view === "local" && selectedNode ? ` · neighborhood of ${selectedNode.title}` : ""}
          {selected && !selectedMatches ? " · selected record retained outside active filters" : ""}
          {pinned.size > 0 ? " · pinned records stay visible across filters" : ""}
        </span>
        {model.warnings.length > 0 && (
          <span className="graph-warning">{model.warnings.join("; ")}</span>
        )}
      </div>

      <div className="graph-workspace">
        <aside className="graph-filters" aria-label="Graph search and filters">
          <div className="graph-field">
            <label className="graph-label" htmlFor={searchId}>
              Find a title, alias, or node ID
            </label>
            <div className="graph-search-wrap">
              <Search className="graph-search-icon" size={16} aria-hidden="true" />
              <input
                className="graph-search-input"
                id={searchId}
                type="search"
                value={query}
                placeholder={`Search ${model.nodes.length.toLocaleString()} records…`}
                autoComplete="off"
                aria-controls={resultsId}
                onChange={(event) => {
                  setQuery(event.target.value);
                  setSearchOpen(true);
                }}
                onFocus={() => setSearchOpen(true)}
                onKeyDown={searchKeyDown}
              />
              {query && (
                <button
                  className="graph-clear-search"
                  type="button"
                  aria-label="Clear graph search"
                  onClick={() => {
                    setQuery("");
                    setSearchOpen(false);
                  }}
                >
                  <X size={15} aria-hidden="true" />
                </button>
              )}
              {searchOpen && normalizedQuery && (
                <ul className="graph-search-results" id={resultsId}>
                  {searchResults.length ? (
                    searchResults.map(({ node }, index) => (
                      <li key={node.id}>
                        <button
                          className="graph-search-result"
                          type="button"
                          ref={(element) => {
                            searchButtons.current[index] = element;
                          }}
                          onClick={() => chooseSearchResult(node.id)}
                          onKeyDown={(event) => resultKeyDown(event, index)}
                        >
                          <strong>{node.title}</strong>
                          <small>
                            {node.type} · {node.id}
                          </small>
                        </button>
                      </li>
                    ))
                  ) : (
                    <li className="graph-no-results" role="status">
                      No matching records. Try a name, alias, or node ID.
                    </li>
                  )}
                </ul>
              )}
            </div>
          </div>

          <button
            className="graph-filter-toggle"
            type="button"
            aria-expanded={filtersOpen}
            aria-controls={`graph-filter-panel-${suffix}`}
            onClick={() => setFiltersOpen(!filtersOpen)}
          >
            Filter records {filtersActive ? "· active" : ""}
            <ChevronRight size={16} />
          </button>
          <div
            id={`graph-filter-panel-${suffix}`}
            className={`graph-filter-panel ${filtersOpen ? "is-open" : ""}`}
          >
            <section className="graph-filter-section" aria-labelledby={`graph-types-${suffix}`}>
              <div className="graph-filter-header">
                <h3 className="graph-filter-heading" id={`graph-types-${suffix}`}>
                  Entity types
                </h3>
                <div className="graph-filter-tools">
                  <button
                    className="graph-link-button"
                    type="button"
                    onClick={() => setTypes(new Set(model.types))}
                  >
                    All
                  </button>
                  <button
                    className="graph-link-button"
                    type="button"
                    onClick={() => setTypes(new Set())}
                  >
                    None
                  </button>
                </div>
              </div>
              <div className="graph-check-list">
                {model.types.map((type) => (
                  <label className="graph-check-row" key={type}>
                    <input
                      type="checkbox"
                      checked={types.has(type)}
                      onChange={() => toggleType(type)}
                    />
                    <span
                      className="graph-swatch"
                      style={{ "--graph-swatch": colorForType(type) } as CSSProperties}
                      aria-hidden="true"
                    />
                    <span>{type}</span>
                    <span className="graph-check-count">{typeCounts.get(type) ?? 0}</span>
                  </label>
                ))}
              </div>
            </section>

            {model.years.length > 0 && (
              <section className="graph-filter-section" aria-labelledby={`graph-years-${suffix}`}>
                <div className="graph-filter-header">
                  <h3 className="graph-filter-heading" id={`graph-years-${suffix}`}>
                    Publication year
                  </h3>
                </div>
                <div className="graph-year-grid">
                  <label>
                    From
                    <select
                      className="graph-select"
                      value={yearFrom}
                      onChange={(event) => setYearFrom(event.target.value)}
                    >
                      <option value="">Any</option>
                      {model.years.map((year) => (
                        <option key={year} value={year}>
                          {year}
                        </option>
                      ))}
                    </select>
                  </label>
                  <label>
                    To
                    <select
                      className="graph-select"
                      value={yearTo}
                      onChange={(event) => setYearTo(event.target.value)}
                    >
                      <option value="">Any</option>
                      {model.years.map((year) => (
                        <option key={year} value={year}>
                          {year}
                        </option>
                      ))}
                    </select>
                  </label>
                </div>
                {reversedYears && (
                  <p className="graph-error-text" role="alert">
                    “From” must not be later than “To”.
                  </p>
                )}
                <p className="graph-note">
                  Year filters retain only records with an explicit year.
                </p>
              </section>
            )}

            <section className="graph-filter-section" aria-labelledby={`graph-flags-${suffix}`}>
              <div className="graph-filter-header">
                <h3 className="graph-filter-heading" id={`graph-flags-${suffix}`}>
                  Evidence-layer flags
                </h3>
              </div>
              <div className="graph-check-list">
                {(Object.keys(CANDIDATE_LABELS) as CandidateFlag[]).map((flag) => (
                  <label className="graph-check-row" key={flag}>
                    <input
                      type="checkbox"
                      checked={flags.has(flag)}
                      onChange={() => toggleFlag(flag)}
                    />
                    <span>{CANDIDATE_LABELS[flag]}</span>
                  </label>
                ))}
              </div>
              <p className="graph-note">Selected flags use OR; other filter groups use AND.</p>
            </section>

            {filtersActive && (
              <button className="graph-reset" type="button" onClick={resetFilters}>
                Reset graph filters
              </button>
            )}
          </div>
        </aside>

        <div className="graph-center">
          {presentation === "graph" ? (
            visibleNodes.length ? (
              <section
                className="graph-canvas-wrap"
                aria-label={`Interactive directed graph showing ${visibleNodes.length} records`}
              >
                <RuntimeBoundary
                  resetKey={`${model.nodes.length}:${model.graph.size}:${visibleNodes.length}`}
                >
                  <SigmaContainer
                    className="graph-canvas"
                    graph={model.graph}
                    settings={SIGMA_SETTINGS}
                  >
                    <CanvasController
                      focus={focus}
                      incoming={model.incoming}
                      outgoing={model.outgoing}
                      pathNodes={path.kind === "found" ? path.nodes : []}
                      onSelect={selectAndFocus}
                      pinned={pinned}
                      selected={selected}
                      selectedNeighbors={selectedNeighbors}
                      visible={visible}
                    />
                  </SigmaContainer>
                </RuntimeBoundary>
                <p className="graph-sr-only">
                  The canvas is a visual overview. Choose Table above for complete keyboard access
                  to every currently visible record.
                </p>
              </section>
            ) : (
              <div className="graph-empty" role="status">
                <strong>No records match these filters.</strong>
                <p>Reset one or more filters, or select additional entity types.</p>
              </div>
            )
          ) : (
            <div className="graph-table-wrap">
              <table className="graph-table">
                <caption className="graph-sr-only">
                  Records visible in the current graph view
                </caption>
                <thead>
                  <tr>
                    <th scope="col">Record</th>
                    <th scope="col">Type</th>
                    <th scope="col">Relation to selection</th>
                    <th scope="col">Year / availability</th>
                    <th scope="col">Action</th>
                  </tr>
                </thead>
                <tbody>
                  {tableNodes.length ? (
                    tableNodes.map((node) => (
                      <tr key={node.id}>
                        <td>
                          <span className="graph-table-title">{node.title}</span>
                          <code className="graph-table-id">{node.id}</code>
                        </td>
                        <td>
                          <span className="graph-table-type">
                            <span
                              className="graph-swatch"
                              style={{ "--graph-swatch": colorForType(node.type) } as CSSProperties}
                              aria-hidden="true"
                            />
                            {node.type}
                          </span>
                        </td>
                        <td>{relationLabel(model, selected, node.id)}</td>
                        <td>{node.year ?? node.availability ?? "—"}</td>
                        <td>
                          <button
                            className="graph-table-action"
                            type="button"
                            onClick={() => selectAndFocusDetails(node.id, true)}
                          >
                            Inspect record
                          </button>
                        </td>
                      </tr>
                    ))
                  ) : (
                    <tr>
                      <td colSpan={5}>No records match the current view.</td>
                    </tr>
                  )}
                </tbody>
              </table>
              {visibleNodes.length > TABLE_PAGE_SIZE && (
                <nav className="graph-pagination" aria-label="Graph table pages">
                  <button
                    className="graph-page-button"
                    type="button"
                    disabled={currentPage === 0}
                    onClick={() => setPage((current) => Math.max(0, current - 1))}
                    aria-label="Previous table page"
                  >
                    <ChevronLeft size={16} aria-hidden="true" />
                  </button>
                  <span>
                    Page {currentPage + 1} of {totalPages}
                  </span>
                  <button
                    className="graph-page-button"
                    type="button"
                    disabled={currentPage >= totalPages - 1}
                    onClick={() => setPage((current) => Math.min(totalPages - 1, current + 1))}
                    aria-label="Next table page"
                  >
                    <ChevronRight size={16} aria-hidden="true" />
                  </button>
                </nav>
              )}
            </div>
          )}
        </div>
        <aside className="graph-details" aria-label="Selected graph record">
          {selectedNode ? (
            <>
              <p className="graph-detail-kicker">Selected record</p>
              <span className="graph-detail-type">
                <span
                  className="graph-swatch"
                  style={{ "--graph-swatch": colorForType(selectedNode.type) } as CSSProperties}
                  aria-hidden="true"
                />
                {selectedNode.type}
              </span>
              <h3 className="graph-detail-title" ref={detailsHeading} tabIndex={-1}>
                {selectedNode.title}
              </h3>
              <code className="graph-detail-id">{selectedNode.id}</code>
              <div className="graph-detail-actions">
                <button
                  className="graph-action-button"
                  type="button"
                  onClick={() => {
                    setPresentation("graph");
                    selectAndFocus(selectedNode.id, true);
                  }}
                >
                  Focus in graph
                </button>
                <button
                  className="graph-action-button"
                  type="button"
                  aria-label={
                    pinned.has(selectedNode.id) ? "Unpin selected record" : "Pin selected record"
                  }
                  aria-pressed={pinned.has(selectedNode.id)}
                  onClick={() => togglePin(selectedNode.id)}
                >
                  {pinned.has(selectedNode.id) ? (
                    <PinOff size={15} aria-hidden="true" />
                  ) : (
                    <Pin size={15} aria-hidden="true" />
                  )}
                </button>
                <button
                  className="graph-action-button graph-clear-selection"
                  type="button"
                  onClick={clearSelection}
                  title="Deselect this record; keep filters, pins, and path results"
                >
                  <X size={15} aria-hidden="true" /> Clear selection
                </button>
              </div>

              {(registryRecord || linkedEvidence.length > 0) && (
                <div className="graph-related-links">
                  {registryRecord && (
                    <>
                      <Link to={`/datasets/?record=${encodeURIComponent(registryRecord.id)}`}>
                        Dataset details <ArrowRight size={14} />
                      </Link>
                      <Link to={`/evidence/?dataset=${encodeURIComponent(registryRecord.id)}`}>
                        Related evaluations <ArrowRight size={14} />
                      </Link>
                    </>
                  )}
                  {linkedEvidence.map((item) => (
                    <Link key={item.id} to={`/evidence/?record=${encodeURIComponent(item.id)}`}>
                      View evaluation {item.id} <ArrowRight size={14} />
                    </Link>
                  ))}
                </div>
              )}
              <dl className="graph-detail-list">
                {selectedNode.year !== undefined && (
                  <div className="graph-detail-row">
                    <dt>Year</dt>
                    <dd>{selectedNode.year}</dd>
                  </div>
                )}
                {selectedNode.paperType && (
                  <div className="graph-detail-row">
                    <dt>Paper type</dt>
                    <dd>{selectedNode.paperType}</dd>
                  </div>
                )}
                {selectedNode.availability && (
                  <div className="graph-detail-row">
                    <dt>Availability</dt>
                    <dd>{selectedNode.availability}</dd>
                  </div>
                )}
                {!!selectedNode.aliases?.length && (
                  <div className="graph-detail-row">
                    <dt>Aliases</dt>
                    <dd>
                      <ul className="graph-alias-list">
                        {[...new Set(selectedNode.aliases)].map((alias) => (
                          <li key={`${selectedNode.id}:${alias}`}>{alias}</li>
                        ))}
                      </ul>
                    </dd>
                  </div>
                )}
                {!!selectedFlags.length && (
                  <div className="graph-detail-row">
                    <dt>Evidence-layer flags</dt>
                    <dd>
                      <ul className="graph-flag-list">
                        {selectedFlags.map((flag) => (
                          <li key={flag}>{CANDIDATE_LABELS[flag]}</li>
                        ))}
                      </ul>
                    </dd>
                  </div>
                )}
                {(sourceUrl || selectedDoi) && (
                  <div className="graph-detail-row">
                    <dt>External identifiers</dt>
                    <dd className="graph-external-links">
                      {selectedDoi && (
                        <a
                          className="graph-external-link"
                          href={selectedDoi}
                          target="_blank"
                          rel="noreferrer"
                        >
                          DOI <ExternalLink size={12} aria-hidden="true" />
                        </a>
                      )}
                      {sourceUrl && (
                        <a
                          className="graph-external-link"
                          href={sourceUrl}
                          target="_blank"
                          rel="noreferrer"
                        >
                          Canonical source <ExternalLink size={12} aria-hidden="true" />
                        </a>
                      )}
                    </dd>
                  </div>
                )}
              </dl>

              <details className="graph-relation-group" open>
                <summary className="graph-relation-summary">
                  Incoming wikilinks ({incoming.length})
                </summary>
                <ul className="graph-relation-list">
                  {incoming.length ? (
                    incoming.map((node) => (
                      <li key={node.id}>
                        <button
                          className="graph-relation-button"
                          type="button"
                          onClick={() => selectAndFocus(node.id, true)}
                        >
                          <span
                            className="graph-relation-arrow"
                            data-direction="incoming"
                            aria-hidden="true"
                          >
                            →
                          </span>
                          <span>
                            <span className="graph-sr-only">Incoming from </span>
                            {node.title} · {node.type}
                          </span>
                        </button>
                      </li>
                    ))
                  ) : (
                    <li className="graph-note">No incoming wikilinks.</li>
                  )}
                </ul>
              </details>
              <details className="graph-relation-group" open>
                <summary className="graph-relation-summary">
                  Outgoing wikilinks ({outgoing.length})
                </summary>
                <ul className="graph-relation-list">
                  {outgoing.length ? (
                    outgoing.map((node) => (
                      <li key={node.id}>
                        <button
                          className="graph-relation-button"
                          type="button"
                          onClick={() => selectAndFocus(node.id, true)}
                        >
                          <span className="graph-relation-arrow" aria-hidden="true">
                            →
                          </span>
                          <span>
                            <span className="graph-sr-only">Outgoing to </span>
                            {node.title} · {node.type}
                          </span>
                        </button>
                      </li>
                    ))
                  ) : (
                    <li className="graph-note">No outgoing wikilinks.</li>
                  )}
                </ul>
              </details>
            </>
          ) : (
            <div className="graph-empty">
              <strong>Select a graph record.</strong>
              <p>
                Search by title, alias, or stable node ID, or choose a record from the table view.
              </p>
            </div>
          )}
        </aside>
      </div>

      <section className="graph-pathfinder" aria-labelledby={`graph-path-${suffix}`}>
        <div className="graph-path-header">
          <h3 className="graph-path-title" id={`graph-path-${suffix}`}>
            Directed wikilink path
          </h3>
          <p className="graph-path-subtitle">
            Find the shortest directed connection between two records. Links do not imply causality.
          </p>
        </div>
        <form
          className="graph-path-form"
          onSubmit={(event) => {
            event.preventDefault();
            findPath();
          }}
        >
          <label className="graph-path-endpoint">
            <span>Source</span>
            <input
              className="graph-select"
              type="search"
              list={pathOptionsId}
              value={pathSourceQuery}
              placeholder="Search title, alias, or node ID…"
              autoComplete="off"
              aria-invalid={pathSourceEntryInvalid}
              onChange={(event) => {
                const entry = event.target.value;
                const node = resolvePathEntry(entry);
                setPathSourceQuery(entry);
                setPathSource(node?.id ?? "");
                setPath({ kind: "idle", nodes: [] });
              }}
            />
          </label>
          <ArrowRight className="graph-path-arrow" size={18} aria-hidden="true" />
          <label className="graph-path-endpoint">
            <span>Target</span>
            <input
              className="graph-select"
              type="search"
              list={pathOptionsId}
              value={pathTargetQuery}
              placeholder="Search title, alias, or node ID…"
              autoComplete="off"
              aria-invalid={pathTargetEntryInvalid}
              onChange={(event) => {
                const entry = event.target.value;
                const node = resolvePathEntry(entry);
                setPathTargetQuery(entry);
                setPathTarget(node?.id ?? "");
                setPath({ kind: "idle", nodes: [] });
              }}
            />
          </label>
          <button className="graph-path-submit" type="submit" disabled={!pathSource || !pathTarget}>
            Find path
          </button>
        </form>
        <div className="path-utilities">
          <button
            type="button"
            onClick={() => {
              setPathSource(pathTarget);
              setPathSourceQuery(pathTargetQuery);
              setPathTarget(pathSource);
              setPathTargetQuery(pathSourceQuery);
              setPath({ kind: "idle", nodes: [] });
            }}
          >
            Reverse direction
          </button>
          {path.kind !== "idle" && (
            <button type="button" onClick={() => setPath({ kind: "idle", nodes: [] })}>
              Clear path
            </button>
          )}
        </div>
        <datalist id={pathOptionsId}>
          {allNodes.map((node) => (
            <option key={node.id} value={pathOptionLabel(node)} />
          ))}
        </datalist>

        {path.kind === "idle" && (
          <p className="graph-path-guidance">
            {pathSourceEntryInvalid
              ? "Choose a source from the matching suggestions so its stable node ID is unambiguous."
              : pathTargetEntryInvalid
                ? "Choose a target from the matching suggestions so its stable node ID is unambiguous."
                : !pathSource && !pathTarget
                  ? "Choose both endpoints. Selecting a graph record also sets it as the source."
                  : !pathSource
                    ? "Choose a source record to enable the directed path search."
                    : !pathTarget
                      ? "Choose a target record to enable the directed path search."
                      : "Ready to search the complete snapshot in the source-to-target direction."}
          </p>
        )}
        {path.kind === "found" && (
          <div
            className="graph-path-result"
            ref={pathResult}
            role="status"
            tabIndex={-1}
            aria-live="polite"
            aria-atomic="true"
          >
            <p>
              {path.nodes.length === 1 ? (
                <>
                  <strong>Same record selected.</strong> No wikilink traversal is needed.
                </>
              ) : (
                <>
                  <strong>Path found.</strong> {path.nodes.length - 1} directed wikilink
                  {path.nodes.length === 2 ? " connects" : "s connect"} “
                  {pathSourceNode?.title ?? pathSource}” to “{pathTargetNode?.title ?? pathTarget}”.
                </>
              )}
            </p>
            <button
              className="graph-action-button show-path"
              type="button"
              onClick={() => {
                setPresentation("graph");
                setFocus((current) => ({
                  scope: "selection",
                  id: path.nodes[0],
                  ids: path.nodes,
                  token: (current?.token ?? 0) + 1,
                }));
                requestAnimationFrame(() =>
                  document.querySelector(".graph-canvas-wrap")?.scrollIntoView({
                    behavior: reducedMotion() ? "auto" : "smooth",
                    block: "center",
                  }),
                );
              }}
            >
              Show path in graph <Network size={15} />
            </button>
            <ol className="graph-path-list">
              {path.nodes.map((id, index) => {
                const node = model.nodeById.get(id);
                if (!node) return null;
                return (
                  <li className="graph-path-item" key={id}>
                    {index > 0 && (
                      <span className="graph-path-step" aria-hidden="true">
                        →
                      </span>
                    )}
                    <button
                      className="graph-path-node"
                      type="button"
                      title={node.id}
                      onClick={() => selectAndFocus(node.id, true, true)}
                    >
                      {node.title} · {node.type}
                    </button>
                  </li>
                );
              })}
            </ol>
          </div>
        )}
        {path.kind === "missing" && (
          <div className="graph-path-result" ref={pathResult} role="alert" tabIndex={-1}>
            <p>
              <strong>No directed path found.</strong> The complete snapshot contains no wikilink
              path from “{pathSourceNode?.title ?? pathSource}” to “
              {pathTargetNode?.title ?? pathTarget}”. Direction matters; reversing the endpoints may
              produce a different result.
            </p>
          </div>
        )}
      </section>
    </section>
  );
}

export default GraphExplorer;
