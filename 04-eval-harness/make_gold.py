import csv
from pathlib import Path
from collections import Counter

images_dir = Path("images")

suffix_list = [".jpg", ".jpeg", ".png", ".webp"]
hard = {
    "beach/beach_03.jpg",      # Beach with ice
    "beach/beach_09.jpg",      # Mainly water
    "bedroom/bedroom_06.jpg",  # Outdoor area shown
    "bedroom/bedroom_08.jpg",  # City skyline, looks like a hotel room
    "gym/gym_03.jpg",          # Mainly for yoga
    "gym/gym_04.jpg",          # Mainly a boxing area
    "kitchen/kitchen_08.jpg",  # Could also be a dining area
    "kitchen/kitchen_10.jpg",  # Outdoor grilling area
    "office/office_03.jpg",    # Looks like a meeting room
    "office/office_04.jpg",    # Looks like a reception desk
    "office/office_05.jpg",    # Looks like a kitchen
}
rows = []
for item in sorted(images_dir.iterdir()):
    if item.is_dir():
        for im in sorted(item.iterdir()):
            if im.suffix.lower() in suffix_list:
                relative_path = im.relative_to(images_dir)
                image_path = relative_path.as_posix()
                slice_name = "hard" if image_path in hard else "typical"
                row = [image_path, item.name, slice_name]
                rows.append(row)

counts = Counter(row[1] for row in rows)

for label, count in counts.items():
    print(f"{label}:{count}")

gold_path = Path("gold.csv")

with gold_path.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["image_path", "label", "slice"])
    writer.writerows(rows)

