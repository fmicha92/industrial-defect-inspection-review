import {
  ArrowDown,
  ArrowRight,
  ArrowUpRight,
  Database,
  Info,
  ShieldCheck,
  Sparkles,
} from "lucide-react";
import { lazy, type ReactNode, Suspense, useRef } from "react";
import { NavLink, useLocation } from "react-router-dom";
import { SectionHeading } from "../components/Layout";
import type { SiteData } from "../types";

const GraphExplorer = lazy(() => import("../components/GraphExplorer"));

export default function HomePage({ data }: { data: SiteData }) {
  const location = useLocation();
  const openingScreen = useRef<HTMLDivElement>(null);
  const scrollToGraph = () => {
    const target = document.getElementById("evidence-graph");
    if (!target || !openingScreen.current) return;
    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const openingBottom = window.scrollY + openingScreen.current.getBoundingClientRect().bottom;
    target.focus({ preventScroll: true });
    window.scrollTo({
      top: Math.ceil(openingBottom),
      behavior: reduceMotion ? "instant" : "smooth",
    });
  };
  return (
    <>
      <div className="opening-screen" ref={openingScreen}>
        <section className="hero-section">
          <div className="hero-copy">
            <p className="eyebrow">Public datasets × synthetic data × inspection models</p>
            <h1 tabIndex={-1}>
              See exactly where <br />
              <em>the evidence holds.</em>
            </h1>
            <p className="lede">
              A dataset-centered map of industrial visual defect inspection. Move from public
              benchmarks to synthesis-supported outcomes while keeping every task, metric, and
              comparator in view.
            </p>
            <div className="hero-actions">
              <button className="primary-action" type="button" onClick={scrollToGraph}>
                Explore the graph <ArrowRight />
              </button>
              <NavLink className="text-action" to="/review/">
                Read the review logic <ArrowUpRight />
              </NavLink>
            </div>
            <section className="hero-publication" aria-labelledby="article-title">
              <p className="kicker">Related article</p>
              <h2 id="article-title">{data.meta.title}</h2>
              <p className="article-authors">
                <span className="sr-only">Authors: </span>
                {data.meta.authors.join(" · ")}
              </p>
            </section>
          </div>
          <div className="hero-aside" role="region" aria-label="Scope summary">
            <p className="kicker">Evidence at a glance</p>
            <div className="hero-metric">
              <strong>61</strong>
              <span>
                public datasets<small>Seven manufacturing domains</small>
              </span>
            </div>
            <div className="hero-metric">
              <strong>39</strong>
              <span>
                dataset-level evaluations<small>From 37 unique studies</small>
              </span>
            </div>
            <div className="hero-metric">
              <strong>0.43</strong>
              <span>
                median normalized change<small>Q1–Q3: 0.20–0.66</small>
              </span>
            </div>
            <p className="scope-warning">
              <Info size={16} /> Descriptive retained evidence—not a global model ranking or
              synthesis success rate.
            </p>
          </div>
        </section>

        <section className="principle-band" aria-label="Interpretive principle">
          <span>One guiding principle</span>
          <p className="principle-statement">
            A reported gain becomes useful when its dataset, task, annotation, metric, and baseline
            remain attached.
          </p>
          <NavLink to="/review/">
            Why this matters <ArrowRight />
          </NavLink>
        </section>
        <div className="opening-scroll">
          <button
            className="continue-scroll"
            type="button"
            aria-controls="evidence-graph"
            onClick={scrollToGraph}
          >
            Continue scrolling <ArrowDown size={17} aria-hidden="true" />
          </button>
        </div>
      </div>

      <section
        className="section-shell graph-section"
        id="evidence-graph"
        tabIndex={-1}
        aria-label="Evidence graph"
      >
        <SectionHeading
          index="01"
          eyebrow="Knowledge structure"
          title="Navigate the evidence graph"
          aside="Move from a dataset to its papers, methods, tasks, domains, and metrics. Links support traceability; they do not represent causal effects or study quality."
        />
        <Suspense fallback={<div className="graph-loading">Preparing the 896-note graph…</div>}>
          <GraphExplorer
            key={location.key + location.search}
            graph={data.graph}
            datasets={data.datasets.datasets}
            evidence={data.evidence.items}
          />
        </Suspense>
      </section>

      <section className="section-shell route-cards-section">
        <SectionHeading
          index="02"
          eyebrow="Three ways in"
          title="Follow the question you have"
          aside="The same source records are organized into distinct views so availability, reported outcomes, and interpretation are not collapsed."
        />
        <div className="route-cards">
          <RouteCard
            icon={<Database />}
            number="61"
            title="Find a candidate public dataset"
            copy="Filter the public registry by manufacturing domain, downstream task, annotation, and modality. Compare reported source descriptions and check access and reuse conditions at the source."
            to="/datasets/"
            label="Browse registry"
            color="teal"
          />
          <RouteCard
            icon={<Sparkles />}
            number="39"
            title="Inspect reported benefit"
            copy="Examine every representative before–after comparison with its synthesis setup, comparator, metric, model family, and exact normalized change."
            to="/evidence/"
            label="Open evidence atlas"
            color="saffron"
          />
          <RouteCard
            icon={<ShieldCheck />}
            number="03"
            title="Audit the interpretation"
            copy="Read the research questions, six-step review logic, normalized-change definition, limitations, recommendations, and source hashes."
            to="/review/"
            label="Review the method"
            color="purple"
          />
        </div>
      </section>
    </>
  );
}

function RouteCard({
  icon,
  number,
  title,
  copy,
  to,
  label,
  color,
}: {
  icon: ReactNode;
  number: string;
  title: string;
  copy: string;
  to: string;
  label: string;
  color: string;
}) {
  return (
    <article className={`route-card ${color}`}>
      <div className="route-card-top">
        <span>{icon}</span>
        <small>{number}</small>
      </div>
      <h3>{title}</h3>
      <p>{copy}</p>
      <NavLink to={to}>
        {label}
        <ArrowRight />
      </NavLink>
    </article>
  );
}
