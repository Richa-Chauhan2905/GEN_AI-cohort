from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

result = client.chat.completion.create(
    model="gpt-4",
    messages = [
        {"role": "system", "content": "You are an AI assistant whoe name is ChaiCode"},
        {"role": "user", "content": "what is 2 + 2 * 0"}
    ]
)

print(result.choices[0].message.content)