import { describe, expect, it } from "vitest";
import {
  assertScientificInvariants,
  CITATION_YEARS,
  type CitationYearCounts,
  type DatasetRecord,
  DOMAIN_IDS,
  DOMAIN_LABELS,
  type DomainDescriptor,
  type DomainId,
  type EvidenceId,
  type EvidenceItem,
  equalsExactText,
  filterDatasets,
  formatCitationCount,
  formatNormalizedChange,
  INSPECTION_TASKS,
  type InspectionTask,
  isCitationCountAvailable,
  matchesExactTextSearch,
  quartilesType7ForDisplay,
  type ScientificValidationInput,
  type TaskCoverage,
  validateScientificInvariants,
} from "./domain";

function makeDataset(index: number): DatasetRecord {
  const domainId = DOMAIN_IDS[index % DOMAIN_IDS.length];
  const primaryTask = INSPECTION_TASKS[index % INSPECTION_TASKS.length];
  const tasks: InspectionTask[] =
    index < 31
      ? [primaryTask, INSPECTION_TASKS[(index + 1) % INSPECTION_TASKS.length]]
      : [primaryTask];

  return {
    id: `dataset-${index + 1}`,
    ordinal: index + 1,
    name: `Dataset ${index + 1}`,
    domain: DOMAIN_LABELS[domainId],
    domainId,
    tasks,
    annotation: "Image labels",
    modality: "RGB",
    resolution: "Source-reported",
    samplesClasses: "Source-reported",
    citationKeys: [`DatasetSource${index + 1}`],
    graphNodeId: null,
    mappingStatus: "unresolved",
    sourceLine: index + 1,
  };
}

function makeEvidence(index: number): EvidenceItem {
  const ordinal = index + 1;
  const studyIndex = index < 37 ? index : index - 37;
  return {
    id: `E${String(ordinal).padStart(2, "0")}` as EvidenceId,
    ordinal,
    studyKey: `Study${studyIndex + 1}`,
    study: {
      title: `Study ${studyIndex + 1}`,
      authors: [],
      year: 2025,
      doi: null,
      url: null,
    },
    dataset: `Dataset ${(index % 61) + 1}`,
    task: "Classification",
    annotation: "Image-level",
    synthesisFamily: "GAN-based",
    setup: "Source-reported synthesis setup",
    comparator: "Source-reported comparator",
    representative: {
      metric: "Accuracy",
      sourceMetricLabel: "Accuracy",
      baseline: 80,
      after: 90,
      normalizedChange: 0.5,
      normalizedChangeSource: "0.5",
    },
    categories: {
      domain: "Semiconductor",
      concept: "Classification",
      model: "CNN",
      family: "GAN",
    },
    sourceLabels: {
      normalizedDataset: `Dataset ${(index % 61) + 1}`,
      normalizedTask: "Classification",
      normalizedAnnotation: "Image-level",
      normalizedFamily: "GAN-based",
    },
    chartScaleConverted: false,
  };
}

function emptyTaskCounts(): Record<InspectionTask, number> {
  return {
    Classification: 0,
    "Object detection": 0,
    Segmentation: 0,
    "Anomaly detection": 0,
    Localization: 0,
  };
}

function makeCoverage(datasets: readonly DatasetRecord[]): TaskCoverage {
  const taskTotals = emptyTaskCounts();
  const cells = {} as Record<DomainId, Record<InspectionTask, number>>;
  const datasetTotals = {} as Record<DomainId, number>;
  const domainOrder: DomainDescriptor[] = [];

  for (const domainId of DOMAIN_IDS) {
    const domainDatasets = datasets.filter((dataset) => dataset.domainId === domainId);
    const counts = emptyTaskCounts();
    for (const dataset of domainDatasets) {
      for (const task of dataset.tasks) {
        const taskKey = task as InspectionTask;
        counts[taskKey] += 1;
        taskTotals[taskKey] += 1;
      }
    }
    cells[domainId] = counts;
    datasetTotals[domainId] = domainDatasets.length;
    domainOrder.push({ id: domainId, label: DOMAIN_LABELS[domainId] });
  }

  return {
    domainOrder,
    taskOrder: [...INSPECTION_TASKS],
    cells,
    datasetTotals,
    taskTotals,
    uniqueDatasets: datasets.length,
    assignmentTotal: datasets.reduce((total, dataset) => total + dataset.tasks.length, 0),
  };
}

function makeValidInput(): ScientificValidationInput {
  const datasets = Array.from({ length: 61 }, (_, index) => makeDataset(index));
  return {
    datasets,
    taskCoverage: makeCoverage(datasets),
    evidence: Array.from({ length: 39 }, (_, index) => makeEvidence(index)),
  };
}

describe("scientific invariant validation", () => {
  it("accepts the manuscript's fixed dataset and evidence counts", () => {
    const input = makeValidInput();
    const result = validateScientificInvariants(input);

    expect(result.ok).toBe(true);
    expect(result.issues).toEqual([]);
    expect(result.observed).toEqual({
      datasets: 61,
      domains: 7,
      taskAssignments: 92,
      evidenceRows: 39,
      uniqueStudies: 37,
      positiveRepresentativeNormalizedChanges: 39,
    });
    expect(() => assertScientificInvariants(input)).not.toThrow();
  });

  it("reports changed counts, duplicate evidence IDs, and non-positive NC values", () => {
    const valid = makeValidInput();
    const datasets = valid.datasets.slice(0, 60).map((dataset) => ({
      ...dataset,
      domainId: "metals" as const,
      domain: "Metals",
    }));
    const evidence = valid.evidence.map((record, index) =>
      index === 0
        ? {
            ...record,
            representative: { ...record.representative, normalizedChange: 0 },
          }
        : index === 1
          ? { ...record, id: valid.evidence[0].id }
          : { ...record, studyKey: `UniqueStudy${index}` },
    );
    const result = validateScientificInvariants({
      datasets,
      taskCoverage: { ...makeCoverage(datasets), uniqueDatasets: 60, assignmentTotal: 91 },
      evidence,
    });
    const codes = result.issues.map((issue) => issue.code);

    expect(result.ok).toBe(false);
    expect(codes).toContain("dataset-count");
    expect(codes).toContain("domain-count");
    expect(codes).toContain("task-assignment-count");
    expect(codes).toContain("coverage-dataset-count");
    expect(codes).toContain("coverage-assignment-count");
    expect(codes).toContain("unique-study-count");
    expect(codes).toContain("duplicate-evidence-id");
    expect(codes).toContain("representative-nc-positive");
    expect(() =>
      assertScientificInvariants({
        datasets,
        taskCoverage: makeCoverage(datasets),
        evidence,
      }),
    ).toThrow(/Scientific invariant validation failed/);
  });
});

describe("citation counts", () => {
  it("keeps a missing year distinct from a true zero", () => {
    const annual: CitationYearCounts = {
      2020: null,
      2021: 0,
      2022: 1,
      2023: 2,
      2024: 3,
      2025: 4,
    };

    expect(CITATION_YEARS.map((year) => annual[year])).toEqual([null, 0, 1, 2, 3, 4]);
    expect(isCitationCountAvailable(annual[2020])).toBe(false);
    expect(isCitationCountAvailable(annual[2021])).toBe(true);
    expect(formatCitationCount(annual[2020])).toBe("Not available");
    expect(formatCitationCount(annual[2021])).toBe("0");
  });
});

describe("presentation-only helpers", () => {
  it("formats existing normalized-change values without recalculating them", () => {
    expect(formatNormalizedChange(0.8505)).toBe("0.85");
    expect(formatNormalizedChange(-0)).toBe("0.00");
    expect(formatNormalizedChange(null)).toBe("Not reported");
  });

  it("uses type-7 quartiles for a fixed display series", () => {
    expect(quartilesType7ForDisplay([0, 1, 2, 3])).toEqual({
      first: 0.75,
      median: 1.5,
      third: 2.25,
    });
  });

  it("uses normalized literal text matching and exact categorical filters", () => {
    const datasets = makeValidInput().datasets;
    expect(equalsExactText("MVTec AD", "mvtec ad")).toBe(true);
    expect(matchesExactTextSearch("MVTec", ["MVTec AD", "BTAD"])).toBe(true);
    expect(matchesExactTextSearch("MVTec-AD", ["MVTec AD"])).toBe(false);
    expect(
      filterDatasets(datasets, {
        domains: ["metals"],
        tasks: ["Classification"],
      }).every(
        (dataset) => dataset.domainId === "metals" && dataset.tasks.includes("Classification"),
      ),
    ).toBe(true);
  });
});
