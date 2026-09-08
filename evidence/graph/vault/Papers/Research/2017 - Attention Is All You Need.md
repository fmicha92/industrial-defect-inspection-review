---
title: "Attention Is All You Need"
paper_key: "arxiv:1222.20000"
paper_type: "research"
year: 2017
venue: "NeurIPS 2017"
authors:
  - "Ashish Vaswani"
  - "Noam Shazeer"
  - "Niki Parmar"
  - "Jakob Uszkoreit"
  - "Llion Jones"
  - "Aidan N. Gomez"
  - "Lukasz Kaiser"
  - "Illia Polosukhin"
status: "processed"
topics:
  - "transformers"
  - "machine translation"
tasks:
  - "[[Machine translation]]"
  - "[[Sequence-to-sequence learning]]"
datasets:
  - "[[WMT 2014 English-German]]"
  - "[[WMT 2014 English-French]]"
methods:
  - "[[Transformer]]"
  - "[[Self-attention]]"
  - "[[Multi-head attention]]"
  - "[[Positional encoding]]"
  - "[[Adam]]"
metrics:
  - "[[BLEU]]"
primary_metric: "[[BLEU]]"
code: "https://github.com/tensorflow/tensor2tensor"
data: "not reported"
source_file: "paper-inbox/10_processed/Research/2017 - Vaswani - Attention Is All You Need.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2017 - Vaswani - Attention Is All You Need.md"
extracted_text: "paper-inbox/90_processing/text/2017 - Vaswani - Attention Is All You Need.txt"
related_methods:
  - "[[Transformer]]"
  - "[[Self-attention]]"
  - "[[Multi-head attention]]"
  - "[[Positional encoding]]"
related_datasets:
  - "[[WMT 2014 English-German]]"
  - "[[WMT 2014 English-French]]"
related_tasks:
  - "[[Machine translation]]"
---
# Attention Is All You Need

## Summary

Vaswani et al. introduce the [[Transformer]], an encoder-decoder sequence transduction architecture based entirely on attention mechanisms. The model replaces recurrent and convolutional sequence layers with stacked [[Multi-head attention]], position-wise feed-forward networks, residual connections, layer normalization, and [[Positional encoding]]. On WMT 2014 translation, the Transformer reaches higher BLEU than prior recurrent and convolutional systems while training substantially faster.

## Paper Type

Research paper introducing a neural architecture and evaluating it on machine translation.

## Problem

Recurrent sequence transduction models are hard to parallelize across positions, making long-sequence training slow. Convolutional alternatives improve parallelism but require longer paths to connect distant positions. The paper targets sequence transduction models that preserve global dependency modeling while improving training parallelism.

## Contribution

- Introduces the Transformer as a recurrence-free and convolution-free encoder-decoder architecture.
- Defines scaled dot-product attention and multi-head attention as the core computation.
- Uses sinusoidal positional encodings to represent order without recurrent computation.
- Shows state-of-the-art WMT 2014 translation quality with substantially lower estimated training cost than prior systems.

## Method

The Transformer encoder uses six identical layers, each containing multi-head self-attention and a position-wise feed-forward network with residual connections and layer normalization. The decoder also uses six layers, adding encoder-decoder attention and masked self-attention so generation remains autoregressive. The base model uses dmodel = 512, dff = 2048, 8 heads, dropout 0.1, label smoothing 0.1, and Adam with beta1 = 0.9, beta2 = 0.98, epsilon = 1e-9, and 4000 warmup steps.

## Evidence

| Result | Dataset | Metric | Reported value |
|---|---|---|---|
| Transformer big | [[WMT 2014 English-German]] | [[BLEU]] | 28.4 BLEU, more than 2 BLEU over prior reported ensembles. |
| Transformer base | [[WMT 2014 English-German]] | [[BLEU]] | 27.3 BLEU. |
| Transformer big | [[WMT 2014 English-French]] | [[BLEU]] | 41.0 BLEU, outperforming prior single models. |
| Training time, base | WMT translation | time | 100,000 steps in about 12 hours on 8 P100 GPUs. |
| Training time, big | WMT translation | time | 300,000 steps in about 3.5 days on 8 P100 GPUs. |
| Ablation | English-German dev set | BLEU | One attention head is 0.9 BLEU worse than the best listed base setting; learned positional embeddings are nearly identical to sinusoidal encodings. |

## ML/DL Extraction

- Task formulation: sequence-to-sequence translation.
- Inputs/outputs: source token sequence to target token sequence.
- Architecture: encoder-decoder Transformer with self-attention, encoder-decoder attention, feed-forward sublayers, residual connections, layer normalization, learned embeddings, and positional encodings.
- Objective/loss: next-token prediction with label smoothing.
- Training data: about 4.5M English-German sentence pairs and 36M English-French sentence pairs.
- Training recipe: Adam, warmup then inverse-square-root learning-rate decay, dropout, label smoothing, checkpoint averaging, beam size 4, length penalty 0.6.
- Compute: 8 NVIDIA P100 GPUs.
- Artifacts: code reported available at https://github.com/tensorflow/tensor2tensor.

## Limitations

- Full self-attention has O(n^2 d) per-layer complexity, which the paper flags as a concern for very long sequences.
- The primary experiments are machine translation; the conclusion proposes but does not demonstrate applications to images, audio, or video.
- Generation remains autoregressive in the decoder.

## Connections

### Graph Hubs

- Tasks: [[Machine translation]], [[Sequence-to-sequence learning]]
- Methods: [[Transformer]], [[Self-attention]], [[Multi-head attention]], [[Positional encoding]], [[Adam]]
- Datasets: [[WMT 2014 English-German]], [[WMT 2014 English-French]]
- Domains: [[Natural language processing]]
- Metrics: [[BLEU]]

| Link | Relation | Rationale |
|---|---|---|
| [[Adam]] | Uses method | Transformer training uses Adam with non-default beta2 and epsilon plus warmup scheduling. |
| [[2019 - BERT Pre-training of Deep Bidirectional Transformers for Language Understanding]] | Builds on | BERT uses Transformer encoders for bidirectional language representation pretraining. |
| [[Machine translation]] | Shares task | The paper's core evidence is WMT 2014 machine translation. |
| [[BLEU]] | Shares metric | BLEU is the primary reported translation metric. |

## Questions

- How do local or sparse attention variants trade off quality and complexity for longer sequences?
- Which parts of the architecture matter most outside text sequence transduction?
