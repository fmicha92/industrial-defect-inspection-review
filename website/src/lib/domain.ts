/**
 * Contracts for the static, source-derived scientific data bundles.
 *
 * Helpers here only search, filter, format, and validate extracted values.
 * They do not calculate normalized change or create scientific evaluations.
 */

export const DOMAIN_IDS = [
  "semiconductor-electronics",
  "solar-pv",
  "metals",
  "textiles",
  "glass",
  "automotive",
  "multi-industry",
] as const;

export type DomainId = (typeof DOMAIN_IDS)[number];

export const DOMAIN_LABELS: Readonly<Record<DomainId, string>> = {
  "semiconductor-electronics": "Semiconductor & Electronics",
  "solar-pv": "Solar Cells / PV",
  metals: "Metals",
  textiles: "Textiles",
  glass: "Glass",
  automotive: "Automotive",
  "multi-industry": "Multi-industry benchmarks",
};

export const INSPECTION_TASKS = [
  "Classification",
  "Object detection",
  "Segmentation",
  "Anomaly detection",
  "Localization",
] as const;

export type InspectionTask = (typeof INSPECTION_TASKS)[number];

export const CITATION_YEARS = [2020, 2021, 2022, 2023, 2024, 2025] as const;
export type CitationYear = (typeof CITATION_YEARS)[number];
export type CitationCount = number | null;
export type CitationYearCounts = Record<string, CitationCount> &
  Record<CitationYear, CitationCount>;

export const GRAPH_NODE_TYPES = [
  "Bases",
  "Benchmarks",
  "Concepts",
  "Datasets",
  "Domains",
  "Learning Paradigms",
  "Methods",
  "Metrics",
  "Papers",
  "Tasks",
] as const;

export type GraphNodeType = (typeof GRAPH_NODE_TYPES)[number];
export type EvidenceId = `E${number}`;
export type MappingStatus = "exact" | "explicit" | "unresolved";

export interface DomainDescriptor {
  readonly id: DomainId;
  readonly label: string;
}

export interface DatasetRecord {
  readonly id: string;
  readonly ordinal: number;
  readonly name: string;
  readonly domain: string;
  readonly domainId: DomainId;
  readonly tasks: string[];
  readonly annotation: string;
  readonly modality: string;
  readonly resolution: string;
  readonly samplesClasses: string;
  readonly citationKeys: string[];
  readonly graphNodeId: string | null;
  readonly mappingStatus: MappingStatus;
  readonly sourceLine: number;
}

export interface DatasetRegistry {
  readonly datasets: DatasetRecord[];
  readonly domains: DomainDescriptor[];
  readonly tasks: string[];
  readonly summary: {
    readonly uniqueDatasets: number;
    readonly taskAssignments: number;
    readonly graphExactMatches: number;
    readonly graphExplicitMatches: number;
    readonly graphUnresolved: number;
  };
}

export type DatasetBundle = DatasetRegistry;

export interface TaskCoverage {
  readonly domainOrder: DomainDescriptor[];
  readonly taskOrder: string[];
  readonly cells: Record<string, Record<string, number>>;
  readonly datasetTotals: Record<string, number>;
  readonly taskTotals: Record<string, number>;
  readonly uniqueDatasets: number;
  readonly assignmentTotal: number;
}

export type TaskCoverageBundle = TaskCoverage;

export type OpenAlexMatchMethod =
  | "doi"
  | "title-search"
  | "low-confidence-title-search"
  | "title-not-found";

export interface CitationTrendRow {
  readonly datasetId: string;
  readonly dataset: string;
  readonly domainId: DomainId;
  readonly domainGroup: string;
  readonly domainDescription: string;
  readonly taskDescription: string;
  readonly paperKey: string;
  readonly title: string;
  readonly publicationYear: number;
  readonly doi: string | null;
  readonly openAlexId: string | null;
  readonly matchMethod: OpenAlexMatchMethod;
  /** Null is unavailable source evidence; zero is an observed zero. */
  readonly annual: CitationYearCounts;
}

export interface PublishedCitationSeries {
  readonly domainId: DomainId | "all";
  readonly label: string;
  readonly annual: Record<string, number> & Record<CitationYear, number>;
  readonly total: number;
}

export interface CitationTrend {
  readonly years: CitationYear[];
  readonly series: PublishedCitationSeries[];
  readonly rows: CitationTrendRow[];
  readonly missingDataset: string;
  readonly missingYearSemantics: string;
  readonly chartPositioning: string;
}

export type CitationTrendsBundle = CitationTrend;

export interface EvidenceStudy {
  readonly title: string;
  readonly authors: string[];
  readonly year: number | null;
  readonly doi: string | null;
  readonly url: string | null;
}

export interface RepresentativeComparison {
  readonly metric: string;
  readonly sourceMetricLabel: string;
  readonly baseline: number;
  readonly after: number;
  /** Existing NC value copied from the normalized-change source. */
  readonly normalizedChange: number;
  readonly normalizedChangeSource: string;
}

export interface EvidenceItem {
  readonly id: EvidenceId;
  readonly ordinal: number;
  readonly studyKey: string;
  readonly study: EvidenceStudy;
  readonly dataset: string;
  readonly task: string;
  readonly annotation: string;
  readonly synthesisFamily: string;
  readonly setup: string;
  readonly comparator: string;
  readonly representative: RepresentativeComparison;
  readonly categories: {
    readonly domain: string;
    readonly concept: string;
    readonly model: string;
    readonly family: string;
  };
  readonly sourceLabels: {
    readonly normalizedDataset: string;
    readonly normalizedTask: string;
    readonly normalizedAnnotation: string;
    readonly normalizedFamily: string;
  };
  readonly chartScaleConverted: boolean;
}

export type EvidenceRecord = EvidenceItem;

export interface EvidenceBundle {
  readonly items: EvidenceItem[];
  readonly summary: {
    readonly evaluations: number;
    readonly uniqueStudies: number;
    readonly allRepresentativeChangesPositive: boolean;
    readonly medianNormalizedChange: number;
    readonly q1NormalizedChange: number;
    readonly q3NormalizedChange: number;
    readonly meanNormalizedChange: number;
    readonly sampleSdNormalizedChange: number;
    readonly familyStatistics: {
      readonly family: string;
      readonly median: number;
      readonly mean: number;
      readonly n?: number;
    }[];
  };
  readonly interpretation: string[];
}

export interface MetaBundle {
  readonly title: string;
  readonly authors: string[];
  readonly manuscript: {
    readonly datasets: number;
    readonly domains: number;
    readonly evaluations: number;
    readonly studies: number;
  };
  readonly graphSnapshot: {
    readonly date: string;
    readonly schemaVersion: string;
    readonly notes: number;
    readonly resolvedEdges: number;
    readonly vaultSha256: string;
  };
  readonly manuscriptGraphSnapshot: {
    readonly notes: number;
    readonly links: number;
  };
  readonly snapshotNote: string;
}

export interface ProvenanceSource {
  readonly id: string;
  /** Repository-relative path; never an absolute local path. */
  readonly sourcePath: string;
  readonly sha256: string;
}

export interface ProvenanceTransformation {
  readonly output: string;
  readonly sources: readonly string[];
  readonly method: string;
}

export interface ProvenanceManifest {
  readonly schemaVersion: string;
  readonly sources: ProvenanceSource[];
  readonly transformations: ProvenanceTransformation[];
  readonly validatedInvariants: Readonly<Record<string, string | number | boolean>>;
  readonly generatedDataPolicy: string;
}

export type ProvenanceBundle = ProvenanceManifest;

export interface GraphNode {
  readonly id: string;
  readonly type: GraphNodeType;
  readonly title: string;
  readonly aliases: string[];
  readonly year?: number;
  readonly paperType?: string;
  readonly availability?: string;
  readonly doi?: string;
  readonly url?: string;
  readonly sourceNote?: string;
  readonly isManufacturingDataset: boolean;
  readonly isPublicDataset: boolean;
  readonly isSynthesisCandidate: boolean;
  readonly isCuratedEvidence: boolean;
}

export interface GraphEdge {
  readonly source: string;
  readonly target: string;
}

export interface GraphSummary {
  readonly counts: {
    readonly ambiguous_edges: number;
    readonly datasets: number;
    readonly duplicate_titles: number;
    readonly notes: number;
    readonly papers: number;
    readonly public_datasets: number;
    readonly public_manufacturing_dataset_candidates: number;
    readonly resolved_edges: number;
    readonly synthesis_impact_candidates: number;
    readonly unique_wikilink_edges: number;
    readonly unresolved_edges: number;
  };
  readonly interpretation: Readonly<Record<string, string>>;
  readonly repository_schema_version: string;
  readonly snapshot_date: string;
  readonly vault_sha256: string;
  readonly typeCounts: Readonly<Record<GraphNodeType, number>>;
  readonly selfLinks: number;
}

export interface GraphBundle {
  readonly nodes: GraphNode[];
  readonly edges: GraphEdge[];
  readonly summary: GraphSummary;
}

export interface DatasetFilters {
  readonly query?: string;
  readonly domains?: readonly DomainId[];
  readonly tasks?: readonly InspectionTask[];
  readonly annotations?: readonly string[];
  readonly modalities?: readonly string[];
}

export interface EvidenceFilters {
  readonly query?: string;
  readonly domains?: readonly string[];
  readonly tasks?: readonly string[];
  readonly synthesisFamilies?: readonly string[];
  readonly metrics?: readonly string[];
  readonly datasets?: readonly string[];
}

export interface GraphNodeFilters {
  readonly query?: string;
  readonly types?: readonly GraphNodeType[];
  readonly years?: readonly number[];
  readonly paperTypes?: readonly string[];
  readonly availability?: readonly string[];
  readonly publicDatasetsOnly?: boolean;
  readonly manufacturingDatasetsOnly?: boolean;
  readonly curatedEvidenceOnly?: boolean;
  readonly excludeAutomatedCandidates?: boolean;
}

export const EXPECTED_SCIENTIFIC_COUNTS = {
  datasets: 61,
  domains: 7,
  taskAssignments: 92,
  evidenceRows: 39,
  uniqueStudies: 37,
} as const;

export type ScientificInvariantCode =
  | "dataset-count"
  | "domain-count"
  | "task-assignment-count"
  | "coverage-dataset-count"
  | "coverage-domain-count"
  | "coverage-assignment-count"
  | "evidence-count"
  | "unique-study-count"
  | "duplicate-evidence-id"
  | "representative-nc-positive"
  | "representative-nc-range";

export interface ScientificInvariantIssue {
  readonly code: ScientificInvariantCode;
  readonly message: string;
  readonly expected: string | number;
  readonly actual: string | number;
}

export interface ScientificValidationInput {
  readonly datasets: readonly DatasetRecord[];
  readonly taskCoverage: TaskCoverage;
  readonly evidence: readonly EvidenceItem[];
}

export interface ScientificValidationResult {
  readonly ok: boolean;
  readonly issues: readonly ScientificInvariantIssue[];
  readonly observed: {
    readonly datasets: number;
    readonly domains: number;
    readonly taskAssignments: number;
    readonly evidenceRows: number;
    readonly uniqueStudies: number;
    readonly positiveRepresentativeNormalizedChanges: number;
  };
}

export function formatNormalizedChange(
  value: number | null | undefined,
  fractionDigits = 2,
): string {
  if (value === null || value === undefined || !Number.isFinite(value)) {
    return "Not reported";
  }
  if (!Number.isInteger(fractionDigits) || fractionDigits < 0 || fractionDigits > 6) {
    throw new RangeError("fractionDigits must be an integer between 0 and 6");
  }
  return (Object.is(value, -0) ? 0 : value).toFixed(fractionDigits);
}

export function isCitationCountAvailable(value: CitationCount): value is number {
  return value !== null;
}

export function formatCitationCount(value: CitationCount): string {
  return isCitationCountAvailable(value)
    ? new Intl.NumberFormat("en-US", { maximumFractionDigits: 0 }).format(value)
    : "Not available";
}

/** Case-insensitive Unicode normalization without stemming or fuzzy matching. */
export function normalizeExactText(value: string): string {
  return value.normalize("NFKC").toLocaleLowerCase("en").replace(/\s+/g, " ").trim();
}

export function equalsExactText(candidate: string, expected: string): boolean {
  return normalizeExactText(candidate) === normalizeExactText(expected);
}

/** Literal substring search: punctuation is kept and no inferred match is made. */
export function matchesExactTextSearch(query: string, fields: readonly string[]): boolean {
  const normalizedQuery = normalizeExactText(query);
  if (normalizedQuery.length === 0) return true;
  return fields.some((field) => normalizeExactText(field).includes(normalizedQuery));
}

function selectedIncludes<T>(selected: readonly T[] | undefined, value: T): boolean {
  return selected === undefined || selected.length === 0 || selected.includes(value);
}

function selectedIncludesText(selected: readonly string[] | undefined, value: string): boolean {
  return (
    selected === undefined ||
    selected.length === 0 ||
    selected.some((candidate) => equalsExactText(candidate, value))
  );
}

export function filterDatasets(
  records: readonly DatasetRecord[],
  filters: DatasetFilters,
): DatasetRecord[] {
  return records.filter(
    (record) =>
      matchesExactTextSearch(filters.query ?? "", [
        record.name,
        record.domain,
        ...record.tasks,
        record.annotation,
        record.modality,
        record.resolution,
        record.samplesClasses,
        ...record.citationKeys,
      ]) &&
      selectedIncludes(filters.domains, record.domainId) &&
      (filters.tasks === undefined ||
        filters.tasks.length === 0 ||
        filters.tasks.some((task) => record.tasks.includes(task))) &&
      selectedIncludesText(filters.annotations, record.annotation) &&
      selectedIncludesText(filters.modalities, record.modality),
  );
}

export function filterEvidence(
  records: readonly EvidenceItem[],
  filters: EvidenceFilters,
): EvidenceItem[] {
  return records.filter(
    (record) =>
      matchesExactTextSearch(filters.query ?? "", [
        record.id,
        record.studyKey,
        record.study.title,
        ...record.study.authors,
        record.dataset,
        record.task,
        record.annotation,
        record.synthesisFamily,
        record.setup,
        record.comparator,
        record.representative.metric,
        record.categories.domain,
        record.categories.concept,
        record.categories.model,
        record.categories.family,
      ]) &&
      selectedIncludesText(filters.domains, record.categories.domain) &&
      selectedIncludesText(filters.tasks, record.task) &&
      selectedIncludesText(filters.synthesisFamilies, record.synthesisFamily) &&
      selectedIncludesText(filters.metrics, record.representative.metric) &&
      selectedIncludesText(filters.datasets, record.dataset),
  );
}

export function filterGraphNodes(
  nodes: readonly GraphNode[],
  filters: GraphNodeFilters,
): GraphNode[] {
  return nodes.filter(
    (node) =>
      matchesExactTextSearch(filters.query ?? "", [
        node.id,
        node.title,
        ...node.aliases,
        node.doi ?? "",
        node.sourceNote ?? "",
      ]) &&
      selectedIncludes(filters.types, node.type) &&
      (filters.years === undefined ||
        filters.years.length === 0 ||
        (node.year !== undefined && filters.years.includes(node.year))) &&
      selectedIncludesText(filters.paperTypes, node.paperType ?? "") &&
      selectedIncludesText(filters.availability, node.availability ?? "") &&
      (!filters.publicDatasetsOnly || node.isPublicDataset) &&
      (!filters.manufacturingDatasetsOnly || node.isManufacturingDataset) &&
      (!filters.curatedEvidenceOnly || node.isCuratedEvidence) &&
      (!filters.excludeAutomatedCandidates || !node.isSynthesisCandidate),
  );
}

/**
 * Hyndman-Fan type-7 quantile, matching the manuscript. Use only for a fixed,
 * source-backed display series; never create filtered-subset claims with it.
 */
export function quantileType7ForDisplay(
  values: readonly number[],
  probability: number,
): number | null {
  if (probability < 0 || probability > 1 || !Number.isFinite(probability)) {
    throw new RangeError("probability must be between 0 and 1");
  }
  if (values.length === 0) return null;
  if (values.some((value) => !Number.isFinite(value))) {
    throw new TypeError("quantile values must all be finite");
  }

  const sorted = [...values].sort((left, right) => left - right);
  const index = (sorted.length - 1) * probability;
  const lowerIndex = Math.floor(index);
  const upperIndex = Math.ceil(index);
  const lower = sorted[lowerIndex];
  const upper = sorted[upperIndex];
  return lower + (upper - lower) * (index - lowerIndex);
}

export function quartilesType7ForDisplay(values: readonly number[]): {
  readonly first: number;
  readonly median: number;
  readonly third: number;
} | null {
  const first = quantileType7ForDisplay(values, 0.25);
  const median = quantileType7ForDisplay(values, 0.5);
  const third = quantileType7ForDisplay(values, 0.75);
  if (first === null || median === null || third === null) return null;
  return { first, median, third };
}

function addIssue(
  issues: ScientificInvariantIssue[],
  code: ScientificInvariantCode,
  expected: string | number,
  actual: string | number,
  message: string,
) {
  if (expected !== actual) issues.push({ code, expected, actual, message });
}

export function validateScientificInvariants(
  input: ScientificValidationInput,
): ScientificValidationResult {
  const { datasets, taskCoverage, evidence } = input;
  const issues: ScientificInvariantIssue[] = [];
  const domainCount = new Set(datasets.map((dataset) => dataset.domainId)).size;
  const taskAssignmentCount = datasets.reduce((total, dataset) => total + dataset.tasks.length, 0);
  const uniqueStudyCount = new Set(evidence.map((record) => record.studyKey.trim()).filter(Boolean))
    .size;
  const positiveNcCount = evidence.filter(
    (record) =>
      Number.isFinite(record.representative.normalizedChange) &&
      record.representative.normalizedChange > 0,
  ).length;

  addIssue(issues, "dataset-count", 61, datasets.length, "Expected 61 registry datasets.");
  addIssue(issues, "domain-count", 7, domainCount, "Expected seven registry domains.");
  addIssue(
    issues,
    "task-assignment-count",
    92,
    taskAssignmentCount,
    "Expected 92 non-exclusive task assignments.",
  );
  addIssue(
    issues,
    "coverage-dataset-count",
    61,
    taskCoverage.uniqueDatasets,
    "Expected 61 datasets in the published coverage matrix.",
  );
  addIssue(
    issues,
    "coverage-domain-count",
    7,
    taskCoverage.domainOrder.length,
    "Expected seven rows in the published coverage matrix.",
  );
  addIssue(
    issues,
    "coverage-assignment-count",
    92,
    taskCoverage.assignmentTotal,
    "Expected 92 assignments in the published coverage matrix.",
  );
  addIssue(issues, "evidence-count", 39, evidence.length, "Expected 39 evidence rows.");
  addIssue(
    issues,
    "unique-study-count",
    37,
    uniqueStudyCount,
    "Expected 37 unique evidence studies.",
  );

  const duplicateEvidenceIds = evidence.length - new Set(evidence.map((record) => record.id)).size;
  addIssue(
    issues,
    "duplicate-evidence-id",
    0,
    duplicateEvidenceIds,
    "Evidence identifiers must be unique.",
  );
  addIssue(
    issues,
    "representative-nc-positive",
    evidence.length,
    positiveNcCount,
    "Every retained representative NC must be finite and positive.",
  );

  const outsideRange = evidence.filter(
    (record) =>
      !Number.isFinite(record.representative.normalizedChange) ||
      record.representative.normalizedChange < -1 ||
      record.representative.normalizedChange > 1,
  ).length;
  addIssue(
    issues,
    "representative-nc-range",
    0,
    outsideRange,
    "Normalized change must remain in its documented [-1, 1] range.",
  );

  return {
    ok: issues.length === 0,
    issues,
    observed: {
      datasets: datasets.length,
      domains: domainCount,
      taskAssignments: taskAssignmentCount,
      evidenceRows: evidence.length,
      uniqueStudies: uniqueStudyCount,
      positiveRepresentativeNormalizedChanges: positiveNcCount,
    },
  };
}

export function assertScientificInvariants(input: ScientificValidationInput): void {
  const result = validateScientificInvariants(input);
  if (result.ok) return;
  throw new Error(
    `Scientific invariant validation failed:\n${result.issues
      .map((issue) => `- ${issue.code}: expected ${issue.expected}, received ${issue.actual}`)
      .join("\n")}`,
  );
}
