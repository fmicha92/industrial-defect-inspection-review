---
title: "Transformer"
aliases:
  - "The Transformer"
  - "Transformer architecture"
tags:
  - method
  - model
---
# Transformer

## Definition

The Transformer is an encoder-decoder sequence transduction architecture built from stacked multi-head self-attention and position-wise feed-forward layers, without recurrence or convolution.

## Why It Matters

The architecture reduces sequential computation during training and shortens the path length between sequence positions, enabling faster parallel training for machine translation.

## Used In These Papers

- [[2017 - Attention Is All You Need]] introduces the Transformer and reports state-of-the-art WMT 2014 English-German and English-French translation results.
- [[2019 - BERT Pre-training of Deep Bidirectional Transformers for Language Understanding]] uses Transformer encoders as the backbone for BERT.

## Related Concepts

- [[Transformers]]
- [[Multi-head attention]]
- [[Self-attention]]
- [[Positional encoding]]
- [[Sequence-to-sequence learning]]

