# assistant.py
from interfaces.speech_recognizer import SpeechRecognizer
from interfaces.screen_capture import ScreenCapture
from interfaces.web_browser import WebBrowser
from interfaces.text_to_speech import TextToSpeech
from interfaces.ai_model import AIModel
from typing import Optional

class Assistant:
    def __init__(self, speech_recognizer: SpeechRecognizer, screen_capture: ScreenCapture, 
                 web_browser: WebBrowser, text_to_speech: TextToSpeech, ai_model: AIModel):
        self.speech_recognizer = speech_recognizer
        self.screen_capture = screen_capture
        self.web_browser = web_browser
        self.text_to_speech = text_to_speech
        self.ai_model = ai_model
        self.activation_word: str = "ei helena"

    def run(self) -> None:
        while True:
            user_input: Optional[str] = self.speech_recognizer.recognize_speech()
            if user_input and self.activation_word in user_input:
                activation_index: int = user_input.index(self.activation_word)
                user_request: str = user_input[activation_index + len(self.activation_word):].strip()
                print(f"Usuário: {user_request}")

                if "tela" in user_request:
                    screenshot_path: str = self.screen_capture.capture()
                    response: str = self.ai_model.generate_image_response(screenshot_path, user_request)
                    print(f"Helena: {response}")
                    self.text_to_speech.speak(text=response, speed=1.5)
                elif "pesquisa" in user_request:
                    search_results: str = self.web_browser.search(user_request)
                    self.text_to_speech.speak(search_results, speed=1.0)
                else:
                    response: str = self.ai_model.generate_response(user_request)
                    self.text_to_speech.speak(response, speed=1.0)