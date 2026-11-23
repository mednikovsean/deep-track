import csv
from pathlib import Path

images_dir = Path("images")

rows = []
for item in sorted(images_dir.iterdir()):
    if item.is_dir():
        for im in sorted(item.iterdir()):
            relative_path = im.relative_to(images_dir)
            row = [relative_path.as_posix(), item.name, "typical"]
            rows.append(row)

gold_path = Path("gold.csv")

with gold_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["image_path", "label", "slice"])
    writer.writerows(rows)

