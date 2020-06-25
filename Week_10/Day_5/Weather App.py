import requests
from pprint import pprint

city = input('Enter your city: ')

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=be540faabb4844772dddeed95cc2e18f&units=metric'.format(
    city)

res = requests.get(url)
data = res.json()


name = data['name']
id = data['sys']['id']
temp = data['main']['temp']
wind_speed = data['wind']['speed']
sunrise = data['sys']['sunrise']
sunset = data['sys']['sunset']
description = data['weather'][0]['description']

print('City : {}'.format(name))
print('City ID: {}'.format(id))
print('Temperature : {} degree celcius'.format(temp))
print('Wind speed: {} m/s'.format(wind_speed))
print('Sunrise : {}'.format(sunrise))
print('Sunset : {}'.format(sunset))
print('Description : {}'.format(description))
# pprint(data)
