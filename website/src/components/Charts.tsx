import { useId, useMemo, useState } from "react";

const familyColors: Record<string, string> = {
  GAN: "#2d7182",
  Rule: "#f2a23a",
  Diffusion: "#80629a",
  Hybrid: "#41a99d",
};

type EvidenceLike = {
  id: string;
  dataset: string;
  representative: {
    metric: string;
    baseline: number;
    after: number;
    normalizedChange: number;
  };
  categories: { domain: string; concept: string; model: string; family: string };
};

type CoverageLike = {
  domainOrder: Array<{ id: string; label: string }>;
  taskOrder: string[];
  cells: Record<string, Record<string, number>>;
  datasetTotals: Record<string, number>;
  taskTotals: Record<string, number>;
  uniqueDatasets: number;
  assignmentTotal: number;
};

type CitationLike = {
  years: number[];
  series: Array<{
    domainId: string;
    label: string;
    annual: Record<string, number>;
    total: number;
  }>;
};

const domainColors = ["#194454", "#2d7182", "#41a99d", "#f2c658", "#fa994a", "#f03630", "#80629a"];

export function CoverageMatrix({
  data,
  onSelect,
}: {
  data: CoverageLike;
  onSelect?: (domain: string, task: string) => void;
}) {
  const maximum = Math.max(
    ...data.domainOrder.flatMap((domain) =>
      data.taskOrder.map((task) => data.cells[domain.id][task]),
    ),
  );
  return (
    <div className="matrix-wrap">
      <table className="coverage-matrix">
        <caption>
          Public-dataset coverage by manufacturing domain and supported task. Counts are
          non-exclusive.
        </caption>
        <thead>
          <tr>
            <th scope="col">Manufacturing domain</th>
            {data.taskOrder.map((task) => (
              <th scope="col" key={task}>
                {task}
              </th>
            ))}
            <th scope="col">Datasets</th>
          </tr>
        </thead>
        <tbody>
          {data.domainOrder.map((domain) => (
            <tr key={domain.id}>
              <th scope="row">{domain.label}</th>
              {data.taskOrder.map((task) => {
                const count = data.cells[domain.id][task];
                const strength = count / maximum;
                return (
                  <td key={task}>
                    <button
                      type="button"
                      onClick={() => onSelect?.(domain.id, task)}
                      aria-label={`${domain.label}, ${task}: ${count} dataset${count === 1 ? "" : "s"}`}
                      className="matrix-cell"
                      style={{
                        background: `color-mix(in srgb, var(--teal) ${Math.round(12 + strength * 78)}%, white)`,
                        color: strength > 0.55 ? "white" : "var(--ink)",
                      }}
                      title={`${domain.label}: ${count} dataset${count === 1 ? " supports" : "s support"} ${task.toLocaleLowerCase("en")}`}
                    >
                      {count}
                    </button>
                  </td>
                );
              })}
              <td className="matrix-total">{data.datasetTotals[domain.id]}</td>
            </tr>
          ))}
        </tbody>
        <tfoot>
          <tr>
            <th scope="row">Task totals</th>
            {data.taskOrder.map((task) => (
              <td key={task}>{data.taskTotals[task]}</td>
            ))}
            <td>
              <strong>{data.uniqueDatasets}</strong>
              <small>{data.assignmentTotal} assignments</small>
            </td>
          </tr>
        </tfoot>
      </table>
    </div>
  );
}

export function CitationTrend({ data }: { data: CitationLike }) {
  const [scaleMode, setScaleMode] = useState<"linear" | "log">("linear");
  const titleId = useId();
  const width = 760;
  const height = 350;
  const margin = { top: 24, right: 30, bottom: 44, left: 58 };
  const domainSeries = data.series.filter((series) => series.domainId !== "all");
  const maximum = Math.max(
    ...domainSeries.flatMap((series) => data.years.map((year) => series.annual[String(year)])),
  );
  const lastYear = data.years[data.years.length - 1] ?? data.years[0];
  const x = (year: number) =>
    margin.left +
    ((year - data.years[0]) / (lastYear - data.years[0])) * (width - margin.left - margin.right);
  const y = (value: number) => {
    const plotHeight = height - margin.top - margin.bottom;
    if (scaleMode === "log") {
      const positioned = Math.max(value, 1);
      return margin.top + (1 - Math.log10(positioned) / Math.log10(maximum)) * plotHeight;
    }
    return margin.top + (1 - value / maximum) * plotHeight;
  };
  const ticks = scaleMode === "log" ? [1, 10, 100, 1000] : [0, 300, 600, 900, 1200];
  return (
    <div className="chart-stack">
      <div className="chart-toolbar">
        <p>
          Annual citations to dataset-source publications
          <span>Published aggregate · 2020–2025</span>
        </p>
        <fieldset className="mini-toggle">
          <legend className="sr-only">Citation chart scale</legend>
          {(["linear", "log"] as const).map((mode) => (
            <button
              key={mode}
              className={scaleMode === mode ? "selected" : ""}
              onClick={() => setScaleMode(mode)}
              type="button"
              aria-pressed={scaleMode === mode}
            >
              {mode}
            </button>
          ))}
        </fieldset>
      </div>
      <svg
        className="evidence-chart citation-chart"
        viewBox={`0 0 ${width} ${height}`}
        role="img"
        aria-labelledby={titleId}
      >
        <title id={titleId}>
          Annual citation counts for seven dataset-domain groups from 2020 through 2025
        </title>
        {ticks.map((tick) => (
          <g key={tick}>
            <line
              className="chart-grid"
              x1={margin.left}
              x2={width - margin.right}
              y1={y(tick)}
              y2={y(tick)}
            />
            <text className="chart-axis" x={margin.left - 10} y={y(tick) + 4} textAnchor="end">
              {tick.toLocaleString("en")}
            </text>
          </g>
        ))}
        {data.years.map((year) => (
          <text className="chart-axis" key={year} x={x(year)} y={height - 14} textAnchor="middle">
            {year}
          </text>
        ))}
        {domainSeries.map((series, seriesIndex) => {
          const path = data.years
            .map(
              (year, index) =>
                `${index === 0 ? "M" : "L"}${x(year)},${y(series.annual[String(year)])}`,
            )
            .join(" ");
          return (
            <g key={series.domainId}>
              <path className="trend-line" d={path} stroke={domainColors[seriesIndex]} />
              {data.years.map((year) => (
                <circle
                  key={year}
                  cx={x(year)}
                  cy={y(series.annual[String(year)])}
                  r="4"
                  fill={domainColors[seriesIndex]}
                >
                  <title>{`${series.label}, ${year}: ${series.annual[String(year)].toLocaleString("en")} citations`}</title>
                </circle>
              ))}
            </g>
          );
        })}
      </svg>
      <div className="chart-legend" role="list" aria-label="Citation chart legend">
        {domainSeries.map((series, index) => (
          <span key={series.domainId} role="listitem">
            <i style={{ background: domainColors[index] }} /> {series.label}
            <small>{series.total.toLocaleString("en")} total</small>
          </span>
        ))}
      </div>
      {scaleMode === "log" && (
        <p className="micro-note">
          Zero remains the scientific value in labels and source data; it is positioned at one only
          for the logarithmic view.
        </p>
      )}
      <details className="chart-data-disclosure">
        <summary>View annual citation values</summary>
        <div className="matrix-wrap">
          <table className="chart-data-table">
            <caption>Annual source-publication citation counts by dataset-domain group.</caption>
            <thead>
              <tr>
                <th scope="col">Domain group</th>
                {data.years.map((year) => (
                  <th scope="col" key={year}>
                    {year}
                  </th>
                ))}
                <th scope="col">Period total</th>
              </tr>
            </thead>
            <tbody>
              {data.series.map((series) => (
                <tr key={series.domainId}>
                  <th scope="row">{series.label}</th>
                  {data.years.map((year) => (
                    <td key={year}>{series.annual[String(year)].toLocaleString("en")}</td>
                  ))}
                  <td>{series.total.toLocaleString("en")}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </details>
    </div>
  );
}

export function EvidenceScatter({
  items,
  onSelect,
}: {
  items: EvidenceLike[];
  onSelect?: (id: string, trigger: Element) => void;
}) {
  const titleId = useId();
  const width = 660;
  const height = 430;
  const margin = { top: 24, right: 24, bottom: 56, left: 62 };
  const x = (value: number) => margin.left + (value / 100) * (width - margin.left - margin.right);
  const y = (value: number) =>
    height - margin.bottom - (value / 100) * (height - margin.top - margin.bottom);
  return (
    <div className="chart-stack">
      <div className="chart-toolbar">
        <p>
          Baseline → synthesis-supported result
          <span>Representative metric per evaluation · source scale 0–100</span>
        </p>
      </div>
      <svg
        className="evidence-chart"
        viewBox={`0 0 ${width} ${height}`}
        role={onSelect ? "group" : "img"}
        aria-labelledby={titleId}
      >
        <title id={titleId}>
          Baseline and synthesis-supported scores for {items.length} comparisons
        </title>
        {[0, 20, 40, 60, 80, 100].map((tick) => (
          <g key={tick}>
            <line
              className="chart-grid"
              x1={x(tick)}
              x2={x(tick)}
              y1={margin.top}
              y2={height - margin.bottom}
            />
            <line
              className="chart-grid"
              x1={margin.left}
              x2={width - margin.right}
              y1={y(tick)}
              y2={y(tick)}
            />
            <text className="chart-axis" x={x(tick)} y={height - 24} textAnchor="middle">
              {tick}
            </text>
            <text className="chart-axis" x={margin.left - 12} y={y(tick) + 4} textAnchor="end">
              {tick}
            </text>
          </g>
        ))}
        <line className="parity-line" x1={x(0)} x2={x(100)} y1={y(0)} y2={y(100)} />
        <text
          className="axis-label"
          x={(margin.left + width - margin.right) / 2}
          y={height - 4}
          textAnchor="middle"
        >
          Baseline score
        </text>
        <text
          className="axis-label"
          transform={`translate(16 ${(margin.top + height - margin.bottom) / 2}) rotate(-90)`}
          textAnchor="middle"
        >
          Synthesis-supported score
        </text>
        {items.map((item) => (
          <circle
            className="scatter-dot"
            key={item.id}
            cx={x(item.representative.baseline)}
            cy={y(item.representative.after)}
            r="6"
            fill={familyColors[item.categories.family] ?? "#194454"}
            role={onSelect ? "button" : undefined}
            aria-label={`${item.id}: ${item.dataset}, ${item.representative.metric}; ${item.representative.baseline} to ${item.representative.after}. Open comparison.`}
            onClick={(event) => onSelect?.(item.id, event.currentTarget)}
            onKeyDown={(event) => {
              if (event.key === "Enter" || event.key === " ") {
                event.preventDefault();
                onSelect?.(item.id, event.currentTarget);
              }
            }}
            tabIndex={0}
          >
            <title>{`${item.id} · ${item.dataset} · ${item.representative.metric}: ${item.representative.baseline} to ${item.representative.after}; NC ${item.representative.normalizedChange.toFixed(2)}`}</title>
          </circle>
        ))}
      </svg>
      {items.length === 0 && (
        <p className="chart-selection-hint" role="status">
          No points match the current filters.
        </p>
      )}
      <div className="chart-legend compact">
        {Object.entries(familyColors).map(([family, color]) => (
          <span key={family}>
            <i style={{ background: color }} /> {family}
          </span>
        ))}
      </div>
      <p className="micro-note">
        Points above the diagonal report higher values. Rows differ in task, metric, baseline, and
        experimental conditions.
      </p>
    </div>
  );
}

export function ChangeDistribution({
  items,
  onSelect,
}: {
  items: EvidenceLike[];
  onSelect?: (id: string, trigger: Element) => void;
}) {
  const titleId = useId();
  const width = 660;
  const height = 235;
  const left = 54;
  const right = 24;
  const x = (value: number) => left + value * (width - left - right);
  const sorted = useMemo(
    () =>
      [...items].sort(
        (a, b) => a.representative.normalizedChange - b.representative.normalizedChange,
      ),
    [items],
  );
  return (
    <div className="chart-stack">
      <div className="chart-toolbar">
        <p>
          Normalized change distribution<span>39 representative comparisons</span>
        </p>
      </div>
      <svg
        className="evidence-chart distribution-chart"
        viewBox={`0 0 ${width} ${height}`}
        role={onSelect ? "group" : "img"}
        aria-labelledby={titleId}
      >
        <title id={titleId}>
          Distribution of 39 positive representative normalized-change values
        </title>
        <rect className="iqr-band" x={x(0.2)} y="44" width={x(0.66) - x(0.2)} height="116" rx="8" />
        <line className="median-line" x1={x(0.43)} x2={x(0.43)} y1="32" y2="174" />
        {Array.from({ length: 6 }, (_, index) => index * 0.2).map((tick) => (
          <g key={tick}>
            <line className="chart-grid" x1={x(tick)} x2={x(tick)} y1="38" y2="174" />
            <text className="chart-axis" x={x(tick)} y="202" textAnchor="middle">
              {tick.toFixed(1)}
            </text>
          </g>
        ))}
        {sorted.map((item, index) => {
          const lane = index % 7;
          return (
            <circle
              className="scatter-dot"
              key={item.id}
              cx={x(item.representative.normalizedChange)}
              cy={65 + lane * 14}
              r="5.2"
              fill={familyColors[item.categories.family] ?? "#194454"}
              role={onSelect ? "button" : undefined}
              aria-label={`${item.id}: ${item.dataset}, ${item.representative.metric}; ${item.representative.baseline} to ${item.representative.after}. Open comparison.`}
              onClick={(event) => onSelect?.(item.id, event.currentTarget)}
              onKeyDown={(event) => {
                if (event.key === "Enter" || event.key === " ") {
                  event.preventDefault();
                  onSelect?.(item.id, event.currentTarget);
                }
              }}
              tabIndex={0}
            >
              <title>{`${item.id} · ${item.dataset}: ${item.representative.normalizedChange.toFixed(4)}`}</title>
            </circle>
          );
        })}
        <text className="chart-annotation" x={x(0.43) + 8} y="28">
          median 0.43
        </text>
        <text className="axis-label" x={(left + width - right) / 2} y="228" textAnchor="middle">
          Normalized change (−1 to 1)
        </text>
      </svg>
      <p className="micro-note">
        Shaded interval is Q1–Q3 (0.20–0.66). This describes the retained published evidence; it is
        not an estimate of how often synthesis succeeds.
      </p>
    </div>
  );
}

export function EvidenceMatrix({
  items,
  onSelect,
}: {
  items: EvidenceLike[];
  onSelect?: (family: string, domain: string) => void;
}) {
  const families = ["GAN", "Rule", "Diffusion", "Hybrid"];
  const domains = [...new Set(items.map((item) => item.categories.domain))];
  const count = (family: string, domain: string) =>
    items.filter((item) => item.categories.family === family && item.categories.domain === domain)
      .length;
  return (
    <div className="matrix-wrap compact-matrix">
      <table className="coverage-matrix evidence-matrix">
        <caption>
          Number of representative comparisons by chart-coded synthesis family and domain.
        </caption>
        <thead>
          <tr>
            <th scope="col">Family</th>
            {domains.map((domain) => (
              <th scope="col" key={domain}>
                {domain}
              </th>
            ))}
            <th scope="col">Rows</th>
          </tr>
        </thead>
        <tbody>
          {families.map((family) => {
            const total = items.filter((item) => item.categories.family === family).length;
            return (
              <tr key={family}>
                <th scope="row">
                  <i style={{ background: familyColors[family] }} />
                  {family}
                </th>
                {domains.map((domain) => (
                  <td key={domain}>
                    <button
                      type="button"
                      className={count(family, domain) ? "count-mark active" : "count-mark"}
                      onClick={() => onSelect?.(family, domain)}
                      disabled={!count(family, domain)}
                      aria-label={`${family}, ${domain}: ${count(family, domain)} comparison${count(family, domain) === 1 ? "" : "s"}`}
                    >
                      {count(family, domain)}
                    </button>
                  </td>
                ))}
                <td className="matrix-total">{total}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
