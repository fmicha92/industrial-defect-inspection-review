---
title: "Multi-head attention"
aliases:
  - "multi-headed self-attention"
  - "scaled dot-product multi-head attention"
tags:
  - method
---
# Multi-Head Attention

## Definition

Multi-head attention projects queries, keys, and values into multiple learned subspaces, applies attention in parallel, then concatenates and projects the resulting head outputs.

## Why It Matters

Multiple heads let the Transformer attend to information from different representation subspaces and positions; the base Transformer uses 8 heads with key and value dimensions of 64.

## Used In These Papers

- [[2017 - Attention Is All You Need]] introduces the multi-head attention module used throughout the Transformer.
- [[2019 - BERT Pre-training of Deep Bidirectional Transformers for Language Understanding]] inherits multi-head attention through the Transformer encoder architecture.

## Related Concepts

- [[Self-attention]]
- [[Transformer]]

