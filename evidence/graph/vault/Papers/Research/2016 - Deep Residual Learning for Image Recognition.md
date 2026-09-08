---
title: "Deep Residual Learning for Image Recognition"
paper_key: "arxiv:2250.01000"
paper_type: "research"
year: 2016
venue: "CVPR 2016"
authors:
  - "Kaiming He"
  - "Xiangyu Zhang"
  - "Shaoqing Ren"
  - "Jian Sun"
status: "processed"
topics:
  - "residual networks"
  - "image classification"
tasks:
  - "[[Image classification]]"
  - "[[Object detection]]"
datasets:
  - "[[ImageNet]]"
  - "[[CIFAR-10]]"
  - "[[COCO]]"
methods:
  - "[[Residual network]]"
  - "[[Stochastic gradient descent]]"
metrics:
  - "[[Top-1 error]]"
  - "[[Top-5 error]]"
primary_metric: "[[Top-5 error]]"
code: "not reported"
data: "not reported"
source_file: "paper-inbox/10_processed/Research/2016 - He - Deep Residual Learning for Image Recognition.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2016 - He - Deep Residual Learning for Image Recognition.md"
extracted_text: "paper-inbox/90_processing/text/2016 - He - Deep Residual Learning for Image Recognition.txt"
related_methods:
  - "[[Residual network]]"
  - "[[ResNet-18]]"
  - "[[ResNet50]]"
related_datasets:
  - "[[ImageNet]]"
  - "[[CIFAR-10]]"
  - "[[COCO]]"
related_tasks:
  - "[[Image classification]]"
  - "[[Object detection]]"
---
# Deep Residual Learning for Image Recognition

## Summary

He, Zhang, Ren, and Sun introduce [[Residual network|residual networks]], which train deep neural networks by learning residual functions with shortcut connections. The paper shows that deeper plain networks can suffer higher training error, while residual counterparts are easier to optimize and improve with depth. The 152-layer ResNet ensemble reports 3.57% ImageNet test-set top-5 error and underpins winning ILSVRC and COCO 2015 submissions.

## Paper Type

Research paper introducing a computer-vision architecture and evaluating it on classification, detection, localization, and segmentation tasks.

## Problem

Simply stacking more layers can produce a degradation problem: accuracy saturates and then worsens, and deeper plain networks can have higher training error than shallower counterparts. The paper argues this is an optimization problem rather than ordinary overfitting.

## Contribution

- Reformulates deep-network blocks to learn residual mappings `F(x) = H(x) - x` and output `F(x) + x`.
- Uses identity shortcut connections that add no extra parameters or computational complexity when dimensions match.
- Demonstrates that 34-layer residual networks optimize better than 34-layer plain networks on ImageNet.
- Scales residual networks to 152 layers on ImageNet and more than 100 layers on CIFAR-10.

## Method

Residual blocks add shortcut connections around stacked convolutional layers. When dimensions match, the shortcut is an identity mapping; when dimensions change, the paper considers zero padding or projection shortcuts. ImageNet models are trained from scratch with batch normalization, SGD minibatch size 256, initial learning rate 0.1 divided by 10 on plateaus, momentum 0.9, weight decay 0.0001, and no dropout.

## Evidence

| Evaluation | Dataset | Metric | Reported value |
|---|---|---|---|
| Plain 18-layer vs 34-layer | [[ImageNet]] validation | [[Top-1 error]] | 18-layer plain 27.94%; 34-layer plain 28.54%, showing degradation. |
| ResNet 18-layer vs 34-layer | [[ImageNet]] validation | [[Top-1 error]] | ResNet-18 27.88%; ResNet-34 25.03%, showing depth gains under residual learning. |
| Model complexity | ImageNet architecture | FLOPs | 34-layer baseline 3.6B FLOPs, 18% of VGG-19's 19.6B FLOPs. |
| Deep residual ensemble | ImageNet test set | [[Top-5 error]] | 3.57%; won ILSVRC 2015 classification. |
| Transfer to detection/segmentation | [[COCO]] and ImageNet tasks | relative improvement | The paper reports 28% relative improvement on COCO object detection from deep residual representations. |

## ML/DL Extraction

- Task formulation: image classification and visual recognition transfer to detection, localization, and segmentation.
- Architecture: residual CNNs from 18 to 152 layers, with two-layer or bottleneck residual blocks.
- Objective/loss: softmax classification loss for ImageNet; detection/segmentation details are referenced through competition submissions.
- Training recipe: scale augmentation, random 224 x 224 crops, horizontal flips, color augmentation, batch normalization, SGD, momentum, weight decay.
- Evaluation protocol: ImageNet validation/test top-1/top-5 error; CIFAR-10 depth experiments; detection/segmentation competition evidence.
- Compute: exact hardware not reported.
- Artifacts: code not reported.

## Limitations

- The paper demonstrates residual learning primarily in computer vision.
- The degradation problem is empirically documented, but the paper leaves its deeper theoretical cause for future study.
- Some detection and segmentation evidence is summarized through competition results rather than fully detailed experimental tables in the extracted source.

## Connections

### Graph Hubs

- Tasks: [[Image classification]], [[Object detection]]
- Methods: [[Residual network]], [[ResNet-18]], [[ResNet50]], [[Stochastic gradient descent]]
- Datasets: [[ImageNet]], [[CIFAR-10]], [[COCO]]
- Domains: [[General computer vision]]
- Metrics: [[Top-1 error]], [[Top-5 error]]

| Link | Relation | Rationale |
|---|---|---|
| [[ResNet-18]] | Model family member | The paper evaluates 18-layer residual networks on ImageNet. |
| [[ResNet50]] | Model family member | The paper defines bottleneck residual networks including 50-layer variants. |
| [[ImageNet]] | Shares dataset | ImageNet classification is the central benchmark. |
| [[COCO]] | Follow-up task evidence | Residual representations improve COCO object detection and support competition submissions. |
| [[Stochastic gradient descent]] | Uses method | Residual networks are trained with SGD, momentum, and weight decay. |

## Questions

- Which residual block design is best for non-vision sequence or tabular problems?
- How much of the improvement comes from residual optimization versus batch normalization and training recipe choices?
