# implementations/gtts_text_to_speech.py
from gtts import gTTS
import pygame
import tempfile
from pydub import AudioSegment
from interfaces.text_to_speech import TextToSpeech

class GTTSTextToSpeech(TextToSpeech):
    def speak(self, text: str, speed: float = 1.0) -> None:
        tts: gTTS = gTTS(text=text, lang='pt', slow=False)
        
        with tempfile.NamedTemporaryFile(delete=True, suffix=".mp3") as fp:
            tts.save(fp.name)
            
            sound: AudioSegment = AudioSegment.from_mp3(fp.name)
            
            if speed != 1.0:
                sound = sound.speedup(playback_speed=speed)
            
            sound.export(fp.name, format="mp3")
            
            pygame.mixer.init()
            pygame.mixer.music.load(fp.name)
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                continue