import { useEffect, useState } from "react";
import type { SiteData } from "../types";

const dataFiles = {
  datasets: "datasets.json",
  coverage: "task-coverage.json",
  citations: "citation-trends.json",
  evidence: "evidence.json",
  graph: "graph.bundle.json",
  meta: "meta.json",
  provenance: "provenance.json",
} as const;

export type SiteDataState =
  | { status: "loading" }
  | { status: "error"; message: string }
  | { status: "ready"; data: SiteData };

export function useSiteData() {
  const [state, setState] = useState<SiteDataState>({ status: "loading" });
  useEffect(() => {
    let cancelled = false;
    Promise.all(
      Object.entries(dataFiles).map(async ([key, file]) => {
        const response = await fetch(`${import.meta.env.BASE_URL}data/${file}`);
        if (!response.ok) throw new Error(`${file}: ${response.status}`);
        return [key, await response.json()] as const;
      }),
    )
      .then((entries) => {
        if (!cancelled) {
          setState({ status: "ready", data: Object.fromEntries(entries) as SiteData });
        }
      })
      .catch((error: unknown) => {
        if (!cancelled) {
          setState({
            status: "error",
            message: error instanceof Error ? error.message : "Unknown data error",
          });
        }
      });
    return () => {
      cancelled = true;
    };
  }, []);
  return state;
}

export function formatDate(value: string) {
  return new Intl.DateTimeFormat("en", {
    day: "2-digit",
    month: "short",
    year: "numeric",
    timeZone: "UTC",
  }).format(new Date(`${value}T00:00:00Z`));
}

export function formatScore(value: number) {
  return Number.isInteger(value) ? value.toFixed(0) : value.toFixed(2).replace(/0$/, "");
}
