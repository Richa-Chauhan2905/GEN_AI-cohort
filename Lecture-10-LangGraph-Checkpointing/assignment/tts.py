from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Read transcribed text from output.txt
text_file_path = Path(__file__).parent / "output.txt"
input_text = text_file_path.read_text(encoding="utf-8")

# Output speech file
output_speech_path = Path(__file__).parent / "output_speech.mp3"

# Convert text to speech
response = client.audio.speech.create(
    model="tts-1",
    voice="nova",  # or shimmer, fable, etc.
    input=input_text,
    response_format="mp3"
)

# Save MP3
output_speech_path.write_bytes(response.content)
print(f"Speech saved to: {output_speech_path}")
