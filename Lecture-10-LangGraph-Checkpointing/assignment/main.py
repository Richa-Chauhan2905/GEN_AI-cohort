import os
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
import speech_recognition as sr

# Load API Key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Step 1: Transcribe using your original speech_recognition code
filename = "audioFile.wav"
recognizer = sr.Recognizer()

with sr.AudioFile(filename) as source:
    audio_data = recognizer.record(source)
    try:
        question = recognizer.recognize_google(audio_data)
        print(f"🎧 Transcribed Text: {question}")
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio.")
        exit()
    except sr.RequestError as e:
        print(f"Could not request results from Google STT service; {e}")
        exit()

# Step 2: Send the transcribed text to GPT
chat_completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You're a helpful assistant."},
        {"role": "user", "content": question}
    ]
)
response_text = chat_completion.choices[0].message.content
print(f"💬 GPT Response: {response_text}")

# Step 3: Convert GPT response to speech
speech_file_path = Path(__file__).parent / "output_response.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="nova",  # other options: alloy, echo, fable, shimmer, onyx
    input=response_text
)
speech_file_path.write_bytes(response.content)
print(f"🔊 Speech saved to {speech_file_path}")
