import csv
import re
from pathlib import Path

RESULTS_FILE = Path("results/claude-haiku-5-5.csv")
GOLD_FILE = Path("gold.csv")
ALLOWED = {"gym", "bedroom", "office", "kitchen", "beach"}

PRICE_IN = 0.10 #Dollars per million input tokens
PRICE_OUT = 0.50 #Dollars per million output tokens

gold = {}
results = {}
scores = []

with GOLD_FILE.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        image_path = row["image_path"]
        label = row["label"]
        slice_name = row["slice"]
        gold[image_path] = {"label":label, "slice":slice_name}

with RESULTS_FILE.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        image_path = row["image_path"]
        results[image_path] = row


def score_image(path, gold, results):
    label = gold[path]["label"]
    slice_name = gold[path]["slice"]
    missing = path not in results 
    if missing: 
        return {
                "label":label, 
                "slice":slice_name, 
                "missing": missing, 
                "correct":False, 
                "strict_ok":False, 
                "raw":"", 
                "normalized":""
                }
    raw = results[path]["prediction"]
    strict_ok = raw in ALLOWED
    normalized = re.sub(r"[^a-z]","", raw.lower())
    correct = normalized==label 
    return {
            "label":label, 
            "slice":slice_name, 
            "missing": missing, 
            "correct": correct, 
            "strict_ok":strict_ok, 
            "raw":raw, 
            "normalized":normalized
            }

strict_count = 0
normalized_count = 0
format_violation_count = 0
missing_count = 0

for ip in gold:
    score = score_image(ip, gold, results)
    correct = score["correct"]
    strict_ok = score["strict_ok"]
    missing = score["missing"]
    if correct and strict_ok:
        strict_count+=1
    if correct:
        normalized_count+=1
    if correct and not strict_ok:
        format_violation_count+=1
    if missing:
        missing_count+=1
    scores.append(score)

score_count = len(scores)

print(f"Strict:{strict_count}/{score_count} ({strict_count/score_count:.1%})")

print(f"Normalized:{normalized_count}/{score_count} ({normalized_count/score_count:.1%})")

print(f"Format Violations:{format_violation_count}/{score_count} ({format_violation_count/score_count:.1%})")

print(f"Missing:{missing_count}/{score_count} ({missing_count/score_count:.1%})")
