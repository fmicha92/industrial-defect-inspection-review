---
status: emerging
concept_type: method
candidate_parent: "Methods/Deployment"
aliases:
  - "YOLOv11-RKNN"
  - "RKNN YOLOv11 deployment"
source_papers:
  - "[[2025 - Workpiece Surface Defect Detection Based on YOLOv11 and Edge Computing]]"
evidence_count: 1
---
# YOLOv11-RKNN edge deployment

## Definition

YOLOv11-RKNN edge deployment converts a cloud-trained YOLOv11 detector into an RKNN model for RK3568 edge inference. The source paper uses RKNN-Toolkit2, asymmetric INT8 quantization, RKNN Lite deployment, and the RKNPU2 driver.

## Why It Matters

The conversion reduces the reported YOLOv11 model size from 10,156 KB to 4,194 KB and reduces 200 x 200 image detection time from 52.1 ms to 33.6 ms while preserving detection accuracy approximately relative to the cloud model.

## Used In These Papers

- [[2025 - Workpiece Surface Defect Detection Based on YOLOv11 and Edge Computing]] - deploys YOLOv11-RKNN on RK3568 for workpiece surface defect detection.

## Related Concepts

- [[YOLOv11]]
- [[Edge intelligence]]
- [[Workpiece surface defect detection]]
- [[Detection time]]
