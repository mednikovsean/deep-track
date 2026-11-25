import base64
import anthropic
import csv
from pathlib import Path
from time import perf_counter
import math


client = anthropic.Anthropic()
model_name = "claude-haiku-5-5"
prompt = "What kind of place is this? Answer with exactly one word from: gym, bedroom, kitchen, beach, office."

results_dir = Path("results.dir")
results_dir.mkdir(exist_ok=True)
model_path = results_dir/f"{model_name}.csv"

gold_path = Path("gold.csv")

image_paths = {}
with gold_path.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        image_path = row["image_path"]
        label = row["label"]
        image_paths[image_path] = label

if not model_path.exists() or model_path.stat().st_size == 0:
     with model_path.open("a", newline="", encoding="utf-8") as file:
          writer = csv.writer(file)
          writer.writerow([
               "image_path", "label", "prediction",
               "input_tokens", "output_tokens", "seconds",
          ])
completed = set()
with model_path.open("r", newline="", encoding="utf-8") as file:
     reader = csv.DictReader(file)
     for row in reader:
          completed.add(row["image_path"])
     

for ip, l in image_paths.items():

    if ip in completed:
         continue
    
    extension = Path(ip).suffix.lower()

    if extension==".jpg" or extension==".jpeg":
                media_type = "image/jpeg"
    elif extension==".png":
        media_type = "image/png"
    elif extension==".webp":
        media_type = "image/webp"
    else:
         raise ValueError(f"Unsupported image extension {extension!r} for {ip!r}")

    with open("images/"+ip, "rb") as f:
        image_data = base64.standard_b64encode(f.read()).decode("utf-8")
        
    start = perf_counter()

    try: 
        print(f"Calling Claude for {ip}")
        response = client.messages.create(
            model = model_name,
            max_tokens = 1000,
            messages = [{
                "role": "user",
                "content": [
                    {"type": "image",
                    "source": {"type":"base64", "media_type":media_type, "data": image_data}},
                    {"type": "text",
                    "text": prompt}
                ],
            }],
        )
    except anthropic.APIError as error:
         print(f"API call failed for {ip}:{error}")
         continue
    
    elapsed = math.floor((perf_counter() - start)*1000)/1000

    prediction = None

    for block in response.content:
         if block.type == "text":
            prediction = block.text.strip().lower()
            break

    if prediction is None:
         print(f"No text answer for {ip}. Stop reason: {response.stop_reason}")
         print([block.type for block in response.content])
         continue

    res = [
            ip, 
            l, 
            prediction, 
            response.usage.input_tokens, 
            response.usage.output_tokens, 
            f"{elapsed:.3f}"
    ]

    with model_path.open("a", newline="", encoding="utf-8") as file:
         writer=csv.writer(file)
         writer.writerow(res)
