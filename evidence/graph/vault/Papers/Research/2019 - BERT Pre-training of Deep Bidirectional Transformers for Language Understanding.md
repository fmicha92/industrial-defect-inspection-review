---
title: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
aliases:
  - "BERT Pre-training of Deep Bidirectional Transformers for Language Understanding"
paper_key: "doi:10.18653/v1/s17-2001"
paper_type: "research"
year: 2019
venue: "not reported"
authors:
  - "Jacob Devlin"
  - "Ming-Wei Chang"
  - "Kenton Lee"
  - "Kristina Toutanova"
status: "processed"
topics:
  - "language model pretraining"
  - "transformers"
tasks:
  - "[[Language understanding]]"
  - "[[Question answering]]"
datasets:
  - "[[GLUE]]"
  - "[[SQuAD v1.1]]"
  - "[[SQuAD v2.0]]"
  - "[[SWAG]]"
methods:
  - "[[BERT]]"
  - "[[Transformer]]"
  - "[[Masked language modeling]]"
  - "[[Next sentence prediction]]"
metrics:
  - "[[Accuracy]]"
  - "[[F1-score]]"
  - "[[Exact match]]"
primary_metric: "[[F1-score]]"
code: "https://github.com/google-research/bert"
data: "not reported"
arxiv: "1810.04805"
url: "https://arxiv.org/abs/1810.04805"
source_file: "paper-inbox/10_processed/Research/2019 - Devlin - BERT Pre-training of Deep Bidirectional Transformers for Language Understanding.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2019 - Devlin - BERT Pre-training of Deep Bidirectional Transformers for Language Understanding.md"
extracted_text: "paper-inbox/90_processing/text/2019 - Devlin - BERT Pre-training of Deep Bidirectional Transformers for Language Understanding.txt"
related_methods:
  - "[[BERT]]"
  - "[[Transformer]]"
  - "[[Masked language modeling]]"
  - "[[Next sentence prediction]]"
related_datasets:
  - "[[GLUE]]"
  - "[[SQuAD v1.1]]"
  - "[[SQuAD v2.0]]"
  - "[[SWAG]]"
related_tasks:
  - "[[Language understanding]]"
  - "[[Question answering]]"
---
# BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding

## Summary

Devlin, Chang, Lee, and Toutanova introduce [[BERT]], a Transformer-encoder representation model pretrained with [[Masked language modeling]] and [[Next sentence prediction]]. BERT fine-tunes with small task-specific output layers and reports state-of-the-art results across GLUE, SQuAD v1.1, SQuAD v2.0, and SWAG. The paper's ablations show that bidirectional MLM pretraining and model scale both matter.

## Paper Type

Research paper introducing a pretrained language representation model and evaluating it across multiple NLP benchmarks.

## Problem

Earlier fine-tuning approaches such as left-to-right language-model pretraining restrict the representation each token can use. This is especially limiting for sentence-pair and token-level tasks such as question answering, where both left and right context are useful.

## Contribution

- Introduces BERT as bidirectional Transformer encoder pretraining followed by task-specific fine-tuning.
- Uses masked language modeling to enable bidirectional token representations.
- Uses next sentence prediction to pretrain text-pair representations.
- Shows that a single pretrained model can be fine-tuned for many sentence-level and token-level tasks.

## Method

BERT packs one or two text segments into a Transformer encoder input with segment embeddings and a `[CLS]` aggregate token. Pretraining combines MLM and NSP. During fine-tuning, GLUE tasks use the final `[CLS]` vector with a classification layer; SQuAD predicts start and end span positions; SWAG scores four candidate continuations.

## Evidence

| Evaluation | Dataset | Metric | Reported value |
|---|---|---|---|
| BERTLARGE | [[GLUE]] | average excluding WNLI | 82.1 versus prior state of the art 74.0 and OpenAI GPT 75.1 in Table 1. |
| BERTLARGE | MNLI | accuracy | 86.7/85.9 matched/mismatched. |
| BERTLARGE single + TriviaQA | [[SQuAD v1.1]] test | EM/F1 | 87.4 EM, 93.2 F1. |
| BERTLARGE single | [[SQuAD v2.0]] test | EM/F1 | 80.0 EM, 83.1 F1. |
| BERTLARGE | [[SWAG]] test | accuracy | 86.3 test accuracy; OpenAI GPT reports 78.0. |
| Pretraining ablation | BERTBASE | dev metrics | Removing NSP hurts QNLI, MNLI, and SQuAD; left-to-right pretraining hurts all listed tasks, especially MRPC and SQuAD. |

## ML/DL Extraction

- Task formulation: general language representation pretraining followed by fine-tuning.
- Architecture: Transformer encoder, with BERTBASE and BERTLARGE variants.
- Objectives: masked language modeling and next sentence prediction during pretraining; task-specific classification/span losses during fine-tuning.
- Training recipe: GLUE fine-tuning uses batch size 32 and 3 epochs; SQuAD v1.1 uses learning rate 5e-5 and batch size 32; SQuAD v2.0 uses 2 epochs, learning rate 5e-5, batch size 48; SWAG uses 3 epochs, learning rate 2e-5, batch size 16.
- Evaluation protocol: server test results for GLUE and SQuAD; ablations over pretraining objectives and model size.
- Compute: fine-tuning can be replicated in at most 1 hour on a single Cloud TPU or a few hours on a GPU from the pretrained model; pretraining compute is not in the excerpted result section.
- Artifacts: code and pretrained models reported at https://github.com/google-research/bert.

## Limitations

- Fine-tuning BERTLARGE is reported as sometimes unstable on small datasets, requiring random restarts.
- The paper's venue is not reported in the extracted source text.
- The source reports strong benchmark gains but does not deeply analyze data contamination or social bias.

## Connections

### Graph Hubs

- Tasks: [[Language understanding]], [[Question answering]]
- Methods: [[BERT]], [[Transformer]], [[Masked language modeling]], [[Next sentence prediction]], [[Language model pretraining]]
- Datasets: [[GLUE]], [[SQuAD v1.1]], [[SQuAD v2.0]], [[SWAG]]
- Domains: [[Natural language processing]]
- Metrics: [[Accuracy]], [[F1-score]], [[Exact match]]

| Link | Relation | Rationale |
|---|---|---|
| [[2017 - Attention Is All You Need]] | Builds on | BERT uses Transformer encoders introduced by the Transformer paper. |
| [[Masked language modeling]] | Shares method | MLM is the central bidirectional pretraining objective. |
| [[Next sentence prediction]] | Shares method | NSP is used for text-pair pretraining and ablated. |
| [[GLUE]] | Shares dataset | GLUE is the broad sentence-level evaluation benchmark. |
| [[SQuAD v1.1]] and [[SQuAD v2.0]] | Shares task | SQuAD evaluates span question answering. |

## Questions

- Which BERT gains come from bidirectionality, data scale, model size, and fine-tuning protocol respectively?
- How robust are NSP benefits outside the task set evaluated here?
