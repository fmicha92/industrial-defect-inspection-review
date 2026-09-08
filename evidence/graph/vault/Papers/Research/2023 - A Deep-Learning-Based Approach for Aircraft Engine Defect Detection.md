---
title: "A Deep-Learning-Based Approach for Aircraft Engine Defect Detection"
aliases:
  - "Aircraft Engine Defect Detection"
paper_key: "sha256:798ee3633148b26064ead03f6245f8a44cbae5d092e78ca32e828d0dd11a2755"
paper_type: research
year: 2023
venue: "Machines"
authors:
  - "Anurag Upadhyay"
  - "Jun Li"
  - "Steve King"
  - "Sri Addepalli"
status: processed
processed_at: 2026-05-20
topics:
  - borescope inspection
  - aircraft engine defect detection
  - image segmentation
  - motion deblurring
tasks:
  - "[[Defect segmentation]]"
domains:
  - "[[Aircraft maintenance]]"
datasets:
  - "[[Compressor blade borescope images]]"
methods:
  - "[[U-Net]]"
  - "[[DCGAN]]"
  - "[[Pix2Pix]]"
  - "motion deblurring"
  - "computer vision preprocessing"
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
primary_metric: "[[Precision]]"
data: "publicly available borescope inspection video frames analyzed"
doi: "10.3390/machines11020192"
arxiv: "not reported"
related_papers:
  - "[[2021 - Defect-GAN High-Fidelity Defect Synthesis for Automated Defect Inspection]]"
  - "[[2021 - Synthetic Image Data Augmentation for Fibre Layup Inspection Processes]]"
  - "[[2021 - Defect Detection in CT Scans of Cast Aluminum Parts]]"
related_concepts:
  - "[[Synthetic data generation]]"
  - "[[Defect segmentation]]"
  - "[[Industrial visual inspection]]"
  - "[[Transfer learning]]"
related_methods:
  - "[[U-Net]]"
  - "[[GAN]]"
  - "[[DCGAN]]"
  - "[[Pix2Pix]]"
related_datasets:
  - "[[Compressor blade borescope images]]"
related_tasks:
  - "[[Defect segmentation]]"
concept_notes_created_or_updated:
  - "[[U-Net]]"
  - "[[DCGAN]]"
  - "[[GAN]]"
  - "[[Defect segmentation]]"
  - "[[Industrial visual inspection]]"
  - "[[Pix2Pix]]"
  - "[[Aircraft maintenance]]"
url: "https://doi.org/10.3390/machines11020192"
pdf: "paper-inbox/10_processed/Research/2023 - Upadhyay - A Deep-Learning-Based Approach for Aircraft Engine Defect Detection.pdf"
source_file: "paper-inbox/10_processed/Research/2023 - Upadhyay - A Deep-Learning-Based Approach for Aircraft Engine Defect Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Upadhyay - A Deep-Learning-Based Approach for Aircraft Engine Defect Detection.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Upadhyay - A Deep-Learning-Based Approach for Aircraft Engine Defect Detection.txt"
artifact_status: "public datasets reported"
tags:
  - paper
  - aircraft-maintenance
  - segmentation
  - gan
---

# A Deep-Learning-Based Approach for Aircraft Engine Defect Detection

## Summary

- The paper proposes a deep learning framework for automated borescope inspection of aircraft engine high-pressure compressor blades.
- It combines image acquisition, preprocessing, motion deblurring, synthetic image generation, and customized U-Net segmentation.
- The abstract reports precision and recall above 90%, a 10x image-quality improvement from the hybrid deblurring model, and limited success on very small defects.

## Contribution

- Claimed: A customized U-Net plus preprocessing and GAN-based synthetic image generation can support automated aircraft engine defect detection.
- Shown: Binary cross-entropy training at 300 epochs reports validation precision 0.949 and validation recall 0.939. The paper reports over 90% precision and recall overall.
- Inferred: Loss selection is a core practical concern because defect size imbalance affects segmentation behavior.

## Method

- Extracts blade images from borescope inspection video.
- Uses a customized DCGAN for synthetic image generation.
- Uses a hybrid deblurring approach combining computer vision and Pix2Pix GAN.
- Trains a customized U-Net using binary cross-entropy, focal loss, Jaccard loss, and focal Tversky loss.

## Evidence

| Experiment | Metric | Reported result |
|---|---|---|
| BCE U-Net, 300 epochs | validation accuracy | 0.995 |
| BCE U-Net, 300 epochs | validation precision | 0.949 |
| BCE U-Net, 300 epochs | validation recall | 0.939 |
| Focal-loss U-Net, 300 epochs | validation precision / recall | 0.965 / 0.922 |
| Focal Tversky U-Net, 300 epochs | validation coefficient | 0.944 |
| Hybrid deblurring | image quality | 10x improvement reported in abstract |
| Random forest feature engineering comparison | average precision | 0.76 |
| Transfer-learning feature comparison | average precision | 0.69 |

## Performance Metrics

The paper uses [[Accuracy]], [[Precision]], and [[Recall]] as key U-Net segmentation indicators, but warns that accuracy alone is unreliable because the image masks are highly imbalanced. With binary cross-entropy loss at 300 epochs, the customized U-Net reports validation accuracy 0.995, validation precision 0.949, and validation recall 0.939. With focal loss at 300 epochs, it reports validation precision 0.965 and validation recall 0.922.

For overlap-oriented losses, the paper reports validation Jaccard coefficient 0.8892 and validation focal Tversky coefficient 0.944 at 300 epochs. It also reports average precision 0.76 for a random-forest segmentation baseline using manually engineered image-filter features and 0.69 for a VGG16-transfer-feature plus random-forest baseline.

## Limitations

- The framework has modest success on very small defects.
- Models tend to overfit beyond 300 epochs due to limited training data.
- GAN synthetic data generation is described as limited by mode collapse, artifact generation, and training instability.

## Connections

### Graph Hubs

- Tasks: [[Defect segmentation]]
- Methods: [[U-Net]], [[GAN]], [[DCGAN]], [[Pix2Pix]], [[Synthetic data generation]]
- Datasets: [[Compressor blade borescope images]]
- Domains: [[Aircraft maintenance]], [[Industrial visual inspection]]
- Metrics: [[Accuracy]], [[Precision]], [[Recall]]
- Concepts: [[Domain gap]], [[Transfer learning]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2021 - Defect-GAN High-Fidelity Defect Synthesis for Automated Defect Inspection]] | Shares method | Both use GAN-based synthetic defect generation; this paper adds aircraft borescope deblurring and U-Net segmentation. |
| [[2021 - Synthetic Image Data Augmentation for Fibre Layup Inspection Processes]] | Shares method | Both use DCGAN in limited-data inspection settings, but for different sensor/domain contexts. |
| [[2021 - Defect Detection in CT Scans of Cast Aluminum Parts]] | Shares task | Both use U-Net-style segmentation for defect localization, but one uses aircraft borescope images and the other CT volumes. |

### Backlinks Updated

- [[U-Net]] links this paper as a customized U-Net segmentation example.
- [[GAN]] links this paper for DCGAN and Pix2Pix GAN usage.
- [[DCGAN]] links this paper as a synthetic aircraft engine defect image example.
- [[Pix2Pix]] links this paper as the GAN-based deblurring example.
- [[Defect segmentation]] links this paper as an aircraft engine segmentation case.
- [[Industrial visual inspection]] links this paper as a borescope inspection use case.

### Concept Notes Created Or Updated

| Concept note | Action | Explanation source |
|---|---|---|
| [[U-Net]] | Created | Processed paper notes |
| [[GAN]] | Created | Processed paper notes |
| [[DCGAN]] | Created | Processed paper notes |
| [[Pix2Pix]] | Created | Processed paper note |
| [[Defect segmentation]] | Created | Processed paper notes |
| [[Industrial visual inspection]] | Created | Processed paper notes |

## Questions

- How large is the final labeled blade image dataset?
- Are the labels and trained models available?
- Which loss function gives the best small-defect recall after full tuning?
