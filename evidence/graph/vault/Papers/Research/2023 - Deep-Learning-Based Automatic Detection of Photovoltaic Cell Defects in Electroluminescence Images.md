---
title: "Deep-Learning-Based Automatic Detection of Photovoltaic Cell Defects in Electroluminescence Images"
aliases:
  - "Deep-Learning-Based Automatic Detection of Photovoltaic Cell Defects in Electroluminescence Images"
paper_key: "sha256:b565a46ef5a7a31284192bff7914db52cf128258853ad561312eb8f74488c300"
paper_type: research
year: 2023
venue: "Sensors"
authors:
  - "Junjie Wang"
  - "Li Bi"
  - "Pengxiang Sun"
  - "Xiaogang Jiao"
  - "Xunde Ma"
  - "Xinyi Lei"
  - "Yongbin Luo"
status: processed
processed_at: 2026-05-22
topics:
  - "photovoltaic cell defects"
  - "electroluminescence images"
  - "feature fusion"
tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect classification]]"
domains:
  - "[[Solar cells and photovoltaic]]"
datasets:
  - "[[ELPV Dataset]]"
  - "[[PVEL-AD]]"
dataset_sizes:
  - "Dataset 1 selected subset: 2,223 ELPV images with 0% or 100% defect labels"
  - "Dataset 2: 5,991 PV EL images across ten classes"
splits:
  - "80/20 train/test split with stratified sampling"
methods:
  - "[[Data augmentation]]"
  - "[[Coordinate attention]]"
  - "class weighting"
model_family:
  - "[[Deep convolutional neural network]]"
architectures:
  - "ResNet152-Xception feature-fusion model"
  - "[[Xception]]"
losses:
  - "not reported"
optimizers:
  - "[[Adam]]"
training_regime:
  - "supervised classification"
augmentation:
  - "[[Data augmentation]]"
metrics:
  - "[[Accuracy]]"
  - "[[F1-score]]"
  - "[[Recall]]"
  - "[[Precision]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  - "Accuracy, recall, precision, and F1-score are defined from TP, TN, FP, and FN; higher is better."
baselines:
  - "CNN"
  - "VGG16"
  - "MobileNetV2"
  - "InceptionV3"
  - "DenseNet121"
  - "ResNet152"
  - "[[Xception]]"
  - "InceptionResNetV2"
benchmarks:
  - "[[ELPV Dataset]]"
  - "[[PVEL-AD]]"
code: "https://github.com/Zayn-Wang/Photovoltaic-cell-surface-defect-detection"
data: "Dataset 1: https://github.com/zae-bayern/elpv-dataset; Dataset 2: http://aihebut.com/col.jsp?id=118"
doi: "10.3390/s23010297"
arxiv: "not applicable"
url: "https://doi.org/10.3390/s23010297"
pdf: "paper-inbox/10_processed/Research/2023 - Wang - Deep-Learning-Based Automatic Detection of Photovoltaic Cell Defects in Electroluminescence Images.pdf"
related_concepts:
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[Data augmentation]]"
  - "[[Coordinate attention]]"
  - "[[Adam]]"
  - "[[Xception]]"
related_datasets:
  - "[[ELPV Dataset]]"
  - "[[PVEL-AD]]"
related_domains:
  - "[[Solar cells and photovoltaic]]"
related_tasks:
  - "[[Solar cell defect detection]]"
  - "[[Defect classification]]"
related_benchmarks:
  - "[[PVEL-AD benchmark]]"
source_file: "paper-inbox/10_processed/Research/2023 - Wang - Deep-Learning-Based Automatic Detection of Photovoltaic Cell Defects in Electroluminescence Images.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Wang - Deep-Learning-Based Automatic Detection of Photovoltaic Cell Defects in Electroluminescence Images.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Wang - Deep-Learning-Based Automatic Detection of Photovoltaic Cell Defects in Electroluminescence Images.txt"
artifact_status: "paper reports public datasets and code availability"
tags:
  - paper
---
# Deep-Learning-Based Automatic Detection of Photovoltaic Cell Defects in Electroluminescence Images

## Summary

Wang et al. propose a supervised deep-learning classifier for photovoltaic cell defect detection in electroluminescence images. The model combines ResNet152 and Xception features, applies hybrid pooling and global average pooling for feature fusion, adds [[Coordinate attention]], and uses data augmentation plus class weighting to handle small, imbalanced PV defect datasets.

The paper evaluates binary defect/no-defect classification on selected [[ELPV Dataset]] images and ten-class PV defect classification on the paper's Dataset 2, which corresponds to the public PVEL-style photovoltaic EL anomaly data linked from `aihebut.com`. The reported best accuracy is 96.17% for binary classification and 92.13% for multiclass defect classification.

## Paper Type

- Type: research.
- Why: the paper proposes a deep-learning model and evaluates it against CNN and transfer-learning baselines on public PV electroluminescence defect datasets.

## Problem

- Task: [[Solar cell defect detection]] and [[Defect classification]].
- Setting: electroluminescence inspection of photovoltaic cells for manufacturing and operational quality assurance.
- Inputs: grayscale EL images of PV cells.
- Outputs: binary defect/no-defect labels for Dataset 1 and ten class labels for Dataset 2.
- Motivation: PV cell defects such as cracks, thick lines, fragments, black cores, horizontal dislocation, short circuits, and other surface anomalies reduce conversion efficiency, service life, and operational safety.
- Key difficulty: scarce defect samples and strong class imbalance make ordinary deep-learning classifiers prone to weak minority-class performance.

## Contribution

- Claimed: data augmentation and class weighting mitigate small-data and imbalance effects in PV EL defect classification.
- Claimed: ResNet152-Xception feature fusion with hybrid pooling improves feature extraction compared with single backbones.
- Claimed: adding [[Coordinate attention]] improves classification accuracy.
- Shown: the final model reports 96.17% binary accuracy on Dataset 1 and 92.13% multiclass accuracy on Dataset 2, outperforming CNN, VGG16, MobileNetV2, InceptionV3, DenseNet121, ResNet152, Xception, and InceptionResNetV2 under the paper's training settings.

## Method

- Core idea: fuse complementary ResNet152 and Xception features for PV EL image classification, then strengthen the fused representation with coordinate attention.
- Feature fusion: ResNet and Xception outputs are passed through mixed pooling, concatenated along the spatial dimension, and globally averaged.
- Hybrid pooling: a random coefficient chooses maximum pooling or average pooling for a rectangular region during training.
- Attention: [[Coordinate attention]] is embedded into feature maps to strengthen feature extraction.
- Imbalance handling: class weights are assigned inversely to per-class sample counts.
- Augmentation: row-row swapping, random vertical flipping, random horizontal flipping, Gaussian blur, motion blur, center blur, brightness enhancement, contrast enhancement, and saturation enhancement.
- Excluded augmentation: random cropping and panning are not used because they can remove key regions needed for model judgment.

## ML / DL Extraction

### Task Formulation

- Input modality: 300 x 300 8-bit grayscale EL images for Dataset 1; high-resolution EL images for Dataset 2.
- Output target: binary classification for selected ELPV labels and multiclass classification across ten Dataset 2 classes.
- Supervision: supervised classification from expert labels or class labels in the public datasets.
- Objective: classification; loss function not explicitly reported in the preprocessed source.

### Model And Training

- Model family: [[Deep convolutional neural network]].
- Architecture: ResNet152-Xception feature-fusion model with mixed pooling, global average pooling, and coordinate attention.
- Baselines: CNN, VGG16, MobileNetV2, InceptionV3, DenseNet121, ResNet152, Xception, and InceptionResNetV2.
- Optimizer: [[Adam]].
- Batch size: 16.
- Initial learning rate: 0.01.
- Minimum learning rate: 0.0001.
- Maximum iterations: 2000.
- Regularization: L2 regularization.
- Learning-rate schedule: warm-up using one-dimensional linear interpolation followed by cosine annealing.
- Hardware/software: Ubuntu, Intel i5-6600 CPU, 16 GB RAM, Nvidia RTX2080 GPU, Python, TensorFlow.
- Parameters, seeds, and trained checkpoints: not reported.

### Data

- Dataset 1: [[ELPV Dataset]], originally 2,624 PV cell images from 44 PV modules, with 18 monocrystalline and 26 polycrystalline modules. The paper uses only the 0% and 100% labels for binary classification.
- Dataset 1 selected subset: 2,223 images; 1,508 normal and 715 defective.
- Dataset 1 split: 1,779 training images and 444 test images. The split table reports monocrystalline 470/251 train and 118/62 test for 0%/100%; polycrystalline 737/321 train and 183/81 test for 0%/100%.
- Dataset 2: high-resolution PV cell defect images from actual industrial manufacturing, jointly released by Hebei University of Technology and Beihang University; linked by the paper at `http://aihebut.com/col.jsp?id=118`.
- Dataset 2 classes: black_core, crack, finger, horizontal_dislocation, vertical_dislocation, short_circuit, star_crack, think_line, multiple defects, and free_defects.
- Dataset 2 total: 5,991 images, split into 4,797 training images and 1,194 test images.
- Dataset 2 per-class totals: black_core 987, crack 496, finger 1172, horizontal_dislocation 266, vertical_dislocation 107, short_circuit 492, star_crack 69, think_line 613, multiple defects 361, free_defects 1428.
- Leakage checks: not reported.
- Dataset license: not reported in the paper text.

### Evaluation

- Protocol: 80/20 train/test split with stratified sampling to preserve class distributions.
- Metrics: [[Accuracy]], [[F1-score]], [[Recall]], and [[Precision]]; the paper states larger values are better.
- Metric definitions: standard TP/TN/FP/FN formulas are provided for all four metrics.
- Statistical tests: not reported.
- Primary reported metric: [[Accuracy]].

## Evidence

### Experimental Setup

- Binary task: Dataset 1, selected 0% and 100% ELPV labels.
- Multiclass task: Dataset 2, ten PV defect classes.
- Baseline fairness: the paper states compared methods were retrained with the same settings as the proposed method.
- Compute: Ubuntu, Intel i5-6600, 16 GB RAM, Nvidia RTX2080, TensorFlow.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| Final binary classifier | Dataset 1 / binary defect classification | Accuracy | higher | Xception 0.8694; ResNet152 0.8221 after augmentation | 0.9617 | After augmentation. |
| Final binary classifier | Dataset 1 / binary defect classification | F1-score | higher | Xception 0.8385; ResNet152 0.7702 after augmentation | 0.9557 | After augmentation. |
| Final binary classifier | Dataset 1 / binary defect classification | Recall | higher | Xception 0.8174; ResNet152 0.7476 after augmentation | 0.9516 | After augmentation. |
| Final binary classifier | Dataset 1 / binary defect classification | Precision | higher | Xception 0.8789; ResNet152 0.8346 after augmentation | 0.9603 | After augmentation. |
| Final binary classifier | Dataset 1 / binary defect classification | Accuracy | higher | CNN 0.7838; VGG16 0.8401; MobileNetV2 0.8739; InceptionV3 0.8896; DenseNet121 0.8761; InceptionResNetV2 0.8896 | 0.9617 | Same training settings according to the paper. |
| Final binary classifier | Dataset 1 / binary defect classification | Accuracy | higher | SVM 82.44%; L-CNN 89.33%; Light CNN 93.02%; DFB-SVM 94.52%; Hessian matrix 93.00% | 96.17% | State-of-the-art comparison table. |
| Final multiclass classifier | Dataset 2 / ten-class PV defect classification | Accuracy | higher | InceptionResNetV2 0.7898; VGG16 0.7772; MobileNetV2 0.7680; DenseNet121 0.7655 | 0.9213 | Best among listed common methods. |
| Final multiclass classifier | Dataset 2 / ten-class PV defect classification | F1-score | higher | InceptionResNetV2 0.7662; VGG16 0.7326 | 0.8898 | Best among listed common methods. |
| Final multiclass classifier | Dataset 2 / ten-class PV defect classification | Recall | higher | InceptionResNetV2 0.7551; VGG16 0.7181 | 0.8961 | Best among listed common methods. |
| Final multiclass classifier | Dataset 2 / ten-class PV defect classification | Precision | higher | InceptionResNetV2 0.7819; VGG16 0.7751 | 0.8872 | Best among listed common methods. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[Accuracy]] | Binary and multiclass classification | `(TP + TN) / (TP + TN + FP + FN)` | higher | yes | Main accuracy values are 96.17% and 92.13%. |
| [[Recall]] | Binary and multiclass classification | `TP / (TP + FN)` | higher | no | Reported in all comparison tables. |
| [[Precision]] | Binary and multiclass classification | `TP / (TP + FP)` | higher | no | Reported in all comparison tables. |
| [[F1-score]] | Binary and multiclass classification | harmonic mean of precision and recall | higher | no | Reported in all comparison tables. |

### Ablations

| Model variant | Accuracy | F1-score | Recall | Precision | Interpretation |
|---|---:|---:|---:|---:|---|
| ResNet152 | 0.6809 | 0.5837 | 0.5933 | 0.6153 | Single backbone. |
| Xception | 0.7379 | 0.6792 | 0.6678 | 0.7077 | Single backbone. |
| ResNet152 + Xception | 0.8702 | 0.8689 | 0.8624 | 0.8349 | Feature fusion improves over single backbones. |
| ResNet152 + Xception + class_weight | 0.8875 | 0.8625 | 0.8478 | 0.8598 | Class weighting improves accuracy/precision. |
| ResNet152 + Xception + class_weight + data enhancement | 0.9032 | 0.9143 | 0.8970 | 0.8744 | Augmentation improves F1 and recall. |
| Final model | 0.9213 | 0.8898 | 0.8961 | 0.8872 | Adds the remaining final-model components reported by the paper. |

## Dataset / Benchmark Details

- Dataset 1 source: `https://github.com/zae-bayern/elpv-dataset`, accessed by the paper on 2022-08-21.
- Dataset 2 source: `http://aihebut.com/col.jsp?id=118`, accessed by the paper on 2022-06-15.
- Dataset 1 labels: 0%, 33%, 67%, and 100% probabilities of PV cell defects; this paper uses 0% and 100% only.
- Dataset 2 labels: ten class labels; `think_line` appears in the paper text where the class likely means thick_line, but the note preserves the paper's spelling.
- Bias/coverage: Dataset 1 is small and class-imbalanced; Dataset 2 is also long-tailed, with star_crack and vertical_dislocation especially small.
- Maintenance: not reported.

## Limitations

- Stated: more defective EL images are needed to increase model generalization for assessing PV cell health.
- Stated future direction: EL sensors and high-performance computing hardware could support deployment in practical large-scale PV plant scenarios.
- Evaluation limitation: no external held-out industrial site, statistical uncertainty, or cross-dataset generalization test is reported.
- Reproducibility limitation: random seeds, exact checkpoint availability, and full implementation details beyond the GitHub repository are not reported in the extracted paper text.

## Reproducibility

- Code: `https://github.com/Zayn-Wang/Photovoltaic-cell-surface-defect-detection`, accessed by the paper on 2022-12-20.
- Data: Dataset 1 and Dataset 2 URLs are reported in the data availability section.
- Hyperparameters: batch size 16, initial learning rate 0.01, minimum learning rate 0.0001, maximum iterations 2000, Adam optimizer, L2 regularization, warm-up plus cosine annealing.
- Random seeds: not reported.
- Environment: Ubuntu, Intel i5-6600, 16 GB RAM, Nvidia RTX2080, Python, TensorFlow.
- Artifact status: public data and code are reported; trained model checkpoints are not reported.

## Systems Details

- Hardware/software stack: Ubuntu, Intel i5-6600, 16 GB RAM, Nvidia RTX2080, Python, TensorFlow.
- Latency: not reported.
- Throughput: not reported.
- Memory beyond RAM: not reported.
- Scaling: deployment to large-scale PV plant scenarios is discussed as future work, not demonstrated.

## Connections

### Graph Hubs

- Tasks: [[Solar cell defect detection]], [[Defect classification]]
- Methods: [[Data augmentation]], [[Coordinate attention]], [[Adam]], [[Xception]]
- Datasets: [[ELPV Dataset]], [[PVEL-AD]]
- Benchmarks: [[PVEL-AD benchmark]]
- Domains: [[Solar cells and photovoltaic]]
- Metrics: [[Accuracy]], [[F1-score]], [[Recall]], [[Precision]]

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2022 - Identifying Defective Solar Cells in Electroluminescence Images Using Deep Feature Representations]] | Shares dataset and task | Both evaluate PV cell defect classification from ELPV electroluminescence images. |
| [[2023 - PVEL-AD A Large-Scale Open-World Dataset for Photovoltaic Cell Anomaly Detection]] | Shares dataset context | The paper's Dataset 2 is a public high-resolution PV EL anomaly dataset from industrial manufacturing and is linked to the PVEL-style dataset source. |
| [[2021 - SIGAN A Novel Image Generation Method for Solar Cell Defect Segmentation and Augmentation]] | Shares task and augmentation theme | Both address scarce PV defect data; this paper uses classical augmentation and class weighting rather than generative segmentation augmentation. |

### Backlinks Updated

- [[ELPV Dataset]], [[PVEL-AD]], [[Data augmentation]], [[Coordinate attention]], [[Solar cells and photovoltaic]], and [[Xception]] were reviewed or updated during audit.

## Questions

- Does the Dataset 2 host still expose exactly the same dataset version used in the paper?
- Are trained weights available in the GitHub repository, or only source code?
- Would the method generalize under cross-dataset testing from ELPV to PVEL-AD-style industrial images?
