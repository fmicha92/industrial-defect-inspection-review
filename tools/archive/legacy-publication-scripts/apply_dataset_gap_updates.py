#!/usr/bin/env python3
"""Apply verified resolution/count updates and emit a provenance audit."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TABLE = ROOT / "table1_dataset_resolution_and_class_counts.csv"
AUDIT = ROOT / "table1_dataset_gap_audit.csv"


UPDATES: dict[str, dict[str, str]] = {
    "MixedWM38": {
        "total_samples": "38015 wafer maps",
        "samples_per_class": (
            "normal: 1000; C2: 1000; C3: 1000; C4: 1000; C5: 1000; C6: 1000; "
            "C7: 149; C8: 1000; C9: 866; C2+C4: 1000; C2+C5: 1000; "
            "C2+C6: 1000; C2+C8: 1000; C3+C4: 1000; C3+C5: 1000; "
            "C3+C6: 1000; C3+C8: 1000; C4+C6: 1000; C4+C8: 1000; "
            "C5+C6: 1000; C5+C8: 1000; C6+C8: 1000; C2+C4+C6: 1000; "
            "C2+C4+C8: 2000; C2+C5+C6: 1000; C2+C5+C8: 1000; "
            "C2+C6+C8: 1000; C3+C4+C6: 1000; C3+C4+C8: 1000; "
            "C3+C5+C6: 1000; C3+C5+C8: 1000; C3+C6+C8: 1000; "
            "C4+C6+C8: 1000; C5+C6+C8: 1000; C2+C4+C6+C8: 1000; "
            "C2+C5+C6+C8: 1000; C3+C4+C6+C8: 1000; C3+C5+C6+C8: 1000"
        ),
        "split_information": "No official fixed train/validation/test split in the release.",
        "count_notes": (
            "Exact label-combination counts were recomputed from the released NPZ and sum to 38015. "
            "C2-C9 are repository codes; physical defect names were not inferred."
        ),
    },
    "DeepPCB": {
        "samples_per_class": (
            "open: 1344; short: 1101; mousebite: 1269; spur: 1184; "
            "pinhole: 1315; spurious copper: 1241"
        ),
        "count_notes": (
            "Counts are image memberships derived from all released annotations and are nonexclusive. "
            "Object totals are 1942/1506/1965/1625/1501/1474 in class order and are not used as sample counts."
        ),
    },
    "DsPCBSD+": {
        "samples_per_class": (
            "short: 604; spur: 2186; spurious copper: 1317; open: 1420; "
            "mouse bite: 1873; hole breakout: 1290; conductor scratch: 1487; "
            "conductor foreign object: 1352; base-material foreign object: 1484"
        ),
        "count_notes": (
            "Image memberships were recomputed from release annotations and are nonexclusive. "
            "The corresponding 20276 annotations remain object counts, not image samples."
        ),
    },
    "Heat Sink Surface Defects": {
        "samples_per_class": "background: 1000; scratch: 700; stain: 972",
        "count_notes": (
            "Counts are image memberships derived from all 1000 released masks. "
            "Foreground memberships overlap; pixel totals are not substituted for image counts."
        ),
    },
    "PV Panel Defect Dataset": {
        "image_resolution": "variable (493 sizes; width 149-6240, height 110-5376)",
        "resolution_notes": (
            "All 1574 release images were inspected; 493 distinct width-by-height pairs occur. "
            "The range is original release resolution, not model preprocessing."
        ),
    },
    "Dataset of Solar Cells Defect Segm.": {
        "image_resolution": (
            "SolarCells: 448x448; SolarCells-S: variable originals (sampled 417x426 to 437x436); "
            "PVEL-S: 512x512 and 1024x1024 observed; model input: 480x480"
        ),
        "samples_per_class": (
            "SolarCells defect: 190; SolarCells-S defect: 36 originals (180 augmented); "
            "PVEL-S defect: 1200"
        ),
        "resolution_notes": (
            "SolarCells is fixed by the paper and release. SolarCells-S and PVEL-S are variable in "
            "representative files from every release split; the paper standardizes model input to 480x480."
        ),
        "count_notes": (
            "Every released input is a defect image paired with a binary mask. Kaggle inventory confirms "
            "152/38 SolarCells, 144/36 augmented SolarCells-S, and 960/240 PVEL-S train/test files."
        ),
    },
    "BenchmarkELimages": {
        "total_samples": (
            "582 in original 20211104 release; 593 stated in paper; later releases contain 2175 and 2354"
        ),
        "samples_per_class": (
            "background: 582; sp multi: 245; sp mono: 264; sp dogbone: 4; ribbons: 573; "
            "border: 319; text: 16; padding: 323; clamp: 1; busbars: 58; crack ribbon edge: 5; "
            "inactive: 65; rings: 1; material: 151; crack: 277; gridline: 385; splice: 61; "
            "dead cell: 2; corrosion: 16; belt mark: 2; edge dark: 34; frame edge: 115; "
            "junction box: 9; measurement artifact: 3"
        ),
        "count_notes": (
            "Counts are nonexclusive image memberships from all 582 masks in the original 20211104 "
            "repository release. The paper/release total discrepancy is retained explicitly."
        ),
    },
    "PV-Multi-Defect": {
        "samples_per_class": (
            "broken: 82; hot_spot: 222; black_border: 159; scratch: 650; no_electricity: 166"
        ),
        "count_notes": (
            "Image memberships were derived from 1106 released XML files and are nonexclusive; two of "
            "1108 images lack XML. The XML files contain 3981 objects, while the paper reports 4235 targets."
        ),
    },
    "Thermal PV UAV Dataset": {
        "samples_per_class": (
            "fault-class image memberships: NA; generic PV-panel annotation present: 351; unlabeled images: 2"
        ),
        "count_notes": (
            "The release labels 351 images with a generic PV-panel class and contains 26678 boxes. "
            "Damage-type memberships are not encoded, so they remain unavailable rather than inferred from overlays."
        ),
    },
    "GC10-DET": {
        "classes": (
            "silk spot; welding line; punching hole; water spot; crescent gap; "
            "oil spot; inclusion; waist folding; crease; rolled pit"
        ),
        "total_samples": (
            "2300 images in current Dataset Ninja snapshot; introducing paper reports 3570"
        ),
        "image_resolution": "2048x1000",
        "samples_per_class": (
            "silk spot: 734; welding line: 512; punching hole: 329; water spot: 310; "
            "crescent gap: 264; oil spot: 250; inclusion: 201; waist folding: 140; "
            "crease: 53; rolled pit: 46"
        ),
        "split_information": (
            "No official fixed train/validation/test split in the Dataset Ninja snapshot."
        ),
        "resolution_notes": (
            "Dataset Ninja reports image size as height x width = 1000x2048; Table 1 converts "
            "this to width x height = 2048x1000."
        ),
        "count_notes": (
            "The Dataset Ninja snapshot contains 2300 images, including 8 unlabeled images, and "
            "3563 bounding boxes. Per-class image memberships sum to 2839 because they are "
            "nonexclusive. The introducing paper's 3570-image total is retained as a source discrepancy."
        ),
        "primary_source": (
            "https://datasetninja.com/gc10-det; "
            "https://github.com/lvxiaoming2019/GC10-DET-Metallic-Surface-Defect-Datasets; "
            "https://doi.org/10.3390/s20061562"
        ),
    },
    "MPDD2": {
        "image_resolution": "256x256 in the public release and benchmark input",
        "resolution_notes": (
            "Public Google Drive samples from all four product classes are 256x256, matching the "
            "introducing paper's benchmark input preprocessing."
        ),
    },
    "HSS-IAD": {
        "total_samples": "12075 release images (README states 8580)",
        "image_resolution": (
            "Casting C1-C3: 1024x1024; STEEL: 1600x256; Magnetic Tile: 122x271; "
            "KolektorSDD2: 229x632; KolektorSDD: 500x1246"
        ),
        "samples_per_class": (
            "Casting_C1: 471; Casting_C2: 1330; Casting_C3: 382; STEEL: 4877; "
            "MTD: 1281; KolektorSDD2: 3335; KolektorSDD: 399"
        ),
        "split_information": (
            "Release train/test folders were audited by source category; category totals sum to 12075."
        ),
        "resolution_notes": "Resolution is category-specific in the released composite folders.",
        "count_notes": (
            "Direct release inventory totals 12075, conflicting with the README's 8580 statement; "
            "the release-derived category totals are reported and the conflict is preserved."
        ),
    },
    "LoHi-WELD": {
        "samples_per_class": "pores: 744; deposits: 1538; discontinuities: 2861; stains: 2117",
        "count_notes": (
            "Counts are nonexclusive image memberships from release labels. Corresponding object totals "
            "are 3950, 2935, 7220, and 8307 and are not used as image counts."
        ),
    },
    "ZJU-Leaper": {
        "total_samples": "94833 images",
        "image_resolution": "512x512",
        "samples_per_class": (
            "White Plain: 3564; Thick Stripe: 4106; Thin Stripe: 4106; Dot Pattern: 4106; "
            "Houndstooth: 5448; Gingham: 5556; Knot Pattern: 6100; Twill Plaid: 5692; "
            "Blue Plaid: 5972; Brown Plaid: 5868; Gray Plaid: 4676; Red Plaid: 5304; "
            "Floral Print1: 5248; Floral Print2: 4928; Floral Print3: 4708; Pattern1: 4253; "
            "Pattern2: 7244; Pattern3: 2358; Pattern4: 5596"
        ),
        "split_information": (
            "Normal/defective totals with normal train/test and defective train/test in parentheses: "
            "White Plain 2673/891 (1768/905; 608/283); "
            "Thick Stripe 3080/1026 (2045/1035; 684/342); "
            "Thin Stripe 3080/1026 (2046/1034; 677/349); "
            "Dot Pattern 3080/1026 (2073/1007; 656/370); "
            "Houndstooth 4086/1362 (2718/1368; 898/464); "
            "Gingham 4167/1389 (2851/1316; 941/448); "
            "Knot Pattern 4575/1525 (3062/1513; 1008/517); "
            "Twill Plaid 4269/1423 (2863/1406; 952/471); "
            "Blue Plaid 4479/1493 (2999/1480; 975/518); "
            "Brown Plaid 4401/1467 (2924/1477; 978/489); "
            "Gray Plaid 3507/1169 (2335/1172; 770/399); "
            "Red Plaid 3978/1326 (2644/1334; 863/463); "
            "Floral Print1 3936/1312 (2632/1304; 861/451); "
            "Floral Print2 3696/1232 (2422/1274; 814/418); "
            "Floral Print3 3531/1177 (2353/1178; 824/353); "
            "Pattern1 3190/1063 (2138/1052; 711/352); "
            "Pattern2 5433/1811 (3603/1830; 1238/573); "
            "Pattern3 1769/589 (1168/601; 380/209); "
            "Pattern4 4197/1399 (2779/1418; 923/476). "
            "Aggregate normal/defective: 71127/23706; aggregate train/test: 63184/31649."
        ),
        "resolution_notes": "Corrected release metadata reports 512x512 images.",
        "count_notes": (
            "Every per-pattern normal and defective total equals its supplied train-plus-test subtotals. "
            "Corrected totals are 94833 images (71127 normal and 23706 defective), comprising "
            "63184 training and 31649 test images."
        ),
    },
    "FabricSpotDefect": {
        "samples_per_class": "Spot: 1014",
        "count_notes": (
            "The primary paper states that all 1014 raw images contain the Spot class; 3288 is the "
            "polygon annotation count, not the number of images."
        ),
    },
    "FD_Dataset": {
        "total_samples": "720 advertised/prepared YOLO images; 723 files in raw FULLDataset folder",
        "image_resolution": (
            "raw variable (401 sizes; width 358-1280, height 299-1280); prepared YOLO: 640x640"
        ),
        "samples_per_class": "Oil: 174; Hole: 180; Cutting: 190; Crack: 188",
        "resolution_notes": (
            "All 723 raw files and all 720 prepared YOLO images were inspected. The raw and prepared "
            "release views are reported separately."
        ),
        "count_notes": (
            "Counts are image memberships from 720 nonempty YOLO labels and are nonexclusive; 12 images "
            "contain more than one class. Object totals are Oil 207, Hole 182, Cutting 197, Crack 195."
        ),
    },
    "AGDD": {
        "image_resolution": "1280x720 source pairs; 640x640 prepared release",
        "samples_per_class": "contusion: 122; scratches: 123; crack: 23; spot: 120",
        "resolution_notes": (
            "Aligned forward/backward source images are 1280x720; the released prepared detection images are 640x640."
        ),
        "count_notes": (
            "Counts are nonexclusive defect memberships across the 219 original paired samples. "
            "Augmented object totals are kept separate from image memberships."
        ),
    },
    "Glass Bangle Defect Detection Classification": {
        "classes": "broken; defect; good",
        "image_resolution": "3000x3000",
        "samples_per_class": "broken: 316; defect: 244; good: 520",
        "split_information": (
            "No fixed split in the release; the paper reports 75/25 train/test with four-fold evaluation."
        ),
        "resolution_notes": "The primary paper reports 3000x3000 RGB originals.",
        "count_notes": (
            "Exact counts come from all 1080 paths in the public Kaggle release and sum to the paper total."
        ),
    },
    "SSGD": {
        "classes": (
            "normal; crack; broken/chip; spot; scratch; light-leakage; blot/foreign matter; broken-membrane"
        ),
        "samples_per_class": (
            "normal: 757; crack: 668; broken/chip: 295; spot: 451; scratch: 546; "
            "light-leakage: 59; blot/foreign matter: 12; broken-membrane: 59"
        ),
        "count_notes": (
            "Image memberships were derived from all released XML files across Parts I and II. "
            "Defect memberships are nonexclusive; 3914 is the defect-object total."
        ),
    },
    "CarDD": {
        "samples_per_class": (
            "dent: 1751; scratch: 2121; crack: 604; glass shatter: 674; tire flat: 309; lamp broken: 693"
        ),
        "count_notes": (
            "Counts are nonexclusive image memberships from the released annotations. Corresponding "
            "instance totals are 2543, 3595, 898, 681, 319, and 704 in class order."
        ),
    },
    "Structural Adhesive Defects Dataset": {
        "classes": "discontinuity; excess adhesive",
        "total_samples": (
            "GAN source: 143 real images; detector: 594 train images (593 labels), 58 validation, "
            "19 holdout label/image pairs (release prose states 18)"
        ),
        "samples_per_class": (
            "train discontinuity/excess: 423/357; validation: 37/41; holdout: 14/13"
        ),
        "split_information": (
            "GAN source: 143 real images; detector: 594 train images, 58 validation images, "
            "and 19 holdout labels; components overlap by purpose and are not summed."
        ),
        "count_notes": (
            "Counts are nonexclusive image memberships from release labels. Train has 593 labels for "
            "594 stated images; holdout has 19 labels although release prose states 18."
        ),
    },
    "Open Stamped Parts Dataset": {
        "classes": "AX1; BY1; CY1; DY1; DY2; DY3; DY4",
        "total_samples": (
            "real: 9660 (1680 labeled, 7980 unlabeled); synthetic release: 11240 "
            "(paper states 11340)"
        ),
        "image_resolution": "1456x1088",
        "samples_per_class": (
            "real labeled - AX1: 354; BY1: 1467; CY1: 630; DY1: 1073; DY2: 1280; "
            "DY3: 846; DY4: 1047; synthetic - AX1: 2411; BY1: 9856; CY1: 4385; "
            "DY1: 7438; DY2: 7629; DY3: 6493; DY4: 6610"
        ),
        "split_information": (
            "real: 1680 labeled/7980 unlabeled; synthetic release JSON: 7909 train/1666 validation/1665 test"
        ),
        "resolution_notes": "All audited real and synthetic release images are 1456x1088.",
        "count_notes": (
            "Class values are nonexclusive image memberships. The synthetic JSON totals 11240, "
            "which conflicts with the paper's 11340 statement; both are retained explicitly."
        ),
    },
    "BTAD": {
        "classes": "product 01; product 02; product 03",
        "total_samples": "2540 inspection images; 290 ground-truth masks",
        "image_resolution": "product 01: 1600x1600; product 02: 600x600; product 03: 800x600",
        "samples_per_class": "product 01: 470; product 02: 629; product 03: 1441",
        "split_information": (
            "train normal/test normal/test anomalous - product 01: 400/21/49; "
            "product 02: 399/30/200; product 03: 1000/400/41"
        ),
        "resolution_notes": "All 2540 inspection images in the official archive were inspected by product.",
        "count_notes": (
            "Product totals sum to 2540 inspection images. The often quoted 2830 count includes the "
            "290 ground-truth mask files and is not an inspection-image total."
        ),
    },
}


AUDIT_META: dict[str, dict[str, str]] = {
    "MixedWM38": {"resolution_status": "verified", "count_status": "verified", "evidence_level": "release audit", "evidence_source": "released NPZ and official GitHub repository", "caveat": "C2-C9 semantics are not mapped to physical names."},
    "DeepPCB": {"resolution_status": "verified", "count_status": "verified", "evidence_level": "release audit", "evidence_source": "official GitHub annotations", "caveat": "Image memberships are nonexclusive."},
    "DsPCBSD+": {"resolution_status": "verified", "count_status": "verified", "evidence_level": "release audit", "evidence_source": "official Figshare archive", "caveat": "Image memberships are nonexclusive."},
    "Heat Sink Surface Defects": {"resolution_status": "verified", "count_status": "verified", "evidence_level": "release audit", "evidence_source": "public release images and masks", "caveat": "Counts describe mask-class presence per image."},
    "PV Panel Defect Dataset": {"resolution_status": "verified", "count_status": "verified", "evidence_level": "release audit", "evidence_source": "public Kaggle release", "caveat": "Resolution is variable across 493 sizes."},
    "Dataset of Solar Cells Defect Segm.": {"resolution_status": "partial", "count_status": "verified", "evidence_level": "primary paper plus release inventory", "evidence_source": "Chen et al. paper and public Kaggle release", "caveat": "SolarCells-S and PVEL-S resolution values are release samples, not a complete dimension distribution."},
    "BenchmarkELimages": {"resolution_status": "verified", "count_status": "verified", "evidence_level": "release audit", "evidence_source": "official GitHub 20211104 release", "caveat": "Paper total 593 conflicts with 582 released masks."},
    "PV-Multi-Defect": {"resolution_status": "verified", "count_status": "verified", "evidence_level": "release audit", "evidence_source": "official GitHub release", "caveat": "Two images lack XML; object total conflicts with paper target total."},
    "Thermal PV UAV Dataset": {"resolution_status": "verified", "count_status": "unresolved", "evidence_level": "release audit", "evidence_source": "official Zenodo archive", "caveat": "Release labels panels, not the listed fault categories."},
    "SolarDK": {"resolution_status": "unresolved", "count_status": "verified", "evidence_level": "primary paper/host", "evidence_source": "official OSF record", "caveat": "Only 10-15 cm/pixel GSD is reported; OSF parts currently return HTTP 502."},
    "GC10-DET": {"resolution_status": "verified", "count_status": "verified", "evidence_level": "secondary release-statistics audit", "evidence_source": "Dataset Ninja snapshot accessed 2026-08-03", "caveat": "Dataset Ninja is an informational secondary source; its 2300-image snapshot conflicts with the introducing paper's 3570-image total, and class image memberships are nonexclusive."},
    "APDDD": {"resolution_status": "verified", "count_status": "unresolved", "evidence_level": "primary host/paper", "evidence_source": "official Tianchi record", "caveat": "5279 values are boxes; release access is request-gated."},
    "MPDD2": {"resolution_status": "verified", "count_status": "verified", "evidence_level": "primary paper plus release sampling", "evidence_source": "official GitHub and Google Drive release", "caveat": "Google Drive listing paginates at 50, so counts remain paper-derived."},
    "CSDD": {"resolution_status": "verified", "count_status": "unresolved", "evidence_level": "primary host", "evidence_source": "official GitHub repository", "caveat": "Archive is supplied by email; 56356 values are objects."},
    "HSS-IAD": {"resolution_status": "verified", "count_status": "verified", "evidence_level": "release audit", "evidence_source": "official GitHub release folders", "caveat": "Release total 12075 conflicts with README total 8580."},
    "LoHi-WELD": {"resolution_status": "verified", "count_status": "verified", "evidence_level": "release audit", "evidence_source": "official GitHub labels", "caveat": "Image memberships are nonexclusive."},
    "BSData": {"resolution_status": "partial", "count_status": "verified", "evidence_level": "primary host/release", "evidence_source": "official GitHub repository and DOI record", "caveat": "Classification crops are 150x150; the detection/segmentation release dimensions remain unreported."},
    "ZJU-Leaper": {"resolution_status": "verified", "count_status": "verified", "evidence_level": "corrected release metadata", "evidence_source": "author-supplied release table", "caveat": "Per-pattern image counts and train/test splits are verified; spatial instance totals remain unreported."},
    "FabricSpotDefect": {"resolution_status": "partial", "count_status": "verified", "evidence_level": "primary paper", "evidence_source": "introducing paper and Mendeley record", "caveat": "Original dimensions are unreported; 416x416 is preprocessing."},
    "FD_Dataset": {"resolution_status": "verified", "count_status": "verified", "evidence_level": "release audit", "evidence_source": "official Figshare raw and prepared releases", "caveat": "Raw folder has 723 files while the prepared/advertised set has 720."},
    "AGDD": {"resolution_status": "verified", "count_status": "verified", "evidence_level": "release audit", "evidence_source": "official GitHub release", "caveat": "Counts are memberships of 219 paired samples."},
    "Glass Bangle Defect Detection Classification": {"resolution_status": "verified", "count_status": "verified", "evidence_level": "primary paper plus release inventory", "evidence_source": "introducing paper and public Kaggle release", "caveat": "Release has no fixed split."},
    "MVEP": {"resolution_status": "partial", "count_status": "unresolved", "evidence_level": "primary host metadata", "evidence_source": "official LIRIS host", "caveat": "1008x1008 is a metadata example; full archive and label distribution are unavailable."},
    "SSGD": {"resolution_status": "verified", "count_status": "verified", "evidence_level": "release audit", "evidence_source": "official GitHub release archive", "caveat": "Defect image memberships are nonexclusive."},
    "CarDD": {"resolution_status": "verified", "count_status": "verified", "evidence_level": "release audit", "evidence_source": "official release annotations", "caveat": "Image memberships are nonexclusive."},
    "Structural Adhesive Defects Dataset": {"resolution_status": "verified", "count_status": "verified", "evidence_level": "release audit", "evidence_source": "official GitHub release assets", "caveat": "One train image is unlabeled; holdout file count conflicts with prose."},
    "Open Stamped Parts Dataset": {"resolution_status": "verified", "count_status": "verified", "evidence_level": "release audit", "evidence_source": "official public blob archive", "caveat": "Synthetic release total conflicts with paper total."},
    "BTAD": {"resolution_status": "verified", "count_status": "verified", "evidence_level": "release audit", "evidence_source": "official BTAD archive", "caveat": "The 2830 figure counts 2540 inspections plus 290 masks."},
}


def main() -> None:
    with TABLE.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fieldnames = reader.fieldnames
        rows = list(reader)
    if not fieldnames:
        raise RuntimeError("Table has no header")

    by_name = {row["dataset_name"]: row for row in rows}
    missing = sorted(set(UPDATES) - set(by_name))
    if missing:
        raise RuntimeError(f"Unknown dataset names: {missing}")
    for name, values in UPDATES.items():
        by_name[name].update(values)

    with TABLE.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)

    audit_fields = [
        "dataset_name",
        "resolution_status",
        "image_resolution",
        "count_status",
        "samples_per_class",
        "evidence_level",
        "evidence_source",
        "caveat",
    ]
    with AUDIT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=audit_fields, lineterminator="\n")
        writer.writeheader()
        for name, metadata in AUDIT_META.items():
            row = by_name[name]
            writer.writerow(
                {
                    "dataset_name": name,
                    "resolution_status": metadata["resolution_status"],
                    "image_resolution": row["image_resolution"],
                    "count_status": metadata["count_status"],
                    "samples_per_class": row["samples_per_class"],
                    "evidence_level": metadata["evidence_level"],
                    "evidence_source": metadata["evidence_source"],
                    "caveat": metadata["caveat"],
                }
            )

    print(f"updated {len(UPDATES)} datasets")
    print(f"wrote {len(AUDIT_META)} audit rows to {AUDIT.name}")


if __name__ == "__main__":
    main()
