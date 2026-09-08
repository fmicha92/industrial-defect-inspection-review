import type { Dataset, EvidenceItem } from "../types";

export function normalizeSearch(value: string): string {
  return value
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .toLocaleLowerCase("en")
    .trim();
}

export function matchesSearch(
  query: string,
  fields: (string | number | null | undefined)[],
): boolean {
  const text = normalizeSearch(fields.filter((value) => value != null).join(" "));
  return normalizeSearch(query)
    .split(/\s+/)
    .filter(Boolean)
    .every((term) => text.includes(term));
}

const subsetDatasets: Record<string, string> = {
  "WM-811K (MIR-WM811K variant)": "WM-811K",
  "ELPV Solar Cell Dataset (0%/100% subset)": "ELPV Solar Cell Dataset",
  "NEU-DET (selected three classes)": "NEU-DET",
  "AITEX (selected three defect types)": "AITEX",
  "MVTec AD (bottle subset)": "MVTec AD",
};

export function relatedDatasets(item: EvidenceItem, datasets: Dataset[]): Dataset[] {
  const names = new Set(
    item.sourceLabels.normalizedDataset.split(";").map((name) => {
      const value = name.trim();
      return normalizeSearch(subsetDatasets[value] ?? value);
    }),
  );
  return datasets.filter((dataset) => names.has(normalizeSearch(dataset.name)));
}

export function safeUrl(value: string | null | undefined): string | null {
  if (!value) return null;
  try {
    const url = new URL(value);
    return ["http:", "https:"].includes(url.protocol) ? url.href : null;
  } catch {
    return null;
  }
}

export function normalizeDoi(value: string | null | undefined): string {
  return (value ?? "")
    .replace(/^https?:\/\/(?:dx\.)?doi\.org\//i, "")
    .trim()
    .toLocaleLowerCase("en");
}

export function publicationUrl(url?: string | null, doi?: string | null): string | null {
  const identifier = normalizeDoi(doi);
  return (
    safeUrl(url) ??
    (identifier.startsWith("10.") ? safeUrl(`https://doi.org/${encodeURI(identifier)}`) : null)
  );
}

export function studyGraphNode<T extends { id: string; title: string; type: string; doi?: string }>(
  item: EvidenceItem,
  nodes: readonly T[],
) {
  const doi = normalizeDoi(item.study.doi);
  const doiMatches = doi ? nodes.filter((node) => normalizeDoi(node.doi) === doi) : [];
  if (doiMatches.length === 1) return doiMatches[0];
  if (doiMatches.length > 1) return undefined;
  const titleMatches = nodes.filter(
    (node) =>
      node.type === "Papers" && normalizeSearch(node.title) === normalizeSearch(item.study.title),
  );
  return titleMatches.length === 1 ? titleMatches[0] : undefined;
}

export function directedPath(
  outgoing: Map<string, Set<string>>,
  source: string,
  target: string,
): string[] | null {
  if (!outgoing.has(source) || !outgoing.has(target)) return null;
  if (source === target) return [source];
  const queue = [source];
  const previous = new Map<string, string | null>([[source, null]]);
  for (let cursor = 0; cursor < queue.length; cursor += 1) {
    const current = queue[cursor];
    for (const next of outgoing.get(current) ?? []) {
      if (previous.has(next)) continue;
      previous.set(next, current);
      if (next === target) {
        const result = [target];
        let step: string | null = current;
        while (step !== null) {
          result.push(step);
          step = previous.get(step) ?? null;
        }
        return result.reverse();
      }
      queue.push(next);
    }
  }
  return null;
}
