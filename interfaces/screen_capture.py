# interfaces/screen_capture.py
from abc import ABC, abstractmethod

class ScreenCapture(ABC):
    @abstractmethod
    def capture(self) -> str:
        pass