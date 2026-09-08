---
title: "Synthetic image data augmentation for fibre layup inspection processes: Techniques to enhance the data set"
aliases:
  - "Synthetic image data augmentation for fibre layup inspection processes"
paper_key: "doi:10.1007/s10845-021-01738-7"
paper_type: research
year: 2021
venue: "Journal of Intelligent Manufacturing"
authors:
  - "Sebastian Meister"
  - "Nantwin Möller"
  - "Jan Stüve"
  - "Roger M. Groves"
status: processed
processed_at: 2026-05-20
topics:
  - synthetic image augmentation
  - automated fiber placement
  - inline inspection
  - generative adversarial networks
tasks:
  - "[[Automated fiber placement inspection]]"
  - "[[Defect classification]]"
domains:
  - "[[Aerospace and composite manufacturing]]"
  - "[[Textile and fiber inspection]]"
datasets:
  - "[[Fiber placement laser line scan images]]"
dataset_sizes:
  - "22 to 166 images per defect class"
methods:
  - "[[DCGAN]]"
  - "geometrical transformation"
  - "[[GAN-Train GAN-Test]]"
metrics:
  - "[[GAN-Train GAN-Test|GAN-Train]]"
  - "[[GAN-Train GAN-Test|GAN-Test]]"
primary_metric: "[[GAN-Train GAN-Test]]"
doi: "10.1007/s10845-021-01738-7"
arxiv: "not reported"
related_papers:
  - "[[2021 - Defect-GAN High-Fidelity Defect Synthesis for Automated Defect Inspection]]"
  - "[[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]]"
related_concepts:
  - "[[Synthetic data generation]]"
  - "[[Automated fiber placement inspection]]"
related_methods:
  - "[[GAN]]"
  - "[[DCGAN]]"
related_datasets: []
related_tasks:
  - "[[Automated fiber placement inspection]]"
  - "[[Defect classification]]"
concept_notes_created_or_updated:
  - "[[Synthetic data generation]]"
  - "[[GAN]]"
  - "[[DCGAN]]"
  - "[[Automated fiber placement inspection]]"
  - "[[Defect classification]]"
  - "[[Aerospace and composite manufacturing]]"
url: "https://doi.org/10.1007/s10845-021-01738-7"
pdf: "paper-inbox/10_processed/Research/2021 - Meister - Synthetic image data augmentation for fibre layup inspection processes.pdf"
source_file: "paper-inbox/10_processed/Research/2021 - Meister - Synthetic image data augmentation for fibre layup inspection processes.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2021 - Meister - Synthetic image data augmentation for fibre layup inspection processes.md"
extracted_text: "paper-inbox/90_processing/text/2021 - Meister - Synthetic image data augmentation for fibre layup inspection processes.txt"
artifact_status: "processed"
code: "available on request"
data: "not reported"
tags:
  - paper
  - synthetic-data
  - gan
  - fibre-placement
---

# Synthetic image data augmentation for fibre layup inspection processes

## Summary

- The paper studies synthetic image data generation for Automated Fiber Placement (AFP) inspection using small real defect image sets.
- It theoretically assesses five traditional methods and eight deep learning approaches, then investigates conditional DCGAN and geometrical transformation techniques.
- The reported conclusion is that conditional DCGAN combined with prior geometrical transformation can generate a large realistic dataset from less than 50 actual input images.

## Contribution

- Claimed: DCGAN-based augmentation can help produce realistic AFP defect images from limited laser line scan sensor data.
- Shown: Experiments use six common fiber placement inspection cases with 22 to 166 images per defect class and evaluate generated images with GAN-Train GAN-Test.
- Inferred: The method is most relevant where the defect appearance is tied to repeatable sensor geometry and defect classes such as wrinkles, twists, foreign bodies, overlaps, and gaps.

## Method

- Uses greyscale depth images from a laser line scan sensor.
- Compares augmentation families, selects DCGAN for detailed investigation, and combines it with geometrical transformations.
- Uses GAN-Train GAN-Test to assess diversity and realism of generated images without relying only on visual inspection.

## Evidence

| Evidence | Reported detail |
|---|---|
| Input data scale | 22 to 166 laser line scan sensor images per defect class |
| Target use case | Six common AFP inspection cases |
| Evaluation | GAN-Train GAN-Test plus visual image evaluation |
| Main finding | Conditional DCGAN plus geometrical transformation is described as suitable for generating a large realistic dataset from fewer than 50 actual input images |
| Acquisition setup | KUKA robot with AT C5-4090 laser line scan sensor over CFRP prepreg material |
| Original scan size | 16-bit grayscale depth images, 4096 x 500 px, representing a 250 x 150 mm sample |
| Defect crop size | 128 x 128 px grayscale depth images |
| Compute/software | Intel Xeon Gold 5122, 48 GB RAM, NVIDIA Quadro P6000, OpenCV 3.4.1, Keras 2.2.4, TensorFlow 1.13.1, Python 3.7.5 |
| Code availability | Python code available on request |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Reported values |
|---|---|---|---|---|---|
| [[GAN-Train GAN-Test]] GAN-Train | Diversity and realism of generated AFP defect images | Train CNN on generated images, evaluate on real/geometrically augmented comparison images | Higher classification rates are better, interpreted with GAN-Test | yes | First validation: >88% diagonal classification for all classes except no-defect at 78.07%; wrinkle and twist >96%; false negatives 10.82%, or 0.24% excluding gap/overlap |
| [[GAN-Train GAN-Test]] GAN-Test | Realism of generated AFP defect images | Train CNN on real/geometrically augmented images, evaluate on generated images | Higher classification rates are better, interpreted with GAN-Train | yes | First validation: all mean classification results >94% except overlap at 87.36%; false negatives 8.88%, or 1.48% excluding gap/overlap |

## Limitations

- Gap and overlap defects remain difficult because their laser line scan depth images are geometrically similar to each other and to no-defect cases.
- The GAN-Train GAN-Test protocol links realism and diversity to the chosen comparison data set, so the source warns that results must be interpreted accordingly.
- The paper did not aim to maximize CNN classification rate; it compares data synthesis methods for AFP inspection.
- A reliable real-world comparison would require extensive empirical analysis in a production environment, which was outside the study.
- Transfer to other sensor settings, materials, and optical properties remains future work.
- Python code is available on request; public code or data URLs are not reported.

## Connections

### Graph Hubs

- Tasks: [[Automated fiber placement inspection]], [[Defect classification]]
- Methods: [[Synthetic data generation]], [[GAN]], [[DCGAN]]
- Datasets: [[Fiber placement laser line scan images]]
- Domains: [[Aerospace and composite manufacturing]], [[Textile and fiber inspection]], [[Industrial visual inspection]], [[Surface defect detection]]
- Metrics: [[GAN-Train GAN-Test|GAN-Train]], [[GAN-Train GAN-Test|GAN-Test]]
- Concepts: [[Domain gap]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2021 - Defect-GAN High-Fidelity Defect Synthesis for Automated Defect Inspection]] | Shares method | Both study GAN-based synthetic defect imagery for inspection; this paper evaluates conditional DCGAN for AFP laser line scan images, while Defect-GAN adds controllable defect composition. |
| [[2022 - Procedural Synthetic Training Data Generation for AI-Based Defect Detection]] | Contrasts with | Both address scarce industrial defect data, but this paper uses DCGAN/geometric augmentation from small real image sets while Schmedemann et al. generate rendered 3D procedural scenes. |
| [[2023 - A Deep-Learning-Based Approach for Aircraft Engine Defect Detection]] | Shares method | Both use DCGAN for synthetic defect imagery in inspection domains with limited data. |

### Backlinks Updated

- [[Synthetic data generation]] links this paper as a DCGAN/geometric augmentation example.
- [[GAN]] links this paper as a GAN-based inspection augmentation example.
- [[DCGAN]] links this paper as a conditional DCGAN example.
- [[Automated fiber placement inspection]] explains this paper's domain.
- [[Defect classification]] links this paper as an augmentation/classification evaluation case.
- [[Aerospace and composite manufacturing]] stages this paper as the current composite layup inspection example.

### Concept Notes Created Or Updated

| Concept note | Action | Explanation source |
|---|---|---|
| [[Synthetic data generation]] | Created | Processed paper notes |
| [[GAN]] | Created | Processed paper notes |
| [[DCGAN]] | Created | Processed paper notes |
| [[Automated fiber placement inspection]] | Created | Processed paper note |
| [[Defect classification]] | Created | Processed paper notes |

## Questions

- Which generated defect classes were hardest to classify or synthesize?
- Are the trained weights and AFP image data available?
- How does this compare with physics-based rendering for the same AFP defects?
