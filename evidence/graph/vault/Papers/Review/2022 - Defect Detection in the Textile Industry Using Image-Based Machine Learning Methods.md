---
title: "Defect Detection in the Textile Industry Using Image-Based Machine Learning Methods: A Brief Review"
aliases:
  - "Defect detection in the textile industry using image-based machine learning methods"
paper_key: "doi:10.1088/1742-6596/2224/1/012010"
paper_type: review
year: 2022
venue: "Journal of Physics: Conference Series"
authors:
  - "Somayeh Shahrabadi"
  - "Yusbel Castilla"
  - "Miguel Guevara"
  - "Luis G. Magalhaes"
  - "Dibet Gonzalez"
  - "Telmo Adao"
status: processed
processed_at: 2026-05-20
topics:
  - textile defect detection
  - fabric inspection
  - automated optical inspection
  - image-based machine learning
tasks:
  - "[[Textile defect detection]]"
  - "[[Defect classification]]"
domains:
  - "[[Textile and fiber inspection]]"
application_area: "Automated optical inspection for textile fabric quality control"
methods:
  - "[[Deep convolutional neural network]]"
  - "[[Classical ML]]"
  - "[[Gabor filters]]"
  - "[[Principal Component Analysis]]"
  - "[[K-means clustering]]"
metrics:
  - "[[Accuracy]]"
  - "[[Precision]]"
  - "[[F1-score]]"
  - "[[AU-ROC|AUC]]"
primary_metric: "not applicable"
datasets:
  - "TILDA"
  - "self-made textile datasets"
  - "KTH-TIPS"
  - "Kylberg Texture"
  - "University of Hong Kong defect library"
doi: "10.1088/1742-6596/2224/1/012010"
url: "https://doi.org/10.1088/1742-6596/2224/1/012010"
related_tasks:
  - "[[Textile defect detection]]"
  - "[[Defect classification]]"
related_methods:
  - "[[Deep convolutional neural network]]"
  - "[[Classical ML]]"
  - "[[Gabor filters]]"
  - "[[Principal Component Analysis]]"
  - "[[K-means clustering]]"
related_datasets:
  - "[[TILDA]]"
related_domains:
  - "[[Textile and fiber inspection]]"
preprocessed_input: "paper-inbox/90_processing/analysis-inputs/2022 - Shahrabadi - Defect Detection in the Textile Industry Using Image-Based Machine Learning Methods A Brief Review.md"
extracted_text: "paper-inbox/90_processing/text/2022 - Shahrabadi - Defect Detection in the Textile Industry Using Image-Based Machine Learning Methods A Brief Review.txt"
pdf: "paper-inbox/10_processed/2022 - Shahrabadi - Defect Detection in the Textile Industry Using Image-Based Machine Learning Methods A Brief Review.pdf"
source_file: "paper-inbox/10_processed/2022 - Shahrabadi - Defect Detection in the Textile Industry Using Image-Based Machine Learning Methods A Brief Review.pdf"
tags:
  - paper
  - review
  - textile-inspection
---
# Defect Detection in the Textile Industry Using Image-Based Machine Learning Methods

## Summary

- Shahrabadi et al. review image-based [[Textile defect detection]] methods for automated optical inspection, with emphasis on machine learning and deep learning work from roughly the previous five years.
- The review frames fabric inspection as a quality-control task where automated systems reduce human inspection error, fatigue, ergonomic burden, subjectivity, and cost.
- The paper argues that CNN-based approaches such as AlexNet-style and VGG16-style models have reached reported textile defect accuracies above 98% in selected reviewed studies, while still requiring structured datasets, costly training, and adequate hardware.

## Paper Type

- Type: review.
- Why: The paper surveys textile defect types, automated optical inspection systems, classical computer vision, machine learning, and deep learning approaches rather than introducing a new dataset or model.

## Problem

- Task: [[Textile defect detection]] and defect classification for textile fabric quality control.
- Setting: Textile manufacturing processes use natural or synthetic raw materials for clothing, coatings, household products, automotive materials, and other outputs.
- Motivation: Fabric defects can create complaints, returns, undervalued products, and process-quality losses.
- Manual inspection problem: Human visual inspection is inaccurate, time-consuming, fatigue-prone, subjective, and affected by ergonomic and environmental conditions.
- AOI setting: Automated optical inspection combines image-acquisition equipment, illumination, processing hardware, and defect-detection algorithms for quality assessment.

## Contribution

- Claimed: The review adds value over prior textile surveys by focusing on recent image-based machine learning approaches and benchmarking them by technique, method, defect type, metric, performance, and dataset.
- Shown: The paper summarizes defect categories, AOI pipeline elements, classical CV methods, supervised ML methods, deep learning methods, metrics, and datasets used by recent textile defect studies.
- Shown: The paper compares classical computer vision and supervised image-based machine/deep learning across problem complexity, dataset dependence, feature-control, development effort, adaptability, hardware demands, and accuracy potential.

## Review / Survey Details

### Scope

- Topic scope: image-based machine learning and automated optical inspection for textile fabric defect detection.
- Time scope: mainly publications from the latest five years before the review, with a smaller set of older works for context.
- Databases queried: Science Direct, IEEE Xplore, ACM Digital Library, MDPI, Google Scholar, and other academic databases.
- Search keywords: "defect detection", "textile fabric", "automatic inspection", "deep learning", and "machine learning", used alone and in combination.
- Screening process: PRISMA-like process with duplicate removal, abstract-level relevance screening, and detailed content inspection before inclusion.

### Defect Taxonomy

- Broad severity categories:
  - Critical defects: anomalies that make an item unusable and may create product-liability or recall risk.
  - Major defects: defects that can affect function, performance, or appearance.
  - Minor defects: small issues that do not substantially affect product function or form.
- Cotton Incorporated categories named in the review:
  - vertical lines
  - horizontal lines
  - isolated defects
  - pattern defects
  - finishing defects
  - printing defects
- Example fabric defects named in the source: missing yarn, broken end, needle line, oil spot, hole, press off, mixed yarn, and gouts.

### Methodological Patterns

- Classical computer vision methods include binarization, morphology, color transformations, [[Gabor filters]], wavelet transforms, Fourier transforms, GLCM features, and curvelet transforms.
- Supervised ML methods include ANN, SVM, Random Forest, KNN, BPN, RBF, RNN, LVQ, and saliency-feature classifiers.
- Deep learning methods include CNNs, AlexNet-based CNNs, YOLO-VOC, stacked autoencoders, modified VGG16, modified DenseNet, multi-scale convolutional denoising autoencoders, and CNN plus low-rank representation.
- Dataset strategy: the review stresses that structured datasets are crucial for supervised methods; options include using public datasets or creating customized datasets for desired defect types.
- Data augmentation strategy: the review mentions rotation, flipping, translation, and random cropping as ways to enlarge existing textile defect datasets for deep neural-network training.

### Classical CV vs ML Trade-Offs

| Criterion | Classical CV | Supervised image-based ML/DL |
|---|---|---|
| Complex problem mapping | low | high |
| Independence from structured datasets | medium | low |
| Control over feature extraction | high | low |
| Independence from development effort | medium | high |
| Adaptability and scalability | low | high |
| Low-profile hardware admissibility | high | low |
| Accuracy potential | medium | high |

### Metrics

- The review does not define one primary metric because it surveys multiple studies.
- Metrics named in the discussion include [[AU-ROC|AUC]], [[Precision]], [[Accuracy]], [[F1-score]], and mean squared error.
- The paper states that AUC, ACC, and precision are the most used metrics among the screened works.

## Evidence

### Reviewed Study Examples

| Method family | Example method | Defect types reported | Metric / result | Dataset detail |
|---|---|---|---|---|
| Spectral / texture features | GLCM and wavelet transform | not reported | not reported | self-made dataset |
| Spectral / texture features | GLCM and DCT | not reported | not reported | not reported |
| ML | ANN with DST-PCA features | needle breakages, hole, press-off, gouts | accuracy 95.46% | self-made dataset |
| ML | SVM and Random Forest over saliency features | broken end, thin bar, thick bar, netting multiple, knots, hole, oil spot, stain | accuracy 95.5% and 93.5% | TILDA and self-made dataset |
| ML | KNN over DWT coefficients | horizontal yarn missing, vertical yarn missing, hole, stain | accuracy 95% | not reported |
| DL | CNN with activation-layer fabric motif map | horizontal, vertical, and isolated defects | accuracy 98% | TILDA and self-made dataset |
| DL | AlexNet-based CNN | hole, knob, stain, hanging, broken warp, broken weft | accuracy 98.2% | TILDA |
| DL | YOLO-VOC | belt yarn, knot tying, hole | precision 94.5% | self-made dataset |
| DL | Stacked autoencoders | broken end, hole, netting multiple, thick bar, thin bar | class-specific accuracies 85.5%, 84.4%, 82.2%, 95.3%, and 86.5% | dataset from the AlexNet paper |
| DL | Modified VGG16 | missing yarn, scratch, twill flaw, dye spot | accuracy 98.1% | Xiamen Face++ Company |
| DL | Modified DenseNet | pin holes, burl mark, chafed yarn, rough, loose warp, stretched warp, end out, overshot, stain | AUC 18% | Alibaba Tianchi Competition |

### Main Claims

- Classical CV can be effective under stable problem conditions but is sensitive to changed context, lighting, and background, often requiring source-code reengineering.
- Supervised image-based machine learning has higher complex-problem mapping capacity and adaptability, but depends strongly on structured datasets and higher processing resources.
- DL methods generally perform better than classical and traditional ML methods in the screened textile defect studies, but that conclusion is based on heterogeneous datasets, defect types, and metrics.
- Responsive industrial AOI may require a compromise: classical CV for gross tasks, DL for sharper inference, and strategies to reduce computational bottlenecks.

## ML / DL Extraction

- Task formulation: image-based detection or classification of textile defects.
- Inputs: fabric images from public or self-made textile datasets.
- Outputs: defect presence, defect class, or defect region depending on the reviewed study.
- Architectures: CNN, AlexNet-based CNN, YOLO-VOC, SAE/FCSAE, modified VGG16, modified DenseNet, MSCDAE, CNN+LRR.
- Training recipe: varies by reviewed paper; the review does not normalize optimizer, learning rate, batch size, epochs, or hardware.
- Evaluation protocol: heterogeneous; table reports study-specific metrics and datasets.
- Compute/hardware: the review discusses high-performance hardware needs generally but does not report a unified compute setup.
- Artifacts: no review dataset, code, or artifact release is reported.

## Limitations

- The paper is a brief review, not a full systematic review with complete inclusion/exclusion counts.
- The review table contains heterogeneous methods, datasets, defect categories, and metrics, making direct ranking weak.
- Several rows report `N/A` or do not report dataset details.
- The paper does not normalize dataset sizes, train/test splits, annotation types, acquisition setups, or deployment latency across reviewed studies.
- The conclusion warns that ML/DL methods require extensive representative datasets, burdensome and time-consuming training, and high-performance hardware.

## Reproducibility

- Review search terms: reported.
- Databases: reported at category level.
- PRISMA-like procedure: reported, but exact paper counts per stage are not visible in the extracted text.
- Included-paper metadata: partly reported through Table 2 and references.
- Code/data release for the review: not reported.

## Connections

### Graph Hubs

- Tasks: [[Textile defect detection]], [[Defect classification]]
- Domains: [[Textile and fiber inspection]]
- Methods: [[Deep convolutional neural network]], [[Classical ML]], [[Gabor filters]], [[Principal Component Analysis]], [[K-means clustering]]
- Metrics: [[Accuracy]], [[Precision]], [[F1-score]], [[AU-ROC|AUC]]
- Datasets: [[TILDA]] is explicitly named in benchmark rows; other reviewed datasets include self-made datasets, KTH-TIPS, Kylberg Texture, University of Hong Kong defect library, and Alibaba Tianchi Competition.

### Related Papers

| Paper | Relationship | Rationale |
|---|---|---|
| [[2021 - Fabric Defect Detection in Textile Manufacturing A Survey of the State of the Art]] | Review context | The source cites it as a recent textile defect detection review and positions itself as a brief review with stronger emphasis on recent image-based ML approaches. |
| [[2019 - A Public Fabric Database for Defect Detection Methods and Results]] | Dataset/method context | This review discusses public textile datasets and several benchmark rows use TILDA or self-made textile datasets. |

### Backlinks Updated

- [[Textile defect detection]] already links this paper as a review of image-based ML methods.
- [[Textile and fiber inspection]] links this paper as a textile inspection review.

## Questions

- Which cited public datasets beyond [[TILDA]] should become canonical dataset notes?
- Should the review's defect taxonomy be split into a reusable textile defect taxonomy note?
- Is a deeper review needed to separate textile defect classification, localization, and segmentation evidence?
