---
title: "HRIPCB: a Challenging Dataset for PCB Defects Detection and Classification"
aliases:
  - "HRIPCB"
  - "A PCB Dataset for Defects Detection and Classification"
  - "PKU-Market-PCB introducing paper"
paper_key: "doi:10.1049/joe.2019.1183"
paper_type: dataset
year: 2020
venue: "The Journal of Engineering"
authors:
  - "Weibo Huang"
  - "Peng Wei"
  - "Manhua Zhang"
  - "Hong Liu"
status: processed
processed_at: 2026-05-20
topics:
  - PCB defect detection
  - PCB defect classification
  - reference-based inspection
tasks:
  - "[[PCB defect detection]]"
  - "[[PCB defect classification]]"
domains:
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[HRIPCB]]"
methods:
  - "[[Reference-based PCB inspection]]"
  - "[[RBCNN]]"
metrics:
  - "[[Average classification precision]]"
  - "[[Defect detection error rate]]"
  - "[[Inference time]]"
primary_metric: "[[Average classification precision]]"
metric_definitions:
  - "Defect detection error rate Pd: (detected defect areas - actual defect areas) / actual defect areas x 100%."
  - "Classification precision rate Pc: correctly predicted defects of a type divided by actual defects of that type x 100%."
  - "Average classification precision APc: mean of Pc across the six defect types."
doi: "10.1049/joe.2019.1183"
arxiv: "1901.08204"
url: "https://doi.org/10.1049/joe.2019.1183"
related_methods:
  - "[[Reference-based PCB inspection]]"
  - "[[RBCNN]]"
related_datasets:
  - "[[HRIPCB]]"
related_tasks:
  - "[[PCB defect detection]]"
  - "[[PCB defect classification]]"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2020 - Huang - HRIPCB a Challenging Dataset for PCB Defects Detection and Classification.md"
extracted_text: "paper-inbox/90_processing/text/2020 - Huang - HRIPCB a Challenging Dataset for PCB Defects Detection and Classification.txt"
pdf: "paper-inbox/10_processed/Dataset/2020 - Huang - HRIPCB a Challenging Dataset for PCB Defects Detection and Classification.pdf"
preprint_pdf: "paper-inbox/10_processed/Dataset/2019 - Huang - A PCB Dataset for Defects Detection and Classification.pdf"
source_file: "paper-inbox/10_processed/Dataset/2020 - Huang - HRIPCB a Challenging Dataset for PCB Defects Detection and Classification.pdf"
tags:
  - paper
  - dataset
  - pcb
---

# HRIPCB: a Challenging Dataset for PCB Defects Detection and Classification

## Summary

- Introduces [[HRIPCB]], also referred to as PKU-PCB or PKU-Market-PCB in later papers, a public synthesized naked-PCB dataset with 1,386 images and six defect kinds.
- Proposes an RBCNN workflow that locates defects through reference comparison and then classifies cropped defect regions with a CNN.
- Reports near-zero detection error for most defect types and average classification precision of 97.74% and 99.40% in the two evaluated sample groups.

## Paper Type

Dataset paper with an accompanying baseline method.

## Contribution

- Claimed: HRIPCB supports PCB defect detection, classification, and registration tasks.
- Shown: The dataset includes template boards, defect annotations, rotated images, and Python access support.
- Shown: Six defect types are missing hole, mouse bite, open circuit, short, spur, and spurious copper.

## Method

The RBCNN approach uses registration, reference comparison, XOR, filtering, mathematical morphology, bounding-box cropping, data augmentation through box offsets, and a CNN classifier.

## Evidence

| Evidence | Reported detail |
|---|---|
| Dataset size | 1,386 images |
| Defect classes | 6 |
| Dataset access | Reported as freely available online at the paper's dataset URL |
| Detection error | 0% for four classes, 0.2% for mouse bite and open circuit |
| Classification APc | 97.74% and 99.40% in the reported evaluations |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[Defect detection error rate]] | Reference-comparison defect localization | Pd = (detected areas - actual areas) / actual areas x 100% | Lower is better | no | Missing hole 0%, mouse bite 0.2%, open circuit 0.2%, short 0%, spur 0%, spurious copper 0%. |
| [[Average classification precision]] | Six-class PCB defect classification | Mean Pc across six defect types | Higher is better | yes | Test data APc 97.74%; all samples APc 99.40%. |
| [[Average classification precision]] | Per-class classification precision, test data | Correct predictions per defect type divided by actual defects of that type | Higher is better | no | Missing hole 98.96%, mouse bite 97.94%, open circuit 97.74%, short 99.48%, spur 93.65%, spurious copper 98.52%. |
| [[Average classification precision]] | Per-class classification precision, all samples | Correct predictions per defect type divided by actual defects of that type | Higher is better | no | Missing hole 100%, mouse bite 99.6%, open circuit 99.18%, short 99.39%, spur 99.39%, spurious copper 98.80%. |
| [[Inference time]] | Full RBCNN pipeline per PCB | Seconds per step | Lower is better | no | Registration 0.6219 s, binarisation 0.1650 s, localisation 0.1808 s, classification 0.0212 s, total 0.9889 s. |

## Limitations

- The dataset is synthesized/colorized rather than a broad set of real production PCB failures.
- The baseline uses template/reference comparison, so it assumes suitable template alignment.
- Registration dominates runtime, taking 0.6219 s of the 0.9889 s total pipeline time.

## Connections

### Graph Hubs

- Tasks: [[PCB defect detection]], [[PCB defect classification]]
- Datasets: [[HRIPCB]]
- Methods: [[Reference-based PCB inspection]], [[RBCNN]]
- Metrics: [[Average classification precision]], [[Defect detection error rate]], [[Inference time]]
- Domains: [[Semiconductor and electronics]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2019 - Online PCB Defect Detector on a New PCB Defect Dataset]] | Shares task | Both create PCB defect datasets and evaluate defect localization/classification methods; DeepPCB emphasizes online detection with mAP and FPS. |
| [[2022 - Semi-Supervised Defect Detection Method with Data-Expanding Strategy for PCB Quality Inspection]] | Dataset reuse | DE-SSD uses PKU-PCB as auxiliary PCB data for data expansion on DeepPCB. |

## Questions

- What license terms apply to the public PKU-Market-PCB / HRIPCB download?
- How well does RBCNN perform without well-aligned templates?
