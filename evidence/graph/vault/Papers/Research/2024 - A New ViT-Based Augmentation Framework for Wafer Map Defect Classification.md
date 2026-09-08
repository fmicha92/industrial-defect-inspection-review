---
title: "A New ViT-Based Augmentation Framework for Wafer Map Defect Classification to Enhance the Resilience of Semiconductor Supply Chains"
aliases:
  - "A New ViT-Based Augmentation Framework for Wafer Map Defect Classification"
paper_key: "sha256:0f55657846757fd4057351ab1990c8c61157c83e40c2554b3b876084db89228e"
paper_type: research
year: 2024
venue: "International Journal of Production Economics"
authors:
  - "Shu-Kai S. Fan"
  - "Shang-Hao Chiu"
status: processed
processed_at: 2026-05-23
audited_at: 2026-06-11
topics:
  - "wafer map defect classification"
  - "ViT augmentation"
  - "semiconductor inspection"
  - "class imbalance"
tasks:
  - "[[Wafer map defect classification]]"
  - "[[Defect classification]]"
domains:
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[WM-811K]]"
methods:
  - "[[ViT-based wafer map augmentation]]"
  - "[[Vision Transformer]]"
  - "[[Data augmentation]]"
  - "[[CycleGAN]]"
architectures:
  - "[[Vision Transformer]]"
  - "[[VGG-16]]"
metrics:
  - "[[Accuracy]]"
  - "[[Recall]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  - "Accuracy: overall wafer-pattern classification accuracy; higher is better"
  - "Recall: class-specific recall for wafer defect patterns; higher is better"
baselines:
  - "VGG16 without augmentation"
  - "CycleGAN augmentation"
benchmarks:
  - "[[WM-811K]]"
code: "not reported"
data: "[[WM-811K]]"
doi: "10.1016/j.ijpe.2024.109275"
arxiv: "not reported"
url: "https://doi.org/10.1016/j.ijpe.2024.109275"
pdf: "paper-inbox/10_processed/Research/2024 - Fan - A New ViT-Based Augmentation Framework for Wafer Map Defect Classification to Enhance the Resilience of Semiconductor Supply Chains.pdf"
related_concepts:
  - "[[Class imbalance]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[ViT-based wafer map augmentation]]"
  - "[[Vision Transformer]]"
  - "[[Data augmentation]]"
  - "[[CycleGAN]]"
related_datasets:
  - "[[WM-811K]]"
related_tasks:
  - "[[Wafer map defect classification]]"
  - "[[Defect classification]]"
source_file: "paper-inbox/10_processed/Research/2024 - Fan - A New ViT-Based Augmentation Framework for Wafer Map Defect Classification to Enhance the Resilience of Semiconductor Supply Chains.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2024 - Fan - A New ViT-Based Augmentation Framework for Wafer Map Defect Classification to Enhance the Resilience of Semiconductor Supply Chains.md"
extracted_text: "paper-inbox/90_processing/text/2024 - Fan - A New ViT-Based Augmentation Framework for Wafer Map Defect Classification to Enhance the Resilience of Semiconductor Supply Chains.txt"
artifact_status: "code not reported; public WM-811K dataset used"
tags:
  - paper
---
# A New ViT-Based Augmentation Framework for Wafer Map Defect Classification to Enhance the Resilience of Semiconductor Supply Chains

## Summary

The paper proposes a [[Vision Transformer]]-based wafer-map augmentation method for imbalanced [[Wafer map defect classification]]. Instead of using ViT only as a classifier, the method converts multi-head self-attention matrices into heatmap-like generated wafer maps, adds those generated samples to the training set, and evaluates whether a VGG16 classifier improves on [[WM-811K]]. The strongest reported comparisons show ViT augmentation outperforming CycleGAN at equalized class training sizes and improving minority-class recall for Donut and Scratch.

## Paper Type

- Type: research.
- Why: The paper proposes an augmentation method and evaluates it experimentally against VGG16 and CycleGAN baselines.

## Problem

- Task: [[Wafer map defect classification]].
- Setting: semiconductor front-end wafer-map inspection with severe class imbalance.
- Motivation: WM-811K has many unlabeled maps and a dominant None class; minority defect classes such as Near-full and Scratch have few labeled examples, making classifier accuracy misleading and minority recall weak.
- Practical framing: the paper links better wafer defect recognition to yield improvement, resource use, and semiconductor supply-chain resilience.

## Contribution

- Claimed: ViT attention matrices can be repurposed as a data augmentation source for wafer defect maps.
- Claimed: row-averaged attention scores from each head can form heatmap-like generated wafer maps.
- Shown: ViT augmentation improves VGG16 classification for selected minority classes and outperforms CycleGAN under equalized training-size strategies.

## Method

- Input resizing: WM-811K wafer maps have 632 image sizes ranging from 6 x 21 to 300 x 202 pixels; experiments resize wafer maps to 75 x 75 by nearest-neighbor interpolation.
- ViT setup: wafer maps are split into patches; the best initial ViT classification setting uses 6 x 6 patches and 4 heads, with average accuracy 91.51%.
- Attention heatmap generation: the trained ViT produces an attention matrix per head; row averages over attention scores are rearranged into a square heatmap that serves as generated wafer-map data.
- Augmentation loop: train ViT, extract attention matrices, create heatmaps per head, resize heatmaps if needed, combine generated samples with original training data, and train a CNN classifier.
- Classifier: VGG16 is used to assess augmentation performance; the paper reports VGG16 average accuracy 93.56% in the preliminary comparison and 97.45% in a later broader model comparison.
- Baseline generator: CycleGAN is used as the main generative augmentation comparison.

## ML / DL Extraction

### Data

- Dataset: [[WM-811K]], 811,457 real wafer maps from 46,393 wafer lots.
- Labeled maps: 172,950 manually annotated maps.
- Defect-pattern maps used for the main experiments: 25,519 labeled maps excluding the dominant None class.
- Unlabeled maps: 638,507.
- None class: 147,432 maps; excluded from the main augmentation experiments because it dominates the labeled data and is visually confounded with Random.

### Class Counts Used

| Class | Count | Percent |
|---|---:|---:|
| Center | 4,294 | 16.83% |
| Donut | 555 | 2.17% |
| Edge-Loc | 5,189 | 20.33% |
| Edge-Ring | 9,680 | 37.93% |
| Loc | 3,593 | 14.08% |
| Near-full | 149 | 0.58% |
| Random | 866 | 3.39% |
| Scratch | 1,193 | 4.67% |
| Total | 25,519 | 100% |

### Splits

- Split: 60% training, 15% validation, and 25% testing for each class.
- Training / validation / testing totals: 15,313 / 3,827 / 6,379.
- Main hardware: Intel i7-8700 CPU and NVIDIA RTX2080 GPU.

### Augmentation Strategies

- Strategy A: augment Donut, Near-full, Random, and Scratch simultaneously using 4 heads.
- Strategies B1-B3: augment Donut individually using 2, 4, and 8 heads.
- Strategies C1-C3: augment Scratch individually using 2, 4, and 8 heads.
- Strategies D1-D4: compare ViT and CycleGAN when all classes are adjusted to equal training sizes of 1,000, 1,500, 3,000, and 5,000.

## Evidence

### Main WM-811K Results

| Strategy | Target / setting | Best reported measure | Benchmark | Improvement |
|---|---|---:|---:|---:|
| A | four minority classes, 4 heads | 93.77% accuracy | 93.56% VGG16 | +0.21 |
| B1 | Donut, 2 heads | 86.69% recall | 83.45% | +3.24 |
| B2 | Donut, 4 heads | 89.35% recall | 83.45% | +5.90 |
| B3 | Donut, 8 heads | 86.33% recall | 83.45% | +2.88 |
| C1 | Scratch, 2 heads | 81.14% recall | 80.33% | +0.81 |
| C2 | Scratch, 4 heads | 83.89% recall | 80.33% | +3.56 |
| C3 | Scratch, 8 heads | 86.21% recall | 80.33% | +5.88 |
| D1 | equal class training size 1,000 | 89.53% accuracy | 84.28% CycleGAN | +5.25 |
| D2 | equal class training size 1,500 | 91.70% accuracy | 90.56% CycleGAN | +1.14 |
| D3 | equal class training size 3,000 | 93.91% accuracy | 91.74% CycleGAN | +2.17 |
| D4 | equal class training size 5,000 | 93.88% accuracy | 93.02% CycleGAN | +0.86 |

### Additional Validation

- The paper also revisits CIFAR-10 and MixedWM38 to validate the augmentation model.
- MixedWM38 validation uses seven single defect patterns, excluding Random because it has only 149 samples; the source says results are in appendices and detailed reports are available upon request.

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Accuracy]] | overall wafer-map classification | percent correct | higher | yes | reported for VGG16, ViT, CycleGAN, and augmentation strategies |
| [[Recall]] | per-class defect recognition | percent of a class correctly retrieved | higher | yes | emphasized for Donut and Scratch minority classes |

## Dataset / Benchmark Details

- WM-811K classes considered: Center, Donut, Edge-Loc, Edge-Ring, Loc, Near-full, Random, Scratch.
- Color bands: 0 means no wafer grain, 1 means non-defect grains, and 2 means defect grains.
- Leakage checks: not reported.
- License: not reported in the paper source.

## Limitations

- The None class is excluded from main experiments, so the reported augmentation results do not cover the dominant real labeled class.
- Random is described as hard to distinguish from None by human visual inspection and often coexisting with None-like patterns.
- Some detailed computational reports and full comparison results are stated as available upon request rather than fully printed.
- The source states that assessing the existing domain-expert annotation quality in WM-811K is future work.

## Reproducibility

- Code: not reported.
- Dataset: [[WM-811K]].
- Hardware: Intel i7-8700 CPU and NVIDIA RTX2080 GPU.
- Split: 60/15/25 train/validation/test by class.
- Random seeds: not reported.

## Connections

### Graph Hubs

- Tasks: [[Wafer map defect classification]], [[Defect classification]]
- Datasets: [[WM-811K]]
- Domains: [[Semiconductor and electronics]]
- Methods: [[ViT-based wafer map augmentation]], [[Vision Transformer]], [[Data augmentation]], [[CycleGAN]]
- Model used for evaluation: [[VGG-16]]
- Metrics: [[Accuracy]], [[Recall]]
- Concept: [[Class imbalance]]

### Relationship Notes

- Shares dataset: [[WM-811K]].
- Shares method: [[ViT-based wafer map augmentation]] and [[Data augmentation]].
- Contrasts with: [[CycleGAN]] as the benchmark augmentation generator.
- Application/domain: [[Semiconductor and electronics]].

## Questions

- How would the augmentation perform if None and Random were both retained in a production-like class distribution?
- Can the ViT attention-heatmap generator be validated against annotation quality issues in WM-811K?
- What are the exact appendix results on CIFAR-10 and MixedWM38?
