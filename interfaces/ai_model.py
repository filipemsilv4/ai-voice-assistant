# interfaces/ai_model.py
from abc import ABC, abstractmethod

class AIModel(ABC):
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        pass

    @abstractmethod
    def generate_image_response(self, image_path: str, prompt: str) -> str:
        pass