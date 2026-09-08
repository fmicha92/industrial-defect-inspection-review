---
title: "IoU@Top10%"
aliases:
  - "IoU at Top 10 percent"
status: emerging
concept_type: metric
candidate_parent: "Metrics/Emerging Metrics"
source_papers:
  - "[[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]]"
evidence_count: 1
---
# IoU@Top10%

## Definition

IoU@Top10% measures overlap between the top 10% most influential pixels in an occlusion sensitivity map and a consistently generated proxy defect mask.

## Direction

Higher indicates stronger localization overlap, but the source paper cautions that high overlap is not the same as full explanation faithfulness.

## Used In These Papers

- [[2026 - Diagnosing Shortcut Learning in CNN-Based Photovoltaic Fault Recognition from RGB Images]] uses IoU@Top10% to evaluate occlusion-map localization.

## Related Concepts

- [[Occlusion sensitivity]]
- [[IoU]]
- [[Shortcut learning]]
