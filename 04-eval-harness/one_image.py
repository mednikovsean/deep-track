import base64
import anthropic

client = anthropic.Anthropic()
model_name = "claude-haiku-5-5"
prompt = "What kind of place is this? Answer with exactly one word from: gym, bedroom, kitchen, beach, office."

with open("images/test.jpg", "rb") as f:
    image_data = base64.standard_b64encode(f.read()).decode("utf-8")

response = client.messages.create(
    model = model_name,
    max_tokens = 20,
    messages = [{
        "role": "user",
        "content": [
            {"type": "image",
             "source": {"type":"base64", "media_type":"image/jpeg", "data": image_data}},
             {"type": "text",
              "text": prompt}
        ],
    }],

)

print(response.content[0].text)
print(response.usage.input_tokens, "input_tokens", response.usage.output_tokens, "output tokens")