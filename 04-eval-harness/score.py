import csv
import re
from collections import defaultdict
from pathlib import Path

RESULTS_FILE = Path("results/claude-haiku-5-5.csv")
GOLD_FILE = Path("gold.csv")
ALLOWED = {"gym", "bedroom", "office", "kitchen", "beach"}

PRICE_IN = 0.10  # Dollars per million input tokens
PRICE_OUT = 0.50  # Dollars per million output tokens


def score_image(path, gold, results):
    label = gold[path]["label"]
    slice_name = gold[path]["slice"]

    if path not in results:
        return {
            "label": label,
            "slice": slice_name,
            "missing": True,
            "correct": False,
            "strict_ok": False,
            "raw": "",
            "normalized": "",
        }

    raw = results[path]["prediction"]
    normalized = re.sub(r"[^a-z]", "", raw.lower())

    return {
        "label": label,
        "slice": slice_name,
        "missing": False,
        "correct": normalized == label,
        "strict_ok": raw in ALLOWED,
        "raw": raw,
        "normalized": normalized,
    }


def score_file(results_file):
    print(f"\n=== {results_file.name} ===")

    gold = {}
    results = {}
    scores = []
    total_in_tokens = 0
    total_out_tokens = 0
    seconds = []

    strict_count = 0
    normalized_count = 0
    format_violation_count = 0
    missing_count = 0

    label_groups = defaultdict(list)
    slice_groups = defaultdict(list)

    with GOLD_FILE.open("r", newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            image_path = row["image_path"]
            gold[image_path] = {"label": row["label"], "slice": row["slice"]}

    with results_file.open("r", newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            image_path = row["image_path"]
            results[image_path] = row
            total_in_tokens += int(row["input_tokens"])
            total_out_tokens += int(row["output_tokens"])
            seconds.append(float(row["seconds"]))

    for ip in gold:
        score = score_image(ip, gold, results)
        correct = score["correct"]
        strict_ok = score["strict_ok"]
        missing = score["missing"]
        label = score["label"]
        slice_name = score["slice"]
        prediction = score["raw"]

        label_groups[label].append(score)
        slice_groups[slice_name].append(score)

        if correct and strict_ok:
            strict_count += 1
        if correct:
            normalized_count += 1

        if missing:
            missing_count += 1
            print(f"MISSING  {ip}  expected: {label}")
        elif not correct:
            print(f"WRONG  {ip}  expected: {label}  got: {prediction}")
        elif not strict_ok:
            format_violation_count += 1
            print(f"FORMAT  {ip}  expected: {label}  got: {prediction!r}")

        scores.append(score)

    total = len(scores)
    strict = strict_count / total if total else 0.0
    normalized = normalized_count / total if total else 0.0

    print(f"Strict:      {strict_count}/{total} ({strict:.1%})")
    print(f"Normalized:  {normalized_count}/{total} ({normalized:.1%})")
    print(f"Format violations: {format_violation_count}   Missing: {missing_count}")

    for heading, groups in (("By label", label_groups), ("By slice", slice_groups)):
        parts = []
        for name, group in sorted(groups.items()):
            right = sum(1 for s in group if s["correct"])
            parts.append(f"{name} {right}/{len(group)}")
        print(f"{heading}:  {', '.join(parts)}")

    cost = (
        (total_in_tokens / 1_000_000) * PRICE_IN
        + (total_out_tokens / 1_000_000) * PRICE_OUT
    )
    cost_per_1k = (cost / total) * 1_000 if total else 0.0
    average_time_elapsed = sum(seconds) / len(seconds) if seconds else None

    print(f"Cost: ${cost:.6f}   Per 1,000: ${cost_per_1k:.4f}")
    if seconds:
        slowest_time_elapsed = max(seconds)
        print(
            f"Avg latency: {average_time_elapsed:.2f}s   "
            f"Slowest: {slowest_time_elapsed:.2f}s"
        )
    else:
        print("Latency: n/a")

    return {
        "file": results_file.name,
        "strict": strict,
        "normalized": normalized,
        "format_violations": format_violation_count,
        "missing": missing_count,
        "cost_per_1k": cost_per_1k,
        "avg_latency": average_time_elapsed,
    }


if __name__ == "__main__":
    score_file(RESULTS_FILE)