import os
from dotenv import load_dotenv
import speech_recognition as sr
from langgraph.checkpoint.mongodb import MongoDBSaver
from graph import create_chat_graph
import asyncio
from openai.helpers import LocalAudioPlayer
from openai import AsyncOpenAI

load_dotenv()

openai = AsyncOpenAI()

MONGODB_URI = "mongodb://localhost:27017/"
print("Connected to mongodb")
config = {"configurable": {"thread_id": "10"}}

def main():
        with MongoDBSaver.from_conn_string(MONGODB_URI) as checkpointer:
            graph = create_chat_graph(checkpointer=checkpointer)

            r = sr.Recognizer()

            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                r.pause_threshold = 2

                while True:
                    print("Say something: ")
                    audio = r.listen(source)

                    print("Processing audio...")
                    stt = r.recognize_google(audio)

                    print("You said: ", stt)
                    for event in graph.stream({ "messages": [{"role": "user", "content": stt}] }, config, stream_mode="values"):
                        if "messages" in event:
                            event["messages"][-1].pretty_print()

async def speak(text: str):
    async with openai.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        input=text,
        instructions="Speak in a very formal tone.",
        response_format="pcm",
    ) as response:
        await LocalAudioPlayer().play(response)
     

if __name__ == "__main__":
     asyncio.run(speak(text="This is a sample voice, Hello there"))