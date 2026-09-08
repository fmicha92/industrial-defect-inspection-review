---
title: "Cost Efficient Defect Detection in Bangle Industry Using Transfer Learning"
aliases:
  - "Cost Efficient Defect Detection in Bangle Industry"
paper_key: "doi:10.1007/978-3-031-31407-0_14"
paper_type: "research"
year: 2023
venue: "Computer Vision and Image Processing"
authors:
  - "Anuranjan Dubey"
  - "Abhinandan Dubey"
status: "processed"
topics:
  - "glass bangle inspection"
  - "transfer learning"
  - "low-cost visual inspection"
tasks:
  - "[[Glass bangle defect classification]]"
  - "[[Defect classification]]"
datasets:
  - "[[Glass Bangle Defect Detection Classification]]"
methods:
  - "[[Transfer learning]]"
  - "[[ResNet50]]"
  - "[[Support vector machine]]"
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[F1-score]]"
primary_metric: "[[Accuracy]]"
related_domains:
  - "[[Glass inspection]]"
related_concepts:
  - "[[Industrial visual inspection]]"
  - "[[Surface defect detection]]"
doi: "10.1007/978-3-031-31407-0_14"
url: "https://doi.org/10.1007/978-3-031-31407-0_14"
pdf: "paper-inbox/10_processed/Research/2023 - Dubey - Cost Efficient Defect Detection in Bangle Industry Using Transfer Learning.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Dubey - Cost Efficient Defect Detection in Bangle Industry Using Transfer Learning.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Dubey - Cost Efficient Defect Detection in Bangle Industry Using Transfer Learning.txt"
---
# Cost Efficient Defect Detection in Bangle Industry Using Transfer Learning

## Summary

The paper proposes a low-cost visual inspection pipeline for classifying glass bangles as good, defective, or broken. It introduces a 1,080-image human-labeled factory dataset and evaluates traditional image features against transfer-learning features from pretrained CNNs. The strongest reported result is a ResNet50 feature extractor paired with SVM, reaching 91% accuracy for three-class classification and 92% accuracy when broken and defective bangles are merged into one defective class.

## Paper Type

Research paper with a dataset contribution. It introduces a factory-collected bangle image dataset, compares feature extraction and classifiers, and motivates the system as a low-cost alternative to manual inspection and infrared thermography in bangle manufacturing.

## Problem

Glass bangle factories need to reject bangles with broken shapes, gaps, bubbles, varying thickness, and other visible defects. Existing practice relies on human sorters and sometimes expensive infrared thermography. The paper scopes the automated task to visible shape and material defects, excluding size/radius defects from the core classification pipeline.

## Contribution

- Introduces a human-labeled dataset of 1,080 bangle images collected from a factory.
- Defines a three-class task: `good`, `defect`, and `broken`.
- Tests traditional features such as Hough transform, contour features, SIFT/BoVW, and Hu moments.
- Proposes preprocessing to remove shadows, then extracts pretrained CNN embeddings for downstream machine-learning classifiers.
- Shows that ResNet50 features with SVM outperform the tested traditional-feature baselines.
- Discusses a low-cost Raspberry Pi and Pi camera deployment concept.

## Method

### Dataset

- Images: 1,080 RGB bangle images.
- Image resolution: 3000 x 3000 pixels.
- Collection setting: bangle factory images under average lighting conditions.
- Augmentation/source construction: each base image was rotated clockwise by 90 degrees to yield four images.
- Labels: human sorters labeled images during capture; labels were cross-validated across different humans.
- Classes: `good`, `defect`, and `broken`.
- Defect scope: broken shapes, gaps, bubbles, thickness variation, and visible deformities.
- Out of scope: bangle size/radius defect detection, though the paper discusses Circular Hough Transform as an extension.

### Preprocessing

The proposed preprocessing removes shadows and emphasizes bangle edges:

- Dilate each RGB channel with a 15 x 15 square kernel.
- Apply median filtering to reduce grainy noise without blurring edges.
- Subtract the dilated/median-filtered image from the original image.
- Apply min-max normalization.
- Resize images to 224 x 224 for CNN feature extraction.

### Feature Extraction and Classification

- Pretrained CNNs were used as feature extractors, with the final softmax layer removed.
- ResNet50 with ImageNet weights produced a 1 x 2048 feature vector per image.
- Classifiers evaluated over extracted features include SVM, decision tree, perceptron, SGD, KNN, random forest, and XGBoost.
- The binary variant merges `defect` and `broken` into `defective`, with `good` as `non-defective`.

## Evidence

### Experimental Setup

- Train/test split: 75/25.
- Cross-validation: 4-fold.
- Metrics: accuracy, precision, recall, and F1-score.
- Traditional-feature baselines: Hough transform, contour features, SIFT features, and image moments.
- Transfer-learning feature extractors: VGG16, VGG19, ResNet50, and Xception.

### Reported Results

- Three-class classification: SVM over ResNet50 features reports 0.91 accuracy.
- Binary classification: ResNet50 + SVM reports 0.92 accuracy, 0.92 precision, 0.92 recall, and 0.92 F1-score.
- VGG19 + SVM on binary classification reports 0.91 accuracy, 0.92 precision, 0.91 recall, and 0.91 F1-score.
- ResNet50 + SVM without the proposed preprocessing reports 0.86 accuracy, indicating that the shadow-removal preprocessing improved performance in the reported setup.
- Combining traditional features with neural features did not improve results.

## ML/DL Extraction

- Task formulation: image classification over bangle quality labels.
- Input: RGB bangle images.
- Output: three-class or binary quality label.
- Feature extractor: pretrained [[ResNet50]], VGG16, VGG19, and Xception tested.
- Primary model: [[Support vector machine]] over pretrained CNN embeddings.
- Training setup: 75/25 train-test split and 4-fold cross-validation.
- Metrics: [[Accuracy]], [[Precision]], [[Recall]], [[F1-score]].
- Hardware/deployment concept: Raspberry Pi 4 with Pi camera and basic electronics; exact inference latency and deployed software environment are not reported.
- Code: not reported.
- Data availability: public Kaggle dataset is linked separately in [[Glass Bangle Defect Detection Classification]].

## Limitations

- The core method does not detect size/radius defects.
- The dataset is small and collected from one bangle-production setting.
- The paper reports classification accuracy but does not report confusion matrices or per-class failure analysis in the extracted text.
- Deployment is discussed conceptually; field validation in an operating factory is not reported.
- Defect severity and borderline accept/reject criteria are not formalized beyond the three labels.

## Connections

### Graph Hubs

- Tasks: [[Glass bangle defect classification]], [[Defect classification]]
- Datasets: [[Glass Bangle Defect Detection Classification]]
- Methods: [[Transfer learning]], [[ResNet50]], [[Support vector machine]]
- Metrics: [[Accuracy]], [[Precision]], [[Recall]], [[F1-score]]
- Domains: [[Glass inspection]]

### Shares Dataset

- [[Glass Bangle Defect Detection Classification]]: the paper introduces and evaluates on this factory-collected bangle image dataset.

### Shares Task

- [[Glass bangle defect classification]]: the main task is classifying bangles as good, defect, or broken.
- [[Defect classification]]: the method maps a product image to a defect/quality class.

### Shares Method

- [[Transfer learning]]: pretrained CNN representations are used instead of training deep networks from scratch.
- [[ResNet50]]: the best reported three-class and binary results use ResNet50 embeddings with SVM.
- [[Support vector machine]]: the strongest classifier in the reported experiments.

### Shares Metric

- [[Accuracy]], [[Precision]], [[Recall]], and [[F1-score]] are reported for traditional features, CNN features, and binary variants.

### Application/domain

- [[Glass inspection]]: the paper targets visual quality inspection for glass bangles.
- [[Industrial visual inspection]]: the method is positioned as low-cost factory inspection.

## Questions

- Does the Kaggle-hosted dataset preserve the exact train/test split used in the paper?
- What are the per-class error modes for `defect` versus `broken`?
- How robust is the method to new factories, camera positions, lighting changes, and bangle colors not represented in the 1,080-image dataset?
