---
title: "Defect-IoU loss"
aliases:
  - "Defect-IoU Loss"
status: emerging
concept_type: method
candidate_parent: "Methods/Models/Computer Vision Models"
source_papers:
  - "[[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]]"
evidence_count: 1
---
# Defect-IoU Loss

## Definition

Defect-IoU loss is the bounding-box regression loss proposed in [[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]]. It scales CIoU with a balance function so small industrial defects can receive more localization-loss attention during training.

## Why It Matters

Industrial defect size can vary sharply within one dataset. The paper reports that Defect-IoU improves aluminium defect detection over CIoU, DIoU, GIoU, Alpha-IoU, and EIoU in its loss comparison table.

## Used In These Papers

- [[2023 - IDD-Net Industrial Defect Detection Method Based on Deep-Learning]] uses Defect-IoU as the localization loss in IDD-Net.

## Related Concepts

- [[IDD-Net]]
- [[mAP@0.50]]
- [[Object detection]]
