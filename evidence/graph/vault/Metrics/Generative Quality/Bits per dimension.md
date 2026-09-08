---
title: "Bits per dimension"
aliases:
  - "bits/dim"
  - "bits per dim"
  - "negative log likelihood in bits per dimension"
tags:
  - metric
  - generative-quality
---

# Bits per dimension

## Definition

Bits per dimension is a codelength-style negative log likelihood measure for image generative models. Lower values indicate a shorter code for the evaluated data under the model.

## Direction

Lower is better.

## Used In These Papers

- [[2020 - Denoising Diffusion Probabilistic Models]] reports CIFAR-10 negative log likelihood in bits/dim and analyzes diffusion-model rate as bits/dim in progressive coding.

## Related Metrics

- [[Log likelihood]]
- [[FID]]
- [[Inception Score]]
- [[Generative quality metrics]]
