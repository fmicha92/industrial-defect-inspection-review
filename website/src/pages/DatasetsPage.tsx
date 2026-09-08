import { ChevronRight, Download, GitCompareArrows, Network, Search, X } from "lucide-react";
import { useCallback, useMemo } from "react";
import { Link } from "react-router-dom";
import { CitationTrend, CoverageMatrix } from "../components/Charts";
import DetailDialog from "../components/DetailDialog";
import { EmptyState, PageHero, SectionHeading } from "../components/Layout";
import { matchesSearch } from "../lib/navigation";
import { useBrowseParams } from "../lib/use-browse-params";
import type { CitationData, Dataset, SiteData } from "../types";

export default function DatasetsPage({ data }: { data: SiteData }) {
  const { params, update } = useBrowseParams();
  const query = params.get("q") ?? "";
  const domain = params.get("domain") ?? "all";
  const task = params.get("task") ?? "all";
  const sort = params.get("sort") ?? "source";
  const selected =
    data.datasets.datasets.find((dataset) => dataset.id === params.get("record")) ?? null;
  const compareIds = [...new Set((params.get("compare") ?? "").split(","))]
    .filter((id) => data.datasets.datasets.some((dataset) => dataset.id === id))
    .slice(0, 3);
  const closeDrawer = useCallback(() => update({ record: null }), [update]);
  const openDataset = (id: string) => update({ record: id });
  const filtered = useMemo(
    () =>
      data.datasets.datasets
        .filter(
          (dataset) =>
            matchesSearch(query, [
              dataset.id,
              dataset.name,
              dataset.domain,
              dataset.annotation,
              dataset.modality,
              dataset.resolution,
              dataset.samplesClasses,
              ...dataset.citationKeys,
              ...dataset.tasks,
            ]) &&
            (domain === "all" || dataset.domainId === domain) &&
            (task === "all" || dataset.tasks.includes(task)),
        )
        .sort(
          (a, b) =>
            (sort === "name"
              ? a.name.localeCompare(b.name)
              : sort === "domain"
                ? a.domain.localeCompare(b.domain) || a.name.localeCompare(b.name)
                : 0) || a.ordinal - b.ordinal,
        ),
    [data.datasets.datasets, query, domain, task, sort],
  );
  const compared = compareIds
    .map((id) => data.datasets.datasets.find((dataset) => dataset.id === id))
    .filter((item): item is Dataset => Boolean(item));
  const toggleCompare = (id: string) =>
    update({
      compare: (compareIds.includes(id)
        ? compareIds.filter((item) => item !== id)
        : compareIds.length < 3
          ? [...compareIds, id]
          : compareIds
      ).join(","),
    });
  const citationRowsWithoutAnnualValues = data.citations.rows.filter((row) =>
    Object.values(row.annual).every((value) => value === null),
  ).length;
  return (
    <>
      <PageHero
        eyebrow="Public dataset landscape"
        title="Start with the evaluation context."
        lede="Explore 61 public dataset sources as the manuscript reports them—organized by domain and non-exclusive task support, with annotation, modality, resolution, scale, and ordered manuscript bibliography keys kept visible."
        stat="61"
        statLabel="registry records"
      />
      <section className="section-shell overview-grid">
        <article className="panel wide-panel">
          <div className="panel-heading">
            <div>
              <p className="kicker">Coverage, not a ranking</p>
              <h2>Where public evaluation is possible</h2>
            </div>
            <span className="panel-badge">92 non-exclusive assignments</span>
          </div>
          <CoverageMatrix
            data={data.coverage}
            onSelect={(nextDomain, nextTask) => update({ domain: nextDomain, task: nextTask })}
          />
        </article>
        <article className="panel wide-panel">
          <div className="panel-heading">
            <div>
              <p className="kicker">Scholarly visibility proxy</p>
              <h2>Source-publication citations</h2>
            </div>
            <span className="panel-badge">Published aggregate</span>
          </div>
          <CitationTrend data={data.citations} />
          <p className="micro-note">
            OpenAlex citations to dataset-source publications are a descriptive proxy for scholarly
            visibility—not direct dataset use, benchmark quality, or relevance for synthesis. The
            row source contains {data.citations.rows.length} of{" "}
            {data.datasets.summary.uniqueDatasets} registry records ({data.citations.missingDataset}{" "}
            is absent), and {citationRowsWithoutAnnualValues} included records have unavailable
            annual values rather than reported zeros. The chart reproduces the manuscript&apos;s
            published domain aggregates.
          </p>
        </article>
      </section>

      <section className="section-shell registry-section">
        <SectionHeading
          index="01"
          eyebrow="Interactive registry"
          title="Compare datasets in context"
          aside="Counts, resolution, and class descriptions retain their source semantics; they are not coerced into a false common schema."
        />
        <div className="filter-bar">
          <label className="search-field">
            <Search size={18} />
            <span className="sr-only">Search datasets</span>
            <input
              value={query}
              onChange={(event) => update({ q: event.target.value })}
              placeholder="Search name, modality, annotation…"
            />
          </label>
          <label>
            <span>Domain</span>
            <select value={domain} onChange={(event) => update({ domain: event.target.value })}>
              <option value="all">All seven domains</option>
              {data.datasets.domains.map((item) => (
                <option key={item.id} value={item.id}>
                  {item.label}
                </option>
              ))}
            </select>
          </label>
          <label>
            <span>Task</span>
            <select value={task} onChange={(event) => update({ task: event.target.value })}>
              <option value="all">All tasks</option>
              {data.datasets.tasks.map((item) => (
                <option key={item}>{item}</option>
              ))}
            </select>
          </label>
          <button
            type="button"
            className="reset-filter"
            onClick={() => {
              update({ q: null, domain: null, task: null, sort: null, page: null });
            }}
          >
            <X size={15} /> Reset
          </button>
        </div>
        <div className="results-meta">
          <span aria-live="polite" aria-atomic="true">
            <strong>{filtered.length}</strong> of 61 datasets
            {filtered.length === 0 && (
              <span className="sr-only">
                . No dataset matches these filters. Try a broader term or reset the domain and task
                filters.
              </span>
            )}
          </span>
          <span>
            <i className="mapping-dot" /> {data.datasets.summary.graphExactMatches} exact ·{" "}
            {data.datasets.summary.graphExplicitMatches} explicit graph mappings ·{" "}
            {data.datasets.summary.graphUnresolved} unresolved
          </span>
          <a href={`${import.meta.env.BASE_URL}data/datasets.json`} download>
            <Download size={15} /> Registry JSON
          </a>
        </div>
        <div className="registry-table-wrap">
          <table className="registry-table">
            <caption className="sr-only">
              Filtered public dataset registry with domain, supported tasks, annotation, modality,
              comparison controls, and detail actions.
            </caption>
            <thead>
              <tr>
                <th scope="col">Dataset</th>
                <th scope="col">Domain</th>
                <th scope="col">Supported tasks</th>
                <th scope="col">Annotation / modality</th>
                <th scope="col">
                  <span className="sr-only">Actions</span>
                </th>
              </tr>
            </thead>
            <tbody>
              {filtered.map((dataset) => (
                <tr key={dataset.id}>
                  <td>
                    <button
                      className="dataset-name"
                      type="button"
                      onClick={() => openDataset(dataset.id)}
                    >
                      <span>{String(dataset.ordinal).padStart(2, "0")}</span>
                      <strong>{dataset.name}</strong>
                    </button>
                  </td>
                  <td>{dataset.domain}</td>
                  <td>
                    <div className="tag-row">
                      {dataset.tasks.map((item) => (
                        <span key={item}>{item}</span>
                      ))}
                    </div>
                  </td>
                  <td>
                    <strong className="cell-primary">{dataset.annotation}</strong>
                    <small>{dataset.modality}</small>
                  </td>
                  <td>
                    <label
                      className="compare-check"
                      title={
                        compareIds.length >= 3 && !compareIds.includes(dataset.id)
                          ? "Compare up to three datasets"
                          : "Add to comparison"
                      }
                    >
                      <input
                        type="checkbox"
                        checked={compareIds.includes(dataset.id)}
                        disabled={compareIds.length >= 3 && !compareIds.includes(dataset.id)}
                        onChange={() => toggleCompare(dataset.id)}
                      />
                      <GitCompareArrows size={17} />
                      <span className="sr-only">Compare {dataset.name}</span>
                    </label>
                    <button
                      className="row-open"
                      type="button"
                      onClick={() => openDataset(dataset.id)}
                      aria-label={`Open ${dataset.name}`}
                    >
                      <ChevronRight />
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
          {filtered.length === 0 && (
            <EmptyState
              title="No dataset matches these filters."
              copy="Try a broader term or reset the domain and task filters."
            />
          )}
        </div>
      </section>
      {compared.length > 0 && (
        <CompareTray
          datasets={compared}
          onRemove={toggleCompare}
          onClear={() => update({ compare: null })}
        />
      )}
      {selected && (
        <DatasetDrawer
          dataset={selected}
          citation={data.citations.rows.find((row) => row.datasetId === selected.id)}
          onClose={closeDrawer}
        />
      )}
    </>
  );
}

function CompareTray({
  datasets,
  onRemove,
  onClear,
}: {
  datasets: Dataset[];
  onRemove: (id: string) => void;
  onClear: () => void;
}) {
  return (
    <aside className="compare-tray" aria-label="Dataset comparison">
      <div className="compare-header">
        <div>
          <GitCompareArrows />
          <span>
            <strong>Dataset comparison</strong>
            <small>{datasets.length}/3 selected</small>
          </span>
        </div>
        <button type="button" onClick={onClear}>
          Clear all
        </button>
      </div>
      <div className="compare-grid">
        {datasets.map((dataset) => (
          <article key={dataset.id}>
            <button
              type="button"
              onClick={() => onRemove(dataset.id)}
              aria-label={`Remove ${dataset.name}`}
            >
              <X />
            </button>
            <p className="kicker">{dataset.domain}</p>
            <h3>{dataset.name}</h3>
            <dl>
              <div>
                <dt>Tasks</dt>
                <dd>{dataset.tasks.join(" · ")}</dd>
              </div>
              <div>
                <dt>Annotation</dt>
                <dd>{dataset.annotation}</dd>
              </div>
              <div>
                <dt>Modality</dt>
                <dd>{dataset.modality}</dd>
              </div>
              <div>
                <dt>Resolution</dt>
                <dd>{dataset.resolution}</dd>
              </div>
              <div>
                <dt>Scale / classes</dt>
                <dd>{dataset.samplesClasses}</dd>
              </div>
            </dl>
          </article>
        ))}
      </div>
    </aside>
  );
}

function DatasetDrawer({
  dataset,
  citation,
  onClose,
}: {
  dataset: Dataset;
  citation?: CitationData["rows"][number];
  onClose: () => void;
}) {
  const annualValues = citation
    ? Object.values(citation.annual).filter((value): value is number => value !== null)
    : [];
  return (
    <DetailDialog labelId="dataset-drawer-title" onClose={onClose}>
      <button
        className="drawer-close"
        type="button"
        onClick={onClose}
        aria-label="Close dataset details"
      >
        <X />
      </button>
      <p className="eyebrow">Registry record {String(dataset.ordinal).padStart(2, "0")}</p>
      <h2 id="dataset-drawer-title">{dataset.name}</h2>
      <p className="drawer-domain">{dataset.domain}</p>
      <div className="tag-row large">
        {dataset.tasks.map((task) => (
          <span key={task}>{task}</span>
        ))}
      </div>
      <dl className="drawer-facts">
        <div>
          <dt>Annotation</dt>
          <dd>{dataset.annotation}</dd>
        </div>
        <div>
          <dt>Modality</dt>
          <dd>{dataset.modality}</dd>
        </div>
        <div>
          <dt>Released resolution</dt>
          <dd>{dataset.resolution}</dd>
        </div>
        <div>
          <dt>Samples and classes</dt>
          <dd>{dataset.samplesClasses}</dd>
        </div>
      </dl>
      <div className="drawer-section">
        <h3>Manuscript source keys</h3>
        <p>{dataset.citationKeys.join(" · ")}</p>
        <small>
          Ordered bibliography keys from the manuscript registry · source line {dataset.sourceLine}
        </small>
      </div>
      <div className="drawer-section">
        <h3>Citation evidence</h3>
        {citation ? (
          <>
            <p>
              <strong>{citation.title}</strong> ({citation.publicationYear})
            </p>
            <div className="year-chips">
              {Object.entries(citation.annual).map(([year, value]) => (
                <span key={year}>
                  {year}
                  <strong>{value === null ? "—" : value}</strong>
                </span>
              ))}
            </div>
            <small>
              {citation.matchMethod} match
              {annualValues.length === 0 ? " · annual values unavailable, not zero" : ""}
            </small>
          </>
        ) : (
          <p>
            No citation-series row is present for this registry record. Absence is not encoded as
            zero.
          </p>
        )}
      </div>
      {dataset.graphNodeId && (
        <Link
          className="primary-action drawer-action"
          to={`/?node=${encodeURIComponent(dataset.graphNodeId)}`}
        >
          Open in evidence graph <Network />
        </Link>
      )}
    </DetailDialog>
  );
}
