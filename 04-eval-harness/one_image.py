import base64
import anthropic

client = anthropic.Anthropic()

with open("images/test.jpg", "rb") as f:
    image_data = base64.standard_b64encode(f.read()).decode("utf-8")

response = client.messages.create(
    model = "claude-haiku-5-5",
    max_tokens = 20,
    messages = [{
        "role": "user",
        "content": [
            {"type": "image",
             "source": {"type":"base64", "media_type":"image/jpeg", "data": image_data}},
             {"type": "text",
              "text":"What kind of place is this? Answer with exactly one word from: gym, bedroom, kitchen, beach, office."}
        ],
    }],

)

print(response.content[0].text)
print(response.usage.input_tokens, "input_tokens", response.usage.output_tokens, "output tokens")