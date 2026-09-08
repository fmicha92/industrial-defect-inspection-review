---
title: "Generalization without Systematicity: On the Compositional Skills of Sequence-to-Sequence Recurrent Networks"
aliases:
  - "Generalization without Systematicity"
  - "SCAN paper"
paper_key: "arxiv:1705.03122"
paper_type: research
year: 2018
venue: "ICML 2018"
authors:
  - "Brenden Lake"
  - "Marco Baroni"
status: processed
processed_at: 2026-06-02
topics:
  - compositional generalization
  - sequence-to-sequence learning
  - SCAN
tasks:
  - "[[Compositional generalization]]"
datasets:
  - "[[SCAN]]"
domains:
  - "[[Natural language processing]]"
methods:
  - "[[Sequence-to-sequence recurrent network]]"
metrics:
  - "[[Exact-match accuracy]]"
related_methods:
  - "[[Sequence-to-sequence recurrent network]]"
doi: "not reported"
arxiv: "1705.03122"
url: "https://github.com/brendenlake/SCAN"
pdf: "paper-inbox/10_processed/Research/2018 - Lake - Generalization without Systematicity On the Compositional Skills of Sequence-to-Sequence Recurrent Networks.pdf"
source_file: "paper-inbox/10_processed/Research/2018 - Lake - Generalization without Systematicity On the Compositional Skills of Sequence-to-Sequence Recurrent Networks.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2018 - Lake - Generalization without Systematicity On the Compositional Skills of Sequence-to-Sequence Recurrent Networks.md"
extracted_text: "paper-inbox/90_processing/text/2018 - Lake - Generalization without Systematicity On the Compositional Skills of Sequence-to-Sequence Recurrent Networks.txt"
artifact_status: "processed"
tags:
  - paper
  - compositional-generalization
---

# Generalization without Systematicity: On the Compositional Skills of Sequence-to-Sequence Recurrent Networks

## Summary

Lake and Baroni introduce [[SCAN]], a synthetic command-to-action benchmark for [[Compositional generalization]]. Standard sequence-to-sequence recurrent networks solve random splits almost perfectly, but fail when the split requires systematic recombination, such as applying a learned primitive in new compositions.

## Paper Type

Research paper with a benchmark contribution. It proposes a diagnostic dataset and uses it to test sequence-to-sequence recurrent networks.

## Problem

Neural sequence models can generalize to held-out examples without necessarily showing systematic compositionality. The paper asks whether recurrent encoder-decoder models can recombine known primitives and modifiers in new structured ways.

## Contribution

- Introduces SCAN, a simplified navigation-command dataset generated from a compositional grammar.
- Shows near-perfect performance on random splits but poor performance on length and new-composition splits.
- Demonstrates that exposure to isolated primitives does not guarantee systematic use of those primitives in composed commands.

## Method

SCAN maps commands such as "jump around right" to action sequences such as repeated right-turn and jump actions. The grammar generates 20,910 unambiguous commands from 13 input words and six output actions. The authors evaluate SRN, LSTM, and GRU encoder-decoder models with and without attention across 180 architectures and five random seeds.

## Evidence

On an 80/20 random split, the best LSTM reaches 99.8% test accuracy. On the longer-sequence split, where training commands require at most 22 actions and test commands require 24 to 48 actions, the best GRU with attention reaches 20.8% and the overall-best model reaches 13.8%. With oracle output lengths, the top model improves but still fails to generalize perfectly.

For the new-primitive split, "turn left" generalizes well because LTURN occurs in other contexts, but "jump" does not: the best model reaches 1.2% accuracy when "jump" appears only as a primitive during training. Adding composed jump examples improves accuracy, but the paper reports that 32 examples are needed to reach 88.4%.

## ML/DL Extraction

- Models: SRN, LSTM, and GRU sequence-to-sequence encoder-decoder networks, with and without attention.
- Hyperparameters: 1 or 2 layers, 25/50/100/200/400 hidden units, dropout 0/0.1/0.5.
- Training: 100,000 trials, Adam learning rate 0.001, teacher forcing half the time, gradient clipping above norm 5.
- Metric: [[Exact-match accuracy]] over full output action sequences.

## Limitations

- SCAN is deliberately synthetic and simplified.
- The machine-translation probe is a toy setup rather than a full natural-language benchmark.
- The results target recurrent sequence-to-sequence models, not all possible neural architectures.

## Connections

### Graph Hubs

- Tasks: [[Compositional generalization]]
- Methods: [[Sequence-to-sequence recurrent network]]
- Datasets: [[SCAN]]
- Domains: [[Natural language processing]]
- Metrics: [[Exact-match accuracy]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[1998 - Gradient-Based Learning Applied to Document Recognition]] | Contrasts with | Both study learned sequence/structured systems, but LeCun et al. focus on visual document recognition and graph transformer networks rather than systematic command composition. |

## Questions

- Which architectural or training biases are sufficient for SCAN-style systematic generalization without direct examples of every composition?
