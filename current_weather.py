import requests
from pprint import pprint
from datetime import datetime


KEY= '137d62f3c460fac41edca5930e84af7c' #generated from https://openweathermap.org/ website

params = {
    'appid': KEY,
    'units': 'metric',
    'lang': 'ru'

}

while True:
    text = input('Enter a city to show the weather: ')
    if text == 'stop':
        break
    params['q'] = text
    try:
        data = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params).json()
        temp = data ['main']['temp']
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        timezone =data['timezone']
        wind = data['wind']['deg']
        sunrise =datetime.utcfromtimestamp(int(data['sys']['sunrise'])+timezone ).strftime('%Y/%m/%D %H:%M: %S')
        sunset = datetime.utcfromtimestamp(int(data['sys']['sunrise'])+timezone).strftime('%Y/%m/%D %H:%M: %S')

        print (f'''In , {text} , now {description}
Temperature of air: {temp} (°C)
wind speed: {wind_speed} m/c
Sunrise: {sunrise}
Sunset: {sunset}
Seconds: {timezone}
Wind degree: {wind} 
''')
    except:
        print('City not found')

