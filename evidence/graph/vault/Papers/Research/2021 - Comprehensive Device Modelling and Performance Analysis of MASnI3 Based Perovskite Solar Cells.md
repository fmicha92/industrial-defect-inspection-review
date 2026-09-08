---
title: "Comprehensive Device Modelling and Performance Analysis of MASnI3 Based Perovskite Solar Cells with Diverse ETM, HTM and Back Metal Contacts"
aliases:
  - "MASnI3 Based Perovskite Solar Cells with Diverse ETM HTM and Back Metal Contacts"
paper_key: "sha256:a23ad9f7051c2d33737c3d6b5fa881a9ca9430f3ad3901716d352445970e82d4"
paper_type: "research"
year: 2021
venue: "Solar Energy"
authors:
  - "K. Deepthi Jayan"
  - "Varkey Sebastian"
status: "processed"
topics:
  - "perovskite solar cells"
  - "solar-cell device simulation"
tasks:
  - "[[Perovskite solar cell device simulation]]"
domains:
  - "[[Solar cells and photovoltaic]]"
datasets:
  - "not applicable"
methods:
  - "[[SCAPS 1D]]"
model_family:
  - "not applicable"
architectures:
  - "not applicable"
metrics:
  - "[[Power conversion efficiency]]"
  - "[[Fill factor]]"
  - "[[Short-circuit current density]]"
  - "[[Open-circuit voltage]]"
  - "[[Quantum efficiency]]"
primary_metric: "[[Power conversion efficiency]]"
metric_definitions:
  - "PCE: power conversion efficiency"
  - "FF: fill factor"
  - "JSC: short-circuit current density"
  - "VOC: open-circuit voltage"
baselines:
  - "not applicable"
benchmarks:
  - "not applicable"
code: "not reported"
data: "not applicable"
doi: "10.1016/j.solener.2021.01.058"
arxiv: "not reported"
url: "https://doi.org/10.1016/j.solener.2021.01.058"
pdf: "paper-inbox/10_processed/Research/2021 - Jayan - Comprehensive Device Modelling and Performance Analysis of MASnI3 Based Perovskite Solar Cells with Diverse ETM HTM and Back Metal C....pdf"
source_file: "paper-inbox/10_processed/Research/2021 - Jayan - Comprehensive Device Modelling and Performance Analysis of MASnI3 Based Perovskite Solar Cells with Diverse ETM HTM and Back Metal C....pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2021 - Jayan - Comprehensive Device Modelling and Performance Analysis of MASnI3 Based Perovskite Solar Cells with Diverse ETM HTM and Back Metal C....md"
extracted_text: "paper-inbox/90_processing/text/2021 - Jayan - Comprehensive Device Modelling and Performance Analysis of MASnI3 Based Perovskite Solar Cells with Diverse ETM HTM and Back Metal C....txt"
related_papers:
  - "not reported"
related_concepts:
  - "[[Perovskite solar cells]]"
related_methods:
  - "[[SCAPS 1D]]"
related_datasets:
  - "not applicable"
related_domains:
  - "[[Solar cells and photovoltaic]]"
related_tasks:
  - "[[Perovskite solar cell device simulation]]"
related_benchmarks:
  - "not applicable"
processed_at: "2026-05-29"
---
# Comprehensive Device Modelling and Performance Analysis of MASnI3 Based Perovskite Solar Cells

## Summary

The paper uses [[SCAPS 1D]] to simulate lead-free MASnI3-based [[Perovskite solar cells]] across alternative electron transport materials, hole transport materials, and back metal contacts. It optimizes absorber thickness, absorber defect density, acceptor dopant concentration, and contact work function to identify high-performing planar heterojunction solar-cell configurations.

The best reported configuration is Glass/FTO/PCBM/MASnI3/CuI/Au, with [[Power conversion efficiency]] of 25.05%, [[Fill factor]] of 69.23%, [[Short-circuit current density]] of 34.26863 mA/cm2, and [[Open-circuit voltage]] of 1.0557 V.

## Paper Type

Research paper. It is a numerical photovoltaic device modelling and performance analysis study, not a defect-detection or machine-learning paper.

## Problem

Lead-based perovskite absorbers have toxicity concerns, while experimental fabrication of many multilayer perovskite solar-cell configurations is time-consuming and expensive. The paper evaluates whether lead-free MASnI3 absorber devices can achieve strong simulated photovoltaic performance with suitable transport layers and contacts.

## Contribution

- Simulates MASnI3 perovskite solar cells with six ETMs: TiO2, PCBM, ZnO, C60, SnO2, and IGZO.
- Simulates nine HTMs: Cu2O, CuSCN, CuSbS2, P3HT, PEDOT:PSS, NiO, CuO, CuI, and SpiroMeOTAD.
- Compares ten back contacts: Au, W, Ni, Pd, Pt, Se, Ag, Cu, C, and Fe.
- Optimizes absorber thickness, total defect density, acceptor dopant concentration, valence-band effective density, and conduction-band effective density for possible layer configurations.

## Method

The study models a planar p-i-n heterojunction stack with FTO as transparent conductive oxide, an ETM, MASnI3 absorber, an HTM, and a back metal contact. It uses [[SCAPS 1D]] version 3.3.08 with Poisson and carrier-continuity equations, AM 1.5G solar spectrum irradiance, and an absorption sub-model for all layers.

The optimization procedure varies the thicknesses of transport layers and the MASnI3 absorber, adds interface defect layers, tests back-contact work functions, and varies absorber defect density and acceptor dopant concentration.

## Evidence

### Best Configurations by ETM

| Device configuration | Optimized absorber thickness | VOC | JSC | FF | PCE |
|---|---:|---:|---:|---:|---:|
| FTO/TiO2/MASnI3/CuO/Au | 1000 nm | 0.9714 V | 34.7186 mA/cm2 | 73.33% | 24.73% |
| FTO/PCBM/MASnI3/CuI/Au | 1100 nm | 0.8758 V | 34.7450 mA/cm2 | 69.23% | 25.05% |
| FTO/C60/MASnI3/CuSbS2/Au | 1000 nm | 1.0204 V | 32.3917 mA/cm2 | 69.4% | 22.94% |
| FTO/ZnO/MASnI3/CuSbS2/Au | 600 nm | 0.8872 V | 33.6155 mA/cm2 | 72.3% | 21.56% |
| FTO/IGZO/MASnI3/CuSbS2/W | 900 nm | 1.1518 V | 34.6411 mA/cm2 | 62.52% | 24.94% |
| FTO/SnO2/MASnI3/CuSbS2/Au | 1100 nm | 1.0186 V | 34.6143 mA/cm2 | 69.28% | 24.43% |

### Optimized Device Findings

- Best stack: Glass/FTO/PCBM/MASnI3/CuI/Au.
- Best simulated PCE: 25.05%.
- Best-configuration FF: 69.23%.
- Best-configuration JSC: 34.26863 mA/cm2 in the abstract/conclusion and 34.7450 mA/cm2 in Table 5.
- Best-configuration VOC: 1.0557 V in the abstract/conclusion and 0.8758 V in Table 5.
- Absorber thickness optimum: approximately 1072 nm, with Table 5 listing 1100 nm for the PCBM/CuI/Au configuration.
- Absorber defect density optimum: 2.5 x 10^13 cm^-3.
- Acceptor dopant concentration optimum: 10^18 cm^-3.
- Temperature trend: performance decreases as temperature increases from 300 K to 550 K; the analyzed configurations are stable at 300 K.
- Quantum efficiency: remains approximately constant to 700 nm and drops to zero at 960 nm.

The source contains a mismatch between the abstract/conclusion and Table 5 for the best configuration's JSC and VOC. Both values are preserved above rather than reconciled.

## ML/DL Extraction

Not applicable. This is not a machine-learning or deep-learning paper.

## Limitations

- Results are simulation-only; experimental fabrication and validation are not reported.
- The study depends on material parameters taken from literature and SCAPS modelling assumptions.
- The abstract/conclusion and Table 5 disagree on the best configuration's JSC and VOC values.
- Stability is discussed through simulated temperature response, not long-term experimental degradation.

## Connections

### Graph Hubs

- Tasks: [[Perovskite solar cell device simulation]]
- Methods: [[SCAPS 1D]]
- Datasets: not applicable
- Domains: [[Solar cells and photovoltaic]]
- Metrics: [[Power conversion efficiency]], [[Fill factor]], [[Short-circuit current density]], [[Open-circuit voltage]], [[Quantum efficiency]]

### Shares Task

- [[Perovskite solar cell device simulation]]: the paper simulates layer stacks and parameter effects for MASnI3 perovskite solar cells.

### Shares Method

- [[SCAPS 1D]]: used as the numerical simulator for the photovoltaic device stack.

### Shares Metric

- [[Power conversion efficiency]], [[Fill factor]], [[Short-circuit current density]], [[Open-circuit voltage]], and [[Quantum efficiency]] are the main reported photovoltaic performance metrics.

### Application/Domain

- [[Solar cells and photovoltaic]]: lead-free perovskite solar-cell design.

### Related Concept

- [[Perovskite solar cells]]: MASnI3 is the absorber material in the simulated lead-free PSC stack.

## Questions

- Which JSC and VOC values should be treated as canonical for the best PCBM/CuI/Au stack given the abstract/Table 5 mismatch?
- Would fabricated MASnI3 devices reproduce the simulated PCE and stability trends?
- How sensitive are the conclusions to uncertainty in literature-sourced material parameters?
