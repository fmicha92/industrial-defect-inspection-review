---
title: "Pix2Pix"
aliases:
  - "Pix2Pix GAN"
tags:
  - concept
  - method
---

# Pix2Pix

## Definition

Pix2Pix is a GAN-based image-to-image translation method used for motion deblurring in aircraft engine inspection. The paper notes do not provide its architecture details, so those details are `not reported` here.

## Why It Matters

The aircraft engine inspection paper treats image quality as part of the defect detection pipeline. Pix2Pix is relevant because poor borescope imagery can affect downstream segmentation quality.

## Used In These Papers

- [[2023 - A Deep-Learning-Based Approach for Aircraft Engine Defect Detection]] uses a hybrid deblurring approach combining computer vision preprocessing and Pix2Pix GAN.

## Related Concepts

- [[GAN]]
- [[Generative Models]]
- [[Learned generative synthesis]]
- [[Industrial visual inspection]]
- [[Defect segmentation]]
