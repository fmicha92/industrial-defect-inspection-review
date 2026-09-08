---
title: "CarDD: A New Dataset for Vision-Based Car Damage Detection"
aliases:
  - "CarDD paper"
paper_key: "doi:10.1109/tits.2023.3258480"
paper_type: dataset
year: 2023
venue: "IEEE Transactions on Intelligent Transportation Systems"
authors:
  - "Xinkuang Wang"
  - "Wenjing Li"
  - "Zhongcheng Wu"
status: processed
processed_at: 2026-06-01
topics:
  - car damage detection
  - car damage segmentation
  - salient object detection
tasks:
  - "[[Car damage detection]]"
  - "[[Defect classification]]"
  - "[[Defect segmentation]]"
  - "[[Salient object detection]]"
domains:
  - "[[Automotive damage assessment]]"
application_area: "car insurance damage assessment"
datasets:
  - "[[CarDD]]"
dataset_sizes:
  - "4,000 high-resolution damaged car images"
  - "over 9,000 labeled damage instances"
  - "six damage categories"
splits:
  - "2,816 training images, 810 validation images, and 374 test images"
labels:
  - dent
  - scratch
  - crack
  - glass shatter
  - lamp broken
  - tire flat
modalities:
  - "high-resolution RGB car damage images"
data_sources:
  - Flickr
  - Shutterstock
  - "manual selection with VGG16-assisted candidate filtering"
methods:
  - "[[DCN+]]"
  - "[[Multi-scale learning]]"
  - "[[Focal loss]]"
model_family:
  - object detection
  - instance segmentation
  - salient object detection
architectures:
  - "[[DCN+]]"
  - "Mask R-CNN"
  - "Cascade Mask R-CNN"
  - "GCNet"
  - "HTC"
  - "DCN"
  - "CSNet"
  - "U2-Net"
  - "PoolNet"
  - "SGL-KRN"
losses:
  - "[[Focal loss]]"
  - "L1 loss"
  - "cross-entropy loss"
training_regime: "Supervised classification, object detection, instance segmentation, and salient object detection on CarDD."
pretraining: "Detection and instance-segmentation baselines use COCO-pretrained initialized models; the data-cleaning classifier uses ImageNet-pretrained VGG16."
augmentation:
  - "[[Multi-scale learning]]"
synthetic_data: "not applicable"
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[Recall]]"
  - "[[Average precision]]"
  - "[[IoU]]"
  - "[[F-measure]]"
  - "[[Weighted F-measure]]"
  - "[[S-measure]]"
  - "[[E-measure]]"
  - "[[Mean Absolute Error]]"
primary_metric: "[[Average precision]]"
metric_definitions:
  - "COCO-style AP averages AP over IoU thresholds from 0.50 to 0.95 in 0.05 steps."
  - "APbb is bounding-box AP; AP without the bb superscript is mask AP."
  - "APS, APM, and APL evaluate small, medium, and large damage instances."
baselines:
  - "Mask R-CNN"
  - "Cascade Mask R-CNN"
  - "GCNet"
  - "HTC"
  - "DCN"
  - "CSNet"
  - "U2-Net"
  - "PoolNet"
  - "SGL-KRN"
benchmarks:
  - "[[CarDD benchmark]]"
evaluation_protocol: "Benchmark classification, object detection, instance segmentation, and salient object detection on CarDD; detection and segmentation use the 374-image test set, and the challenging setting adds 500 undamaged images."
statistical_tests: "not reported"
parameters: "not reported"
compute: "NVIDIA Tesla P100 for baseline detection/segmentation training; NVIDIA RTX 3090 for DCN+ training."
hardware: "NVIDIA Tesla P100; NVIDIA RTX 3090"
training_time: "not reported"
inference_cost: "not reported"
code: "https://github.com/CarDD-USTC/CarDD-USTC.github.io"
data: "https://cardd-ustc.github.io/"
dataset_download_url: "https://drive.google.com/file/d/1bbyqVCKZX5Ur5Zg-uKj0jD0maWAVeOLx/view?usp=sharing"
artifact_status: "Project site provides paper, Google Drive dataset link, GitHub code/project repository, and license form; Google Drive listed CarDD_release.zip as a 5.6 GB file on 2026-06-09, while the project page still asks users to complete the licensing form before access/use."
doi: "10.1109/tits.2023.3258480"
url: "https://doi.org/10.1109/TITS.2023.3258480"
pdf: "paper-inbox/10_processed/Dataset/2023 - Wang - CarDD A New Dataset for Vision-Based Car Damage Detection.pdf"
source_file: "paper-inbox/10_processed/Dataset/2023 - Wang - CarDD A New Dataset for Vision-Based Car Damage Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2023 - Wang - CarDD A New Dataset for Vision-Based Car Damage Detection.md"
extracted_text: "paper-inbox/90_processing/text/2023 - Wang - CarDD A New Dataset for Vision-Based Car Damage Detection.txt"
related_papers: []
related_concepts:
  - "[[Automotive damage assessment]]"
  - "[[Industrial visual inspection]]"
related_methods:
  - "[[DCN+]]"
  - "[[Multi-scale learning]]"
  - "[[Focal loss]]"
related_datasets:
  - "[[CarDD]]"
related_domains:
  - "[[Automotive damage assessment]]"
related_tasks:
  - "[[Car damage detection]]"
  - "[[Defect classification]]"
  - "[[Defect segmentation]]"
  - "[[Salient object detection]]"
related_benchmarks:
  - "[[CarDD benchmark]]"
---
# CarDD: A New Dataset for Vision-Based Car Damage Detection

## Summary

Wang, Li, and Wu introduce [[CarDD]], a high-resolution image dataset for vehicle damage classification, object detection, instance segmentation, and salient object detection. The dataset contains 4,000 damaged-car images, over 9,000 annotated damage instances, and six damage categories: dent, scratch, crack, glass shatter, lamp broken, and tire flat. The paper also benchmarks object detection, instance segmentation, and salient object detection methods, and proposes [[DCN+]], a deformable-convolution model variant using [[Focal loss]] and [[Multi-scale learning]] to improve difficult categories.

## Paper Type

Dataset paper. The core contribution is the release and analysis of [[CarDD]], with annotations, split protocol, baseline experiments, and access artifacts for car damage assessment.

## Problem

Vision-based car damage assessment must locate, classify, and outline exterior vehicle damage for insurance workflows. Earlier public datasets either focus on classification only or lack damage type and location labels, limiting fair comparison for detection and segmentation models.

## Contribution

- Introduces [[CarDD]], described as a large public dataset for car damage detection and segmentation with damage type, location, and magnitude annotations.
- Provides annotations for classification, object detection, instance segmentation, and [[Salient object detection]].
- Benchmarks Mask R-CNN, Cascade Mask R-CNN, GCNet, HTC, DCN, CSNet, U2-Net, PoolNet, SGL-KRN, and [[DCN+]] on [[CarDD benchmark]].
- Shows that dent, scratch, and crack are difficult classes because they are small, scale-diverse, visually similar, and often intertwined.

## Method

### Dataset Construction

- Raw images were collected from Flickr and Shutterstock.
- Duplicate Cleaner removed duplicates, followed by manual double-checking.
- A VGG16 binary classifier trained on 500 manually selected damaged-car samples and 500 negative samples filtered candidate images from raw data.
- More than 10,000 candidate images were collected; manual selection retained 4,000 images for annotation across the six target damage classes.
- Privacy handling mosaicked or removed images containing human faces or license plates.

### Annotation

- The annotation guidelines use Ping An Insurance Company claim rules.
- Mixed dent/scratch/crack damage is labeled by priority: crack > dent > scratch.
- Damage across different car components is split into separate instances.
- Adjacent same-class damage on the same component is merged into one instance.
- Twenty annotators participated; five were car-damage assessment experts and 15 were selected after training and a 100-image annotation test requiring recall above 90%.
- Expert verification and re-annotation were used for inconsistent regions.
- Object detection and instance segmentation annotations use COCO-style instance IDs, category labels, mask contours, and tight bounding boxes.
- Salient object detection uses binary maps generated from instance-segmentation annotations.

### Model Experiments

- Detection and instance-segmentation baselines: Mask R-CNN, Cascade Mask R-CNN, GCNet, HTC, and DCN.
- [[DCN+]] adds [[Focal loss]] and [[Multi-scale learning]] to a ResNet-101 DCN baseline.
- DCN+ uses multi-scale resizing with image height sampled from 640 to 1200 while keeping width at 1333.
- DCN+ uses focal loss with alpha 0.50 and gamma 2.0, plus L1 and cross-entropy losses.
- Salient object detection baselines: CSNet, U2-Net, PoolNet, and SGL-KRN.

## Evidence

### Dataset Statistics

- Images: 4,000 damaged-car images.
- Instances: over 9,000 labeled instances.
- Categories: dent, scratch, crack, glass shatter, lamp broken, and tire flat.
- Split: 2,816 training images, 810 validation images, and 374 test images.
- Object sizes: 38.6% small, 32.6% medium, and 28.8% large instances.
- Image quality: lowest CarDD resolution is 1,000 x 413 pixels; average resolution is 684,231 pixels; average file size is 739 KB.
- Annotation metadata includes number of instances, number of damage categories, damage severity, and shooting angle for each image.

### Classification Filter

- The VGG16 binary classifier for candidate filtering reports 94.3% accuracy, 91.6% precision, and 97.6% recall on a 1,000-sample test set.
- False positives are 4.5% and false negatives are 1.2% of the test set.

### Detection and Segmentation Results

- On the standard test set, ResNet-101 [[DCN+]] reports 57.0 mask AP and 60.6 box AP, compared with 52.5 mask AP and 54.3 box AP for ResNet-101 DCN.
- ResNet-101 DCN+ reports AP50/APbb50 of 77.7/78.8 and AP75/APbb75 of 58.4/64.8.
- ResNet-101 DCN+ reports small-object AP/APbbS of 34.6/37.1, substantially higher than ResNet-101 DCN's 19.7/22.7.
- Per-category ResNet-101 DCN+ mask/box AP: dent 40.5/42.2, scratch 34.3/42.3, crack 16.6/29.6, glass shatter 89.6/90.1, lamp broken 70.8/69.5, tire flat 90.0/90.2.
- In the challenging setting with 500 extra undamaged test images, ResNet-101 DCN+ reports 55.8 mask AP and 59.4 box AP. The paper says this is a 1.2% AP reduction relative to the damaged-only setting.

### Salient Object Detection Results

- SOD metrics: [[F-measure]], [[Weighted F-measure]], [[S-measure]], [[E-measure]], and [[Mean Absolute Error]].
- SGL-KRN reports Fβ 0.791, weighted Fβ 0.744, Sm 0.809, Em 0.884, and MAE 0.071.
- PoolNet reports the best Sm and tied-best MAE in the table: Sm 0.811 and MAE 0.071.
- SGL-KRN per-class Fβ: dent 0.698, scratch 0.664, crack 0.433, glass shatter 0.957, lamp broken 0.854, and tire flat 0.936.
- The paper argues that MAE is sensitive to object size and is not well suited to comparing classes with very different damage-region sizes.

## ML/DL Extraction

- Task formulation: multi-task visual car damage assessment covering classification, detection, instance segmentation, and salient object detection.
- Inputs: high-resolution RGB vehicle-damage images.
- Outputs: damage category labels, bounding boxes, instance masks, and binary salient-object maps depending on task.
- Architectures: VGG16 for candidate filtering; Mask R-CNN, Cascade Mask R-CNN, GCNet, HTC, DCN, and [[DCN+]] for detection/segmentation; CSNet, U2-Net, PoolNet, and SGL-KRN for SOD.
- Training setup: detection/segmentation models are fine-tuned from COCO-pretrained weights using MMDetection.
- Detection/segmentation optimizer: SGD with batch size 8 for 24 epochs, learning rate 0.01 for epochs 1-16, 0.001 for epochs 17-22, and 0.0001 for epochs 23-24; weight decay 0.0001 and momentum 0.9.
- DCN+ compute: NVIDIA RTX 3090.
- Baseline detection/segmentation compute: NVIDIA Tesla P100.
- SOD optimizer: Adam for CSNet, U2-Net, PoolNet, and SGL-KRN.
- U2-Net training: batch size 12 for 140,800 iterations, equivalent to 600 epochs with 2,816 training images.

## Limitations

- CarDD does not own the copyright to the source images; the paper says copyrights remain with Flickr and Shutterstock.
- Dataset use is limited to non-commercial research and educational purposes, and the project license requires prior consent. A 2026-06-09 host audit found that the project site lists a Google Drive dataset link, but the project page still instructs users to first submit the licensing form.
- The paper identifies dent, scratch, and crack as hard categories because they are small, shape-diverse, visually similar, and often intertwined.
- The SOD experiments remove category information, which can improve localization of hard shapes but does not solve class-specific damage assessment.
- The paper does not report inference cost or training time for the benchmark models.

## Connections

### Graph Hubs

- Tasks: [[Car damage detection]], [[Defect classification]], [[Defect segmentation]], [[Salient object detection]]
- Methods: [[DCN+]], [[Focal loss]], [[Multi-scale learning]]
- Datasets: [[CarDD]]
- Domains: [[Automotive damage assessment]]
- Metrics: [[Average precision]], [[F-measure]], [[Weighted F-measure]], [[S-measure]], [[E-measure]], [[Mean Absolute Error]]

### Shares Dataset

- [[CarDD]]: introduced by this paper for car damage classification, detection, instance segmentation, and salient object detection.

### Shares Task

- [[Car damage detection]]: primary task for locating and classifying vehicle damage.
- [[Defect classification]]: CarDD supports image- and instance-level damage category prediction.
- [[Defect segmentation]]: CarDD provides instance masks and SOD binary maps for localization.
- [[Salient object detection]]: the paper evaluates SOD models as a category-agnostic damage localization alternative.

### Shares Method

- [[DCN+]]: proposed in this paper as an improved DCN variant.
- [[Focal loss]]: used in DCN+ to focus on hard categories.
- [[Multi-scale learning]]: used in DCN+ to handle scale-diverse damage instances.

### Shares Metric

- [[Average precision]]: primary detection and segmentation metric.
- [[F-measure]], [[Weighted F-measure]], [[S-measure]], [[E-measure]], and [[Mean Absolute Error]]: SOD metrics.

### Application/Domain

- [[Automotive damage assessment]]: the paper targets insurance-oriented vehicle damage assessment.

## Questions

- Are the released annotation files unchanged from the paper's 2023 version?
- Does the downloadable package include the unannotated rusty, burned, and smashed candidate images mentioned as attached for further research?
- Which current SOD or segmentation metrics best handle the paper's concern that MAE is object-size sensitive?
