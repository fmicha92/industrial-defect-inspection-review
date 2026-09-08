---
title: "Wafer Defect Pattern Labeling and Recognition Using Semi-Supervised Learning"
aliases:
  - "Wafer Defect Pattern Labeling and Recognition Using Semi-Supervised Learning"
paper_key: "doi:10.1109/tsm.2022.3159246"
paper_type: research
year: 2022
venue: "IEEE Transactions on Semiconductor Manufacturing"
authors:
  - "Katherine Shu-Min Li"
  - "Xu-Hao Jiang"
  - "Leon Li-Yang Chen"
  - "Sying-Jyan Wang"
  - "Andrew Yi-Ann Huang"
  - "Jwu E. Chen"
  - "Hsing-Chung Liang"
  - "Chun-Lung Hsu"
status: processed
processed_at: 2026-05-20
topics:
  - wafer defect labeling
  - semi-supervised learning
  - wafer map recognition
tasks:
  - "[[Wafer map defect classification]]"
domains:
  - "[[Semiconductor and electronics]]"
application_area: "Wafer-map defect pattern relabeling and recognition for semiconductor yield learning"
datasets:
  - "[[WM-811K]]"
dataset_sizes:
  - "811,457 wafer maps; roughly 20% manually labeled"
  - "Roughly 1.84% discarded because of erroneous format or missing wafer-map data"
splits:
  - "Labeled samples are reorganized by defect type so the training set is slightly larger than the test set"
modalities:
  - wafer map
methods:
  - "[[Semi-supervised learning]]"
  - "[[Bagging ensemble classifier]]"
  - "[[Self-organizing map]]"
  - "[[DBSCAN wafer-map denoising]]"
  - "[[Pseudo-labeling]]"
model_family:
  - ensemble learning
  - unsupervised clustering
architectures:
  - "Bagging ensemble with 1,000 decision trees"
  - "Self-organizing map with U-matrix clustering"
losses:
  - "not applicable"
training_regime: "Train a low-tolerance supervised ensemble on labeled wafer maps, remove questionable samples, classify unlabeled maps above a confidence threshold, cluster unresolved maps with SOM, add human-reviewed labels, and repeat until labeling stabilizes."
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
primary_metric: "[[Recall]]"
metric_definitions:
  - "Precision_i = TP_i / (TP_i + FP_i)"
  - "Recall_i = TP_i / (TP_i + FN_i)"
  - "F1_i = 2 * Precision_i * Recall_i / (Precision_i + Recall_i)"
  - "Accuracy sums TP and TN over all defect types divided by all TP, TN, FP, and FN counts"
baselines:
  - "Iteration 0 supervised model trained directly on WM-811K labels"
  - "Prior wafer-map recognition methods compared in Table IV"
benchmarks:
  - "[[WM-811K]]"
evaluation_protocol: "Run five semi-supervised iterations on WM-811K; report iteration accuracy, per-defect precision/recall/F1, unlabeled-data classification distributions, and comparisons with prior methods."
compute: "PC with Intel Core i5-8365U CPU at 1.6 GHz and 16 GB DRAM"
hardware: "Intel Core i5-8365U CPU at 1.6 GHz; 16 GB DRAM"
training_time: "Several days per iteration on the reported PC"
inference_cost: "not reported"
code: "not reported"
data: "Uses labeled and unlabeled wafer maps from WM-811K"
doi: "10.1109/TSM.2022.3159246"
url: "https://doi.org/10.1109/TSM.2022.3159246"
pdf: "paper-inbox/10_processed/Research/2022 - Li - Wafer Defect Pattern Labeling and Recognition Using Semi-Supervised Learning.pdf"
source_file: "paper-inbox/10_processed/Research/2022 - Li - Wafer Defect Pattern Labeling and Recognition Using Semi-Supervised Learning.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Li - Wafer Defect Pattern Labeling and Recognition Using Semi-Supervised Learning.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Li - Wafer Defect Pattern Labeling and Recognition Using Semi-Supervised Learning.txt"
related_papers:
  - "[[2015 - Wafer Map Failure Pattern Recognition and Similarity Ranking for Large-Scale Data Sets]]"
  - "[[2020 - A Light-Weight Neural Network for Wafer Map Classification Based on Data Augmentation]]"
related_datasets:
  - "[[WM-811K]]"
related_domains:
  - "[[Semiconductor and electronics]]"
related_tasks:
  - "[[Wafer map defect classification]]"
related_methods:
  - "[[Semi-supervised learning]]"
  - "[[Bagging ensemble classifier]]"
  - "[[Self-organizing map]]"
  - "[[DBSCAN wafer-map denoising]]"
  - "[[Pseudo-labeling]]"
related_benchmarks:
  - "[[WM-811K]]"
tags:
  - paper
  - wafer-map
  - semi-supervised-learning
---
# Wafer Defect Pattern Labeling and Recognition Using Semi-Supervised Learning

## Summary

- Li et al. propose a semi-supervised workflow for mislabeled and undefined wafer defect patterns in [[WM-811K]].
- The workflow trains a low-tolerance ensemble model from labeled wafer maps, excludes questionable samples, pseudo-labels confident unlabeled samples, and clusters remaining samples to identify additional wafer-map defect types.
- After five iterations, the method defines five new defect pattern types and reports 14 total defect types recognized with 94.37% overall accuracy.

## Paper Type

- Type: research.
- Why: The paper proposes and evaluates a semi-supervised wafer-map relabeling and recognition method on a public semiconductor manufacturing dataset.

## Problem

- Task: [[Wafer map defect classification]].
- Setting: Semiconductor wafer maps provide spatial failed-die patterns for root-cause analysis and yield learning.
- Inputs: Labeled and unlabeled wafer maps from [[WM-811K]].
- Outputs: Existing and newly identified wafer-map defect pattern labels.
- Motivation: Manual engineer labels can be inconsistent, some wafer maps contain multiple patterns, and rare or undefined patterns are not recognized by ordinary supervised classifiers.
- Label-quality issues shown in the paper: visually similar maps can receive different labels, scratch-like maps can be mislabeled as Donut, and mixed patterns such as Center+Edge-ring or Edge-ring+Scratch are forced into a single existing class.

## Contribution

- Claimed: Semi-supervised learning can improve wafer-map label quality while requiring limited human review.
- Claimed: Unresolved wafer maps should be clustered to identify previously undefined defect types rather than forced into predefined classes.
- Shown: Five new labels are defined: Half-random, Center+Edge-local, Center+Local, Edge-ring+Local, and Normal.
- Shown: The process recognizes 14 defect types with 94.37% overall accuracy after five iterations.

## Method

- Phase I preprocessing:
  - Filters out roughly 1.84% of wafer maps because of erroneous format or missing data.
  - Applies [[DBSCAN wafer-map denoising]] to remove randomly distributed defects before extracting clean spatial patterns.
  - Standardizes wafer maps into four sizes: 32 x 32, 64 x 64, 128 x 128, and 256 x 256.
- Phase II feature extraction:
  - Extracts connected-component geometry, including component counts, distances to wafer center and edge, area, eccentricity, and solidity for the two largest components.
  - Extracts statistical features, including whole-wafer defect ratio, component size ratios, Hu image moments, and defect density / defect clustering over edge, local, and center circular areas.
  - Extracts Radon-transform features using maximum, mean, and standard deviation across row vectors.
- Phase III supervised model:
  - Uses [[Bagging ensemble classifier]] with 1,000 decision trees.
  - Each tree trains on a random 80% sample of training data.
  - Classification confidence is the fraction of trees voting for a defect type.
  - Repeats model construction 10 times to screen mislabeled data and build a low-tolerance classifier.
  - Sets each class threshold to mean probability minus three standard deviations.
- Phase IV unlabeled-data classification:
  - Applies the supervised model to unlabeled wafer maps.
  - Accepts a predicted label only when confidence exceeds the class threshold; otherwise the sample becomes an error wafer.
- Phase V unsupervised clustering:
  - Uses [[Self-organizing map]] to cluster unresolved wafer maps.
  - Applies median wall finding and image closing to make U-matrix cluster boundaries clearer.
  - Uses connected-component analysis to label separated SOM regions.
- Phase VI enhanced labeling:
  - Human review assigns SOM clusters to existing labels or creates new defect labels.
  - The enhanced labels are combined with confident classified wafers and used in the next iteration.

## Evidence

### Experimental Setup

| Item | Reported detail |
|---|---|
| Dataset | [[WM-811K]] |
| Total wafer maps | 811,457 |
| Manually labeled share | roughly 20% |
| Imbalance | 85.2% of wafers belong to None |
| Rare original classes | Donut 0.3%, Near-full 0.1%, Random 0.5%, Scratch 0.7% |
| Removed records | roughly 1.84% because of erroneous format or missing data |
| Supervised model | Bagging with 1,000 decision trees |
| Per-tree sample | random 80% of training data |
| Iterations | five semi-supervised iterations |
| Hardware | Intel Core i5-8365U CPU at 1.6 GHz and 16 GB DRAM |

### Main Results

| Result | Dataset / task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Iteration 0 supervised model | [[WM-811K]] / wafer-map classification | [[Accuracy]] | higher | not applicable | 97.68% | Misleading because None dominates and four real defect recalls are below 80% |
| Iteration 1 after supervised filtering | [[WM-811K]] / wafer-map classification | [[Accuracy]] | higher | 97.68% | 98.47% | Improves recall for real defect patterns |
| Iteration 2 after adding new labels | [[WM-811K]] / wafer-map classification | [[Accuracy]] | higher | 98.47% | 93.82% | Drop attributed to new labels and lower None share |
| Final iteration | [[WM-811K]] / wafer-map classification | [[Accuracy]] | higher | 97.68% | 94.37% | 14 defect types after five iterations |
| New label discovery | [[WM-811K]] / enhanced labeling | New classes | not applicable | 9 original classes | 5 new classes | Half-random, Center+Edge-local, Center+Local, Edge-ring+Local, Normal |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Precision]] | Per-defect recognition | TP / (TP + FP) | higher | no | Reported for each defect type |
| [[Recall]] | Per-defect recognition | TP / (TP + FN) | higher | yes | The paper emphasizes recall because high overall accuracy hides weak real-defect recognition |
| [[F1-score]] | Per-defect recognition | Harmonic mean of precision and recall | higher | no | Half-random and Edge-ring+Local have F1 below 85% because sample counts are small |
| [[Accuracy]] | Overall recognition | Sum of correct counts over all defect types | higher | no | Accuracy is skewed by the dominant None class |

### Detailed Findings

- The original nine WM-811K labels are Center, Donut, Edge-local, Edge-ring, Local, Near-full, Random, Scratch, and None.
- The method adds Center+Edge-local, Center+Local, and Normal after Iteration 1.
- The method adds Half-random and Edge-ring+Local after Iteration 4.
- After Iteration 5, the prediction model classifies unlabeled data with a lower None share than the Iteration 1 model, suggesting that the original nine classes are not sufficient for all visible patterns.
- Compared with prior methods, the proposed method reports comparable recall values without using class-balanced augmented data; the paper notes that one prior deep CNN method uses augmented data to balance defect types.

## ML / DL Extraction

### Task Formulation

- Input modality: wafer map.
- Output target: wafer-map defect pattern type.
- Supervision: semi-supervised; combines initially labeled wafer maps, confident model-assigned labels, and human-reviewed SOM clusters.
- Objective: improve label quality and recognition for known and undefined wafer-map defect types.

### Model And Training

- Model family: ensemble learning plus unsupervised clustering.
- Architecture: 1,000-tree Bagging classifier; SOM for unresolved samples.
- Parameters: per-tree training uses random 80% of all training data.
- Thresholding: class-specific confidence threshold is mean probability minus three standard deviations.
- Training compute: several days per iteration on a PC with Intel Core i5-8365U CPU at 1.6 GHz and 16 GB DRAM.
- Random seeds: not reported.
- Software: MiniSom is reported for SOM; full software environment is not reported.

### Data

- Dataset: [[WM-811K]].
- Size: 811,457 wafer maps.
- Labels: roughly 20% manually labeled.
- Known original classes: Center, Donut, Edge-local, Edge-ring, Local, Near-full, Random, Scratch, and None.
- New labels: Half-random, Center+Edge-local, Center+Local, Edge-ring+Local, and Normal.
- Preprocessing: filtering, DBSCAN denoising, and size standardization.
- Leakage checks: not reported.
- License: not reported in the paper.

### Evaluation

- Protocol: compare Iteration 0 with five semi-supervised iterations and report class-wise metrics.
- Used performance metrics: [[Precision]], [[Recall]], [[F1-score]], and [[Accuracy]].
- Primary metric: [[Recall]], because the source stresses that high accuracy can be misleading under the None-heavy class distribution.
- Baselines: direct supervised model on original labels and prior wafer-map recognition methods.
- Statistical tests: not reported.

## Limitations

- The process is not fully automated because SOM-derived groups need human labeling.
- Phase III is time-consuming because the workflow runs 10 Bagging rounds and each uses 1,000 decision trees.
- A complete iteration takes several days on the reported PC.
- Half-random and Edge-ring+Local have weak precision and F1 because sample counts are small.
- The source does not report code release, random seeds, full software versions, or inference cost.

## Reproducibility

- Code: not reported.
- Data: [[WM-811K]] is used.
- Hyperparameters: 1,000 decision trees, 80% random sampling per tree, 10 supervised screening repeats, and class threshold mean minus three standard deviations.
- Environment: MiniSom is reported for SOM; complete environment is not reported.
- Hardware: Intel Core i5-8365U CPU at 1.6 GHz and 16 GB DRAM.
- Artifact status: not reported.

## Connections

### Graph Hubs

- Tasks: [[Wafer map defect classification]]
- Datasets: [[WM-811K]]
- Domains: [[Semiconductor and electronics]]
- Methods: [[Semi-supervised learning]], [[Bagging ensemble classifier]], [[Self-organizing map]], [[DBSCAN wafer-map denoising]], [[Pseudo-labeling]]
- Metrics: [[Accuracy]], [[Precision]], [[Recall]], [[F1-score]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2015 - Wafer Map Failure Pattern Recognition and Similarity Ranking for Large-Scale Data Sets]] | Dataset source | Introduces [[WM-811K]], which this paper relabels and reclassifies. |
| [[2020 - A Light-Weight Neural Network for Wafer Map Classification Based on Data Augmentation]] | Shares dataset | Both use [[WM-811K]] and discuss class imbalance, but this paper focuses on relabeling and undefined patterns. |

### Backlinks Updated

- [[WM-811K]] already links this paper as a semi-supervised labeling study.
- [[Wafer map defect classification]] already links this paper as a task example.
- [[Semiconductor and electronics]] already links the wafer-map dataset and related task.
- [[Bagging ensemble classifier]], [[Self-organizing map]], [[DBSCAN wafer-map denoising]], and [[Pseudo-labeling]] link this paper as a source case.

## Questions

- Could a smaller Bagging ensemble preserve the low-tolerance screening behavior while reducing iteration time?
- Are the five added pattern labels stable under independent engineer review?
- Would modern representation learning reduce the manual cluster-labeling step?
