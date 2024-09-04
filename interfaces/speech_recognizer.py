# interfaces/speech_recognizer.py
from abc import ABC, abstractmethod
from typing import Optional

class SpeechRecognizer(ABC):
    @abstractmethod
    def recognize_speech(self) -> Optional[str]:
        pass