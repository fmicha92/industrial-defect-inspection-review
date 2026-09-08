---
title: "AdaMax"
aliases:
  - "AdaMax optimizer"
tags:
  - method
  - optimizer
---
# AdaMax

## Definition

AdaMax is an Adam variant derived by taking Adam's adaptive update rule to the infinity-norm limit.

## Why It Matters

The Adam paper presents AdaMax as a numerically stable extension with a simpler update-magnitude bound than Adam.

## Used In These Papers

- [[2015 - Adam A Method for Stochastic Optimization]] introduces AdaMax with default tested settings alpha = 0.002, beta1 = 0.9, and beta2 = 0.999.

## Related Concepts

- [[Adam]]
- [[Optimizers]]

