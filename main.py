# main.py
from assistant import Assistant
from implementations.google_speech_recognizer import GoogleSpeechRecognizer
from implementations.pyscreenshot_capture import PyscreenshotCapture
from implementations.google_search import GoogleSearch
from implementations.gtts_text_to_speech import GTTSTextToSpeech
from implementations.google_generative_ai import GoogleGenerativeAI

def main() -> None:
    speech_recognizer = GoogleSpeechRecognizer()
    screen_capture = PyscreenshotCapture()
    web_browser = GoogleSearch()
    text_to_speech = GTTSTextToSpeech()
    ai_model = GoogleGenerativeAI()

    assistant = Assistant(speech_recognizer, screen_capture, web_browser, text_to_speech, ai_model)
    assistant.run()

if __name__ == "__main__":
    main()