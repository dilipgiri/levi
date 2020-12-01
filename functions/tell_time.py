from datetime import datetime
from text_to_speech import speak
def what_is_time():
    speak("The time is " + datetime.strftime(datetime.now(), '%H:%M:%S'))
