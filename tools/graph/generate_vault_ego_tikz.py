#!/usr/bin/env python3
"""Generate a curated TikZ ego graph from Obsidian vault wikilinks."""

from __future__ import annotations

import argparse
import math
import re
from collections import Counter, defaultdict
from pathlib import Path


LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")

CATEGORY_STYLES = {
    "Papers": ("paper", "blue!70!black", "blue!10"),
    "Datasets": ("dataset", "green!55!black", "green!10"),
    "Methods": ("method", "purple!65!black", "purple!10"),
    "Tasks": ("task", "orange!85!black", "orange!12"),
    "Metrics": ("metric", "red!70!black", "red!10"),
    "Domains": ("domain", "teal!70!black", "teal!10"),
    "Benchmarks": ("benchmark", "pink!70!black", "pink!12"),
    "Concepts": ("concept", "brown!70!black", "brown!10"),
}

CATEGORY_LAYOUT = {
    "Papers": (-5.9, 1.65, -1),
    "Datasets": (-5.9, -1.65, -1),
    "Methods": (5.9, 1.65, 1),
    "Tasks": (5.9, -1.65, 1),
    "Concepts": (-2.05, 3.55, 0),
    "Domains": (2.05, 3.55, 0),
    "Benchmarks": (-2.05, -3.55, 0),
    "Metrics": (2.05, -3.55, 0),
}

PRIORITY = {
    "Papers": [
        "2021 - CutPaste Self-Supervised Learning for Anomaly Detection and Localization",
        "2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics",
        "2024 - AnomalyDiffusion Few-Shot Anomaly Image Generation with Diffusion Model",
        "2024 - AnomalyXFusion Multi-modal Anomaly Synthesis with Diffusion",
        "2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection",
    ],
    "Datasets": [
        "MVTec AD",
        "BTAD",
        "VisA",
        "Defect Spectrum",
        "NEU-CLS",
        "DAGM2007",
    ],
    "Methods": [
        "Learned generative synthesis",
        "Procedural and simulation-based synthesis",
        "Hybrid generative-procedural synthesis",
        "Rule-based data synthesis",
        "Defect synthesis",
        "AnomalyDiffusion",
    ],
    "Tasks": [
        "Industrial anomaly detection",
        "Defect segmentation",
        "Object detection",
        "Surface defect detection",
        "Defect classification",
    ],
    "Metrics": [
        "AU-ROC",
        "AU-PRO",
        "mIoU",
        "F1-score",
        "Average precision",
    ],
    "Domains": [
        "Multi-industry anomaly detection",
        "Semiconductor and electronics",
        "Solar cells and photovoltaic",
        "Textile and fiber inspection",
        "Steel surface inspection",
    ],
    "Concepts": [
        "Domain gap",
        "Class imbalance",
        "Industrial visual inspection",
        "Surface defect detection",
        "Distribution shift",
    ],
    "Benchmarks": [
        "MVTec AD",
        "BTAD",
        "VisA",
        "DAGM2007",
    ],
}

DISPLAY = {
    "2021 - CutPaste Self-Supervised Learning for Anomaly Detection and Localization": "CutPaste",
    "2024 - Defect Spectrum A Granular Look of Large-Scale Defect Datasets with Rich Semantics": "Defect Spectrum paper",
    "2024 - AnomalyDiffusion Few-Shot Anomaly Image Generation with Diffusion Model": "AnomalyDiffusion",
    "2024 - AnomalyXFusion Multi-modal Anomaly Synthesis with Diffusion": "AnomalyXFusion",
    "2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection": "Procedural 3D defects",
    "Procedural and simulation-based synthesis": "Procedural / simulation",
    "Hybrid generative-procedural synthesis": "Hybrid synthesis",
    "Learned generative synthesis": "GAN / diffusion / VAE",
    "Rule-based data synthesis": "Rule-based insertion",
    "Industrial anomaly detection": "Anomaly detection",
    "Multi-industry anomaly detection": "Multi-industry",
    "Semiconductor and electronics": "Semiconductor",
    "Solar cells and photovoltaic": "Photovoltaics",
    "Textile and fiber inspection": "Textile / fiber",
    "Steel surface inspection": "Steel surfaces",
    "Surface defect detection": "Surface defects",
    "Industrial visual inspection": "Industrial inspection",
}


def tex_escape(value: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in value)


def note_title(path: Path) -> str:
    return path.stem


def normalize_link(link: str) -> str:
    return Path(link.strip()).name


def classify(path: Path, vault: Path) -> str | None:
    rel = path.relative_to(vault)
    first = rel.parts[0]
    if first in CATEGORY_STYLES:
        return first
    if first == "Learning Paradigms":
        return "Concepts"
    return None


def read_links(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    return {normalize_link(match) for match in LINK_RE.findall(text)}


def build_graph(vault: Path):
    files = sorted(vault.rglob("*.md"))
    title_to_path = {}
    for path in files:
        title_to_path.setdefault(note_title(path), path)

    links = {note_title(path): read_links(path) for path in files}
    backlinks = defaultdict(set)
    for source, targets in links.items():
        for target in targets:
            backlinks[target].add(source)

    return title_to_path, links, backlinks


def ego_nodes(center: str, links, backlinks) -> tuple[set[str], set[str]]:
    one_hop = set(links.get(center, set())) | set(backlinks.get(center, set()))
    one_hop = {node for node in one_hop if node in links}

    two_hop = set(one_hop)
    for node in one_hop:
        two_hop.update(target for target in links.get(node, set()) if target in links)
        two_hop.update(source for source in backlinks.get(node, set()) if source in links)
    two_hop.discard(center)
    return one_hop, two_hop


def pick_nodes(category: str, candidates: list[str], one_hop: set[str], max_count: int) -> list[str]:
    selected = []
    candidate_set = set(candidates)

    for item in PRIORITY.get(category, []):
        if item in candidate_set and item not in selected:
            selected.append(item)

    remaining = [node for node in candidates if node not in selected]
    remaining.sort(key=lambda node: (node not in one_hop, len(node), node.lower()))
    selected.extend(remaining)
    return selected[:max_count]


def short_label(title: str) -> str:
    if title in DISPLAY:
        return DISPLAY[title]
    label = re.sub(r"^\d{4}\s+-\s+", "", title)
    label = label.replace("Synthetic data generation", "Synthesis")
    if len(label) > 28:
        label = label[:25].rstrip() + "..."
    return label


def node_positions(cx: float, cy: float, side: int, count: int) -> list[tuple[float, float]]:
    if count <= 0:
        return []
    radius = 1.45 if count <= 4 else 1.68
    if side < 0:
        angles = [140, 180, 220, 105, 255, 75]
    elif side > 0:
        angles = [40, 0, -40, 75, -75, 105]
    else:
        radius = 1.78
        angles = [155, 25, -155, -25, 90, -90]
    return [
        (cx + radius * math.cos(math.radians(angle)), cy + radius * math.sin(math.radians(angle)))
        for angle in angles[:count]
    ]


def write_figure(output: Path, category_nodes: dict[str, list[str]], category_counts: Counter):
    lines = []
    add = lines.append
    add(r"\begin{figure*}[tbp]")
    add(r"    \centering")
    add(r"    \resizebox{0.98\textwidth}{!}{%")
    add(r"    \begin{tikzpicture}[")
    add(r"        font=\sffamily\scriptsize,")
    add(r"        >=stealth,")
    add(r"        hub/.style={circle, draw=black!55, fill=violet!70, text=white,")
    add(r"            minimum size=2.15cm, align=center, font=\sffamily\bfseries\scriptsize},")
    add(r"        group/.style={rounded corners=4pt, draw=black!25, fill=#1,")
    add(r"            text width=3.05cm, minimum height=1.18cm, align=center,")
    add(r"            inner sep=4pt, font=\sffamily\scriptsize},")
    add(r"        dot/.style={circle, draw=#1!70!black, fill=#1!65, minimum size=4.8mm, inner sep=0pt},")
    add(r"        label/.style={font=\sffamily\tiny, align=center, text=black!85},")
    add(r"        edge/.style={line width=0.35pt, draw=black!24},")
    add(r"        trace/.style={line width=0.85pt, draw=violet!78, -stealth},")
    add(r"        legend/.style={font=\sffamily\tiny, align=left}")
    add(r"    ]")
    add("")
    add(r"        \node[hub] (center) at (0,0) {Synthetic\\data\\generation};")
    add("")

    group_names = {}
    node_names = {}
    for category, (cx, cy, side) in CATEGORY_LAYOUT.items():
        style, color, fill = CATEGORY_STYLES[category]
        count = category_counts.get(category, 0)
        group_name = f"group{category}"
        group_names[category] = group_name
        selected_labels = "; ".join(short_label(title) for title in category_nodes.get(category, [])[:3])
        add(
            rf"        \node[group={fill}] ({group_name}) at ({cx:.2f},{cy:.2f}) "
            rf"{{\textbf{{{tex_escape(category)}}}\\{count} linked notes\\[-0.2ex]"
            rf"{{\tiny {tex_escape(selected_labels)}}}}};"
        )

        nodes = category_nodes.get(category, [])
        positions = node_positions(cx, cy, side, len(nodes))
        node_names[category] = []
        for idx, (title, (x, y)) in enumerate(zip(nodes, positions), start=1):
            node_name = f"{style}{idx}"
            node_names[category].append(node_name)
            add(rf"        \node[dot={color}] ({node_name}) at ({x:.2f},{y:.2f}) {{}};")
        add("")

    add(r"        \begin{scope}[on background layer]")
    for category, group_name in group_names.items():
        add(rf"            \draw[edge] (center) -- ({group_name});")
        for node_name in node_names.get(category, []):
            add(rf"            \draw[edge] ({group_name}) -- ({node_name});")
    add(r"            \draw[trace] (dataset1) .. controls (-3.6,-0.4) and (-2.6,0.2) .. (center);")
    add(r"            \draw[trace] (center) .. controls (2.0,0.7) and (3.6,1.1) .. (method1);")
    add(r"            \draw[trace] (method1) .. controls (4.5,0.2) and (4.6,-0.6) .. (task1);")
    add(r"            \draw[trace] (task1) .. controls (3.4,-2.7) and (1.7,-3.2) .. (metric1);")
    add(r"        \end{scope}")
    add("")
    add(r"        \node[")
    add(r"            draw=black!20,")
    add(r"            fill=white,")
    add(r"            rounded corners=2pt,")
    add(r"            inner sep=3pt,")
    add(r"            legend")
    add(r"        ] at (-5.8,-4.85) {")
    add(r"            \textbf{Node type colors}\\")
    add(r"            \tikz{\node[dot=blue!70!black, minimum size=3mm]{};} Papers \quad")
    add(r"            \tikz{\node[dot=green!55!black, minimum size=3mm]{};} Datasets \quad")
    add(r"            \tikz{\node[dot=purple!65!black, minimum size=3mm]{};} Methods\\")
    add(r"            \tikz{\node[dot=orange!85!black, minimum size=3mm]{};} Tasks \quad")
    add(r"            \tikz{\node[dot=red!70!black, minimum size=3mm]{};} Metrics \quad")
    add(r"            \tikz{\node[dot=teal!70!black, minimum size=3mm]{};} Domains\\")
    add(r"            \tikz{\node[dot=brown!70!black, minimum size=3mm]{};} Concepts \quad")
    add(r"            \tikz{\node[dot=pink!70!black, minimum size=3mm]{};} Benchmarks")
    add(r"        };")
    add("")
    add(r"        \node[")
    add(r"            draw=black!20,")
    add(r"            fill=gray!5,")
    add(r"            rounded corners=2pt,")
    add(r"            text width=13.2cm,")
    add(r"            align=center,")
    add(r"            font=\sffamily\tiny")
    add(r"        ] at (0,-5.75) {")
    add(r"            Generated from the two-hop Obsidian wikilink neighborhood around \emph{Synthetic data generation};")
    add(r"            labels show curated representative notes and counts summarize all linked notes by vault folder.")
    add(r"        };")
    add("")
    add(r"    \end{tikzpicture}%")
    add(r"    }")
    add("")
    add(r"    \caption{Stylized vault-link graph used during evidence organization. The figure reconstructs the two-hop Obsidian neighborhood around the synthetic-data-generation note and groups linked notes by vault folder: papers, datasets, methods, tasks, metrics, domains, and concepts. Node labels are curated representatives selected from the generated link neighborhood, while the group counts summarize the broader linked-note structure. The highlighted path illustrates how the vault supported traceable navigation from public datasets through synthesis methods and downstream inspection tasks to evaluation metrics; the graph is a transparency aid rather than quantitative evidence.}")
    add(r"    \label{fig:obsidian_vault_graph}")
    add(r"\end{figure*}")
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--vault", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--center", default="Synthetic data generation")
    args = parser.parse_args()

    title_to_path, links, backlinks = build_graph(args.vault)
    if args.center not in title_to_path:
        raise SystemExit(f"Center note not found: {args.center}")

    one_hop, two_hop = ego_nodes(args.center, links, backlinks)
    category_members = defaultdict(list)
    for node in sorted(two_hop):
        path = title_to_path.get(node)
        if path is None:
            continue
        category = classify(path, args.vault)
        if category in CATEGORY_STYLES:
            category_members[category].append(node)

    category_counts = Counter({category: len(nodes) for category, nodes in category_members.items()})
    max_labels = {
        "Papers": 5,
        "Datasets": 5,
        "Methods": 5,
        "Tasks": 4,
        "Metrics": 4,
        "Domains": 4,
        "Concepts": 4,
        "Benchmarks": 3,
    }
    category_nodes = {
        category: pick_nodes(category, nodes, one_hop, max_labels.get(category, 4))
        for category, nodes in category_members.items()
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    write_figure(args.output, category_nodes, category_counts)

    print(f"Wrote {args.output}")
    print("Two-hop category counts:")
    for category in sorted(category_counts):
        print(f"  {category}: {category_counts[category]}")


if __name__ == "__main__":
    main()
