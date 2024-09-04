# interfaces/text_to_speech.py
from abc import ABC, abstractmethod

class TextToSpeech(ABC):
    @abstractmethod
    def speak(self, text: str, speed: float) -> None:
        pass