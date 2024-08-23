from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import os
import speech_recognition as sr
import pyscreenshot as ps
import webbrowser
from dotenv import load_dotenv
import google.generativeai as genai
from gtts import gTTS
import pygame
import tempfile

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Inicializa o reconhecedor de voz
r = sr.Recognizer()

# Palavra de ativação do assistente
ACTIVATION_WORD = "ei helena"

# Lista de ferramentas disponíveis
AVAILABLE_TOOLS = ["captura de tela", "pesquisa na internet", "pergunta para o Google Generative AI"]

# Autentica na API do Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")

# Função para capturar a entrada de áudio do usuário
def capture_audio():
    with sr.Microphone() as source:
        print("Diga algo...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language="pt-BR").lower()
        print(f"Você disse: {text}")
        return text
    except sr.UnknownValueError:
        print("Desculpe, não entendi o que você disse.")
        return None
    except sr.RequestError as e:
        print("Não foi possível processar a sua fala; {0}".format(e))
        return None

# Função para capturar e salvar a tela
def capture_screenshot():
    screenshot = ps.grab()
    screenshot_path = "screenshot.png"
    screenshot.save(screenshot_path)
    return screenshot_path

# Função para pesquisar na internet
def search_on_internet(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return f"Abrindo a pesquisa no Google."

# Função para sintetizar e reproduzir fala com gtts e pygame
def speak(text):
    tts = gTTS(text=text, lang='pt')
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts.save(fp.name + ".mp3")
        pygame.mixer.init()
        pygame.mixer.music.load(fp.name + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

# Função principal do assistente
def assistant():
    while True:
        # Captura a entrada de áudio do usuário
        user_input = capture_audio()
        if user_input and ACTIVATION_WORD in user_input:
            # Remove a palavra de ativação do input do usuário
            user_request = user_input.replace(ACTIVATION_WORD, "").strip()

            # Identifica a ferramenta a ser usada
            if "tela" in user_request:
                # Captura a tela
                screenshot_path = capture_screenshot()
                # Envia a imagem para o Google Generative AI
                screenshot_in_genai = genai.upload_file(screenshot_path)
                prompt_parts = [screenshot_in_genai, "Observe a minha captura de tela e responda:" + user_input]
                response = model.generate_content(prompt_parts, request_options={"timeout": 2000})
                print("Helena: " + response.text)
                speak(response.text)

            elif "pesquisa" in user_request:
                # Realiza a pesquisa na internet
                search_results = search_on_internet(user_request)
                # Lê os resultados da pesquisa
                speak(search_results)
            else:
                # Envia a pergunta para o Google Generative AI e lê a resposta
                
                chat_session = model.start_chat(
                    history=[
                    ]
                )

                response = chat_session.send_message(user_request).text
                speak(response)

# Inicia o assistente
assistant()