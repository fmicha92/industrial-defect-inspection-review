import type {
  CitationTrend,
  DatasetRegistry,
  EvidenceBundle,
  GraphBundle,
  ProvenanceManifest,
  TaskCoverage,
} from "./lib/domain";

export type Dataset = DatasetRegistry["datasets"][number];
export type EvidenceItem = EvidenceBundle["items"][number];
export type DatasetData = DatasetRegistry;
export type CoverageData = TaskCoverage;
export type CitationData = CitationTrend;
export type EvidenceData = EvidenceBundle;
export type { GraphBundle, ProvenanceManifest };

export type MetaData = {
  title: string;
  authors: string[];
  manuscript: { datasets: number; domains: number; evaluations: number; studies: number };
  graphSnapshot: {
    date: string;
    schemaVersion: string;
    notes: number;
    resolvedEdges: number;
    vaultSha256: string;
  };
  manuscriptGraphSnapshot: { notes: number; links: number };
  snapshotNote: string;
};

export type SiteData = {
  datasets: DatasetData;
  coverage: CoverageData;
  citations: CitationData;
  evidence: EvidenceData;
  graph: GraphBundle;
  meta: MetaData;
  provenance: ProvenanceManifest;
};
