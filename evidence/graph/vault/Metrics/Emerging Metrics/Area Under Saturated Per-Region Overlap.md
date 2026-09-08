---
title: "Area Under Saturated Per-Region Overlap"
aliases:
  - "AUsPRO"
status: emerging
concept_type: metric
candidate_parent: "Metrics/Emerging Metrics"
source_papers:
  - "[[2022 - Beyond Dents and Scratches Logical Constraints in Unsupervised Anomaly Detection and Localization]]"
  - "[[2024 - Detecting Visual Anomalies in an Industrial Environment Unsupervised Methods Put to the Test on the AutoVI Dataset]]"
evidence_count: 2
tags:
  - metric
  - emerging-taxonomy
---
# Area Under Saturated Per-Region Overlap

## Definition

Area Under Saturated Per-Region Overlap summarizes saturated per-region overlap over anomaly-threshold settings. [[2022 - Beyond Dents and Scratches Logical Constraints in Unsupervised Anomaly Detection and Localization]] introduces it as a generalized PRO metric for logical anomalies where a correct localization may need to mark only a sufficient subregion of an annotated context area.

## Why It Matters

Logical defects may involve missing or misplaced items where the entire context region does not need to be segmented to count as a useful detection. AUsPRO lets the benchmark define saturation thresholds for defect regions so segmentation methods are not penalized for failing to mark every context pixel.

## Used In These Papers

- [[2022 - Beyond Dents and Scratches Logical Constraints in Unsupervised Anomaly Detection and Localization]] introduces AUsPRO and reports normalized area under the sPRO curve up to 5% average false positive rate per pixel on [[MVTec LOCO AD]].
- [[2024 - Detecting Visual Anomalies in an Industrial Environment Unsupervised Methods Put to the Test on the AutoVI Dataset]] reports mean AUsPRO for CFlow, DRAEM, DSR, EfficientAD, PaDiM, and Patchcore; Patchcore has the best reported mean AUsPRO at 68.9%.

## Related Concepts

- [[Industrial anomaly detection]]
- [[Surface defect detection]]
- [[Logical anomalies]]
- [[AU-ROC]]
- [[Average precision]]
