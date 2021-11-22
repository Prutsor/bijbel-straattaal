import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from gtts import gTTS
from time import sleep
from pygame import mixer

from .verse import Verse

class TextToSpeech():
    def __init__(self):
        self.__package = os.path.dirname(os.path.realpath(__file__))
        self.__temp = os.path.join(self.__package, 'temp')
        self.__file = os.path.join(self.__temp, 'tts.mp3')

    def say(self, verse:Verse, language:str, slow:bool):
        tts = gTTS(text=verse.text, lang=language, slow=slow)
        tts.save(self.__file)

        mixer.init()
        mixer.music.load(self.__file)
        mixer.music.play()

        while mixer.music.get_busy():
            sleep(0.1)

        mixer.quit()

        os.remove(self.__file)