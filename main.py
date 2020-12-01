import sys
import time
import speech_recognition as sr
from text_to_speech import speak
from brain import brain

speak('Welcome, How can I help you?')


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        speech_text = r.recognize_google(audio).lower().replace("'", "")
        print("Levi thinks you said '" + speech_text + "'")
    except sr.UnknownValueError:
        print("Levi could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
    return speech_text

time.sleep(1)

while(1):
    text = get_audio()
    brain(text)
