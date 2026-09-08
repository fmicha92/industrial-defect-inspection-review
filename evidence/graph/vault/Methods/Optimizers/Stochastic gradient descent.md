---
title: "Stochastic gradient descent"
aliases:
  - "SGD"
  - "SGD with momentum"
  - "Nesterov momentum"
tags:
  - method
  - optimizer
---
# Stochastic Gradient Descent

## Definition

Stochastic gradient descent updates parameters using gradients computed from random examples or minibatches rather than the full objective.

## Why It Matters

SGD is the baseline first-order optimizer against which Adam and residual-network training are compared in the foundational papers processed here.

## Used In These Papers

- [[2020 - Segmentation-Based Deep-Learning Approach for Surface-Defect Detection]] trains the proposed segmentation and decision networks with SGD without momentum.
- [[2015 - Adam A Method for Stochastic Optimization]] compares Adam with SGD using Nesterov momentum.
- [[2016 - Deep Residual Learning for Image Recognition]] trains residual networks with SGD, momentum 0.9, weight decay 0.0001, and minibatch size 256.
- [[2021 - Mixed Supervision for Surface-Defect Detection From Weakly to Fully Supervised Learning]] trains the mixed-supervision defect detector with SGD without momentum or weight decay.

## Related Concepts

- [[Optimizers]]
- [[Adam]]
- [[AdaGrad]]
