from pyowm.owm import OWM
owm = OWM('be540faabb4844772dddeed95cc2e18f')

country = input('what country (two letter code)?')
city = input('what city?')
reg = owm.city_id_registry()
city = reg.ids_for(city.title(), country.upper())
city_id = city[0][0]
print(city_id)

mgr = owm.weather_manager()
observation = mgr.weather_at_id(city_id)
w = observation.weather

temp = w.temperature('celsius')['temp']
wind_speed = w.wind()['speed']
sunrise = w.sunrise_time(timeformat='iso')
sunset = w.sunset_time(timeformat='iso')

print('Temperature : {} degree celcius'.format(temp))
print('Wind speed: {} m/s'.format(wind_speed))
print('Sunrise : {}'.format(sunrise))
print('Sunset : {}'.format(sunset))
