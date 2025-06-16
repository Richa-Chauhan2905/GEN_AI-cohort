import speech_recognition as sr

filename = "audioFile.wav"
r = sr.Recognizer()

with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)

    print("Transcribed text:", text)

    # Save to file for use in TTS
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(text)
