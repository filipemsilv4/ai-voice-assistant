# implementations/google_speech_recognizer.py
import speech_recognition as sr
from interfaces.speech_recognizer import SpeechRecognizer
from typing import Optional

class GoogleSpeechRecognizer(SpeechRecognizer):
    def __init__(self):
        self.recognizer: sr.Recognizer = sr.Recognizer()

    def recognize_speech(self) -> Optional[str]:
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Diga algo...")
            audio: sr.AudioData = self.recognizer.listen(source)
        try:
            return self.recognizer.recognize_google(audio, language="pt-BR").lower()
        except sr.UnknownValueError:
            print("Desculpe, não entendi o que você disse.")
            return None
        except sr.RequestError as e:
            print(f"Não foi possível processar a sua fala; {e}")
            return None

