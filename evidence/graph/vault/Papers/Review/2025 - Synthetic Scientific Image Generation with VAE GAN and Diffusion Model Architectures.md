---
title: "Synthetic Scientific Image Generation with VAE, GAN, and Diffusion Model Architectures"
aliases:
  - "Synthetic Scientific Image Generation with VAE, GAN, and Diffusion Model Architectures"
paper_key: "doi:10.3390/jimaging11080252"
paper_type: review
year: 2025
venue: "Journal of Imaging"
authors:
  - "Sordo"
  - "Chagnon"
  - "Hu"
  - "Donatelli"
  - "Andeer"
  - "Nico"
  - "Northen"
  - "Ushizima"
status: processed
processed_at: 2026-05-29
topics:
  - scientific image generation
  - generative AI
  - synthetic data
tasks:
  - "[[Scientific image generation]]"
domains:
  - "[[Scientific imaging]]"
  - "[[Nondestructive testing]]"
datasets:
  - "CMC microCT dataset"
  - "EcoFAB root image dataset"
  - "Rocks microCT dataset"
dataset_sizes:
  - "CMC: 937 images, 2560 x 2560"
  - "EcoFAB: 375 images, 2039 x 3000"
  - "Rocks: 502 images, 1813 x 1830"
splits:
  - "not reported"
modalities:
  - "microCT"
  - "high-resolution root scans"
methods:
  - "[[Variational Autoencoder]]"
  - "[[GAN]]"
  - "[[Diffusion models]]"
  - "[[Learned generative synthesis]]"
model_family:
  - "[[Generative Models]]"
architectures:
  - "DCGAN"
  - "StyleGAN"
  - "DALL-E 2"
  - "DALL-E 3"
  - "Stable unCLIP"
  - "LEDITS++"
  - "InstructPix2Pix"
  - "ControlNet"
  - "DiffEdit"
losses:
  - "ELBO"
  - "adversarial loss"
  - "cycle consistency loss"
training_regime: "GAN models trained from scratch per dataset; diffusion/API models used for inference without task-specific fine-tuning"
augmentation:
  - "[[Synthetic data generation]]"
synthetic_data: "scientific image synthesis for data augmentation, simulation, and hypothesis generation"
metrics:
  - "[[SSIM]]"
  - "[[LPIPS]]"
  - "[[FID]]"
  - "[[CLIPScore]]"
primary_metric: "not reported"
metric_definitions:
  - "SSIM: structural similarity for paired image fidelity"
  - "LPIPS: learned perceptual similarity for paired images"
  - "FID: distributional similarity between real and generated image sets"
  - "CLIPScore: image-text alignment for prompt-conditioned generation"
baselines:
  - "DCGAN"
  - "StyleGAN"
  - "DALL-E 2"
  - "DALL-E 3"
  - "ControlNet"
  - "Stable unCLIP"
  - "InstructPix2Pix"
  - "LEDITS++"
  - "DiffEdit"
  - "DALL-E 2 edit"
benchmarks:
  - "not reported"
evaluation_protocol: "Quantitative metrics plus qualitative expert visual assessment on CMC, EcoFAB, and Rocks scientific image datasets."
parameters: "not reported"
compute: "NVIDIA A100 GPUs; DCGAN used 1 GPU, StyleGAN used 4 GPUs, API inference used 1 GPU"
hardware: "NVIDIA A100 GPUs"
training_time: "DCGAN: 40 min per iteration; StyleGAN: 4 h 30 min per iteration"
inference_cost: "Diffusion model API inference: 4 to 8 min per iteration; DALL-E API inference: 10 to 15 s"
url: "https://doi.org/10.3390/jimaging11080252"
pdf: "paper-inbox/10_processed/Review/2025 - Sordo - Synthetic Scientific Image Generation with VAE GAN and Diffusion Model Architectures.pdf"
code: "https://github.com/lbl-camera/genAI"
data: "Reported as available through the project GitHub with links to public archived datasets after acceptance."
doi: "10.3390/jimaging11080252"
arxiv: "not reported"
related_papers: []
related_concepts:
  - "[[Scientific image generation]]"
  - "[[Synthetic data generation]]"
  - "[[Domain gap]]"
related_methods:
  - "[[Variational Autoencoder]]"
  - "[[GAN]]"
  - "[[Diffusion models]]"
  - "[[Learned generative synthesis]]"
related_datasets: []
related_domains:
  - "[[Scientific imaging]]"
  - "[[Nondestructive testing]]"
related_tasks:
  - "[[Scientific image generation]]"
related_benchmarks:
  - "not applicable"
concept_notes_created_or_updated:
  - "[[Scientific image generation]]"
  - "[[Scientific imaging]]"
  - "[[Variational Autoencoder]]"
  - "[[SSIM]]"
  - "[[CLIPScore]]"
source_file: "paper-inbox/10_processed/Review/2025 - Sordo - Synthetic Scientific Image Generation with VAE GAN and Diffusion Model Architectures.pdf"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2025 - Sordo - Synthetic Scientific Image Generation with VAE GAN and Diffusion Model Architectures.md"
extracted_text: "paper-inbox/90_processing/text/2025 - Sordo - Synthetic Scientific Image Generation with VAE GAN and Diffusion Model Architectures.txt"
artifact_status: "reported available; not independently verified"
tags:
  - paper
---

# Synthetic Scientific Image Generation with VAE, GAN, and Diffusion Model Architectures

## Summary

- The paper reviews [[Variational Autoencoder|VAEs]], [[GAN|GANs]], and [[Diffusion models]] for scientific image synthesis, then compares representative systems on scientific image datasets.
- The experiments use three domain-specific image collections: CMC microCT images, EcoFAB root scans, and rock microCT images.
- The main finding is that standard image-generation metrics are useful but insufficient for scientific validity: several models score well while producing artifacts, semantic drift, or scientifically implausible structures.

## Paper Type

- Type: review with comparative empirical evaluation.
- Why: The paper surveys generative image architectures and reports a controlled comparison of selected models across scientific image domains.

## Problem

- Task: [[Scientific image generation]].
- Setting: scientific imaging contexts where generated images must preserve domain-specific structure rather than only look plausible.
- Inputs: random noise, text prompts, source scientific images, semantic edit prompts, or masked image regions, depending on the model.
- Outputs: generated, edited, varied, or inpainted scientific images.
- Motivation: scientific image datasets can be scarce, expensive, instrument-specific, or difficult to annotate, making reliable synthetic image generation attractive for augmentation, simulation, and hypothesis generation.
- Assumptions: General-purpose generative models may not transfer cleanly to scientific imaging because their encoders and training data are dominated by natural images and web-scale image-text pairs.

## Contribution

- Claimed: A comparative analysis of VAE, GAN, and diffusion-based image synthesis architectures with emphasis on scientific relevance.
- Claimed: An empirical comparison over CMC, EcoFAB, and Rocks images using SSIM, LPIPS, FID, CLIPScore, and qualitative expert inspection.
- Shown: Editing-focused diffusion systems and StyleGAN often produce plausible images, but visual inspection identifies artifacts and scientific-fidelity failures that metrics alone miss.
- Inferred: The paper is most useful as a bridge between synthetic-data generation methods and scientific-image validation protocols.

## Method

- Core idea: Review major generative image model families and test representative models on scientific image generation, variation, and inpainting tasks.
- Architecture / algorithm: VAEs, GANs, diffusion models, transformer-conditioned diffusion models, and image editing/inpainting systems.
- Objective / loss: ELBO for VAEs; adversarial and cycle-consistency losses for GAN variants; denoising objectives for diffusion models; exact training losses for API systems are not reported.
- Optimization: not reported for API systems; GANs were trained from scratch for each dataset.
- Training data: CMC, EcoFAB, and Rocks images for GAN training; diffusion/API models were used in pretrained form without task-specific fine-tuning.
- Data pipeline: high-resolution scientific images were cropped or resized when required by fixed input resolutions.
- Augmentation / synthesis: synthesis from noise/text, image-to-image translation, semantic variation, and masked image editing.
- Inference: inference-only evaluation for pretrained diffusion/API models, with 1 to 3 outputs generated per input and roughly 1000 to 2000 total images per model.
- Complexity / deployment constraints: diffusion sampling was slower than DALL-E API inference; StyleGAN training required four A100 GPUs.

## ML / DL Extraction

### Task Formulation

- Input modality: microCT slices, high-resolution plant root scans, text prompts, masks, and source images.
- Output target: scientific images that preserve structural, perceptual, and semantic properties.
- Supervision: GAN models used dataset-specific training; pretrained diffusion/API models used zero-shot or prompt/image-conditioned inference.
- Objective: assess whether model outputs are visually realistic and scientifically meaningful.

### Model And Training

- Model family: [[Generative Models]].
- Architecture: DCGAN, StyleGAN, DALL-E 2, DALL-E 3, Stable unCLIP, LEDITS++, InstructPix2Pix, ControlNet, DiffEdit, and DALL-E 2 edit/variation modes.
- Parameters: not reported.
- Pretraining: diffusion/API systems were pretrained; training data details are not reported.
- Fine-tuning: no task-specific fine-tuning for diffusion/API systems.
- Losses: ELBO, adversarial loss, cycle consistency loss, and diffusion denoising objectives are described at the architecture level.
- Optimizer: not reported.
- Hyperparameters: not reported.
- Seeds: not reported.
- Training compute: DCGAN used 1 NVIDIA A100 GPU; StyleGAN used 4 NVIDIA A100 GPUs.

### Data

- Datasets: CMC, EcoFAB, and Rocks.
- Data source: LBNL facilities, including synchrotron microCT for rocks and fibers and EcoBOT scans for roots.
- Dataset size: CMC has 937 images at 2560 x 2560; EcoFAB has 375 images at 2039 x 3000; Rocks has 502 images at 1813 x 1830.
- Labels / annotations: not reported.
- Splits: not reported.
- Preprocessing: resizing, cropping, and fixed-resolution adaptation are reported.
- Augmentation: generated synthetic scientific images.
- Synthetic data: the evaluated outputs are synthetic images produced by the generative models.
- Leakage checks: not reported.
- License: article is CC BY; dataset license not reported.

### Evaluation

- Protocol: quantitative evaluation plus qualitative expert visual assessment across the three datasets.
- Used performance metrics: [[SSIM]], [[LPIPS]], [[FID]], and [[CLIPScore]].
- Primary metric: not reported.
- Metric definitions: SSIM and LPIPS are pairwise metrics; FID and CLIPScore are set-level or prompt-alignment metrics.
- Metric direction / units: higher SSIM and CLIPScore are better; lower LPIPS and FID are better.
- Baselines: DCGAN, StyleGAN, DALL-E 2/3, ControlNet, Stable unCLIP, InstructPix2Pix, LEDITS++, DiffEdit, and DALL-E 2 edit/variation.
- Benchmarks: not reported as formal benchmarks.
- Statistical tests: not reported.
- Failure cases: artifact generation, semantic drift, stylized outputs, weak structural preservation, and misleadingly high metric scores.

## Evidence

### Experimental Setup

- Datasets: CMC, EcoFAB, Rocks.
- Splits: not reported.
- Baselines: DCGAN, StyleGAN, DALL-E 2, DALL-E 3, ControlNet, Stable unCLIP, InstructPix2Pix, LEDITS++, DiffEdit, DALL-E 2 variation, and DALL-E 2 edit.
- Used performance metrics: SSIM, LPIPS, FID, and CLIPScore.
- Compute: NVIDIA A100 GPUs.
- Hardware: 1 A100 for DCGAN, 4 A100s for StyleGAN, 1 A100 for diffusion/API inference.
- Training time: DCGAN 40 min per iteration; StyleGAN 4 h 30 min per iteration.
- Inference cost: diffusion model API inference 4 to 8 min per iteration; DALL-E API inference 10 to 15 s.

### Main Results

| Result | Dataset / Task | Metric | Direction | Baseline | Paper result | Notes |
|---|---|---|---|---:|---:|---|
| DiffEdit had the best CMC FID among reported models | CMC / masked image editing | FID | lower | StyleGAN 77.374 | 39.945 | DiffEdit also had SSIM 0.664 +/- 0.076 and LPIPS 0.053 +/- 0.044. |
| LEDITS++ had strong CMC distributional and perceptual performance | CMC / image-to-image editing | FID / LPIPS | lower | DALL-E 2 edit FID 41.305 | FID 46.332; LPIPS 0.092 +/- 0.070 | Qualitative assessment found structural preservation but stylized output. |
| DiffEdit scored best on EcoFAB metrics but produced visual artifacts | EcoFAB / masked image editing | SSIM / LPIPS / FID | higher / lower / lower | DALL-E 2 edit FID 189.235 | SSIM 0.843 +/- 0.046; LPIPS 0.147 +/- 0.030; FID 64.686 | The paper says black or RGB artifacts made the metric result misleading. |
| StyleGAN produced the most plausible EcoFAB textures by visual assessment | EcoFAB / generation | FID | lower | DCGAN 305.426 | 90.520 | The paper reports muted color but realistic textures. |
| DALL-E 2 edit had the best overall balance on Rocks | Rocks / masked image editing | SSIM / LPIPS / FID | higher / lower / lower | DiffEdit FID 124.199 | SSIM 0.635 +/- 0.012; LPIPS 0.216 +/- 0.015; FID 75.104 | The paper describes realistic edits that maintain original content. |
| Text-to-image models generally underperformed | CMC, EcoFAB, Rocks / prompt generation | FID and visual inspection | lower | not applicable | DALL-E 2/3 FID values were typically high | The paper attributes failures to prompt misinterpretation and poor scientific-domain alignment. |

### Performance Metrics

| Metric | Used for | Definition / unit | Direction | Primary? | Notes |
|---|---|---|---|---|---|
| [[SSIM]] | paired structural fidelity | structural similarity between paired real and generated images | higher | no | Less meaningful for unconditional generation without paired references. |
| [[LPIPS]] | paired perceptual similarity | learned perceptual image distance | lower | no | Used with paired inference/editing outputs. |
| [[FID]] | distributional image realism/diversity | feature-distribution distance between real and generated image sets | lower | no | Emphasized for unconditional models. |
| [[CLIPScore]] | prompt-image alignment | image-text embedding similarity | higher | no | The paper reports poor alignment for scientific image domains. |

### Ablations

- No formal ablation study is reported.
- The comparison varies model family, task type, and input conditioning mode rather than isolating individual architecture components.

## Dataset / Benchmark Details

- Source: LBNL scientific imaging facilities and systems.
- Collection: CMC and Rocks are microCT image slices; EcoFAB images are high-resolution scans of plant roots from EcoBOT.
- Annotation: not reported.
- Size: CMC 937 images; EcoFAB 375 images; Rocks 502 images.
- Splits: not reported.
- Modalities: microCT and high-resolution optical scanning.
- License: dataset license not reported.
- Leakage risks: not reported.
- Bias / coverage: The paper emphasizes limited representation of these scientific image domains in web-scale training data.
- Maintenance: data and code are reported as available through the project GitHub with links to archived datasets.

## Review / Survey Details

- Scope: VAE, GAN, diffusion, and transformer-conditioned image-generation architectures for scientific image synthesis.
- Inclusion criteria: not reported as a systematic review protocol.
- Taxonomy: image generation from noise/text, image translation and semantic variation, and masked image inpainting.
- Major themes: controllability, structural fidelity, semantic alignment, metric limitations, scientific validation, and computational cost.
- Gaps: need for domain-adapted evaluation metrics, scientific image-text alignment, expert validation protocols, and fine-tuning strategies for specialized scientific data.

## Limitations

- Stated: standard metrics do not reliably capture scientific relevance or semantic validity.
- Stated: CLIP-like encoders and natural-image visual encoders are poorly aligned with specialized scientific image domains.
- Stated: diffusion models can be computationally expensive.
- Inferred: The pretrained API model comparison is sensitive to unknown training data, proprietary system details, and lack of task-specific fine-tuning.
- Inferred: Dataset splits, statistical uncertainty across repeated runs, and downstream task transfer are not fully reported.

## Reproducibility

- Code: https://github.com/lbl-camera/genAI.
- Data: reported as available through the same project GitHub with public archived dataset links.
- Hyperparameters: not reported.
- Random seeds: not reported.
- Environment: not reported.
- Checkpoints / models: not reported.
- Exact preprocessing: crop/resize constraints are described, but full preprocessing details are not reported.
- Artifact status: reported available; not independently verified.

## Connections

### Graph Hubs

- Tasks: [[Scientific image generation]]
- Methods: [[Variational Autoencoder]], [[GAN]], [[Diffusion models]], [[Learned generative synthesis]]
- Datasets: CMC microCT dataset, EcoFAB root image dataset, Rocks microCT dataset
- Domains: [[Scientific imaging]], [[Nondestructive testing]]
- Metrics: [[SSIM]], [[LPIPS]], [[FID]], [[CLIPScore]]

### Builds On

- [[Generative Models]]: the paper compares major generative model families for image synthesis.
- [[Synthetic data generation]]: the paper frames scientific image generation as a way to augment scarce scientific datasets.

### Contrasts With

- [[GAN]]: GANs can produce realistic textures but have training instability and limited controllability.
- [[Diffusion models]]: diffusion systems offer strong quality and controllability but can be slow and still fail scientific validation.
- [[Variational Autoencoder]]: VAEs are treated as foundational but generally blurrier than GANs and diffusion models for image synthesis.

### Shares Dataset

- not applicable

### Shares Task

- [[Scientific image generation]]: the paper directly evaluates generation, variation, editing, and inpainting of scientific images.

### Shares Method

- [[Learned generative synthesis]]: evaluated systems synthesize images with learned generative models.
- [[GAN]]: DCGAN and StyleGAN are trained and evaluated.
- [[Diffusion models]]: DiffEdit, Stable unCLIP, ControlNet, LEDITS++, InstructPix2Pix, and DALL-E systems are evaluated as diffusion or transformer-diffusion systems.

### Shares Metric

- [[SSIM]]: used for structural similarity in paired evaluations.
- [[LPIPS]]: used for perceptual similarity in paired evaluations.
- [[FID]]: used for distributional similarity and realism.
- [[CLIPScore]]: used for text-image semantic alignment.

### Application / Domain

- [[Scientific imaging]]: scientific image fidelity, instrument-specific structure, and domain-expert validation are central to the paper.
- [[Nondestructive testing]]: microCT datasets include composite fibers and rocks where structural image fidelity matters.

### Follow-Up Reading

- [[Synthetic data generation]]
- [[Learned generative synthesis]]
- [[Generative quality metrics]]

## Questions

- Are the GitHub datasets and code complete enough to reproduce the reported tables?
- Would domain-specific image-text encoders improve CLIPScore-like evaluation on microCT and root imagery?
- Do generated images improve downstream segmentation or detection models, or only improve visual plausibility?
