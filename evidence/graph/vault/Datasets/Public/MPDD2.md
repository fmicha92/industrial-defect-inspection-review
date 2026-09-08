---
title: "MPDD2"
aliases:
  - "MPDD2"
  - "Metal Parts Defect Detection Dataset 2"
  - "Real-world industrial anomaly benchmark dataset"
  - "metal parts fabrication anomaly benchmark"
related_domain: "[[Metal inspection]]"
url: "https://github.com/stepanje/MPDD2"
download_url: "https://drive.google.com/drive/folders/1KAJfPPuusS4fEbPocHtIjLehCkpSEUSS?usp=sharing"
data_sources: "GitHub"
license: "Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International"
introduced_by: "[[2022 - Anomaly Detection for Real-World Industrial Applications Benchmarking Recent Self-Supervised and Pretrained Methods]]"
---
# MPDD2

## Definition

MPDD2, or Metal Parts Defect Detection Dataset 2, contains images of metal parts from an industrial manufacturing setting, with anomaly-free training samples and validation samples containing both normal and anomalous images.

## Why It Matters

It tests whether methods that perform well on [[MVTec AD]] remain robust under fewer samples and higher acquisition variability, including object position, rotation, lighting, and motion blur.

## Used In These Papers

- [[2022 - Anomaly Detection for Real-World Industrial Applications Benchmarking Recent Self-Supervised and Pretrained Methods]] introduces MPDD2 and benchmarks CutPaste, NSA, PatchCore, FastFlow, CFLOW-AD, PaDiM, and CFA on four metal-part classes.

## Dataset Details

- Classes: Bracket Brown, Bracket Grey, Bracket White, and Rosette.
- Training images: 385 normal images.
- Test images: 96 normal images and 264 anomalous images.
- Repository description: Metal Parts Defect Detection Dataset 2.
- Host-reported size: more than 700 images.
- Host-reported split: training subset with anomaly-free samples and validation subset with normal and anomalous samples.
- Task: image-level [[Industrial anomaly detection]].
- Domain: [[Metal inspection]].
- Input preprocessing in the benchmark: images resized to 256 x 256 pixels.
- Labels: normal/anomalous image labels are reported.
- License: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International.
- Download: Google Drive folder linked from the repository.

## Source Anchors

- Hosting source: https://github.com/stepanje/MPDD2.
- Download link: https://drive.google.com/drive/folders/1KAJfPPuusS4fEbPocHtIjLehCkpSEUSS?usp=sharing.
- Introducing paper: [[2022 - Anomaly Detection for Real-World Industrial Applications Benchmarking Recent Self-Supervised and Pretrained Methods]].

## Related Concepts

- [[Metal inspection]]
- [[Surface defect detection]]
- [[Industrial visual inspection]]
