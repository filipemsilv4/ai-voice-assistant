# implementations/google_generative_ai.py
import os
from typing import List
import google.generativeai as genai
from interfaces.ai_model import AIModel
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

class GoogleGenerativeAI(AIModel):
    def __init__(self):
        self.model: genai.GenerativeModel = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")
        self.chat_session: genai.ChatSession = self.model.start_chat(history=[])

    def generate_response(self, prompt: str) -> str:
        return self.chat_session.send_message(prompt).text

    def generate_image_response(self, image_path: str, prompt: str) -> str:
        image_in_genai: genai.UploadedFile = genai.upload_file(image_path)
        prompt_parts: List[str] = [image_in_genai, f"Observe a minha captura de tela e responda de forma sucinta em pt-br ao seguinte prompt: {prompt}"]
        response: genai.GeneratedContent = self.model.generate_content(prompt_parts, request_options={"timeout": 2000})
        return response.text