#!/usr/bin/env python3
"""Render Table 1 and its versioned machine-readable registry.

The source CSV retains the full release audit. This renderer supplies the
publication-facing controlled vocabulary, selects one canonical release view
when sources conflict, and writes the supplementary registry used to audit the
compact table cells.
"""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_CSV = ROOT / "table1_dataset_resolution_and_class_counts.csv"
TABLE_PATH = ROOT / "latex_dataset_paper" / "tables" / "dataset_registry.tex"
SUPPLEMENT_PATH = (
    ROOT / "latex_dataset_paper" / "data" / "table1_dataset_registry_v1.0.0.csv"
)
REGISTRY_VERSION = "1.0.0"
SNAPSHOT_DATE = "2026-08-03"


TASK_LABELS = {
    "Cls": "Classification",
    "Det": "Object detection",
    "Seg": "Semantic segmentation",
    "InstSeg": "Instance segmentation",
    "AD": "Anomaly detection",
    "Loc": "Localization",
    "Reg": "Image registration",
    "SOD": "Salient-object detection",
    "FS-Seg": "Few-shot segmentation",
    "WF": "Wear forecasting",
}


TASK_CODES = {
    "WM-811K": "Cls",
    "MixedWM38": "Cls",
    "DeepPCB": "Det",
    "HRIPCB": "Cls; Det; Reg",
    "DsPCBSD+": "Det",
    "Heat Sink Surface Defects": "Seg",
    "ELPV Solar Cell Dataset": "Cls",
    "PVEL-AD": "Cls; Det",
    "EL-2019 (SIGAN dataset)": "Seg",
    "PV Panel Defect Dataset": "Cls",
    "Dataset of Solar Cells Defect Segm.": "Seg",
    "BenchmarkELimages": "Seg",
    "PV-Multi-Defect": "Det",
    "InfraredSolarModules": "Cls",
    "Thermal PV UAV Dataset": "Det",
    "SolarDK": "Cls; Loc",
    "NEU-CLS": "Cls",
    "X-SDD": "Cls; Det",
    "NEU-DET": "Det",
    "NEU-SEG": "Seg",
    "GC10-DET": "Det",
    "Severstal Steel Defect": "Cls; Seg",
    "KolektorSDD": "Seg; Loc",
    "KolektorSDD2": "Seg; Loc",
    "Magnetic Tile Defects": "Seg; Loc",
    "APDDD": "Det",
    "MPDD": "AD; Loc",
    "MPDD2": "AD",
    "CSDD": "Det; Seg",
    "MSDD": "Det",
    "HSS-IAD": "AD; Loc",
    "LoHi-WELD": "Cls; Det",
    "BSData": "Cls; Det; Seg; WF",
    "AITEX": "Cls; Seg",
    "TILDA": "Cls; Loc",
    "ZJU-Leaper": "Det; Seg",
    "Lusitano": "AD",
    "FabricSpotDefect": "Det; Seg",
    "Batavia/Sarga Woven Fabric": "Cls",
    "DME Fabric Defect Detection": "Cls",
    "FD_Dataset": "Cls; Det; Seg",
    "AGDD": "Det",
    "Glass Bangle Defect Detection Classification": "Cls",
    "MSD": "Seg",
    "MVEP": "Cls; Det",
    "SSGD": "Det",
    "CarDD": "Cls; Det; InstSeg; SOD",
    "AutoVI": "AD; Loc",
    "Structural Adhesive Defects Dataset": "Det",
    "Open Stamped Parts Dataset": "Det; Seg",
    "MVTec AD": "AD; Loc",
    "VisA": "AD; Seg",
    "BTAD": "AD; Loc",
    "MVTec LOCO AD": "AD; Loc",
    "MVTec AD 2": "AD; Loc",
    "Real-IAD": "AD; Seg",
    "Industrial-5i": "FS-Seg",
    "Bosch SDI": "Cls",
    "Bottle-Cap Dataset": "AD; Loc",
    "DAGM2007": "Cls; Loc",
    "Defect Spectrum": "Cls; Seg",
}

TASKS = {
    name: "; ".join(TASK_LABELS[code] for code in codes.split("; "))
    for name, codes in TASK_CODES.items()
}


ANNOTATIONS = {
    "WM-811K": "Image labels",
    "MixedWM38": "Image labels",
    "DeepPCB": "Bounding boxes",
    "HRIPCB": "Image labels + boxes",
    "DsPCBSD+": "Bounding boxes",
    "Heat Sink Surface Defects": "Pixel masks",
    "ELPV Solar Cell Dataset": "Probabilistic image labels",
    "PVEL-AD": "Image labels + boxes",
    "EL-2019 (SIGAN dataset)": "Pixel masks",
    "PV Panel Defect Dataset": "Image labels",
    "Dataset of Solar Cells Defect Segm.": "Pixel masks",
    "BenchmarkELimages": "Multi-label pixel masks",
    "PV-Multi-Defect": "Bounding boxes",
    "InfraredSolarModules": "Image labels",
    "Thermal PV UAV Dataset": "Bounding boxes",
    "SolarDK": "Image labels + pixel masks",
    "NEU-CLS": "Image labels",
    "X-SDD": "Image labels + boxes",
    "NEU-DET": "Bounding boxes",
    "NEU-SEG": "Pixel masks",
    "GC10-DET": "Bounding boxes",
    "Severstal Steel Defect": "Image labels + pixel masks",
    "KolektorSDD": "Pixel masks",
    "KolektorSDD2": "Pixel masks",
    "Magnetic Tile Defects": "Pixel masks",
    "APDDD": "Bounding boxes",
    "MPDD": "Image labels + pixel masks",
    "MPDD2": "Image labels",
    "CSDD": "Boxes + pixel masks",
    "MSDD": "Bounding boxes",
    "HSS-IAD": "Image labels + pixel masks",
    "LoHi-WELD": "Image labels + boxes",
    "BSData": "Image labels + instance masks",
    "AITEX": "Image labels + pixel masks",
    "TILDA": "Image labels + defect-location metadata",
    "ZJU-Leaper": "Image labels + boxes + pixel masks",
    "Lusitano": "Image labels",
    "FabricSpotDefect": "Boxes + polygon masks",
    "Batavia/Sarga Woven Fabric": "Patch labels",
    "DME Fabric Defect Detection": "Image labels",
    "FD_Dataset": "Object labels",
    "AGDD": "Oriented + axis-aligned boxes",
    "Glass Bangle Defect Detection Classification": "Image labels",
    "MSD": "Pixel masks",
    "MVEP": "Boxes + ordinal labels",
    "SSGD": "Bounding boxes",
    "CarDD": "Image labels + boxes + polygon masks",
    "AutoVI": "Image labels + pixel masks",
    "Structural Adhesive Defects Dataset": "Bounding boxes",
    "Open Stamped Parts Dataset": "Boxes + synthetic masks",
    "MVTec AD": "Image labels + pixel masks",
    "VisA": "Image labels + pixel masks",
    "BTAD": "Image labels + pixel masks",
    "MVTec LOCO AD": "Image labels + pixel masks",
    "MVTec AD 2": "Image labels + public/server masks",
    "Real-IAD": "Image labels + pixel masks",
    "Industrial-5i": "Pixel masks",
    "Bosch SDI": "Image labels",
    "Bottle-Cap Dataset": "Image labels; spatial schema NR",
    "DAGM2007": "Image labels + ellipse masks",
    "Defect Spectrum": "Pixel masks + semantic labels + captions",
}


RESOLUTIONS = {
    "WM-811K": r"Var.: 6\,$\times$\,21--300\,$\times$\,202",
    "MixedWM38": r"52\,$\times$\,52",
    "DeepPCB": r"640\,$\times$\,640",
    "HRIPCB": r"Source: 4{,}608\,$\times$\,3{,}456; release crops: 64\,$\times$\,64",
    "DsPCBSD+": r"226\,$\times$\,226",
    "Heat Sink Surface Defects": r"320\,$\times$\,320",
    "ELPV Solar Cell Dataset": r"300\,$\times$\,300",
    "PVEL-AD": r"1{,}024\,$\times$\,1{,}024",
    "EL-2019 (SIGAN dataset)": r"Source: 1{,}024\,$\times$\,1{,}024; release patches: 128\,$\times$\,128",
    "PV Panel Defect Dataset": r"Var.: 149--6{,}240 wide; 110--5{,}376 high",
    "Dataset of Solar Cells Defect Segm.": (
        r"SolarCells: 448\,$\times$\,448; other subsets var. "
        r"(verified 417\,$\times$\,426--1{,}024\,$\times$\,1{,}024)"
    ),
    "BenchmarkELimages": r"512\,$\times$\,512",
    "PV-Multi-Defect": r"Source: 5{,}800\,$\times$\,3{,}504; release: 600\,$\times$\,600",
    "InfraredSolarModules": r"24\,$\times$\,40",
    "Thermal PV UAV Dataset": r"640\,$\times$\,512",
    "SolarDK": r"NR; 10--15\,cm/pixel GSD",
    "NEU-CLS": r"200\,$\times$\,200",
    "X-SDD": r"128\,$\times$\,128",
    "NEU-DET": r"200\,$\times$\,200",
    "NEU-SEG": r"200\,$\times$\,200",
    "GC10-DET": r"2{,}048\,$\times$\,1{,}000",
    "Severstal Steel Defect": r"1{,}600\,$\times$\,256",
    "KolektorSDD": r"1{,}408\,$\times$\,512",
    "KolektorSDD2": r"Var.; approx. 230\,$\times$\,630",
    "Magnetic Tile Defects": r"Var. released crops",
    "APDDD": r"640\,$\times$\,640",
    "MPDD": r"1{,}024\,$\times$\,1{,}024",
    "MPDD2": r"256\,$\times$\,256",
    "CSDD": r"3{,}648\,$\times$\,3{,}648",
    "MSDD": r"Source: up to 2{,}560\,$\times$\,1{,}920; release patches: 640\,$\times$\,640",
    "HSS-IAD": (
        r"Category-specific: 122\,$\times$\,271--1{,}600\,$\times$\,1{,}024"
    ),
    "LoHi-WELD": r"Low: 640\,$\times$\,480; high: 2{,}048\,$\times$\,1{,}080",
    "BSData": r"Cls crops: 150\,$\times$\,150; Det/Seg: NR",
    "AITEX": r"4{,}096\,$\times$\,256",
    "TILDA": r"768\,$\times$\,512",
    "ZJU-Leaper": r"512\,$\times$\,512",
    "Lusitano": r"4{,}096\,$\times$\,1{,}024",
    "FabricSpotDefect": r"NR",
    "Batavia/Sarga Woven Fabric": r"Source: 2{,}048\,$\times$\,696; release patches: 365\,$\times$\,365",
    "DME Fabric Defect Detection": r"1{,}920\,$\times$\,1{,}080",
    "FD_Dataset": r"Raw var.: 358--1{,}280 wide, 299--1{,}280 high; prepared release: 640\,$\times$\,640",
    "AGDD": r"Source pairs: 1{,}280\,$\times$\,720; prepared release: 640\,$\times$\,640",
    "Glass Bangle Defect Detection Classification": r"3{,}000\,$\times$\,3{,}000",
    "MSD": r"1{,}920\,$\times$\,1{,}080",
    "MVEP": r"NR for full set; metadata example: 1{,}008\,$\times$\,1{,}008",
    "SSGD": r"1{,}500\,$\times$\,1{,}000",
    "CarDD": r"Var. high-resolution; minimum 1{,}000\,$\times$\,413",
    "AutoVI": r"400\,$\times$\,400 or 1{,}000\,$\times$\,750 by category",
    "Structural Adhesive Defects Dataset": r"1{,}024\,$\times$\,1{,}024",
    "Open Stamped Parts Dataset": r"1{,}456\,$\times$\,1{,}088",
    "MVTec AD": r"Category-specific: 700\,$\times$\,700--1{,}024\,$\times$\,1{,}024",
    "VisA": r"Source: 6{,}000\,$\times$\,4{,}000; release crops var.",
    "BTAD": r"Product-specific: 600\,$\times$\,600--1{,}600\,$\times$\,1{,}600",
    "MVTec LOCO AD": r"Category-specific: 800\,$\times$\,1{,}600--1{,}700\,$\times$\,1{,}000",
    "MVTec AD 2": r"Category-specific: 1{,}400--4{,}224 wide; 1{,}024--2{,}048 high",
    "Real-IAD": r"Source: 3{,}648\,$\times$\,5{,}472; release downsample: 1{,}024\,$\times$\,1{,}024",
    "Industrial-5i": r"Var. composite of six source datasets",
    "Bosch SDI": r"Var.; fixed dimensions NR",
    "Bottle-Cap Dataset": r"NR for full set; repository sample: 1{,}280\,$\times$\,960",
    "DAGM2007": r"512\,$\times$\,512",
    "Defect Spectrum": r"Var. across four source benchmarks",
}


DAGGER = r"\textsuperscript{\(\dagger\)}"
SAMPLE_SUMMARIES = {
    "WM-811K": r"811{,}457 maps; 172{,}950 labelled; 9 single-label patterns; 149--147{,}431 per pattern",
    "MixedWM38": rf"38{{,}}015 maps{DAGGER}; 38 single-label combination classes; 149--2{{,}}000 per class",
    "DeepPCB": r"1{,}500 aligned pairs (3{,}000 files); 1{,}500 annotated defective images; 10{,}013 boxes; 6 multi-label defect types",
    "HRIPCB": r"1{,}386 annotated release crops; instances not reported; 6 single-label types; 230--232 per type",
    "DsPCBSD+": r"10{,}259 images; 20{,}276 boxes; 9 multi-label defect types",
    "Heat Sink Surface Defects": r"1{,}000 masked images; 2 multi-label foreground types; scratch/stain memberships: 700/972",
    "ELPV Solar Cell Dataset": r"2{,}624 images; 4 probabilistic levels: 1{,}508/295/106/715",
    "PVEL-AD": r"36{,}543 images: 11{,}351 normal, 21{,}044 boxed, 4{,}148 category-only; 37{,}380 boxes; 8 boxed types",
    "EL-2019 (SIGAN dataset)": r"540 masked patches; 3 single-label conditions: 280/130/130",
    "PV Panel Defect Dataset": r"1{,}574 images; 6 single-label conditions; 225--298 per class",
    "Dataset of Solar Cells Defect Segm.": r"Masked images by subset: 190/36/1{,}200; binary foreground",
    "BenchmarkELimages": rf"582 masked images{DAGGER} (release 20211104); 24 multi-label mask classes",
    "PV-Multi-Defect": rf"1{{,}}108 images; 1{{,}}106 annotated; 3{{,}}981 boxes{DAGGER}; 5 multi-label defect types",
    "InfraredSolarModules": rf"20{{,}}000 images{DAGGER}; 12 single-label conditions; 175--10{{,}}000 per class",
    "Thermal PV UAV Dataset": r"353 images; 351 annotated; 26{,}678 panel boxes; 1 released box class; 6 fault types unencoded",
    "SolarDK": r"23{,}417 images; absent/present: 22{,}537/880; binary labels; masks available",
    "NEU-CLS": r"1{,}800 images; 6 single-label defect types; 300 per class",
    "X-SDD": r"1{,}360 images; 7 single-label defect types; 63--397 per class; later box count not reported",
    "NEU-DET": r"1{,}800 annotated images; box count not reported; 6 defect types; 300 per type",
    "NEU-SEG": r"900 masked images; 3 defect types; 300 per type",
    "GC10-DET": rf"2{{,}}300 images{DAGGER} (2{{,}}292 annotated); 3{{,}}563 boxes; 10 multi-label defect types; 46--734 images/type",
    "Severstal Steel Defect": r"12{,}568 images; mask-positive/negative: 6{,}666/5{,}902; 4 multi-label defect types",
    "KolektorSDD": rf"400 images{DAGGER}; mask-positive/negative: 50/350; binary defect; 3-fold cross-validation",
    "KolektorSDD2": r"3{,}335 images; mask-positive/negative: 356/2{,}979; binary defect",
    "Magnetic Tile Defects": r"1{,}344 images; normal/defective: 952/392; 5 defect types plus normal; masks available",
    "APDDD": r"3{,}719 images; 5{,}279 boxes; 10 defect types; images per type not reported",
    "MPDD": r"Train normal/test normal/test anomalous: 888/176/282; total 1{,}346 images; 6 products; anomaly masks",
    "MPDD2": r"Train normal/test normal/test anomalous: 385/96/264; total 745 images; 4 products; image labels",
    "CSDD": r"2{,}100 images; 56{,}356 box/mask instances; 3 defect types",
    "MSDD": rf"138{{,}}585 single-channel plus 9{{,}}239 pseudo-colour images{DAGGER}; 8 defect types; pseudo-colour normal/defect: 5{{,}}746/3{{,}}493",
    "HSS-IAD": rf"12{{,}}075 images{DAGGER}; 7 products; normal-only training; test-anomaly masks; splits in Supplementary Data S1",
    "LoHi-WELD": r"3{,}022 images; 22{,}412 boxes; 4 multi-label defect types",
    "BSData": r"Classification crops: 21{,}853 (binary 11{,}075/10{,}778); detection images: 1{,}104 (394 annotated); instances not reported",
    "AITEX": r"245 images: 140 normal/105 defective; 105 masks; 12 defect types",
    "TILDA": rf"3{{,}}200 images{DAGGER}; 8 single-label inspection conditions; 400 per class",
    "ZJU-Leaper": r"94{,}833 images: 71{,}127 normal/23{,}706 defective; train/test: 63{,}184/31{,}649; 19 pattern classes; 2{,}358--7{,}244 per pattern",
    "Lusitano": r"Train normal/test normal/test anomalous: 32{,}000/1{,}038/1{,}646; total 34{,}684 images; 1 product",
    "FabricSpotDefect": r"1{,}014 positive images; 3{,}288 polygons; 1 defect type",
    "Batavia/Sarga Woven Fabric": r"4{,}303 source images; 47{,}269 patches; binary patch labels: 8{,}955 case/38{,}314 control",
    "DME Fabric Defect Detection": r"97 images; 5 single-label conditions; 17--20 per class",
    "FD_Dataset": rf"720 prepared images{DAGGER}; 781 boxes; 4 multi-label defect types",
    "AGDD": r"219 source pairs; 1{,}752 released pairs; 4{,}784 augmented boxes; 4 multi-label defect types",
    "Glass Bangle Defect Detection Classification": r"1{,}080 images; 3 single-label conditions; 244--520 per class",
    "MSD": r"1{,}200 masked images; 3 single-label defect types; 400 per type",
    "MVEP": r"16{,}000 multi-view images; ordinal severity labels; label distribution and instances not reported",
    "SSGD": r"2{,}504 images; 3{,}914 boxes; 7 defect types plus normal; multi-label",
    "CarDD": r"4{,}000 images; 8{,}740 instances; 6 multi-label damage types",
    "AutoVI": rf"Train normal/test normal/test anomalous: 1{{,}}530/1{{,}}533/887; total 3{{,}}950 images{DAGGER}; 6 products; anomaly masks",
    "Structural Adhesive Defects Dataset": rf"Generator source: 143 real images; detector train/validation/test: 594/58/18{DAGGER}; 2 multi-label defect types; instances not reported",
    "Open Stamped Parts Dataset": rf"9{{,}}660 real images (1{{,}}680 annotated); 11{{,}}240 synthetic images{DAGGER}; 7 multi-label hole categories",
    "MVTec AD": r"Train normal/test normal/test anomalous: 3{,}629/467/1{,}258; total 5{,}354 images; 15 products; anomaly masks",
    "VisA": r"10{,}821 images: 9{,}621 normal/1{,}200 anomalous; 12 products; anomaly masks",
    "BTAD": r"Train normal/test normal/test anomalous: 1{,}799/451/290; total 2{,}540 images; 3 products; 290 masks",
    "MVTec LOCO AD": r"Train normal/validation normal/test normal/test anomalous: 1{,}772/304/575/993; total 3{,}644 images; 5 products",
    "MVTec AD 2": r"Train/validation/test: 2{,}528/302/5{,}174; total 8{,}004 images; 8 products; some test masks server-held",
    "Real-IAD": r"151{,}050 images: 99{,}721 normal/51{,}329 anomalous; 30 products; normal-only protocol; anomaly masks",
    "Industrial-5i": r"17{,}182 images: 12{,}768 normal/4{,}414 anomalous; 20 products; anomaly masks; 4-fold cross-validation",
    "Bosch SDI": r"20{,}414 images; 3 single-label conditions; normal/scratch/spot: 18{,}750/628/1{,}036",
    "Bottle-Cap Dataset": rf"978 repository images{DAGGER}; 7 reported anomaly types; label distribution and split not reported",
    "DAGM2007": r"16{,}100 images; 10 texture categories; binary normal/defect labels; 1{,}150--2{,}300 per category",
    "Defect Spectrum": r"3{,}518 real/1{,}920 synthetic images; 125 semantic multi-label defects; 552 multi-defect images",
}


LABEL_SEMANTICS = {
    name: "single-label" for name in (
        "WM-811K", "HRIPCB", "PV Panel Defect Dataset", "NEU-CLS",
        "X-SDD", "NEU-DET", "NEU-SEG", "DME Fabric Defect Detection",
        "Glass Bangle Defect Detection Classification", "MSD", "Bosch SDI",
    )
}
LABEL_SEMANTICS.update({
    "MixedWM38": "single-label combination class; constituent defect patterns may overlap",
    "DeepPCB": "multi-label defect types",
    "DsPCBSD+": "multi-label defect types",
    "Heat Sink Surface Defects": "multi-label foreground masks",
    "ELPV Solar Cell Dataset": "probabilistic ordinal levels",
    "PVEL-AD": "mixed normal, boxed defect-type, and category-only labels",
    "EL-2019 (SIGAN dataset)": "single-label condition with binary masks",
    "Dataset of Solar Cells Defect Segm.": "binary foreground masks",
    "BenchmarkELimages": "multi-label semantic masks",
    "PV-Multi-Defect": "multi-label defect types",
    "InfraredSolarModules": "single-label anomaly condition",
    "Thermal PV UAV Dataset": "single released panel class; fault types not encoded",
    "SolarDK": "binary presence label with localization masks",
    "GC10-DET": "multi-label defect types",
    "Severstal Steel Defect": "multi-label defect types plus no-defect condition",
    "KolektorSDD": "binary defect condition",
    "KolektorSDD2": "binary defect condition",
    "Magnetic Tile Defects": "single-label normal or defect type",
    "APDDD": "multi-label defect types",
    "MPDD": "product category plus binary anomaly condition",
    "MPDD2": "product category plus binary anomaly condition",
    "CSDD": "multi-label defect types",
    "MSDD": "binary condition plus defect types",
    "HSS-IAD": "product category plus binary anomaly condition",
    "LoHi-WELD": "multi-label defect types",
    "BSData": "binary pitting condition; spatial instances in separate release view",
    "AITEX": "binary condition plus defect taxonomy",
    "TILDA": "single-label inspection condition",
    "ZJU-Leaper": "pattern category plus binary defect condition",
    "Lusitano": "binary anomaly condition",
    "FabricSpotDefect": "single positive defect type",
    "Batavia/Sarga Woven Fabric": "binary patch condition",
    "FD_Dataset": "multi-label defect types",
    "AGDD": "multi-label defect types",
    "MVEP": "ordinal severity labels",
    "SSGD": "multi-label defect types plus normal condition",
    "CarDD": "multi-label damage types",
    "AutoVI": "product category plus binary anomaly condition",
    "Structural Adhesive Defects Dataset": "two nonexclusive defect types",
    "Open Stamped Parts Dataset": "multi-label hole categories",
    "MVTec AD": "product category plus binary anomaly condition",
    "VisA": "product category plus binary anomaly condition",
    "BTAD": "product category plus binary anomaly condition",
    "MVTec LOCO AD": "product category plus structural/logical anomaly condition",
    "MVTec AD 2": "product category plus binary anomaly condition",
    "Real-IAD": "product category plus binary anomaly condition",
    "Industrial-5i": "product category plus binary anomaly condition",
    "Bottle-Cap Dataset": "reported anomaly types; repository folder semantics unresolved",
    "DAGM2007": "texture category plus binary defect condition",
    "Defect Spectrum": "multi-label semantic defect concepts",
})


DATASET_TYPES = {
    "MixedWM38": "mixed real/simulated",
    "HRIPCB": "original with deterministic augmentation",
    "Dataset of Solar Cells Defect Segm.": "composite with augmented subset",
    "HSS-IAD": "composite/curated derivative",
    "AGDD": "original with augmented release",
    "Structural Adhesive Defects Dataset": "mixed real/synthetic",
    "Open Stamped Parts Dataset": "mixed real/synthetic",
    "Industrial-5i": "composite benchmark",
    "DAGM2007": "synthetic",
    "Defect Spectrum": "composite mixed real/synthetic benchmark",
}
PARENT_DATASETS = {
    "Dataset of Solar Cells Defect Segm.": "SolarCells; SolarCells-S; PVEL-S",
    "HSS-IAD": "casting source; Severstal Steel Defect; Magnetic Tile Defects; KolektorSDD2; KolektorSDD",
    "Industrial-5i": "MVTec AD; KolektorSDD; KolektorSDD2; Magnetic Tile Defects; RSDDs; BSData",
    "Defect Spectrum": "MVTec AD; VISION V1; DAGM2007; Cotton-Fabric",
}


DISCREPANCIES = {
    "MixedWM38": "Released NPZ contains 38,015 maps; the introducing paper describes 38,000.",
    "BenchmarkELimages": "Canonical 20211104 release contains 582 masks; paper states 593; later releases contain 2,175 and 2,354.",
    "PV-Multi-Defect": "Release XML contains 3,981 objects; paper reports 4,235 targets.",
    "InfraredSolarModules": "Official total is 20,000 images; published per-class counts sum to 20,006.",
    "GC10-DET": "Dataset Ninja reports 2,300 images in its current snapshot; the introducing paper reports 3,570.",
    "KolektorSDD": "Canonical construction is 400 images with 50 positives; an alternate archive view has 399 files with 52 positives.",
    "MSDD": "ScienceDB/Table 1 view has 138,585 single-channel and 9,239 pseudo-color images; the paper also reports 149,312 and 9,332.",
    "HSS-IAD": "Audited release folders total 12,075 images; paper and README state 8,580.",
    "TILDA": "Dataset host reports 3,200 images; the reference report counts 3,228 files including catalog images.",
    "FD_Dataset": "Prepared/advertised set contains 720 images; raw folder contains 723 files.",
    "AutoVI": "Canonical Zenodo v1.0.0 has 3,950 images in six categories; the official landing page reports 7,184 images and 11 classes.",
    "Structural Adhesive Defects Dataset": "Release has 18 holdout image files but 19 holdout label files.",
    "Open Stamped Parts Dataset": "Release JSON totals 11,240 synthetic images; paper states 11,340.",
    "Bottle-Cap Dataset": "Current repository snapshot contains 978 files; related paper reports more than 1,100 images.",
}


CANONICAL_RELEASE_BASIS = {
    name: "audited primary release or introducing-paper total" for name in TASKS
}
CANONICAL_RELEASE_BASIS.update({
    "MixedWM38": "released NPZ inventory",
    "BenchmarkELimages": "original GitHub release 20211104",
    "PV-Multi-Defect": "released XML inventory",
    "InfraredSolarModules": "official repository stated total",
    "GC10-DET": "Dataset Ninja statistics snapshot accessed 2026-08-03",
    "KolektorSDD": "introducing benchmark construction",
    "MSDD": "ScienceDB/Table 1 release view",
    "HSS-IAD": "audited release-folder inventory",
    "TILDA": "dataset-host benchmark total",
    "FD_Dataset": "prepared/advertised Figshare release",
    "AutoVI": "Zenodo v1.0.0",
    "Structural Adhesive Defects Dataset": "released image-file inventory",
    "Open Stamped Parts Dataset": "released synthetic JSON inventory",
    "Bottle-Cap Dataset": "current public repository snapshot",
})


ACCESS_CONDITIONS = {name: "public" for name in TASKS}
ACCESS_CONDITIONS.update({
    "SolarDK": "public OSF record; archive unavailable during audit",
    "GC10-DET": "public Dataset Ninja statistics snapshot; original data linked via Kaggle",
    "APDDD": "request-gated",
    "CSDD": "archive supplied by email request",
    "ZJU-Leaper": "publicly documented; release link unavailable during audit",
    "CarDD": "dataset-use consent required",
    "Real-IAD": "gated access",
    "MVEP": "public metadata; full archive not verified",
})
LICENSES = {name: "not reported in audited metadata" for name in TASKS}
LICENSES.update({
    "InfraredSolarModules": "MIT",
    "FD_Dataset": "CC BY 4.0",
    "AutoVI": "CC BY-NC-SA 4.0",
    "Industrial-5i": "CC BY-NC-SA 4.0",
})
RELEASE_VERSIONS = {name: "unversioned audited release" for name in TASKS}
RELEASE_VERSIONS.update({
    "BenchmarkELimages": "20211104",
    "GC10-DET": "Dataset Ninja snapshot accessed 2026-08-03",
    "FD_Dataset": "v2",
    "AutoVI": "v1.0.0",
    "Industrial-5i": "V1",
    "Bottle-Cap Dataset": "repository snapshot at registry version 1.0.0",
})


NORMAL_ONLY_TRAINING = {name: "not applicable" for name in TASKS}
for name in (
    "MPDD", "MPDD2", "HSS-IAD", "Lusitano", "AutoVI", "MVTec AD",
    "VisA", "BTAD", "MVTec LOCO AD", "MVTec AD 2",
):
    NORMAL_ONLY_TRAINING[name] = "yes"
NORMAL_ONLY_TRAINING.update({
    "Real-IAD": "yes for UIAD; FUIAD also studies contaminated training",
    "Industrial-5i": "normal support images; few-shot query protocol",
    "Bottle-Cap Dataset": "not reported",
})


SPATIAL_SCOPE = {}
for name, annotation in ANNOTATIONS.items():
    if any(token in annotation.lower() for token in ("box", "mask", "ellipse", "polygon", "location")):
        SPATIAL_SCOPE[name] = "spatial annotations available; exact scope in annotation/count notes"
    else:
        SPATIAL_SCOPE[name] = "none reported"
SPATIAL_SCOPE.update({
    "PVEL-AD": "partial: boxes for 21,044 defective images; 4,148 category-only images",
    "Thermal PV UAV Dataset": "generic panel boxes; reported fault types are not encoded",
    "X-SDD": "boxes belong to a later detection use; native coverage unresolved",
    "Severstal Steel Defect": "pixel masks for positive training images",
    "MPDD": "pixel masks for anomalous test images",
    "HSS-IAD": "pixel masks for anomalous test images",
    "AutoVI": "one or more masks for defective test images",
    "MVTec AD": "pixel masks for anomalous test images",
    "VisA": "pixel masks for anomalous images",
    "BTAD": "290 masks for anomalous test images",
    "MVTec LOCO AD": "pixel masks for structural/logical test anomalies",
    "MVTec AD 2": "public and server-held test masks",
    "Real-IAD": "pixel masks for anomalous images",
    "Industrial-5i": "binary masks for abnormal query images",
    "Bottle-Cap Dataset": "not reported",
})


TABLE_CAPTION = (
    "    \\caption{Public dataset registry for manufacturing visual defect inspection. "
    "Rows are grouped by manufacturing context, with cross-domain benchmarks separated explicitly. "
    "Tasks are written in full using the controlled vocabulary defined below; resolution reports native or "
    "released dimensions rather than downstream model preprocessing. Plain-language count descriptions "
    "distinguish images, annotated samples, spatial instances or masks, product categories, and "
    "label semantics. Canonical release counts are shown when sources conflict. Full distributions, "
    "splits, lineage, access, licenses, provenance, and discrepancy notes are provided in Supplementary "
    "Data S1 (\\texttt{table1\\_dataset\\_registry\\_v1.0.0.csv}; version 1.0.0; metadata snapshot "
    "2026-08-03). Each dataset name is followed by its data-host and introducing/source-paper citations, "
    "with an additional audited-statistics source where applicable.}"
)


NOTES_BEGIN = "% BEGIN GENERATED TABLE 1 NOTES"
NOTES_END = "% END GENERATED TABLE 1 NOTES"
TABLE_NOTES = r"""% BEGIN GENERATED TABLE 1 NOTES
\noindent\footnotesize\textit{Controlled terminology and notation.}
Task names are written in full and use one controlled meaning throughout.
Annotation terms describe released label granularity. The Samples/classes
column states each counting unit explicitly and distinguishes images, annotated
samples, spatial instances, masks, defect-label classes, and product categories.
Anomaly-detection split counts identify training, validation, normal-test, and
anomalous-test samples in words. Dimensions are width $\times$ height in pixels
unless GSD is reported; var. = variable and NR = not reported.
EL = electroluminescence; IR = infrared; ROI = region of interest;
GSD = ground sample distance.
$\dagger$ indicates a canonical release or snapshot selected amid conflicting
source counts; alternatives and the selection basis are recorded in
Supplementary Data S1.
% END GENERATED TABLE 1 NOTES
""".strip()


SUPPLEMENT_FIELDS = (
    "registry_version",
    "metadata_snapshot_date",
    "dataset_name",
    "domain_group",
    "task_controlled",
    "task_source",
    "annotation_controlled",
    "modality",
    "native_or_released_resolution",
    "label_semantics",
    "dataset_type",
    "parent_datasets",
    "canonical_release_basis",
    "release_version",
    "release_discrepancy",
    "total_samples_source",
    "classes_source",
    "samples_per_class_source",
    "official_split_or_protocol",
    "normal_only_training",
    "spatial_annotation_scope",
    "positive_sample_availability",
    "access_condition",
    "license",
    "resolution_notes",
    "count_notes",
    "primary_source",
)


def dataset_key(dataset_cell: str) -> str:
    """Recover the CSV key without changing the rendered dataset cell."""
    return dataset_cell.split("~", 1)[0].replace(r"\_", "_").strip()


def split_status(split_information: str) -> str:
    lower = split_information.lower()
    if lower == "na" or "no official" in lower or "no fixed" in lower or "no authoritative" in lower:
        return "no canonical split; " + split_information
    return "reported protocol; " + split_information


def positive_sample_availability(record: dict[str, str]) -> str:
    if record["samples_per_class"].strip().upper() == "NA":
        return "not resolved"
    return "reported; see samples_per_class_source and count_notes"


def validate_metadata(names: set[str]) -> None:
    mappings = {
        "tasks": TASKS,
        "annotations": ANNOTATIONS,
        "resolutions": RESOLUTIONS,
        "sample summaries": SAMPLE_SUMMARIES,
        "label semantics": LABEL_SEMANTICS,
        "canonical basis": CANONICAL_RELEASE_BASIS,
        "access": ACCESS_CONDITIONS,
        "licenses": LICENSES,
        "release versions": RELEASE_VERSIONS,
        "normal-only training": NORMAL_ONLY_TRAINING,
        "spatial scope": SPATIAL_SCOPE,
    }
    for label, mapping in mappings.items():
        missing = names - mapping.keys()
        extra = mapping.keys() - names
        if missing or extra:
            raise ValueError(
                f"{label} mismatch: missing={sorted(missing)}, extra={sorted(extra)}"
            )


def main() -> None:
    with SOURCE_CSV.open(encoding="utf-8", newline="") as handle:
        records = list(csv.DictReader(handle))
    records_by_name = {record["dataset_name"]: record for record in records}
    csv_names = set(records_by_name)
    if len(records_by_name) != len(records):
        raise ValueError("Source CSV contains duplicate dataset names")
    validate_metadata(csv_names)

    text = TABLE_PATH.read_text(encoding="utf-8")
    if NOTES_BEGIN in text:
        before, remainder = text.split(NOTES_BEGIN, 1)
        _, after = remainder.split(NOTES_END, 1)
        text = before.rstrip() + "\n" + after.lstrip("\n")
    rendered_names: list[str] = []
    rendered_lines: list[str] = []
    modalities: dict[str, str] = {}
    dataset_cells: dict[str, str] = {}
    domain_groups: dict[str, str] = {}
    current_group: str | None = None

    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith(r"\caption{"):
            rendered_lines.append(TABLE_CAPTION)
            continue
        if "Multi-industry anomaly" in line:
            line = line.replace("Multi-industry anomaly", "Cross-domain industrial benchmarks")
        if r"\multicolumn{6}" in line and r"\textit{" in line:
            current_group = line.split(r"\textit{", 1)[1].split("}", 1)[0]
            current_group = current_group.replace(r"\&", "&")
        if "citep{" not in line or stripped.startswith("%"):
            rendered_lines.append(line)
            continue

        cells = line.strip().removesuffix(r"\\").strip().split(" & ")
        if len(cells) != 6:
            raise ValueError(f"Expected six cells in dataset row: {line}")
        name = dataset_key(cells[0])
        if name not in csv_names:
            raise ValueError(f"Table dataset is absent from source CSV: {name}")

        rendered_names.append(name)
        dataset_cells[name] = cells[0]
        modalities[name] = cells[3]
        if current_group is None:
            raise ValueError(f"Dataset row appears before a domain group: {name}")
        domain_groups[name] = current_group
        rendered_lines.append(
            "    "
            + " & ".join(
                (
                    cells[0],
                    TASKS[name],
                    ANNOTATIONS[name],
                    cells[3],
                    RESOLUTIONS[name],
                    SAMPLE_SUMMARIES[name],
                )
            )
            + r" \\"
        )

    if rendered_names != [record["dataset_name"] for record in records]:
        raise ValueError("Table and source CSV dataset order differ")
    if len(rendered_names) != 61 or len(set(rendered_names)) != 61:
        raise ValueError("Table must contain exactly 61 unique active dataset rows")

    while rendered_lines and rendered_lines[-1] == "":
        rendered_lines.pop()
    if rendered_lines[-1] != r"\endgroup":
        raise ValueError("Unexpected Table 1 file ending")
    rendered_lines.insert(-1, "")
    rendered_lines.insert(-1, TABLE_NOTES)
    TABLE_PATH.write_text("\n".join(rendered_lines) + "\n", encoding="utf-8")

    SUPPLEMENT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with SUPPLEMENT_PATH.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=SUPPLEMENT_FIELDS, lineterminator="\n")
        writer.writeheader()
        for name in rendered_names:
            source = records_by_name[name]
            writer.writerow({
                "registry_version": REGISTRY_VERSION,
                "metadata_snapshot_date": SNAPSHOT_DATE,
                "dataset_name": name,
                "domain_group": domain_groups[name],
                "task_controlled": TASKS[name],
                "task_source": source["task"],
                "annotation_controlled": ANNOTATIONS[name],
                "modality": modalities[name],
                "native_or_released_resolution": source["image_resolution"].replace(
                    "; model input: 480x480", ""
                ).replace("NA originals; 416x416 preprocessed", "NA").replace(
                    "1920x1080 originals; 128x128 model input", "1920x1080"
                ).replace(
                    "1920x1080 originals; 1440x810 paper downsample", "1920x1080"
                ),
                "label_semantics": LABEL_SEMANTICS[name],
                "dataset_type": DATASET_TYPES.get(name, "original release"),
                "parent_datasets": PARENT_DATASETS.get(name, "none"),
                "canonical_release_basis": CANONICAL_RELEASE_BASIS[name],
                "release_version": RELEASE_VERSIONS[name],
                "release_discrepancy": DISCREPANCIES.get(name, "none identified"),
                "total_samples_source": source["total_samples"],
                "classes_source": source["classes"],
                "samples_per_class_source": source["samples_per_class"],
                "official_split_or_protocol": split_status(source["split_information"]),
                "normal_only_training": NORMAL_ONLY_TRAINING[name],
                "spatial_annotation_scope": SPATIAL_SCOPE[name],
                "positive_sample_availability": positive_sample_availability(source),
                "access_condition": ACCESS_CONDITIONS[name],
                "license": LICENSES[name],
                "resolution_notes": source["resolution_notes"],
                "count_notes": source["count_notes"],
                "primary_source": source["primary_source"],
            })

    print(
        f"Rendered {len(rendered_names)} Table 1 rows and wrote "
        f"{SUPPLEMENT_PATH.relative_to(ROOT)}"
    )


if __name__ == "__main__":
    main()
