from jarvis.voice import Microphone, SpeechRecognizer

microphone = Microphone()
recognizer = SpeechRecognizer()

audio = microphone.listen()

text = recognizer.recognize(audio)

print()
print(f"You said: {text}")