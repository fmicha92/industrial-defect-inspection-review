---
title: "Parzen window log-likelihood"
aliases:
  - "Parzen-window log-likelihood"
  - "Parzen density estimate log-likelihood"
tags:
  - metric
concept_type: metric
---

# Parzen window log-likelihood

## Definition

Parzen window log-likelihood estimates a sample-generating model's density indirectly by fitting a Gaussian Parzen-window density to generated samples and evaluating test examples under that fitted density. Higher log-likelihood estimates indicate that test data receive higher probability under the fitted sample density.

## Why It Matters

The original [[2014 - Generative Adversarial Nets]] paper uses this metric because the adversarial generator can sample but does not explicitly represent `p_g(x)`. The paper also notes that this estimator has high variance and performs poorly in high-dimensional spaces.

## Used In These Papers

- [[2014 - Generative Adversarial Nets]] reports Parzen-window log-likelihood estimates on MNIST and the Toronto Face Database.
- [[2015 - Deep Unsupervised Learning using Nonequilibrium Thermodynamics]] uses the Parzen-window code from Goodfellow et al. 2014 for MNIST log-likelihood comparison with prior generative models.

## Related Concepts

- [[Generative quality metrics]]
- [[GAN]]
- [[Generative Models]]
