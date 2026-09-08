import { createHash } from "node:crypto";
import {
  copyFileSync,
  existsSync,
  mkdirSync,
  readFileSync,
  statSync,
  writeFileSync,
} from "node:fs";
import { basename, dirname, join, relative, resolve, sep } from "node:path";
import { fileURLToPath } from "node:url";
import Papa from "papaparse";

type CsvRow = Record<string, string>;

type SourceRecord = {
  id: string;
  sourcePath: string;
  sha256: string;
};

type DatasetRecord = {
  id: string;
  ordinal: number;
  name: string;
  domain: string;
  domainId: string;
  tasks: string[];
  annotation: string;
  modality: string;
  resolution: string;
  samplesClasses: string;
  citationKeys: string[];
  graphNodeId: string | null;
  mappingStatus: "exact" | "explicit" | "unresolved";
  sourceLine: number;
};

const websiteRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const repoRoot = resolve(process.env.EVIDENCE_REPO_ROOT ?? join(websiteRoot, ".."));
const manuscriptRootOverride = process.env.MANUSCRIPT_ROOT;
const manuscriptRoot = resolve(
  manuscriptRootOverride ?? join(repoRoot, "evidence", "review", "publication"),
);
const outDir = join(websiteRoot, "public", "data");
const downloadDir = join(websiteRoot, "public", "downloads");
const sources: SourceRecord[] = [];

const sourcePaths = {
  registry: join(manuscriptRoot, "tables", "dataset_registry.tex"),
  evidence: join(manuscriptRoot, "tables", "synthesis_impact_longtable.tex"),
  normalized: join(manuscriptRoot, "data", "synthesis_impact_normalized_change.csv"),
  plot: join(manuscriptRoot, "data", "table3_baseline_after_synthesis.csv"),
  citationRows: join(
    manuscriptRoot,
    "data",
    "dataset_citation_counts_wide_2020_2025_all_domains.csv",
  ),
  citationTable: join(manuscriptRoot, "tables", "dataset_source_citation_trends.tex"),
  coverage: join(
    manuscriptRoot,
    manuscriptRootOverride === undefined ? "figures" : "figs",
    "fig_dataset_task_coverage_matrix_final.tex",
  ),
  bibliography:
    manuscriptRootOverride === undefined
      ? join(manuscriptRoot, "manuscript", "library.bib")
      : join(manuscriptRoot, "library.bib"),
  nodes: join(repoRoot, "evidence", "graph", "exports", "nodes.csv"),
  edges: join(repoRoot, "evidence", "graph", "exports", "edges.csv"),
  graphSummary: join(repoRoot, "evidence", "graph", "exports", "summary.json"),
  datasetRegistry: join(repoRoot, "evidence", "graph", "exports", "dataset_registry.csv"),
  publicDatasetRegistry: join(
    repoRoot,
    "evidence",
    "graph",
    "exports",
    "public_dataset_registry.csv",
  ),
  datasetCandidates: join(
    repoRoot,
    "evidence",
    "graph",
    "exports",
    "manufacturing_dataset_candidates.csv",
  ),
  paperEvidence: join(repoRoot, "evidence", "graph", "exports", "paper_evidence.csv"),
  synthesisCandidates: join(
    repoRoot,
    "evidence",
    "graph",
    "exports",
    "synthesis_impact_candidates.csv",
  ),
};

function fail(message: string): never {
  throw new Error(`Data preparation failed: ${message}`);
}

function validateSourcePaths() {
  const missing = Object.entries(sourcePaths).filter(([, path]) => {
    try {
      return !statSync(path).isFile();
    } catch {
      return true;
    }
  });
  if (missing.length > 0) {
    fail(
      `Required source files are missing or unavailable:\n${missing
        .map(([id, path]) => `  - ${id}: ${relative(repoRoot, path).split(sep).join("/")}`)
        .join("\n")}\nProvide all required source files before running prepare:data.`,
    );
  }
}

function ensureDirectory(path: string) {
  mkdirSync(path, { recursive: true });
}

function sha256(content: Buffer | string) {
  return createHash("sha256").update(content).digest("hex");
}

function readSource(id: string, path: string) {
  if (!existsSync(path)) fail(`Missing source: ${path}`);
  const content = readFileSync(path);
  const sourcePath = relative(repoRoot, path).split(sep).join("/");
  if (!sources.some((source) => source.id === id)) {
    sources.push({ id, sourcePath, sha256: sha256(content) });
  }
  return content.toString("utf8");
}

function parseCsv(id: string, path: string): CsvRow[] {
  const text = readSource(id, path);
  const parsed = Papa.parse<CsvRow>(text, {
    header: true,
    skipEmptyLines: true,
  });
  if (parsed.errors.length > 0) {
    fail(`${basename(path)}: ${parsed.errors.map((error) => error.message).join("; ")}`);
  }
  return parsed.data;
}

function writeJson(name: string, value: unknown) {
  ensureDirectory(outDir);
  const target = join(outDir, name);
  writeFileSync(target, `${JSON.stringify(value)}\n`, "utf8");
  return target;
}

function copyDownload(path: string, outputName = basename(path)) {
  ensureDirectory(downloadDir);
  copyFileSync(path, join(downloadDir, outputName));
}

function splitTopLevelAmpersands(value: string) {
  const cells: string[] = [];
  let current = "";
  let depth = 0;
  for (let index = 0; index < value.length; index += 1) {
    const character = value[index];
    const escaped = index > 0 && value[index - 1] === "\\";
    if (!escaped && character === "{") depth += 1;
    if (!escaped && character === "}") depth -= 1;
    if (!escaped && character === "&" && depth === 0) {
      cells.push(current.trim());
      current = "";
    } else {
      current += character;
    }
  }
  cells.push(current.trim());
  return cells;
}

function decodeTex(value: string) {
  let result = value
    .replace(/(?<!\\)%.*$/gm, "")
    .replace(/\\(?:textbf|textit|emph|mbox)\{([^{}]*)\}/g, "$1")
    .replace(/\\(?:textbf|textit|emph|mbox)\{([^{}]*)\}/g, "$1")
    .replace(/\\citep\{[^}]+\}/g, "")
    .replace(/\{,\}/g, ",")
    .replace(/\\&/g, "&")
    .replace(/\\_/g, "_")
    .replace(/\\%/g, "%")
    .replace(/\\times/g, "x")
    .replace(/\\textgreater/g, ">")
    .replace(/\\approx/g, "approx.")
    .replace(/\\,/g, "")
    .replace(/\\;/g, " ")
    .replace(/\\!/g, "")
    .replace(/\$|\{|\}/g, "")
    .replace(/~/g, " ")
    .replace(/--/g, "-")
    .replace(/\\(?:,|quad|qquad)/g, " ")
    .replace(/\\[a-zA-Z]+/g, "")
    .replace(/\\\\/g, "")
    .replace(/\s+/g, " ")
    .trim();
  result = result.replace(/\s+([,.;:])/g, "$1");
  return result;
}

function normalizeText(value: string) {
  return value
    .normalize("NFKC")
    .toLocaleLowerCase("en")
    .replace(/[–—]/g, "-")
    .replace(/[^a-z0-9+.-]+/g, " ")
    .trim()
    .replace(/\s+/g, " ");
}

function slugify(value: string) {
  return normalizeText(value).replace(/[.+]/g, "").replace(/\s+/g, "-");
}

const domainAliases: Record<string, string> = {
  "Semiconductor & Electronics": "semiconductor-electronics",
  "Semiconductor & electronics": "semiconductor-electronics",
  "Solar Cells / PV": "solar-pv",
  "Solar cells / PV": "solar-pv",
  Metals: "metals",
  Textiles: "textiles",
  Glass: "glass",
  Automotive: "automotive",
  "Multi-industry benchmarks": "multi-industry",
  "Multi-industry anomaly": "multi-industry",
};

const canonicalTasks: Record<string, string> = {
  classification: "Classification",
  "object detection": "Object detection",
  segmentation: "Segmentation",
  "anomaly detection": "Anomaly detection",
  localization: "Localization",
};

const explicitDatasetGraphMappings: Record<string, string> = {
  "Heat Sink Surface Defects": "Datasets/Public/Heat Sink Surface Defect Dataset",
  "ELPV Solar Cell Dataset": "Datasets/Public/ELPV Dataset",
  "EL-2019 (SIGAN dataset)": "Datasets/Public/EL-2019",
  "Dataset of Solar Cells Defect Segm.":
    "Datasets/Public/Dataset of Solar Cells Defect Segmentation",
  "Thermal PV UAV Dataset":
    "Datasets/Public/Thermal PV Panel Detection and Fault Detection Dataset for UAV-Based Inspection",
  "Severstal Steel Defect": "Datasets/Public/Severstal Steel Defect Dataset",
  "Batavia/Sarga Woven Fabric": "Datasets/Public/Batavia and Sarga woven fabric images",
  "DME Fabric Defect Detection": "Datasets/Public/DME Fabric Defect Detection Dataset",
  "Bosch SDI": "Datasets/Public/Bosch Surface Defect Inspection Dataset",
};

function canonicalTask(value: string) {
  const task = canonicalTasks[value.trim().toLocaleLowerCase("en")];
  if (!task) fail(`Unknown dataset task: ${value}`);
  return task;
}

// __DATASET_PARSERS__
type GraphNode = {
  id: string;
  type: string;
  title: string;
  aliases: string[];
  year?: number;
  paperType?: string;
  availability?: string;
  doi?: string;
  url?: string;
  sourceNote?: string;
  isManufacturingDataset: boolean;
  isPublicDataset: boolean;
  isSynthesisCandidate: boolean;
  isCuratedEvidence: boolean;
};

const domainOrder = [
  { id: "semiconductor-electronics", label: "Semiconductor & Electronics" },
  { id: "solar-pv", label: "Solar Cells / PV" },
  { id: "metals", label: "Metals" },
  { id: "textiles", label: "Textiles" },
  { id: "glass", label: "Glass" },
  { id: "automotive", label: "Automotive" },
  { id: "multi-industry", label: "Multi-industry benchmarks" },
] as const;

const taskOrder = [
  "Classification",
  "Object detection",
  "Segmentation",
  "Anomaly detection",
  "Localization",
];

function parseDatasetRegistry(graphNodes: GraphNode[]) {
  const text = readSource("dataset-registry-tex", sourcePaths.registry);
  const graphTerms = new Map<string, string[]>();
  for (const node of graphNodes.filter((candidate) => candidate.type === "Datasets")) {
    for (const term of [node.title, ...node.aliases]) {
      const key = normalizeText(term);
      graphTerms.set(key, [...(graphTerms.get(key) ?? []), node.id]);
    }
  }

  let activeDomain = "";
  const datasets: DatasetRecord[] = [];
  const lines = text.split(/\r?\n/);
  for (let index = 0; index < lines.length; index += 1) {
    const line = lines[index];
    const heading = line.includes("\\multicolumn{6}") ? line.match(/\\textbf\{([^}]+)\}/) : null;
    if (heading) {
      activeDomain = decodeTex(heading[1]);
      continue;
    }
    if (!line.includes("\\citep{")) continue;
    const cells = splitTopLevelAmpersands(line.replace(/\\\\\s*$/, ""));
    if (cells.length !== 6) fail(`Registry line ${index + 1} has ${cells.length} cells`);
    const nameAndCitations = cells[0].match(/^(.*?)~?\\citep\{([^}]+)\}/);
    if (!nameAndCitations) fail(`Registry line ${index + 1} has no citation group`);
    const name = decodeTex(nameAndCitations[1]);
    const citationKeys = nameAndCitations[2].split(",").map((key) => key.trim());
    const domainId = domainAliases[activeDomain];
    if (!domainId) fail(`Unknown registry domain: ${activeDomain}`);
    const tasks = decodeTex(cells[1]).split(",").map(canonicalTask);
    const graphMatches = graphTerms.get(normalizeText(name)) ?? [];
    const uniqueMatches = [...new Set(graphMatches)];
    const explicitMatch = explicitDatasetGraphMappings[name];
    if (explicitMatch && !graphNodes.some((node) => node.id === explicitMatch)) {
      fail(`Explicit dataset graph mapping does not resolve: ${name}`);
    }
    datasets.push({
      id: `dataset-${String(datasets.length + 1).padStart(2, "0")}-${slugify(name)}`,
      ordinal: datasets.length + 1,
      name,
      domain: activeDomain,
      domainId,
      tasks,
      annotation: decodeTex(cells[2]),
      modality: decodeTex(cells[3]),
      resolution: decodeTex(cells[4]),
      samplesClasses: decodeTex(cells[5]),
      citationKeys,
      graphNodeId: uniqueMatches.length === 1 ? uniqueMatches[0] : (explicitMatch ?? null),
      mappingStatus:
        uniqueMatches.length === 1 ? "exact" : explicitMatch ? "explicit" : "unresolved",
      sourceLine: index + 1,
    });
  }

  if (datasets.length !== 61) fail(`Expected 61 datasets, found ${datasets.length}`);
  const assignments = datasets.reduce((total, dataset) => total + dataset.tasks.length, 0);
  if (assignments !== 92) fail(`Expected 92 task assignments, found ${assignments}`);
  if (new Set(datasets.map((dataset) => dataset.domainId)).size !== 7) {
    fail("Expected seven dataset domains");
  }
  return {
    datasets,
    domains: domainOrder,
    tasks: taskOrder,
    summary: {
      uniqueDatasets: datasets.length,
      taskAssignments: assignments,
      graphExactMatches: datasets.filter((dataset) => dataset.mappingStatus === "exact").length,
      graphExplicitMatches: datasets.filter((dataset) => dataset.mappingStatus === "explicit")
        .length,
      graphUnresolved: datasets.filter((dataset) => dataset.mappingStatus === "unresolved").length,
    },
  };
}

function parseCoverage(datasets: DatasetRecord[]) {
  const text = readSource("task-coverage-tex", sourcePaths.coverage);
  const matches = [...text.matchAll(/\\CoverageCell\{(\d+)\}\{(\d+)\}\{(\d+)\}/g)];
  if (matches.length !== 35) fail(`Expected 35 coverage cells, found ${matches.length}`);
  const cells: Record<string, Record<string, number>> = {};
  for (const domain of domainOrder) {
    cells[domain.id] = Object.fromEntries(taskOrder.map((task) => [task, 0]));
  }
  for (const match of matches) {
    const task = taskOrder[Number(match[1])];
    const domain = domainOrder[Number(match[2])];
    if (!task || !domain) fail(`Coverage cell outside the declared matrix: ${match[0]}`);
    cells[domain.id][task] = Number(match[3]);
  }
  for (const domain of domainOrder) {
    for (const task of taskOrder) {
      const registryCount = datasets.filter(
        (dataset) => dataset.domainId === domain.id && dataset.tasks.includes(task),
      ).length;
      if (cells[domain.id][task] !== registryCount) {
        fail(`Coverage mismatch for ${domain.label} / ${task}`);
      }
    }
  }
  const datasetTotals = Object.fromEntries(
    domainOrder.map((domain) => [
      domain.id,
      datasets.filter((dataset) => dataset.domainId === domain.id).length,
    ]),
  );
  const taskTotals = Object.fromEntries(
    taskOrder.map((task) => [
      task,
      datasets.filter((dataset) => dataset.tasks.includes(task)).length,
    ]),
  );
  return {
    domainOrder,
    taskOrder,
    cells,
    datasetTotals,
    taskTotals,
    uniqueDatasets: 61,
    assignmentTotal: 92,
  };
}

function parseCitationTrends(datasets: DatasetRecord[]) {
  const rows = parseCsv("citation-rows-csv", sourcePaths.citationRows);
  if (rows.length !== 60) fail(`Expected 60 citation rows, found ${rows.length}`);
  const datasetsByName = new Map(datasets.map((dataset) => [normalizeText(dataset.name), dataset]));
  const years = [2020, 2021, 2022, 2023, 2024, 2025];
  const joinedRows = rows.map((row, index) => {
    const dataset = datasetsByName.get(normalizeText(row.dataset));
    if (!dataset)
      fail(`Citation row ${index + 2} does not match a registry dataset: ${row.dataset}`);
    return {
      datasetId: dataset.id,
      dataset: dataset.name,
      domainId: dataset.domainId,
      domainGroup: row.domain_group,
      domainDescription: row.domain,
      taskDescription: row.task,
      paperKey: row.paper_key,
      title: row.bib_title,
      publicationYear: Number(row.bib_year),
      doi: row.doi || null,
      openAlexId: row.openalex_id || null,
      matchMethod: row.openalex_match_method,
      annual: Object.fromEntries(
        years.map((year) => {
          const raw = row[String(year)];
          return [year, raw === "" ? null : Number(raw)];
        }),
      ),
    };
  });
  const omitted = datasets.filter(
    (dataset) => !joinedRows.some((row) => row.datasetId === dataset.id),
  );
  if (omitted.length !== 1 || omitted[0].name !== "X-SDD") {
    fail(`Expected X-SDD to be the only registry dataset omitted from citation rows`);
  }

  const tableText = readSource("citation-aggregate-tex", sourcePaths.citationTable);
  const labels = [
    "Semiconductor \\& electronics",
    "Solar cells / PV",
    "Metals",
    "Textiles",
    "Glass",
    "Automotive",
    "Multi-industry anomaly",
    "Total",
  ];
  const series = labels.map((label) => {
    const escaped = label.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    const match = tableText.match(
      new RegExp(
        `${escaped}\\s*&\\s*(\\d+)\\s*&\\s*(\\d+)\\s*&\\s*(\\d+)\\s*&\\s*(\\d+)\\s*&\\s*(\\d+)\\s*&\\s*(\\d+)\\s*&\\s*(\\d+)`,
      ),
    );
    if (!match) fail(`Missing published citation aggregate row: ${decodeTex(label)}`);
    const values = match.slice(1).map(Number);
    const decodedLabel = decodeTex(label);
    return {
      domainId: decodedLabel === "Total" ? "all" : (domainAliases[decodedLabel] ?? ""),
      label: decodedLabel,
      annual: Object.fromEntries(years.map((year, index) => [year, values[index]])),
      total: values[6],
    };
  });
  if (series.at(-1)?.total !== 7428) fail("Published citation aggregate must total 7,428");
  return {
    years,
    series,
    rows: joinedRows,
    missingDataset: "X-SDD",
    missingYearSemantics:
      "Null means unavailable source evidence; literal zero means a reported zero citation count.",
    chartPositioning:
      "Log-scale views may position zero at one, but labels and accessible values retain zero.",
  };
}

// __EVIDENCE_PARSERS__
type BibEntry = {
  key: string;
  title?: string;
  author?: string;
  year?: string;
  doi?: string;
  url?: string;
};

function parseBibtex(text: string) {
  const entries = new Map<string, BibEntry>();
  let cursor = 0;
  while (cursor < text.length) {
    const at = text.indexOf("@", cursor);
    if (at < 0) break;
    const open = text.indexOf("{", at);
    if (open < 0) break;
    let depth = 1;
    let end = open + 1;
    while (end < text.length && depth > 0) {
      if (text[end] === "{") depth += 1;
      if (text[end] === "}") depth -= 1;
      end += 1;
    }
    if (depth !== 0) fail("Unbalanced BibTeX entry");
    const body = text.slice(open + 1, end - 1);
    const comma = body.indexOf(",");
    if (comma > 0) {
      const key = body.slice(0, comma).trim();
      const fields: BibEntry = { key };
      const rest = body.slice(comma + 1);
      const fieldPattern = /([a-zA-Z][\w-]*)\s*=\s*/g;
      const starts = [...rest.matchAll(fieldPattern)];
      for (let index = 0; index < starts.length; index += 1) {
        const start = starts[index];
        const field = start[1].toLocaleLowerCase("en") as keyof BibEntry;
        if (!["title", "author", "year", "doi", "url"].includes(field)) continue;
        const valueStart = (start.index ?? 0) + start[0].length;
        const valueEnd =
          index + 1 < starts.length ? (starts[index + 1].index ?? rest.length) : rest.length;
        const rawValue = rest.slice(valueStart, valueEnd).replace(/,\s*$/, "").trim();
        fields[field] = decodeTex(rawValue.replace(/^\{|\}$/g, "").replace(/^"|"$/g, ""));
      }
      entries.set(key, fields);
    }
    cursor = end;
  }
  return entries;
}

function parseEvidence() {
  const normalizedRows = parseCsv("normalized-change-csv", sourcePaths.normalized);
  const plotRows = parseCsv("evidence-plot-csv", sourcePaths.plot);
  const tex = readSource("synthesis-impact-tex", sourcePaths.evidence);
  const bibliography = parseBibtex(readSource("bibliography-bib", sourcePaths.bibliography));
  if (normalizedRows.length !== 39 || plotRows.length !== 39) {
    fail(`Evidence sources must each contain 39 rows`);
  }

  const starts = [...tex.matchAll(/\\textbf\{(E\d{2})\}\s*\\citep\{([^}]+)\}/g)];
  if (starts.length !== 39) fail(`Expected 39 TeX evidence rows, found ${starts.length}`);
  const texRows = starts.map((start, index) => {
    const from = start.index ?? 0;
    const to =
      index + 1 < starts.length
        ? (starts[index + 1].index ?? tex.length)
        : tex.indexOf("\\end{longtable}", from);
    const block = tex.slice(from, to).replace(/(?<!\\)%.*$/gm, "");
    const cells = splitTopLevelAmpersands(block);
    if (cells.length < 8) fail(`${start[1]} has fewer than eight top-level cells`);
    return {
      id: start[1],
      studyKey: start[2],
      dataset: decodeTex(cells[1]),
      task: decodeTex(cells[2]),
      annotation: decodeTex(cells[3]),
      synthesisFamily: decodeTex(cells[4]),
      setup: decodeTex(cells[5]),
      comparator: decodeTex(cells[6]),
    };
  });

  const items = texRows.map((texRow, index) => {
    const normalized = normalizedRows[index];
    const plot = plotRows[index];
    const expectedId = `E${String(index + 1).padStart(2, "0")}`;
    if (
      texRow.id !== expectedId ||
      plot.evidence_id !== expectedId ||
      Number(normalized.long_table_row) !== index + 1 ||
      normalized.study !== texRow.studyKey
    ) {
      fail(`Evidence alignment failed at ${expectedId}`);
    }
    const bib = bibliography.get(texRow.studyKey);
    if (!bib) fail(`Missing BibTeX entry for ${texRow.studyKey}`);
    const normalizedChange = Number(normalized.normalized_change);
    if (!(normalizedChange > 0)) fail(`${expectedId} must have positive normalized change`);
    return {
      id: expectedId,
      ordinal: index + 1,
      studyKey: texRow.studyKey,
      study: {
        title: bib.title ?? texRow.studyKey,
        authors: bib.author?.split(/\s+and\s+/i) ?? [],
        year: bib.year ? Number(bib.year) : null,
        doi: bib.doi || null,
        url: bib.url || null,
      },
      dataset: texRow.dataset,
      task: texRow.task,
      annotation: texRow.annotation,
      synthesisFamily: texRow.synthesisFamily,
      setup: texRow.setup,
      comparator: texRow.comparator,
      representative: {
        metric: plot.metric,
        sourceMetricLabel: normalized.metric,
        baseline: Number(plot.baseline),
        after: Number(plot.after),
        normalizedChange,
        normalizedChangeSource: normalized.normalized_change,
      },
      categories: {
        domain: plot.domain,
        concept: plot.concept,
        model: plot.model,
        family: plot.family,
      },
      sourceLabels: {
        normalizedDataset: normalized.dataset,
        normalizedTask: normalized.task,
        normalizedAnnotation: normalized.annotation,
        normalizedFamily: normalized.synthesis_family,
      },
      chartScaleConverted: ["E12", "E19", "E22", "E24", "E26", "E27"].includes(expectedId),
    };
  });
  const uniqueStudies = new Set(items.map((item) => item.studyKey)).size;
  if (uniqueStudies !== 37) fail(`Expected 37 unique evidence studies, found ${uniqueStudies}`);
  return {
    items,
    summary: {
      evaluations: 39,
      uniqueStudies: 37,
      allRepresentativeChangesPositive: true,
      medianNormalizedChange: 0.43,
      q1NormalizedChange: 0.2,
      q3NormalizedChange: 0.66,
      meanNormalizedChange: 0.45,
      sampleSdNormalizedChange: 0.29,
      familyStatistics: [
        { family: "GAN", median: 0.48, mean: 0.51 },
        { family: "Rule", median: 0.32, mean: 0.4 },
        { family: "Diffusion", median: 0.22, mean: 0.38 },
        { family: "Hybrid", median: 0.64, mean: 0.53, n: 3 },
      ],
    },
    interpretation: [
      "Values are descriptive representative comparisons, not a meta-analysis or a success rate.",
      "Metrics, tasks, datasets, baselines, and experimental conditions differ across rows.",
      "Normalized change is interpreted within each reported comparison and must not be used as a universal ranking.",
      "Comparator types are preserved from the manuscript and are not inferred.",
    ],
  };
}

// __GRAPH_PARSER__
function parseGraph(evidence: ReturnType<typeof parseEvidence>) {
  const nodeRows = parseCsv("graph-nodes-csv", sourcePaths.nodes);
  const edgeRows = parseCsv("graph-edges-csv", sourcePaths.edges);
  const datasetCandidates = parseCsv("dataset-candidates-csv", sourcePaths.datasetCandidates);
  const publicDatasets = parseCsv("public-datasets-csv", sourcePaths.publicDatasetRegistry);
  const synthesisCandidates = parseCsv("synthesis-candidates-csv", sourcePaths.synthesisCandidates);
  const summary = JSON.parse(readSource("graph-summary-json", sourcePaths.graphSummary)) as {
    counts: Record<string, number>;
    interpretation: Record<string, string>;
    repository_schema_version: string;
    snapshot_date: string;
    vault_sha256: string;
  };
  if (nodeRows.length !== 896 || edgeRows.length !== 8926) {
    fail(`Graph snapshot must contain 896 nodes and 8,926 edges`);
  }
  const datasetCandidateIds = new Set(datasetCandidates.map((row) => row.dataset_id));
  const publicDatasetIds = new Set(publicDatasets.map((row) => row.dataset_id));
  const synthesisSourceNotes = new Set(synthesisCandidates.map((row) => row.source_note));
  const evidenceDois = new Set(
    evidence.items
      .map((item) => item.study.doi?.toLocaleLowerCase("en"))
      .filter((doi): doi is string => Boolean(doi)),
  );
  const evidenceTitles = new Set(evidence.items.map((item) => normalizeText(item.study.title)));
  const nodes: GraphNode[] = nodeRows.map((row) => ({
    id: row.node_id,
    type: row.node_type,
    title: row.title,
    aliases: row.aliases
      ? row.aliases
          .split("|")
          .map((alias) => alias.trim())
          .filter(Boolean)
      : [],
    ...(row.year ? { year: Number(row.year) } : {}),
    ...(row.paper_type ? { paperType: row.paper_type } : {}),
    ...(row.availability ? { availability: row.availability } : {}),
    ...(row.doi ? { doi: row.doi } : {}),
    ...(row.url ? { url: row.url } : {}),
    ...(row.source_note ? { sourceNote: row.source_note } : {}),
    isManufacturingDataset: datasetCandidateIds.has(row.node_id),
    isPublicDataset: publicDatasetIds.has(row.node_id),
    isSynthesisCandidate: synthesisSourceNotes.has(row.source_note),
    isCuratedEvidence:
      (row.doi ? evidenceDois.has(row.doi.toLocaleLowerCase("en")) : false) ||
      evidenceTitles.has(normalizeText(row.title)),
  }));
  const nodeIds = new Set(nodes.map((node) => node.id));
  const edges = edgeRows.map((row, index) => {
    if (!nodeIds.has(row.source_id) || !nodeIds.has(row.target_id)) {
      fail(`Graph edge ${index + 1} references an unknown node`);
    }
    return { source: row.source_id, target: row.target_id };
  });
  if (nodes.filter((node) => node.isManufacturingDataset).length !== 76) {
    fail("Expected 76 manufacturing dataset candidates");
  }
  if (nodes.filter((node) => node.isPublicDataset).length !== 85) {
    fail("Expected 85 documented public datasets");
  }
  if (nodes.filter((node) => node.isSynthesisCandidate).length !== 142) {
    fail("Expected 142 automated synthesis-impact candidates");
  }
  return {
    nodes,
    edges,
    summary: {
      ...summary,
      typeCounts: Object.fromEntries(
        [...new Set(nodes.map((node) => node.type))]
          .sort()
          .map((type) => [type, nodes.filter((node) => node.type === type).length]),
      ),
      selfLinks: edges.filter((edge) => edge.source === edge.target).length,
    },
  };
}

// __MAIN__
function main() {
  validateSourcePaths();
  const evidence = parseEvidence();
  const graph = parseGraph(evidence);
  const datasetData = parseDatasetRegistry(graph.nodes);
  const coverage = parseCoverage(datasetData.datasets);
  const citations = parseCitationTrends(datasetData.datasets);

  writeJson("datasets.json", datasetData);
  writeJson("task-coverage.json", coverage);
  writeJson("citation-trends.json", citations);
  writeJson("evidence.json", evidence);
  writeJson("graph.bundle.json", graph);
  writeJson("meta.json", {
    title:
      "Synthetic Data for Machine Learning in Industrial Visual Defect Inspection: A Review Centered on Public Datasets",
    authors: ["Michael Friedrich", "Tobias Schlosser", "Danny Kowerko"],
    manuscript: { datasets: 61, domains: 7, evaluations: 39, studies: 37 },
    graphSnapshot: {
      date: graph.summary.snapshot_date,
      schemaVersion: graph.summary.repository_schema_version,
      notes: graph.nodes.length,
      resolvedEdges: graph.edges.length,
      vaultSha256: graph.summary.vault_sha256,
    },
    manuscriptGraphSnapshot: { notes: 894, links: 8859 },
    snapshotNote:
      "The repository graph snapshot is newer than the manuscript snapshot; both are labeled and are not silently reconciled.",
  });
  writeJson("provenance.json", {
    schemaVersion: "1.0.0",
    sources: [...sources].sort((left, right) => left.id.localeCompare(right.id)),
    transformations: [
      {
        output: "datasets.json",
        sources: ["dataset-registry-tex", "graph-nodes-csv"],
        method: "Narrow TeX parsing, exact text mapping, and declared-label normalization.",
      },
      {
        output: "evidence.json",
        sources: [
          "synthesis-impact-tex",
          "normalized-change-csv",
          "evidence-plot-csv",
          "bibliography-bib",
        ],
        method: "Validated row-order and citation-key join; no new evaluation or rescaling.",
      },
      {
        output: "graph.bundle.json",
        sources: ["graph-nodes-csv", "graph-edges-csv", "graph-summary-json"],
        method: "Strict public-field allowlist and exact candidate joins.",
      },
    ],
    validatedInvariants: {
      datasets: 61,
      domains: 7,
      taskAssignments: 92,
      evidenceRows: 39,
      uniqueEvidenceStudies: 37,
      graphNodes: 896,
      graphEdges: 8926,
      allRepresentativeNormalizedChangesPositive: true,
    },
    generatedDataPolicy:
      "The website transforms and presents already-present sources. It generates no new scientific data or evaluation.",
  });

  copyDownload(sourcePaths.normalized);
  copyDownload(sourcePaths.plot);
  copyDownload(sourcePaths.citationRows);

  console.log(
    `Prepared ${datasetData.datasets.length} datasets, ${evidence.items.length} evidence rows, ${graph.nodes.length} graph nodes, and ${graph.edges.length} graph edges.`,
  );
}

main();
