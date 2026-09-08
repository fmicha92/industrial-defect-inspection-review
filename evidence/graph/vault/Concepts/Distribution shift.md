---
title: "Distribution shift"
aliases:
  - "Dataset shift"
  - "Train-test distribution shift"
  - "Data shift"
tags:
  - concept
---

# Distribution Shift

## Definition

Distribution shift is a mismatch between the data distribution used for training and the distribution encountered during testing or deployment. In industrial inspection papers, it can arise from new products, components, acquisition settings, materials, defect patterns, or sensors.

## Why It Matters

Models that perform well on random splits may fail when the test set contains unseen component types or defect appearances. Distribution-shift benchmarks make this failure mode measurable instead of assuming IID train and test data.

## Used In These Papers

- [[2025 - A Dataset and Baseline for Deep Learning-Based Visual Quality Inspection in Remanufacturing]] defines S1-S4 split protocols to create increasingly severe shifts for gearbox component OK/nOK classification.

## Related Concepts

- [[Domain gap]]
- [[Gearbox component distribution-shift inspection benchmark]]
- [[Remanufacturing inspection]]
- [[Industrial visual inspection]]
