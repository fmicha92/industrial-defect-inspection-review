---
title: "TILDA"
aliases:
  - "TILDA Textile Texture Database"
  - "TILDA Textile Texture-Database"
related_domain: "[[Textile and fiber inspection]]"
url: "https://lmb.informatik.uni-freiburg.de/resources/datasets/tilda.en.html"
data_sources:
  - "University of Freiburg Computer Vision Group dataset host"
introduced_by: "[[1996 - TILDA Reference Dataset Report]]"
citation_key: "schulz1996tilda"
licenses: "not reported"
---
# TILDA

## Definition

TILDA is a public textile texture database for evaluating visual inspection algorithms for textile surface defects. It contains monochrome 8-bit grayscale TIFF images of textile surfaces, organized by textile kind and defect class.

## Why It Matters

The dataset is an early reference dataset for textile surface inspection. It provides controlled textile classes, defined defect categories, and per-defect text descriptions, making it useful for comparing classical texture-analysis and visual-inspection methods.

## Dataset Details

- Hosting source: https://lmb.informatik.uni-freiburg.de/resources/datasets/tilda.en.html.
- Availability: public download from the University of Freiburg Computer Vision Group page.
- Size: the host page reports 3,200 TIFF images and a total size of 1.2 GB; the German reference report reports 3,228 images, 2,828 defect-description text files, and 1.27 GB including 20 additional catalog images.
- Image format: TIFF.
- Image resolution: 768 x 512 pixels.
- Image type: monochrome grayscale with 256 gray levels / 8-bit grayscale.
- Textile coverage: four fabric classes defined by surface-structure regularity, with two representatives per class in the dataset.
- Defect-free data: 50 defect-free images per representative.
- Defect categories: e0 no defect; e1 holes and cuts from mechanical damage; e2 oil stains and color defects; e3 thread defects, thread compactions, and missing threads; e4 foreign bodies on the fabric; e5 folds without mechanical damage; e6 changed illumination conditions; e7 affine distortions caused by camera tilt or changed camera distance.
- Annotation: each defect image has an accompanying ASCII text file describing defect location and size.
- Naming convention: image files follow `CREN.TIF`, where `C` is fabric class, `R` is representative, `E` is defect class, and `N` is image number; text files use the same convention with `.TXT`.
- License: not reported.

## Source Anchors

- Dataset host: https://lmb.informatik.uni-freiburg.de/resources/datasets/tilda.en.html.
- Reference report: [[1996 - TILDA Reference Dataset Report]].
- Translated report title: "A reference dataset for evaluating visual inspection methods for textile surfaces."

## Citation

Citation key: `schulz1996tilda`

```bibtex
@article{schulz1996tilda,
  title={Tilda-ein referenzdatensatz zur evaluierung von sichtpr{\"u}fungsverfahren f{\"u}r textiloberfl{\"a}chen},
  author={Schulz-Mirbach, H},
  journal={Interner Bericht},
  volume={4},
  pages={96},
  year={1996}
}
```

## Used In These Papers

- [[1996 - TILDA Reference Dataset Report]] describes the dataset structure, textile classes, defect classes, file naming, and defect-description files.
- [[2025 - Artificial Intelligence Driving Innovation in Textile Defect Detection]] lists TILDA among textile defect datasets and reports 3,200 samples with seven defect classes.
- [[2021 - Fabric Defect Detection in Textile Manufacturing A Survey of the State of the Art]] mentions TILDA in fabric defect detection dataset tables.
- [[2020 - Weakly-Supervised Defect Segmentation on Periodic Textures Using CycleGAN]] uses C3R1 and C3R3 periodic-texture subsets for weakly supervised defect segmentation; the paper reports 12.27% and 14.84% mIoU for its augmented weakly supervised method on those subsets.
- [[2025 - Blind super-resolution network based on local fuzzy discriminative loss for fabric data augmentation]] uses 395 preprocessed TILDA images resized to 512 x 512 for super-resolution enhancement generalization and reports OurSR image-quality metrics of 69.433 FID, 15.22 PSNR, 0.750 SSIM, and 0.357 LPIPS.

## Related Concepts

- [[Textile and fiber inspection]]
- [[Textile defect detection]]
- [[Industrial visual inspection]]
