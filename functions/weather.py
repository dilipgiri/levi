import pyowm
from text_to_speech import speak

def weather():
    owm = pyowm.OWM('c52482b8b220cf92f2efffb459b2e6b3')
    observation = owm.weather_at_place('Pokhara, NP')
    weather = observation.get_weather()
    temperature = weather.get_temperature('celsius')['temp']
    wind=weather.get_wind('miles_hour')["speed"]
    status=weather.get_detailed_status()
    speak("The temperature in Pokhara is:" +str(temperature)+ "degree celsius." + ",Wind is travelling with speed:"+str(wind)+"miles per hour."+",The weather status today is"+status)

