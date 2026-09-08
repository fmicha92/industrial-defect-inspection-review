---
title: "Simulation-Based Data Augmentation for the Quality Inspection of Structural Adhesive With Deep Learning"
aliases:
  - "Simulation-Based Data Augmentation for Structural Adhesive Inspection"
paper_key: "doi:10.1109/access.2021.3082690"
paper_type: research
year: 2021
venue: "IEEE Access"
authors:
  - "Ricardo Silva Peres"
  - "Magno Guedes"
  - "Fábio Miranda"
  - "Jose Barata"
status: processed
processed_at: 2026-05-20
topics:
  - simulation-based data augmentation
  - quality inspection
  - structural adhesive
  - object detection
tasks:
  - "[[Adhesive bead defect detection]]"
domains:
  - "[[Automotive manufacturing]]"
datasets:
  - "[[SEE-Q]]"
  - "[[A-SEE-Q]]"
dataset_sizes:
  - "124 manually annotated real adhesive bead images"
  - "4000 synthetic images for augmentation experiments"
methods:
  - "[[Simulation-based data augmentation]]"
  - "[[YOLOv4]]"
  - "YOLOv4-Tiny"
  - Scaled-YOLOv4
metrics:
  - "[[mAP@0.15]]"
  - "[[mAP@0.30]]"
  - "[[mAP@0.50]]"
  - "[[Detection time]]"
primary_metric: "[[mAP@0.50]]"
code: "reported available with data at GitHub; repository unavailable as of 2026-06-06"
data: "reported public in paper; GitHub repository unavailable as of 2026-06-06"
doi: "10.1109/ACCESS.2021.3082690"
arxiv: "not reported"
related_papers:
  - "[[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]]"
related_concepts:
  - "[[Synthetic data generation]]"
  - "[[Simulation-based data augmentation]]"
  - "[[Domain gap]]"
related_methods:
  - "[[Simulation-based data augmentation]]"
related_datasets:
  - "[[SEE-Q]]"
  - "[[A-SEE-Q]]"
related_tasks:
  - "[[Adhesive bead defect detection]]"
  - "[[Surface defect detection]]"
concept_notes_created_or_updated:
  - "[[Simulation-based data augmentation]]"
  - "[[Synthetic data generation]]"
  - "[[Industrial visual inspection]]"
  - "[[Domain gap]]"
url: "https://doi.org/10.1109/ACCESS.2021.3082690"
pdf: "paper-inbox/10_processed/Other/2021 - Peres - Simulation-Based Data Augmentation for the Quality Inspection of Structural Adhesive With Deep Learning.pdf"
source_file: "paper-inbox/10_processed/Other/2021 - Peres - Simulation-Based Data Augmentation for the Quality Inspection of Structural Adhesive With Deep Learning.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2021 - Peres - Simulation-Based Data Augmentation for the Quality Inspection of Structural Adhesive With Deep Learning.md"
extracted_text: "paper-inbox/90_processing/text/2021 - Peres - Simulation-Based Data Augmentation for the Quality Inspection of Structural Adhesive With Deep Learning.txt"
artifact_status: "code and data reported available in paper; GitHub repository unavailable as of 2026-06-06"
tags:
  - paper
  - synthetic-data
  - simulation
  - object-detection
---

# Simulation-Based Data Augmentation for the Quality Inspection of Structural Adhesive With Deep Learning

## Summary

The paper proposes a simulation-based method for generating annotated synthetic training images for structural adhesive inspection in an automotive production cell. It introduces [[SEE-Q]], a 124-image real adhesive bead dataset reported as public in the paper, and augments it with [[A-SEE-Q]], 4000 simulation-generated synthetic defect images with YOLO-format bounding boxes. The recorded GitHub repository for the data and artifacts was unavailable during the 2026-06-06 host audit. The main reported result is that YOLOv4 trained on real plus synthetic data improves mAP at the measured IoU thresholds, including a 3.1 percentage-point mAP@0.50 improvement in a scarce, imbalanced manufacturing data setting.

## Contribution

- Claimed: Synthetic simulation data can reduce data collection cost and improve object detection performance for structural adhesive inspection.
- Shown: YOLOv4 trained with augmented real-plus-synthetic data improved mAP across IoU thresholds; the abstract reports a 3.1% mAP@0.50 improvement.
- Inferred: Simulation is positioned as practical when GAN training data are too scarce.

## Method

- Simulation environment: CoppeliaSim scene modeling the end result of industrial structural adhesive application to an automotive part.
- Defect classes: discontinuity and excess adhesive; the simulation can be parameterized for additional defect types such as bead narrowing.
- Defect generation: each synthetic part receives 1 to 3 defects; the algorithm selects defect type, bead-relative start position, and length.
- Annotation generation: bounding boxes are generated in YOLO format with object class, center coordinates, width, and height. Polynomial coordinate approximations convert bead-relative defect positions into image coordinates.
- Models: YOLOv4, YOLOv4-Tiny, and Scaled-YOLOv4 variants trained with Darknet.
- Transfer learning: models use MS COCO pretrained initial weights.
- Scenario A: train only on 4000 synthetic images and test on 124 real images.
- Scenario B: compare synthetic-only, real-only, and real-plus-synthetic augmented training sets on a holdout set of 36 real images with 69 defect instances.
- Baseline-vs-augmentation comparison: Scenario B treats real-only training as the common-practice baseline and tests whether adding simulation-generated synthetic images improves detection on held-out real images.
- Validation cell: high-throughput pilot automotive adhesive application cell at Introsys S.A. with an ABB IRB 2400 robot, Nordson dispensing hardware, an in-process inspection ring with IDS cameras and IR lighting, post-process Teledine cameras, conveyor transport, and Siemens Simatic S7-400 PLC control.

## Evidence

| Evidence | Reported detail |
|---|---|
| Real dataset | SEE-Q: 124 manually annotated real adhesive bead images |
| Real defect instances | 160 discontinuity instances and 70 excess-defect instances |
| Synthetic augmentation | 4000 synthetic images in Scenario A |
| Test set | Scenario B uses a holdout set of 36 real images containing 69 defect instances |
| Main metric claim | +3.1 percentage points mAP@0.50 after synthetic augmentation in the abstract |
| Baseline-vs-improvement | Real-only YOLOv4 training is compared against real-plus-synthetic augmented training; the augmented YOLOv4 model improves mAP at IoU 0.15, 0.30, and 0.50 |
| Runtime tradeoff | YOLOv4 had higher mAP, while YOLOv4-Tiny was nearly twice as fast and trained in 85 minutes versus about 660 minutes for YOLOv4 |
| Artifacts | Simulation, configurations, weights, and data are reported available at https://github.com/RicardoSPeres/simulation-synth-adhesive; host audit on 2026-06-06 found the repository unavailable / 404. A related public repository, https://github.com/RicardoSPeres/GAN_Synth_Adhesive, hosts dataset assets for the separate GAN structural-adhesive augmentation paper, but the release descriptions do not match SEE-Q/A-SEE-Q exactly. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[mAP@0.15]] | Adhesive defect detection at lenient overlap | Mean average precision at IoU 0.15 | Higher is better | no | Reported in Scenario A and Scenario B tables; exact table values are in the source tables |
| [[mAP@0.30]] | Adhesive defect detection at medium overlap | Mean average precision at IoU 0.30 | Higher is better | no | Reported in Scenario A and Scenario B tables; exact table values are in the source tables |
| [[mAP@0.50]] | Adhesive defect detection at stricter overlap | Mean average precision at IoU 0.50 | Higher is better | yes | Abstract reports a 3.1 percentage-point improvement; YOLOv4 outperforms the best YOLOv4-Tiny model by about 9.16 percentage points in mAP@0.50 |
| [[Detection time]] | Per-image inference speed | Average detection time per image | Lower is better | no | YOLOv4-Tiny is reported nearly twice as fast as YOLOv4 |

## Limitations

- Extreme cases that differ too much from the training set remain difficult.
- The paper identifies annotation generation, especially bounding box coordinate approximation, as a clear improvement point.
- Simulation must be modeled for the specific use case.
- The simulation output is not a perfect photorealistic representation of the real environment.
- The paper suggests that future GAN-based approaches may become attractive if GANs become stable with fewer than 500 samples, because they could reduce per-use-case simulation modeling effort.

## Connections

### Graph Hubs

- Tasks: [[Adhesive bead defect detection]], [[Surface defect detection]]
- Methods: [[Simulation-based data augmentation]], [[Synthetic data generation]], [[YOLOv4]]
- Datasets: [[SEE-Q]], [[A-SEE-Q]]
- Domains: [[Automotive manufacturing]], [[Industrial visual inspection]]
- Metrics: [[mAP@0.15]], [[mAP@0.30]], [[mAP@0.50]], [[Detection time]]
- Concepts: [[Domain gap]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]] | Shares method | Both use simulation-generated inspection images to improve training with scarce real examples; this paper targets adhesive bead object detection while Schmedemann et al. target rendered surface defect classification. |
| [[2021 - Defect Detection in CT Scans of Cast Aluminum Parts]] | Shares method | Both use simulation to avoid manual labeling bottlenecks, but this paper generates 2D adhesive images and bounding annotations while Fuchs et al. generate CT volumes with voxel labels. |

### Backlinks Updated

- [[Simulation-based data augmentation]] links this paper as an adhesive-inspection simulation example.
- [[Synthetic data generation]] links this paper as a simulation-generated augmentation example.
- [[Industrial visual inspection]] links this paper as an automotive production-cell inspection use case.
- [[Domain gap]] links this paper for extreme cases outside the training set.
- [[Adhesive bead defect detection]] links this paper as its source-backed inspection task.

### Concept Notes Created Or Updated

| Concept note | Action | Explanation source |
|---|---|---|
| [[Simulation-based data augmentation]] | Created | Processed paper notes |
| [[Synthetic data generation]] | Created | Processed paper notes |
| [[Industrial visual inspection]] | Created | Processed paper notes |
| [[Domain gap]] | Created | Paper limitations and linked notes |

## Questions

- Can the unavailable `simulation-synth-adhesive` repository be recovered, and how exactly do the related `GAN_Synth_Adhesive` release splits map onto SEE-Q/A-SEE-Q, if at all?
- How sensitive is performance to simulation fidelity versus annotation accuracy?
- Would pixel-level labels improve inspection over bounding boxes for adhesive defects?
