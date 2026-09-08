---
title: "Surface Defect Detection of Heat Sink Based on Lightweight Fully Convolutional Network"
aliases:
  - "GSLU-Net heat sink surface defect detection"
paper_key: "doi:10.1109/tim.2022.3188033"
paper_type: "research"
year: 2022
venue: "IEEE Transactions on Instrumentation and Measurement"
authors:
  - "Kaifeng Yang"
  - "Yuliang Liu"
  - "Shiwen Zhang"
  - "Jiajian Cao"
status: "processed"
topics:
  - "heat sink surface defect detection"
  - "lightweight segmentation networks"
tasks:
  - "[[Defect segmentation]]"
  - "[[Surface defect detection]]"
domains:
  - "[[Semiconductor and electronics]]"
datasets:
  - "[[Heat Sink Surface Defect Dataset]]"
methods:
  - "[[GSLU-Net]]"
  - "[[Ghost module]]"
  - "[[U-Net]]"
model_family:
  - "[[Segmentation Models]]"
architectures:
  - "[[GSLU-Net]]"
  - "[[U-Net]]"
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[IoU]]"
  - "[[F1-score]]"
  - "[[Inference time]]"
  - "[[Parameter count]]"
primary_metric: "[[Accuracy]]"
metric_definitions:
  - "Accuracy: (TP + TN) / (TP + TN + FP + FN)"
  - "Precision: TP / (TP + FP)"
  - "Recall: TP / (TP + FN)"
  - "IoU: TP / (TP + FN + FP)"
  - "F1-score: 2 * precision * recall / (precision + recall)"
baselines:
  - "U-Net"
  - "Light U-Net"
  - "Ghost light U-Net"
  - "SE light U-Net"
  - "FCN32S"
  - "FCN16S"
  - "FCN8S"
  - "SegNet"
  - "Pix2pix GAN"
  - "DeepLabv3+"
  - "Mix-FCN"
  - "Wang's Net"
  - "BSU-Net"
benchmarks:
  - "Heat Sink Surface Defect Dataset"
  - "RSDDs Type I"
  - "RSDDs Type II"
  - "Kolektor SDD"
  - "Kolektor SDD2"
code: "not reported"
data: "https://www.kaggle.com/datasets/kaifengyang/heat-sink-surface-defect-dataset"
doi: "10.1109/TIM.2022.3188033"
arxiv: "not reported"
url: "https://doi.org/10.1109/TIM.2022.3188033"
pdf: "paper-inbox/10_processed/Research/2022 - Yang - Surface Defect Detection of Heat Sink Based on Lightweight Fully Convolutional Network.pdf"
source_file: "paper-inbox/10_processed/Research/2022 - Yang - Surface Defect Detection of Heat Sink Based on Lightweight Fully Convolutional Network.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Yang - Surface Defect Detection of Heat Sink Based on Lightweight Fully Convolutional Network.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Yang - Surface Defect Detection of Heat Sink Based on Lightweight Fully Convolutional Network.txt"
related_concepts:
  - "[[Surface defect detection]]"
  - "[[Class imbalance]]"
related_methods:
  - "[[GSLU-Net]]"
  - "[[Ghost module]]"
  - "[[U-Net]]"
related_datasets:
  - "[[Heat Sink Surface Defect Dataset]]"
related_domains:
  - "[[Semiconductor and electronics]]"
related_tasks:
  - "[[Defect segmentation]]"
  - "[[Surface defect detection]]"
related_benchmarks:
  - "RSDDs Type I"
  - "RSDDs Type II"
  - "Kolektor SDD"
  - "Kolektor SDD2"
processed_at: "2026-06-03"
---
# Surface Defect Detection of Heat Sink Based on Lightweight Fully Convolutional Network

## Summary

The paper proposes [[GSLU-Net]], a lightweight fully convolutional segmentation network for detecting scratches and stains on gold-plated tungsten-copper alloy heat sinks. The full pipeline includes an image acquisition system, preprocessing that crops and resizes each heat-sink object to 320 x 320 pixels, and pixelwise segmentation with a U-Net-inspired encoder-decoder.

The paper also introduces [[Heat Sink Surface Defect Dataset]], a 1000-image pixel-level annotated dataset. GSLU-Net reports 97.96% accuracy and 14.115 ms inference time per image on this dataset, with 276,131 trainable parameters and 552,314 FLOPs.

## Paper Type

Research paper. It introduces a lightweight FCN architecture and contributes a pixel-level heat-sink surface defect dataset, but the main experimental claim is the speed-accuracy balance of GSLU-Net.

## Problem

Gold-plated tungsten-copper alloy heat sinks are millimeter-scale electronic-chip heat-dissipation parts with thin gold coating. Manual microscope inspection is slow, labor intensive, and dependent on inspector skill. The target task requires small-defect pixel localization, because bounding boxes do not outline the scratch or stain contour and heavy FCNs can lose details through repeated downsampling.

## Contribution

- Introduces [[Heat Sink Surface Defect Dataset]] with 1000 annotated images of gold-plated tungsten-copper alloy heat sink defects.
- Proposes an acquisition and preprocessing pipeline that captures 5496 x 3672 RGB images, segments foreground heat-sink objects, crops them, and resizes them to 320 x 320.
- Proposes [[GSLU-Net]], a lightweight U-Net-style FCN using [[Ghost module]] layers and squeeze-and-excitation channel recalibration.
- Reports better speed-accuracy tradeoff than several FCN baselines on the heat-sink dataset and stronger F1-score ranks across additional surface-defect datasets.

## Method

The image acquisition system uses a DAHENG MER-2000-5GC industrial camera with a Sony IMX 183 CMOS sensor, a Canrill telecentric lens, and a 60-bead LED ring array light source. The captured images are binarized with Otsu thresholding, cleaned with closing, processed with border following, and cropped using minimum enclosing rectangles from Jarvis march and rotating calipers geometry. The final training images are 320 x 320.

GSLU-Net simplifies U-Net into a three-class pixelwise model for background, scratch, and stain. The first contracting step uses ordinary 3 x 3 convolutions because the input has only three channels. Later contracting steps use Ghost modules: a 1 x 1 convolution generates initial feature maps, then depthwise convolution creates additional feature maps, and the outputs are concatenated. SE blocks use global max pooling, global average pooling, concatenation, dense layers, and softmax channel weights to recalibrate feature responses. The expansive path uses transposed convolutions, skip concatenations, and a final pixelwise softmax.

Training uses Adam with weighted categorical cross-entropy. The paper evaluates learning rates 0.0001, 0.0002, and 0.0003 for 60 epochs on an NVIDIA RTX 2070 GPU.

## Evidence

### Dataset

| Dataset | Size | Split | Labels | Notes |
|---|---:|---|---|---|
| [[Heat Sink Surface Defect Dataset]] | 1000 images | 700 train, 200 validation, 100 test | background, scratch, stain | pixel-level annotations; 320 x 320 cropped heat-sink defect images |
| RSDDs Type I | not reported in extracted text | not reported | binary defect masks | open rail surface defect dataset |
| RSDDs Type II | not reported in extracted text | not reported | binary defect masks | open rail surface defect dataset |
| Kolektor SDD | not reported in extracted text | not reported | binary defect masks | open industrial surface defect dataset |
| Kolektor SDD2 | not reported in extracted text | not reported | binary defect masks | open industrial surface defect dataset |

### Performance Metrics

| Metric | Definition | Direction | Primary | Context |
|---|---|---|---|---|
| [[Accuracy]] | `(TP + TN) / (TP + TN + FP + FN)` | higher | yes | pixel classification correctness |
| [[Precision]] | `TP / (TP + FP)` | higher | no | false-detection control |
| [[Recall]] | `TP / (TP + FN)` | higher | no | missed-defect control |
| [[IoU]] | `TP / (TP + FN + FP)` | higher | no | overlap and localization quality |
| [[F1-score]] | harmonic mean of precision and recall | higher | no | balance between missed and false defect pixels |
| [[Inference time]] | milliseconds per image | lower | no | deployment speed |
| [[Parameter count]] | trainable parameters | lower | no | model size |

### Reported Results

- GSLU-Net reaches 97.96% accuracy and 14.115 ms inference time per image on [[Heat Sink Surface Defect Dataset]].
- The model uses 276,131 trainable parameters and 552,314 FLOPs.
- Ablations show that reducing U-Net depth and channels greatly reduces FLOPs and inference time with a small accuracy loss; replacing later convolutions with Ghost modules roughly halves FLOPs relative to light U-Net with similar accuracy; adding SE blocks improves accuracy by about 0.5% with only slight efficiency cost.
- Comparative experiments include FCN32S, FCN16S, FCN8S, SegNet, Pix2pix GAN, DeepLabv3+, Mix-FCN, Wang's Net, and BSU-Net. The paper states that GSLU-Net surpasses these networks across multiple indicators on the heat-sink dataset.
- Additional experiments on RSDDs Type I, RSDDs Type II, Kolektor SDD, and Kolektor SDD2 support the claim that GSLU-Net generalizes to other surface-defect segmentation settings. A Friedman test over F1-score ranks rejects equal performance with reported `X^2 = 28.72`.

## ML/DL Extraction

- Task formulation: semantic segmentation of heat-sink surface defects.
- Inputs: 320 x 320 RGB cropped heat-sink surface images.
- Outputs: per-pixel background, scratch, or stain labels.
- Architecture: U-Net-like FCN with a three-level contracting path, symmetric expansive path, skip concatenations, Ghost modules, SE blocks, transposed convolutions, and final pixelwise softmax.
- Loss: weighted categorical cross-entropy.
- Optimizer: Adam.
- Training recipe: 60 epochs; learning rates 0.0001, 0.0002, and 0.0003 evaluated.
- Hardware: NVIDIA RTX 2070 GPU with 8 GB memory.
- Baselines: U-Net variants, FCN variants, SegNet, Pix2pix GAN, DeepLabv3+, Mix-FCN, Wang's Net, BSU-Net, residual-block variant, MobileNet depthwise-separable variant, and ShuffleNet-unit variant.
- Artifacts: public dataset is available on Kaggle; code is not reported.

## Limitations

- Table extraction in the available source does not preserve every numeric result from the comparison tables.
- The paper warns that surface-defect datasets are class imbalanced; a model predicting normal pixels can have high accuracy, so weighted loss is needed.
- The paper notes that cheap operations such as depthwise and group convolution can increase memory-access frequency, so lower FLOPs do not guarantee lower inference time.
- Code availability is not reported.

## Connections

### Graph Hubs

- Tasks: [[Defect segmentation]], [[Surface defect detection]]
- Methods: [[GSLU-Net]], [[Ghost module]], [[U-Net]]
- Datasets: [[Heat Sink Surface Defect Dataset]]
- Domains: [[Semiconductor and electronics]]
- Metrics: [[Accuracy]], [[Precision]], [[Recall]], [[IoU]], [[F1-score]], [[Inference time]], [[Parameter count]]

### Shares Dataset

- [[Heat Sink Surface Defect Dataset]]: the paper creates the dataset and uses it for the main heat-sink segmentation experiments.

### Shares Task

- [[Defect segmentation]]: the model predicts pixel-level scratch and stain masks.
- [[Surface defect detection]]: the paper targets automated industrial surface inspection.

### Shares Method

- [[U-Net]]: GSLU-Net adapts a U-Net-like encoder-decoder with skip connections.
- [[Ghost module]]: used to reduce computation in later contracting steps.

### Application/Domain

- [[Semiconductor and electronics]]: the inspected heat sinks are used for chip heat dissipation before packaging on electronic chips.

## Questions

- The exact train/validation/test class distributions are not reported in the extracted text.
- Code release status is not reported.
- Full per-baseline table values need PDF table inspection if exact values are required.
