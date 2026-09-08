---
title: "Log likelihood"
aliases:
  - "Model log likelihood"
  - "Likelihood"
tags:
  - metric
  - generative-quality
---

# Log likelihood

## Definition

Log likelihood measures the probability a generative model assigns to observed data. Higher values indicate that the model assigns more probability mass to the evaluated examples, though reported units and estimators vary by paper.

## Direction

Higher is better unless the paper reports negative log likelihood or codelength.

## Used In These Papers

- [[2015 - Deep Unsupervised Learning using Nonequilibrium Thermodynamics]] reports a lower bound on log likelihood for diffusion probabilistic models across toy, binary, MNIST, CIFAR-10, bark, and dead-leaves datasets.

## Related Metrics

- [[Bits per dimension]]
- [[Parzen window log-likelihood]]
- [[Generative quality metrics]]
