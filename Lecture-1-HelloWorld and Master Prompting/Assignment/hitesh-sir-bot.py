from dotenv import load_dotenv
from openai import OpenAI
import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

with open("system_prompt.txt", "r", encoding="utf-8") as file:
    system_prompt = file.read()

messages = [{"role": "system", "content": system_prompt}]

while True:
    query = input("> ")

    if query.lower() in {"exit", "bye", "quit"}:
        print("Exiting chat. Goodbye!")
        break

    messages.append({"role": "user", "content": query})

    response = client.chat.completions.create(
        model="gemini-2.0-flash",
        n=1,
        messages=messages,
    )

    parsed_output = json.loads(response.choices[0].message.content)
    messages.append({"role": "assistant", "content": json.dumps(parsed_output)})

    print(response.choices[0].message.content)
