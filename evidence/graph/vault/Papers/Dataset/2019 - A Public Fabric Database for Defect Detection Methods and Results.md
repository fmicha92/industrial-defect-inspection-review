---
title: "A Public Fabric Database for Defect Detection Methods and Results"
aliases:
  - "A Public Fabric Database for Defect Detection Methods and Results"
paper_key: "sha256:dd562ebbe12ad3676e28b5c81e82237a67cd8ff3bf57494fb9388d9b0e6f1d70"
paper_type: dataset
year: 2019
venue: "AUTEX Research Journal"
authors:
  - "Javier Silvestre-Blanes"
  - "Teresa Albero-Albero"
  - "Ignacio Miralles"
  - "Ruben Perez-Llorens"
  - "Jorge Moreno"
status: processed
processed_at: 2026-05-22
topics:
  - "fabric inspection"
  - "public benchmark"
  - "machine vision"
tasks:
  - "[[Textile defect detection]]"
  - "[[Defect classification]]"
domains:
  - "[[Textile and fiber inspection]]"
datasets:
  - "[[AITEX]]"
methods:
  - "[[Gabor filters]]"
model_family:
  - "[[Classical ML]]"
architectures: []
metrics:
  - "[[Detection success rate]]"
  - "[[Detection rate]]"
  - "[[Specificity]]"
  - "[[False alarm rate]]"
primary_metric: "[[Detection success rate]]"
metric_definitions:
  - "Detection success rate: correctly detected samples divided by all defective and defect-free samples."
  - "Detection rate or sensitivity: correctly detected defective samples divided by all defective samples."
  - "Specificity: correctly classified defect-free samples divided by all defect-free samples."
  - "False alarm rate: false alarms among defect-free samples."
baselines: []
benchmarks:
  - "[[AITEX]]"
code: "not reported"
data: "www.aitex.es/afid"
doi: "10.2478/aut-2019-0035"
arxiv: "not reported"
url: "https://doi.org/10.2478/aut-2019-0035"
pdf: "not reported"
data_sources:
  - "factory capture system"
  - "www.aitex.es/afid"
licenses: "not reported"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Gabor filters]]"
  - "[[Classical ML]]"
related_datasets:
  - "[[AITEX]]"
related_domains:
  - "[[Textile and fiber inspection]]"
related_tasks:
  - "[[Textile defect detection]]"
  - "[[Defect classification]]"
related_benchmarks:
  - "[[AITEX]]"
source_file: "paper-inbox/00_incoming/document.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2019 - Silvestre-Blanes - A Public Fabric Database for Defect Detection Methods and Results.md"
extracted_text: "paper-inbox/90_processing/text/2019 - Silvestre-Blanes - A Public Fabric Database for Defect Detection Methods and Results.txt"
artifact_status: "public dataset reported; code and trained models not reported"
tags:
  - paper
---
# A Public Fabric Database for Defect Detection Methods and Results

## Summary

Silvestre-Blanes et al. introduce a public annotated database for plain-fabric defect detection and classification. The dataset contains 245 grayscale fabric images captured from a real production installation, with 140 defect-free images and 105 defective images across 12 defect types and seven fabric structures.

The paper also reviews earlier fabric defect databases and methods, then demonstrates the dataset with a Gabor-filter detection pipeline. The demonstration is not presented as a new state-of-the-art detector; it is used to show how the public dataset can support comparable evaluation.

## Paper Type

- Type: dataset.
- Why: The central contribution is a public annotated benchmark of fabric images and segmentation masks, plus an example evaluation protocol.

## Problem

- Task: [[Textile defect detection]] and [[Defect classification]].
- Setting: automated quality inspection in textile manufacturing.
- Inputs: 4096 x 256 pixel grayscale images of plain fabric textures.
- Outputs: defective or defect-free detections, defect localization masks, and defect-type examples.
- Motivation: prior textile defect detection papers often used private, small, differently captured image collections, preventing objective comparison.
- Assumptions: the dataset focuses mainly on plain fabrics with uniform textures; patterned fabrics are not the main target.

## Contribution

- Claimed: a public annotated benchmark of plain fabrics, including images with and without defects, to enable direct comparison of detection and classification methods.
- Shown: 245 real-production images from seven fabric structures, 12 defect types, and hand-created segmentation masks for defective images.
- Shown: a Gabor-filter detection example evaluated with detection success rate, detection rate, specificity, and false alarm rate.

## Method

- Dataset construction: images were captured in a production plant by a machine-vision system with a linear GigaEthernet camera, LED linear lighting, encoder synchronization, PC processing, and tablet-based operator labeling.
- Annotation: an operator stopped production when defects were detected, labeled them through an Android tablet application, and the system stored labels with captured images.
- Detection example: the paper applies preprocessing, a Gabor filter bank, thresholding, image addition across filtered responses, morphology filtering, and contour extraction.
- Gabor setup: an uneven filter is applied four times with different orientations while sigma, lambda, and psi are fixed per test; the paper reports two sigma settings.
- Training: no learned training procedure is reported for the Gabor demonstration.
- Deployment constraints: the capture setup is industrial and tied to production-line inspection; exact runtime and compute are not reported.

## ML / DL Extraction

### Task Formulation

- Input modality: grayscale textile inspection images.
- Output target: defective/defect-free classification plus defect localization using masks and detected contours.
- Supervision: supervised labels and hand-created masks are available for defective images.
- Objective: benchmark comparable fabric defect detection and classification methods.

### Model And Training

- Model family: [[Classical ML]].
- Method: [[Gabor filters]].
- Parameters: two reported test settings vary sigma while theta, lambda, and psi are fixed; the OCR text exposes theta/sigma/lambda/psi inconsistently, but the paper states sigma changes between tests.
- Pretraining: not applicable.
- Fine-tuning: not applicable.
- Losses: not applicable.
- Optimizer: not applicable.
- Hyperparameters: Gabor theta, sigma, lambda, and psi are the core parameters; exact table values are partially garbled in the extracted text.
- Seeds: not applicable.
- Training compute: not applicable.

### Data

- Dataset: [[AITEX]].
- Data source: real production plant images.
- Dataset size: 245 images, each 4096 x 256 pixels.
- Defect-free images: 140 total, 20 for each of seven fabric structures.
- Defective images: 105 total.
- Defect categories: 12 types are available in the database: cut selvage, broken end, crease, warp ball, broken yarn, knots, contamination, nep, broken pick, weft crack, weft curling, and fuzzy ball.
- Labels / annotations: image-level defect status, defect labels, and segmentation masks for defective images.
- Splits: not reported.
- Preprocessing: the Gabor demonstration uses initial preprocessing before filtering; exact preprocessing operations are not reported.
- Augmentation: not reported.
- Synthetic data: not reported.
- Leakage checks: not reported.
- License: not reported.
- Public access: the paper reports Internet access at `www.aitex.es/afid`.

### Evaluation

- Protocol: evaluate the Gabor-filter pipeline on 105 defective and 140 defect-free images.
- Used performance metrics: [[Detection success rate]], [[Detection rate]], [[Specificity]], and [[False alarm rate]].
- Primary metric: [[Detection success rate]].
- Metric direction / units: DSR, detection rate, and specificity are percentages where higher is better; false alarm rate is a percentage where lower is better.
- Baselines: no direct method baseline is evaluated on the proposed dataset.
- Benchmarks: [[AITEX]].
- Statistical tests: not reported.
- Failure cases: test 1 has lower detection rate but few false alarms; test 2 has higher detection rate but more false defects.

## Evidence

### Experimental Setup

- Dataset: [[AITEX]].
- Defective samples: 105.
- Defect-free samples: 140.
- Method under test: Gabor-filter detection pipeline.
- Baselines: not reported.
- Compute: PC-based processing in the capture system is reported; hardware specifications are not reported.
- Training time: not applicable.
- Inference cost: not reported.

### Main Results

| Test | Dataset / Task | Detection rate / sensitivity | Specificity | False alarm rate | Detection success rate | Notes |
|---|---|---:|---:|---:|---:|---|
| Test 1 | [[AITEX]] / [[Textile defect detection]] | 82/105 = 78.10% | 136/140 = 97.14% | 2.90% | 88.98% | More conservative parameters; lower detection rate and fewer false alarms. |
| Test 2 | [[AITEX]] / [[Textile defect detection]] | 91/105 = 86.67% | 124/140 = 88.57% | 11.4% | 87.76% | Higher detection rate with more false defects. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Detection success rate]] | Overall defect detection | Correctly detected samples divided by all defective and defect-free samples; percent | Higher is better | yes | Also called detection accuracy in the paper. |
| [[Detection rate]] | Defective-sample detection | Correctly detected defective samples divided by all defective samples; percent | Higher is better | no | The paper also calls this sensitivity. |
| [[Specificity]] | Defect-free classification | Correctly classified defect-free samples divided by all defect-free samples; percent | Higher is better | no | Reported from true negatives over 140 defect-free images. |
| [[False alarm rate]] | False detections on defect-free images | False alarms among defect-free samples; percent | Lower is better | no | Increases from test 1 to test 2. |

### Ablations

- The paper compares two Gabor-parameter settings. It does not report a broader ablation over filter-bank design, thresholding, morphology, or fabric structure.

## Dataset / Benchmark Details

- Source: `www.aitex.es/afid`.
- Collection: real production plant capture over 6 months.
- Capture hardware: linear GigaEthernet camera, LED linear lighting, encoder synchronization, PC processing, and tablet labeling.
- Image format / resolution: grayscale images, 4096 x 256 pixels.
- Size: 245 images.
- Defect-free coverage: 140 images, 20 for each of seven fabric structures.
- Defective coverage: 105 images with 12 defect types.
- Annotation: operator labels plus hand-created segmentation masks for all defective images.
- Modalities: visual fabric inspection imagery and binary segmentation masks.
- License: not reported.
- Leakage risks: no split or leakage analysis is reported.
- Bias / coverage: focuses on plain fabrics; defect frequency reflects observed production rates during data collection.
- Maintenance: the authors propose installing more machines in other factories so the dataset can continue to grow.

## Limitations

- The Gabor-filter example is not intended to establish the best detection method.
- Test results are sensitive to parameter selection; the paper states different values can be used according to textile type.
- The dataset has uneven defect counts because the images come from real production where defects occur at different rates.
- Splits, train/test protocols, license terms, and code availability are not reported.
- Patterned fabrics are not the main scope.

## Reproducibility

- Code: not reported.
- Data: public access reported at `www.aitex.es/afid`.
- Hyperparameters: Gabor parameter categories are reported; extracted table values are partially garbled.
- Random seeds: not applicable.
- Environment: not reported.
- Checkpoints / models: not applicable.
- Exact preprocessing: partially reported; exact threshold and morphology settings are not reported.
- Artifact status: dataset and masks are reported public; source code is not reported.

## Systems Details

- Hardware / software stack: linear GigaEthernet camera, LED linear lighting, encoder, PC, tablet, socket-based label communication, and Android labeling application.
- Latency: not reported.
- Throughput: not reported.
- Memory: not reported.
- Scaling: future work proposes adding machines in other factories and managing larger data volumes.
- Deployment assumptions: production-line capture with human operator labeling.
- Cost: not reported.
- Failure modes: parameter changes trade detection rate against false alarms.

## Connections

### Graph Hubs

- Tasks: [[Textile defect detection]], [[Defect classification]]
- Methods: [[Gabor filters]], [[Classical ML]]
- Datasets: [[AITEX]]
- Benchmarks: [[AITEX]]
- Domains: [[Textile and fiber inspection]]
- Metrics: [[Detection success rate]], [[Detection rate]], [[Specificity]], [[False alarm rate]]
- Concepts: [[Surface defect detection]], [[Industrial visual inspection]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2021 - ZJU-Leaper A Benchmark Dataset for Fabric Defect Detection and a Comparative Study]] | Follow-up reading | ZJU-Leaper is another public fabric defect benchmark and explicitly contrasts with earlier public fabric datasets. |

### Backlinks Updated

- [[AITEX]]
- [[Textile and fiber inspection]]
- [[Detection success rate]]
- [[Detection rate]]
- [[Specificity]]
- [[False alarm rate]]

### Concept Notes Created Or Updated

| Concept note | Action | Explanation source |
|---|---|---|
| [[Detection success rate]] | Created | Metric definitions and Table 5. |
| [[Detection rate]] | Created | Metric definitions and Table 5. |
| [[False alarm rate]] | Created | Metric definitions and Table 5. |

## Questions

- What are the current access status and license terms for `www.aitex.es/afid`?
- Can later papers using this dataset establish standard splits or protocols?
- Which Gabor parameter values are reliable after checking the PDF table directly rather than OCR text?
