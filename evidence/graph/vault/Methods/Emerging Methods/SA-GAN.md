---
status: emerging
concept_type: method
candidate_parent: "Methods/Synthetic Data Generation/Learned Generative Synthesis"
aliases:
  - "Self-attention GAN"
  - "Self-Attention Generative Adversarial Network"
source_papers:
  - "[[2025 - Workpiece Surface Defect Detection Based on YOLOv11 and Edge Computing]]"
evidence_count: 1
---
# SA-GAN

## Definition

SA-GAN is a self-attention GAN used in the YOLOv11 edge-computing paper to synthesize workpiece surface defect images. The paper describes it as using query, key, and value projections to model global image dependencies and generate diverse defect samples coordinated with the image background.

## Why It Matters

SA-GAN expands limited surface defect datasets before detector training. In the source paper, adding SA-GAN augmentation raises YOLOv11 mAP@0.5 on NEU-DET from 81.4% to 85.1% and supports a Tianchi aluminium profile generalization experiment.

## Used In These Papers

- [[2025 - Workpiece Surface Defect Detection Based on YOLOv11 and Edge Computing]] - uses SA-GAN with random cropping, flipping, and rotation to expand NEU-DET and Tianchi aluminium profile defect data before YOLO training.

## Related Concepts

- [[GAN]]
- [[Synthetic data generation]]
- [[Data augmentation]]
- [[Workpiece surface defect detection]]
- [[NEU-DET]]
