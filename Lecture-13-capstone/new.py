import base64
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

with open("system_prompt.txt", "r", encoding="utf-8") as file:
    system_prompt = file.read()

with open("page_1.jpg", "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode("utf-8")

data_url = f"data:image/jpeg;base64,{base64_image}"

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Analyze the attached image."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": data_url,
                        "detail": "auto"
                    }
                }
            ]
        }
    ]
)

print(response.choices[0].message.content)
