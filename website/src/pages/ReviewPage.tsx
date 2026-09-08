import { ArrowRight, Download, FileCheck2, Quote } from "lucide-react";
import { PageHero, SectionHeading } from "../components/Layout";
import { challenges, recommendations, researchQuestions, workflow } from "../lib/review-content";
import type { SiteData } from "../types";

export default function ReviewPage({ data }: { data: SiteData }) {
  const summary = data.evidence.summary;
  return (
    <>
      <PageHero
        eyebrow="Review logic & provenance"
        title="Inspect how claims become evidence."
        lede="The companion site preserves the manuscript's dataset-first logic: availability is curated before synthesis-supported outcomes are interpreted, and automated graph candidates never become evidence without a human eligibility gate."
        stat="03"
        statLabel="research questions"
      />
      <section className="section-shell rq-section">
        <SectionHeading
          index="01"
          eyebrow="Scope"
          title="Three questions, one conditional logic"
          aside="Dataset availability, synthesis evidence, and ML-method evidence stay separate so conclusions remain attached to their evaluation context."
        />
        <div className="rq-grid">
          {researchQuestions.map(([id, title, question]) => (
            <article key={id}>
              <span>{id}</span>
              <h3>{title}</h3>
              <p>{question}</p>
            </article>
          ))}
        </div>
      </section>
      <section className="workflow-section">
        <div className="section-shell">
          <SectionHeading
            index="02"
            eyebrow="Dataset-centered evaluation"
            title="A six-step chain of interpretation"
            aside="Each link must remain visible. A high final score alone cannot reveal whether synthesis, tuning, rebalancing, or another pipeline component caused the change."
          />
          <div className="workflow-grid">
            {workflow.map(([number, title, copy], index) => (
              <article key={number}>
                <span>{number}</span>
                <div>
                  <h3>{title}</h3>
                  <p>{copy}</p>
                </div>
                {index < workflow.length - 1 && <ArrowRight aria-hidden="true" />}
              </article>
            ))}
          </div>
        </div>
      </section>
      <section className="section-shell method-grid">
        <article className="nc-card">
          <p className="kicker">Comparable representation</p>
          <h2>Normalized change</h2>
          <p>
            For positively oriented metrics bounded in [0,1], NC scales improvement against the
            remaining attainable gain and deterioration against the baseline.
          </p>
          <div
            className="equation"
            role="math"
            aria-label="Normalized change, NC, equals normalized gain, NG, which is n minus b divided by one minus b when n is greater than b; zero when n equals b; or signed normalized loss, SNL, which is n minus b divided by b when n is less than b."
          >
            <span className="equation-lhs" aria-hidden="true">
              <var>NC</var>
              <span>=</span>
            </span>
            <svg
              className="equation-brace"
              viewBox="0 0 28 144"
              preserveAspectRatio="none"
              aria-hidden="true"
              focusable="false"
            >
              <path
                d="M26 2C12 2 12 18 12 34V52C12 64 8 70 2 72C8 74 12 80 12 92V110C12 126 12 142 26 142"
                fill="none"
                stroke="currentColor"
                strokeWidth="2.5"
                strokeLinecap="round"
                vectorEffect="non-scaling-stroke"
              />
            </svg>
            <span className="equation-cases" aria-hidden="true">
              <span className="equation-case">
                <span className="equation-expression">
                  <span className="equation-branch">
                    <var>NG</var> =
                  </span>
                  <span className="equation-fraction">
                    <span>
                      <var>n</var> − <var>b</var>
                    </span>
                    <span>
                      1 − <var>b</var>
                    </span>
                  </span>
                  <span>,</span>
                </span>
                <span className="equation-condition">
                  if <var>n</var> &gt; <var>b</var>
                </span>
              </span>
              <span className="equation-case">
                <span className="equation-expression equation-zero">
                  <span>0</span>
                  <span>,</span>
                </span>
                <span className="equation-condition">
                  if <var>n</var> = <var>b</var>
                </span>
              </span>
              <span className="equation-case">
                <span className="equation-expression">
                  <span className="equation-branch">
                    <var>SNL</var> =
                  </span>
                  <span className="equation-fraction">
                    <span>
                      <var>n</var> − <var>b</var>
                    </span>
                    <span>
                      <var>b</var>
                    </span>
                  </span>
                  <span>,</span>
                </span>
                <span className="equation-condition">
                  if <var>n</var> &lt; <var>b</var>
                </span>
              </span>
            </span>
          </div>
          <div className="formula-legend">
            <span>
              <strong>b</strong> baseline
            </span>
            <span>
              <strong>n</strong> new score
            </span>
            <span>
              <strong>NC</strong> range −1 to 1
            </span>
          </div>
        </article>
        <article className="limits-card">
          <Quote />
          <p>
            Normalized change provides a common representation of relative performance changes, but
            it does not make the underlying metrics or tasks equivalent.
          </p>
          <div>
            <strong>{summary.medianNormalizedChange.toFixed(2)}</strong>
            <span>
              median
              <small>
                Q1–Q3 {summary.q1NormalizedChange.toFixed(2)}–
                {summary.q3NormalizedChange.toFixed(2)}
              </small>
            </span>
          </div>
          <div>
            <strong>{summary.meanNormalizedChange.toFixed(2)}</strong>
            <span>
              mean<small>sample SD {summary.sampleSdNormalizedChange.toFixed(2)}</small>
            </span>
          </div>
          <small>Descriptive summary of the 39 retained representative comparisons.</small>
        </article>
      </section>
      <section className="section-shell challenges-section">
        <SectionHeading
          index="03"
          eyebrow="Interpretive boundaries"
          title="Six open challenges"
          aside="These boundaries explain why the evidence is useful when read conditionally—and misleading when compressed into a universal winner."
        />
        <ol>
          {challenges.map((challenge, index) => (
            <li key={challenge}>
              <span>{String(index + 1).padStart(2, "0")}</span>
              <p>{challenge}</p>
            </li>
          ))}
        </ol>
      </section>
      <section className="recommendations-section">
        <div className="section-shell">
          <SectionHeading
            index="04"
            eyebrow="Actionable guidance"
            title="Seven recommendations for future evaluation"
            aside="The manuscript translates gaps into practical reporting and experimental-design choices."
          />
          <div className="recommendation-list">
            {recommendations.map(([title, copy], index) => (
              <article key={title}>
                <span>{String(index + 1).padStart(2, "0")}</span>
                <div>
                  <h3>{title}</h3>
                  <p>{copy}</p>
                </div>
              </article>
            ))}
          </div>
        </div>
      </section>
      <section className="section-shell provenance-section">
        <SectionHeading
          index="05"
          eyebrow="Reproducibility"
          title="A transformation trail, not a new analysis"
          aside={data.provenance.generatedDataPolicy}
        />
        <div className="provenance-grid">
          <article className="source-manifest">
            <div className="panel-heading">
              <div>
                <p className="kicker">Source manifest</p>
                <h2>{data.provenance.sources.length} hashed inputs</h2>
              </div>
              <FileCheck2 />
            </div>
            <div className="source-list">
              {data.provenance.sources.map((source) => (
                <div key={source.id}>
                  <span>
                    <strong>{source.id}</strong>
                  </span>
                  <code title={source.sha256}>{source.sha256.slice(0, 12)}…</code>
                </div>
              ))}
            </div>
            <a
              className="download-action"
              href={`${import.meta.env.BASE_URL}data/provenance.json`}
              download
            >
              <Download /> Download complete manifest
            </a>
          </article>
        </div>
      </section>
    </>
  );
}
