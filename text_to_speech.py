import os
import sys
import playsound
from gtts import gTTS


def speak(message):
    tts=gTTS(text=message, lang="en", slow=False)
    filename="voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
