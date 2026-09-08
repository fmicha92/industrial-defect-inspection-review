---
title: "mAP@0.50-0.95"
aliases:
  - "mAP@0.5:0.95"
  - "mean average precision at IoU 0.50 to 0.95"
tags:
  - metric
  - detection
---
# mAP@0.50-0.95

## Definition

mAP@0.50-0.95 averages mean average precision across IoU thresholds from 0.50 to 0.95.

## Direction

Higher is better.

## Used In These Papers

- [[2025 - You Only Look Once-Aluminum]] uses mAP@0.50-0.95 in training curves and ablation experiments for [[YOLO-AL]] on [[APDDD]].
- [[2024 - A Dataset for Deep Learning Based Detection of Printed Circuit Board Surface Defect]] reports [[DsPCBSD+]] AP50:95 of 0.492 for [[Co-DETR]] and 0.514 for [[YOLOv6-L6]].

## Related Metrics

- [[mAP]]
- [[mAP@0.50]]
- [[Average precision]]
