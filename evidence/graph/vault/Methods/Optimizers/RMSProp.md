---
title: "RMSProp"
aliases:
  - "RMSProp optimizer"
tags:
  - method
  - optimizer
---
# RMSProp

## Definition

RMSProp is an adaptive stochastic optimizer that uses an exponential moving average of squared gradients to scale updates.

## Why It Matters

The Adam paper treats RMSProp as an important precursor for non-stationary objectives and notes that removing Adam's bias-correction terms produces a RMSProp-with-momentum-like variant.

## Used In These Papers

- [[2015 - Adam A Method for Stochastic Optimization]] compares Adam against RMSProp and shows that bias correction matters when beta2 is close to 1.

## Related Concepts

- [[Optimizers]]
- [[Adam]]
- [[AdaGrad]]

