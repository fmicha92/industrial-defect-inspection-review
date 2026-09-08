---
title: "PGA-Net: Pyramid Feature Fusion and Global Context Attention Network for Automated Surface Defect Detection"
aliases:
  - "PGA-Net"
paper_key: "doi:10.1109/tii.2019.2958826"
paper_type: "research"
year: 2020
venue: "IEEE Transactions on Industrial Informatics"
authors:
  - "Hongwen Dong"
  - "Kechen Song"
  - "Yu He"
  - "Jing Xu"
  - "Yunhui Yan"
  - "Qinggang Meng"
doi: "10.1109/tii.2019.2958826"
url: "https://doi.org/10.1109/TII.2019.2958826"
pdf: "paper-inbox/10_processed/Research/2020 - Dong - PGA-Net Pyramid Feature Fusion and Global Context Attention Network for Automated Surface Defect Detection.pdf"
source_file: "paper-inbox/10_processed/Research/2020 - Dong - PGA-Net Pyramid Feature Fusion and Global Context Attention Network for Automated Surface Defect Detection.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2020 - Dong - PGA-Net Pyramid Feature Fusion and Global Context Attention Network for Automated Surface Defect Detection.md"
extracted_text: "paper-inbox/90_processing/text/2020 - Dong - PGA-Net Pyramid Feature Fusion and Global Context Attention Network for Automated Surface Defect Detection.txt"
status: "processed"
processed_at: "2026-06-05"
topics:
  - "surface defect segmentation"
  - "pyramid feature fusion"
  - "global context attention"
tasks:
  - "[[Defect segmentation]]"
  - "[[Metallic surface defect detection]]"
domains:
  - "[[Metal inspection]]"
datasets:
  - "[[NEU-SEG]]"
  - "[[DAGM2007]]"
  - "[[Magnetic Tile Defects]]"
methods:
  - "[[PGA-Net]]"
  - "[[VGG-16]]"
  - "[[Segmentation Models]]"
architectures:
  - "[[PGA-Net]]"
model_family:
  - "[[Segmentation Models]]"
metrics:
  - "[[mIoU]]"
  - "[[Mean pixel accuracy]]"
  - "[[FPS]]"
primary_metric: "[[mIoU]]"
baselines:
  - "SegNet"
  - "PSPNet"
  - "DeepLab"
  - "RefineNet"
  - "FCN"
code: "not reported"
data: "NEU-Seg is hosted from the Northeastern University surface defect database page and linked NEU_Seg repository."
artifact_status: "NEU-Seg introduced; code not reported in paper; dataset host URL available"
related_datasets:
  - "[[NEU-SEG]]"
  - "[[DAGM2007]]"
  - "[[Magnetic Tile Defects]]"
related_domains:
  - "[[Metal inspection]]"
related_tasks:
  - "[[Defect segmentation]]"
  - "[[Metallic surface defect detection]]"
related_methods:
  - "[[PGA-Net]]"
  - "[[VGG-16]]"
related_concepts:
  - "[[Surface defect detection]]"
related_papers:
  - "[[2013 - A Noise Robust Method Based on Completed Local Binary Patterns for Hot-Rolled Steel Strip Surface Defects]]"
  - "[[2022 - FDSNet An Accurate Real-Time Surface Defect Segmentation Network]]"
---
# PGA-Net: Pyramid Feature Fusion and Global Context Attention Network for Automated Surface Defect Detection

## Summary

Dong et al. propose [[PGA-Net]], a pixel-wise surface defect segmentation network that fuses multilevel VGG-16 features into multiple resolutions, passes global context from low-resolution maps to high-resolution maps, and refines prediction boundaries. The paper introduces [[NEU-SEG]] by selecting three defect classes from the NEU surface defect database and adding pixel-wise LabelMe annotations for inclusion, patches, and scratches.

## Paper Type

Research paper. It proposes a semantic segmentation model for automated surface defect detection and introduces NEU-Seg as a pixel-wise hot-rolled steel strip defect segmentation dataset.

## Problem

Industrial surface defects are difficult to segment automatically because defects can have low contrast against the background, large intraclass shape and scale variation, and interclass similarity in texture and grayscale. The paper argues that image-level classification cannot localize defects, region-level detection gives only coarse boxes, and pixel-wise segmentation is needed for precise defect boundaries.

## Contribution

- Proposes [[PGA-Net]] for pixel-wise surface defect detection across four datasets.
- Introduces a pyramid feature fusion module that fuses multilevel CNN features into five output resolutions.
- Adds a global context attention module to transfer context from low-resolution fusion maps to high-resolution maps.
- Adds boundary refinement and deep supervision to improve boundary prediction and optimization.
- Introduces [[NEU-SEG]] by adding pixel-wise LabelMe annotations to three selected NEU steel-strip defect classes.

## Method

PGA-Net uses a VGG-16 backbone pretrained on ImageNet as the feature extraction module. It extracts multilevel features from the last convolution layer of each stage and feeds them into a pyramid feature fusion module. The fusion module uses convolution, deconvolution, dense skip connections, concatenation, and 1 x 1 convolution to produce five fused feature maps: Dec-1s, Dec-2s, Dec-4s, Dec-8s, and Dec-16s.

The global context attention module combines adjacent-resolution feature maps by using global pooling over the lower-resolution map to weight the higher-resolution map, then upsamples and adds the lower-resolution map. Boundary refinement blocks operate as residual refinement structures for coarse score maps. Deep supervision applies per-pixel cross-entropy losses to the five resolution branches, and test-time prediction fuses outputs from these branches.

## Dataset

[[NEU-SEG]] is introduced as a pixel-wise segmentation dataset for hot-rolled steel strip surface defects. The paper starts from the NEU surface defect database, which contains six classes with 300 images per class at 200 x 200 resolution and tight-fitting bounding-box annotations. For pixel-wise segmentation, the paper selects three typical defects: inclusion, patches, and scratches. Pixel-wise labels are created with LabelMe, and the resulting dataset is named NEU-Seg.

The paper also evaluates on DAGM 2007, MT defect, and a road defect dataset. DAGM 2007 has artificial texture-background defects; MT defect has 1,344 magnetic-tile defect images with pixel-level labels; the road defect dataset includes crack and inlaid-patch classes.

## Evidence

The abstract reports PGA-Net performance on four real-world defect datasets using mean intersection over union: 82.15% on NEU-Seg, 74.78% on DAGM 2007, 71.31% on MT defect, and 79.54% on Road defect.

For NEU-Seg, the paper reports that PGA-Net performs better than SegNet, PSPNet, DeepLab, RefineNet, and FCN in the compared visual and quantitative results. The text states that NEU-Seg contains low contrast, intraclass appearance variation, and interclass similarity, making it challenging for hot-rolled strip steel surface detection.

The paper reports average test throughput of 41-49 fps/s across the evaluated datasets. It also reports failure cases where PGA-Net misses parts of defect regions or mistakes strong image changes for defects, attributing these errors to limited dataset size/diversity and model generalization limits.

## Performance Metrics

- [[mIoU]]: primary segmentation metric; PGA-Net reports 82.15% on [[NEU-SEG]].
- [[Mean pixel accuracy]]: reported as an evaluation metric, but the extracted text does not expose exact table values.
- [[FPS]]: throughput metric; the paper reports 41-49 fps/s for testing each image across the four datasets.

## ML/DL Extraction

- Task formulation: multi-class pixel-wise semantic segmentation of industrial surface defects.
- Inputs: cropped or resized defect images; NEU-Seg images are 200 x 200 before training-time extraction.
- Outputs: pixel-wise class maps for defect categories.
- Architecture: VGG-16 feature extraction module, pyramid feature fusion, global context attention, boundary refinement, and deep supervision.
- Objective/loss: per-pixel cross-entropy applied to five resolution branches.
- Optimizer/training setup: base learning rate 1e-5, decay 0.005, maximum 100k iterations, mini-batch size 5.
- Initialization: VGG-16 parameters from ImageNet pretrained model; other convolutional layers initialized with Xavier scheme.
- Augmentation: crop all datasets to 200 x 200; rotate cropped images by 90, 180, and 270 degrees; delete samples where defect area is less than 10%; randomly extract 192 x 192 areas and horizontal reflections during training.
- Compute: TensorFlow in PyCharm on Ubuntu 16.04 with an NVIDIA GTX TITAN GPU with 12 GB memory.
- Artifacts: NEU-Seg host is available from the NEU surface defect database page; code is not reported in the paper text.

## Limitations

- The paper states that some defects are missed or wrongly detected because of limited dataset size and diversity.
- The model can be oversensitive to image changes when defect regions change strongly.
- The reported speed is acceptable for real detection in the paper, but further optimization is needed for real-time and high-accuracy requirements.
- Training and test samples require labels, which is time-consuming.

## Connections

### Graph Hubs

- Tasks: [[Defect segmentation]], [[Metallic surface defect detection]]
- Methods: [[PGA-Net]], [[VGG-16]], [[Segmentation Models]]
- Datasets: [[NEU-SEG]], [[DAGM2007]], [[Magnetic Tile Defects]]
- Domains: [[Metal inspection]]
- Metrics: [[mIoU]], [[Mean pixel accuracy]], [[FPS]]

### Shares dataset

- [[NEU-SEG]]: introduced by this paper as a pixel-wise annotated three-class steel strip defect segmentation dataset.
- [[DAGM2007]]: used as a texture-defect segmentation benchmark.
- [[Magnetic Tile Defects]]: used as a magnetic-tile surface defect segmentation benchmark.

### Shares task

- [[Defect segmentation]]: PGA-Net predicts pixel-level defect masks.
- [[Metallic surface defect detection]]: NEU-Seg covers hot-rolled steel strip surface defects.

### Shares method

- [[PGA-Net]]: central segmentation architecture proposed by the paper.
- [[VGG-16]]: used as the pretrained feature extraction backbone.
- [[Segmentation Models]]: PGA-Net is a CNN-based semantic segmentation model.

### Shares metric

- [[mIoU]]: primary reported segmentation metric.
- [[Mean pixel accuracy]]: reported alongside mIoU.
- [[FPS]]: reported for average test speed.

### Application/domain

- [[Metal inspection]]: NEU-Seg and the NEU source imagery concern hot-rolled strip steel defects.

### Follow-up reading

- [[2022 - FDSNet An Accurate Real-Time Surface Defect Segmentation Network]]: later evaluates a real-time segmentation network on [[NEU-SEG]].

## Questions

- What exact split files are distributed with NEU-Seg, if any?
- What license applies to the NEU-Seg GitHub release and the underlying NEU imagery?
- Are the table values for mean pixel accuracy recoverable from a cleaner PDF extraction?
