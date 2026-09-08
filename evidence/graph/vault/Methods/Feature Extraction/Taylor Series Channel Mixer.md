---
title: "Taylor Series Channel Mixer"
aliases:
  - "TSCM"
tags:
  - method
  - feature-extraction
---

# Taylor Series Channel Mixer

## Definition

Taylor Series Channel Mixer is the image-mixing module introduced in [[2025 - A Dataset for Surface Defect Detection on Complex Structured Parts Based on Photometric Stereo]]. It combines multi-angle illumination images into RGB pseudo-color images using a fourth-order Taylor-series nonlinear layer followed by a linear layer.

## Why It Matters

TSCM converts multi-channel strobe images into detector-ready pseudo-color images while preserving depth-related cues from [[Photometric stereo]]. In the paper's ablation, TSCM improves reconstruction PSNR by about 6.02 to 6.03 compared with simpler mixing variants.

## Used In These Papers

- [[2025 - A Dataset for Surface Defect Detection on Complex Structured Parts Based on Photometric Stereo]] trains TSCM with a VQ-VAE-style reconstruction objective and uses it to produce [[MSDD]] mixed images.

## Related Concepts

- [[Stroboscopic Illuminant Image Acquisition]]
- [[Phase-Invariant Feature Module]]
- [[Photometric stereo]]
- [[SSIM]]
