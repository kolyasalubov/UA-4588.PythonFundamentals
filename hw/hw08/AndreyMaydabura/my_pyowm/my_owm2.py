from pyowm import OWM
from config import KEY

# from pyowm.utils import config
# from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------


owm = OWM(KEY)
mgr = owm.weather_manager()

input_city = input("What city you are interested:")

# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(input_city)
w = observation.weather


status_clouds = w.detailed_status         # 'clouds'
speed_wind = w.wind()['speed']                  # {'speed': 4.6, 'deg': 330}
humidity = w.humidity                # 87
# {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
temperature_max = w.temperature('celsius')['temp_max']
temperature = w.temperature('celsius')['temp']
temperature_min = w.temperature('celsius')['temp_min']

print(f"In {input_city} the wind speed is {speed_wind} km/hours")
print(f"In {input_city} the humidity of the air is {humidity}")
print(f"In {input_city} the temperature of the air is {temperature}")
print(f"In {input_city} the maximal temperature of the air is {temperature_max}")
print(f"In {input_city} the minimal temperature of the air is {temperature_min}")
