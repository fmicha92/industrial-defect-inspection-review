import { ArrowRight, ChevronRight, Download, ExternalLink, Info, Search, X } from "lucide-react";
import { useCallback, useMemo, useRef } from "react";
import { Link } from "react-router-dom";
import { ChangeDistribution, EvidenceMatrix, EvidenceScatter } from "../components/Charts";
import DetailDialog from "../components/DetailDialog";
import { EmptyState, PageHero, SectionHeading } from "../components/Layout";
import { matchesSearch, publicationUrl, relatedDatasets } from "../lib/navigation";
import { formatScore } from "../lib/site-data";
import { useBrowseParams } from "../lib/use-browse-params";
import type { EvidenceItem, SiteData } from "../types";

export default function EvidencePage({ data }: { data: SiteData }) {
  const { params, update } = useBrowseParams();
  const query = params.get("q") ?? "";
  const domain = params.get("domain") ?? "all";
  const family = params.get("family") ?? "all";
  const concept = params.get("task") ?? "all";
  const sort = params.get("sort") ?? "source";
  const datasetId = params.get("dataset");
  const retainedItems = data.evidence.items;
  const selected = retainedItems.find((item) => item.id === params.get("record")) ?? null;
  const returnFocusRef = useRef<Element | null>(null);
  const domains = [...new Set(retainedItems.map((item) => item.categories.domain))];
  const families = [...new Set(retainedItems.map((item) => item.categories.family))];
  const concepts = [...new Set(retainedItems.map((item) => item.categories.concept))];
  const filtered = useMemo(
    () =>
      retainedItems
        .filter(
          (item) =>
            matchesSearch(query, [
              item.id,
              item.dataset,
              item.study.title,
              item.studyKey,
              item.study.year,
              ...item.study.authors,
              item.task,
              item.annotation,
              item.synthesisFamily,
              item.setup,
              item.comparator,
              item.representative.metric,
              ...Object.values(item.categories),
            ]) &&
            (domain === "all" || item.categories.domain === domain) &&
            (family === "all" || item.categories.family === family) &&
            (concept === "all" || item.categories.concept === concept) &&
            (!datasetId ||
              relatedDatasets(item, data.datasets.datasets).some(
                (record) => record.id === datasetId,
              )),
        )
        .sort(
          (a, b) =>
            (sort === "year"
              ? (b.study.year ?? 0) - (a.study.year ?? 0)
              : sort === "dataset"
                ? a.dataset.localeCompare(b.dataset)
                : 0) || a.ordinal - b.ordinal,
        ),
    [retainedItems, data.datasets.datasets, query, domain, family, concept, datasetId, sort],
  );
  const openEvidence = useCallback(
    (item: EvidenceItem, trigger?: Element | null) => {
      returnFocusRef.current = trigger ?? document.activeElement;
      update({ record: item.id });
    },
    [update],
  );
  const closeEvidence = useCallback(() => update({ record: null }), [update]);
  const openChartEvidence = (id: string, trigger: Element) => {
    const item = retainedItems.find((record) => record.id === id);
    if (item) openEvidence(item, trigger);
  };
  return (
    <>
      <PageHero
        eyebrow="Synthesis-supported evidence"
        title="Read the gain with its conditions attached."
        lede="Inspect 39 representative downstream comparisons retained from 37 studies. Every row preserves the public dataset, task, annotation, synthesis setup, comparator, reported metric, and precise normalized change."
        stat="0.43"
        statLabel="median NC"
      />
      <section className="interpretation-banner">
        <Info />
        <div>
          <strong>Descriptive evidence, not a league table.</strong>
          <p>
            All 39 representative normalized-change values are positive, but the evaluations are
            heterogeneous and partly non-independent. The view does not estimate how often synthesis
            succeeds.
          </p>
        </div>
        <Link to="/review/">
          Read the boundary conditions <ExternalLink />
        </Link>
      </section>
      <section className="section-shell evidence-dashboard">
        <div className="evidence-chart-grid">
          <article className="panel" aria-labelledby="filtered-scatter-scope">
            <p className="micro-note" id="filtered-scatter-scope">
              <strong>Filtered chart</strong> · {filtered.length} of {retainedItems.length} retained
              comparisons match the controls below.
            </p>
            <EvidenceScatter items={filtered} onSelect={openChartEvidence} />
          </article>
          <article className="panel">
            <div id="change-distribution" aria-labelledby="full-distribution-scope">
              <p className="micro-note" id="full-distribution-scope">
                <strong>Full retained set</strong> · the distribution remains fixed at all{" "}
                {retainedItems.length} comparisons when filters change.
              </p>
              <ChangeDistribution items={retainedItems} onSelect={openChartEvidence} />
            </div>
            <div aria-labelledby="filtered-matrix-scope">
              <p className="micro-note" id="filtered-matrix-scope">
                <strong>Filtered cross-tab</strong> · {filtered.length} of {retainedItems.length}{" "}
                comparisons.
              </p>
              <EvidenceMatrix
                items={filtered}
                onSelect={(nextFamily, nextDomain) =>
                  update({ family: nextFamily, domain: nextDomain })
                }
              />
            </div>
          </article>
        </div>
        <div className="results-meta">
          <span id="full-family-statistics-scope">
            <strong>Full-set family statistics</strong> · fixed manuscript summaries for all{" "}
            {retainedItems.length} retained comparisons
          </span>
        </div>
        <div className="family-stat-row" aria-labelledby="full-family-statistics-scope">
          {data.evidence.summary.familyStatistics.map((stat) => (
            <article key={stat.family}>
              <span className={`family-swatch ${stat.family.toLocaleLowerCase("en")}`} />
              <p>{stat.family}</p>
              <strong>{stat.median.toFixed(2)}</strong>
              <small>
                full-set median NC · mean {stat.mean.toFixed(2)}
                {stat.n ? ` · n=${stat.n}` : ""}
              </small>
            </article>
          ))}
        </div>
      </section>
      <section className="section-shell evidence-table-section" id="evidence-records">
        <SectionHeading
          index="01"
          eyebrow="Evidence atlas"
          title="Open any comparison"
          aside="The plotted baseline and after values use the manuscript's chart-ready 0–100 scale. Precise NC comes from the normalized-change source table; six explicitly documented rows were already scale-converted upstream."
        />
        <div className="filter-bar evidence-filters">
          <label className="search-field">
            <Search size={18} />
            <span className="sr-only">Search evidence</span>
            <input
              value={query}
              onChange={(event) => update({ q: event.target.value })}
              placeholder="Search dataset, study, setup…"
            />
          </label>
          <label>
            <span>Domain</span>
            <select value={domain} onChange={(event) => update({ domain: event.target.value })}>
              <option value="all">All domains</option>
              {domains.map((item) => (
                <option key={item}>{item}</option>
              ))}
            </select>
          </label>
          <label>
            <span>Family</span>
            <select value={family} onChange={(event) => update({ family: event.target.value })}>
              <option value="all">All families</option>
              {families.map((item) => (
                <option key={item}>{item}</option>
              ))}
            </select>
          </label>
          <label>
            <span>Task</span>
            <select value={concept} onChange={(event) => update({ task: event.target.value })}>
              <option value="all">All task groups</option>
              {concepts.map((item) => (
                <option key={item}>{item}</option>
              ))}
            </select>
          </label>
          <button
            type="button"
            className="reset-filter"
            onClick={() => {
              update({
                q: null,
                domain: null,
                family: null,
                task: null,
                dataset: null,
                sort: null,
                page: null,
              });
            }}
          >
            <X size={15} /> Reset
          </button>
        </div>
        <div className="results-meta">
          <span id="evidence-results-count" role="status" aria-live="polite" aria-atomic="true">
            <strong>{filtered.length}</strong> of 39 comparisons
          </span>
          <a
            href={`${import.meta.env.BASE_URL}downloads/synthesis_impact_normalized_change.csv`}
            download
          >
            <Download size={15} /> Download source CSV
          </a>
        </div>
        <div className="registry-table-wrap">
          <table
            className="registry-table evidence-table"
            aria-describedby="evidence-results-count"
          >
            <caption className="sr-only">
              Synthesis-supported evidence comparisons matching the active search and filters;{" "}
              {filtered.length} of {retainedItems.length} retained rows shown.
            </caption>
            <thead>
              <tr>
                <th scope="col">Evidence / study</th>
                <th scope="col">Dataset & task</th>
                <th scope="col">Synthesis</th>
                <th scope="col">Reported shift</th>
                <th scope="col">NC</th>
                <th scope="col">
                  <span className="sr-only">Open</span>
                </th>
              </tr>
            </thead>
            <tbody>
              {filtered.map((item) => (
                <tr key={item.id}>
                  <td>
                    <button
                      className="dataset-name"
                      type="button"
                      onClick={(event) => openEvidence(item, event.currentTarget)}
                    >
                      <span>{item.id}</span>
                      <strong>{item.study.title}</strong>
                    </button>
                    <small>
                      {item.study.year} · {item.studyKey}
                    </small>
                  </td>
                  <td>
                    <strong className="cell-primary">{item.dataset}</strong>
                    <small>
                      {item.task} · {item.annotation}
                    </small>
                  </td>
                  <td>
                    <span
                      className={`family-pill ${item.categories.family.toLocaleLowerCase("en")}`}
                    >
                      {item.categories.family}
                    </span>
                    <small>{item.categories.model}</small>
                  </td>
                  <td>
                    <strong className="score-shift">
                      {formatScore(item.representative.baseline)} <ArrowRight />{" "}
                      {formatScore(item.representative.after)}
                    </strong>
                    <small>{item.representative.metric}</small>
                  </td>
                  <td>
                    <strong className="nc-value">
                      {item.representative.normalizedChange.toFixed(2)}
                    </strong>
                  </td>
                  <td>
                    <button
                      className="row-open"
                      type="button"
                      onClick={(event) => openEvidence(item, event.currentTarget)}
                      aria-label={`Open ${item.id}`}
                    >
                      <ChevronRight />
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
          {filtered.length === 0 && (
            <div role="status" aria-live="polite" aria-atomic="true">
              <EmptyState
                title="No comparison matches these filters."
                copy="Reset one or more filters to return to the retained evidence set."
              />
            </div>
          )}
        </div>
      </section>
      {selected && (
        <EvidenceDrawer
          key={selected.id}
          item={selected}
          onClose={closeEvidence}
          returnFocus={returnFocusRef.current}
        />
      )}
    </>
  );
}

function EvidenceDrawer({
  item,
  onClose,
  returnFocus,
}: {
  item: EvidenceItem;
  onClose: () => void;
  returnFocus: Element | null;
}) {
  const sourceUrl = publicationUrl(item.study.url, item.study.doi);
  return (
    <DetailDialog
      labelId="evidence-drawer-title"
      descriptionId="evidence-drawer-context evidence-drawer-caveat"
      className="evidence-drawer"
      onClose={onClose}
      returnFocus={returnFocus}
    >
      <button
        className="drawer-close"
        type="button"
        onClick={onClose}
        aria-label="Close evidence details"
      >
        <X />
      </button>
      <div className="evidence-id-line">
        <span>{item.id}</span>
        <span className={`family-pill ${item.categories.family.toLocaleLowerCase("en")}`}>
          {item.categories.family}
        </span>
      </div>
      <h2 id="evidence-drawer-title">{item.dataset}</h2>
      <p className="drawer-domain" id="evidence-drawer-context">
        {item.task} · {item.annotation}
      </p>
      <div className="result-callout">
        <div>
          <span>{item.representative.metric}</span>
          <strong>
            {formatScore(item.representative.baseline)}
            <ArrowRight />
            {formatScore(item.representative.after)}
          </strong>
          <small>baseline → synthesis-supported</small>
        </div>
        <div>
          <span>Normalized change</span>
          <strong>{item.representative.normalizedChangeSource}</strong>
          <small>precise source value</small>
        </div>
      </div>
      <div className="drawer-section numbered">
        <span>01</span>
        <div>
          <h3>Synthesis-supported setup</h3>
          <p>{item.setup}</p>
        </div>
      </div>
      <div className="drawer-section numbered">
        <span>02</span>
        <div>
          <h3>Comparator preserved from the manuscript</h3>
          <p>{item.comparator}</p>
        </div>
      </div>
      <div className="drawer-section numbered">
        <span>03</span>
        <div>
          <h3>Study</h3>
          <p>
            <strong>{item.study.title}</strong>
          </p>
          <p>{item.study.authors.join(" · ")}</p>
          <small>
            {item.study.year} · {item.studyKey}
          </small>
          {sourceUrl && (
            <a
              className="external-study"
              href={sourceUrl ?? undefined}
              target="_blank"
              rel="noreferrer"
            >
              Open publication <ExternalLink />
            </a>
          )}
        </div>
      </div>
      <div className="condition-grid">
        <span>
          Domain<strong>{item.categories.domain}</strong>
        </span>
        <span>
          Task group<strong>{item.categories.concept}</strong>
        </span>
        <span>
          Model group<strong>{item.categories.model}</strong>
        </span>
        <span>
          Source family label<strong>{item.synthesisFamily}</strong>
        </span>
      </div>
      {item.chartScaleConverted && (
        <p className="scale-note">
          <Info /> The plot source already expresses this row on the 0–100 scale. The website does
          not rescale it again.
        </p>
      )}
      <p className="drawer-caveat" id="evidence-drawer-caveat">
        This is one representative reported comparison. It does not make metrics, tasks, or
        experimental conditions equivalent.
      </p>
    </DetailDialog>
  );
}
