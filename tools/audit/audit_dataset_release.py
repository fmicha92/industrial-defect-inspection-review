#!/usr/bin/env python3
"""Audit released image datasets without conflating images and annotations."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree

import numpy as np
from PIL import Image


IMAGE_SUFFIXES = {".bmp", ".jpeg", ".jpg", ".png", ".tif", ".tiff", ".webp"}


def class_names(value: str | None) -> list[str]:
    return [item.strip() for item in value.split(",")] if value else []


def named(counter: Counter, names: list[str]) -> dict[str, int]:
    return {
        names[int(key)] if str(key).isdigit() and int(key) < len(names) else str(key): value
        for key, value in sorted(counter.items(), key=lambda item: str(item[0]))
    }


def dimensions(root: Path) -> dict:
    counts: Counter = Counter()
    unreadable: list[str] = []
    files = [path for path in root.rglob("*") if path.suffix.lower() in IMAGE_SUFFIXES]
    for path in files:
        try:
            with Image.open(path) as image:
                counts[f"{image.width}x{image.height}"] += 1
        except Exception:
            unreadable.append(str(path))
    return {"files": len(files), "dimensions": dict(counts), "unreadable": unreadable}


def yolo(root: Path, names: list[str], class_index: int) -> dict:
    objects: Counter = Counter()
    memberships: Counter = Counter()
    files = sorted(path for path in root.rglob("*") if path.suffix.lower() in {".txt", ".yolo"})
    invalid: list[str] = []
    for path in files:
        present = set()
        for line_number, line in enumerate(path.read_text(errors="replace").splitlines(), 1):
            fields = line.split()
            if not fields:
                continue
            try:
                label = str(int(float(fields[class_index])))
            except (IndexError, ValueError):
                invalid.append(f"{path}:{line_number}")
                continue
            objects[label] += 1
            present.add(label)
        memberships.update(present)
    return {
        "annotation_files": len(files),
        "image_memberships": named(memberships, names),
        "objects": named(objects, names),
        "invalid_lines": invalid,
    }


def voc(root: Path) -> dict:
    objects: Counter = Counter()
    memberships: Counter = Counter()
    invalid: list[str] = []
    files = sorted(root.rglob("*.xml"))
    for path in files:
        try:
            labels = [node.text.strip() for node in ElementTree.parse(path).findall(".//object/name")]
        except Exception:
            invalid.append(str(path))
            continue
        objects.update(labels)
        memberships.update(set(labels))
    return {
        "annotation_files": len(files),
        "image_memberships": dict(sorted(memberships.items())),
        "objects": dict(sorted(objects.items())),
        "invalid_files": invalid,
    }


def masks(root: Path, names: list[str]) -> dict:
    memberships: Counter = Counter()
    pixel_counts: Counter = Counter()
    files = [path for path in root.rglob("*") if path.suffix.lower() in IMAGE_SUFFIXES]
    invalid: list[str] = []
    for path in files:
        try:
            values, counts = np.unique(np.asarray(Image.open(path)), return_counts=True)
        except Exception:
            invalid.append(str(path))
            continue
        labels = [str(int(value)) for value in values]
        memberships.update(labels)
        pixel_counts.update({str(int(value)): int(count) for value, count in zip(values, counts)})
    return {
        "mask_files": len(files),
        "image_memberships": named(memberships, names),
        "pixels": named(pixel_counts, names),
        "invalid_files": invalid,
    }


def npz_summary(path: Path) -> dict:
    with np.load(path, allow_pickle=False) as archive:
        return {
            key: {"shape": list(archive[key].shape), "dtype": str(archive[key].dtype)}
            for key in archive.files
        }


def npz_multilabel(path: Path, key: str, names: list[str]) -> dict:
    with np.load(path, allow_pickle=False) as archive:
        labels = archive[key]
    if labels.ndim != 2:
        raise ValueError(f"Expected a two-dimensional label array, got {labels.shape}")
    combination_counts: Counter = Counter()
    memberships: Counter = Counter()
    for row in labels:
        active = tuple(int(index) for index in np.flatnonzero(row))
        combination = "+".join(names[index] if index < len(names) else str(index) for index in active)
        combination_counts[combination or "normal"] += 1
        memberships.update(active)
    return {
        "samples": int(labels.shape[0]),
        "label_dimensions": int(labels.shape[1]),
        "combinations": dict(sorted(combination_counts.items())),
        "image_memberships": named(memberships, names),
    }


def coco(path: Path) -> dict:
    data = json.loads(path.read_text())
    categories = {int(item["id"]): item["name"] for item in data["categories"]}
    dimensions = Counter(
        f"{item['width']}x{item['height']}"
        for item in data["images"]
        if "width" in item and "height" in item
    )
    objects: Counter = Counter()
    image_labels: dict[int, set[int]] = {}
    for annotation in data["annotations"]:
        category = int(annotation["category_id"])
        image_id = int(annotation["image_id"])
        objects[category] += 1
        image_labels.setdefault(image_id, set()).add(category)
    memberships: Counter = Counter()
    for labels in image_labels.values():
        memberships.update(labels)
    return {
        "images": len(data["images"]),
        "dimensions": dict(sorted(dimensions.items())),
        "annotated_images": len(image_labels),
        "image_memberships": {
            categories[key]: value for key, value in sorted(memberships.items())
        },
        "objects": {categories[key]: value for key, value in sorted(objects.items())},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    dimensions_parser = subparsers.add_parser("dimensions")
    dimensions_parser.add_argument("root", type=Path)

    yolo_parser = subparsers.add_parser("yolo")
    yolo_parser.add_argument("root", type=Path)
    yolo_parser.add_argument("--classes")
    yolo_parser.add_argument("--class-index", type=int, default=0)

    voc_parser = subparsers.add_parser("voc")
    voc_parser.add_argument("root", type=Path)

    masks_parser = subparsers.add_parser("masks")
    masks_parser.add_argument("root", type=Path)
    masks_parser.add_argument("--classes")

    npz_parser = subparsers.add_parser("npz-summary")
    npz_parser.add_argument("path", type=Path)

    multilabel_parser = subparsers.add_parser("npz-multilabel")
    multilabel_parser.add_argument("path", type=Path)
    multilabel_parser.add_argument("--key", default="arr_1")
    multilabel_parser.add_argument("--classes")

    coco_parser = subparsers.add_parser("coco")
    coco_parser.add_argument("path", type=Path)

    args = parser.parse_args()
    if args.command == "dimensions":
        result = dimensions(args.root)
    elif args.command == "yolo":
        result = yolo(args.root, class_names(args.classes), args.class_index)
    elif args.command == "voc":
        result = voc(args.root)
    elif args.command == "masks":
        result = masks(args.root, class_names(args.classes))
    elif args.command == "npz-summary":
        result = npz_summary(args.path)
    elif args.command == "npz-multilabel":
        result = npz_multilabel(args.path, args.key, class_names(args.classes))
    else:
        result = coco(args.path)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
