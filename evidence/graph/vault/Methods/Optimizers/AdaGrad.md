---
title: "AdaGrad"
aliases:
  - "Adaptive Gradient"
tags:
  - method
  - optimizer
---
# AdaGrad

## Definition

AdaGrad is an adaptive gradient optimizer that scales parameter updates using accumulated squared gradients, making it useful for sparse features and sparse gradients.

## Why It Matters

Adam is explicitly positioned as combining AdaGrad's sparse-gradient advantages with RMSProp's non-stationary-objective behavior.

## Used In These Papers

- [[2015 - Adam A Method for Stochastic Optimization]] compares Adam with AdaGrad on MNIST, IMDB bag-of-words, multilayer neural networks, and CIFAR-10 convolutional models.

## Related Concepts

- [[Optimizers]]
- [[Adam]]
- [[Stochastic gradient descent]]

