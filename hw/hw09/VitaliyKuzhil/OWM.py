from pyowm import OWM
from config import API_KEY


def format_response(weather:object) -> str:
    '''
    Function which forming response for user
    '''
    try:
        detail = weather.detailed_status
        w_speed = weather.wind()['speed']
        w_deg = weather.wind()['deg']
        w_humidity = weather.humidity
        w_temperature = weather.temperature('celsius')['temp']
        w_temperature_min = weather.temperature('celsius')['temp_min']
        w_temperature_max = weather.temperature('celsius')['temp_max']
        w_rain = weather.rain
        w_heat_index = weather.heat_index
        w_clouds = weather.clouds

        final_str = f'''Status: {detail}\nWind: speed: {w_speed}, deg: {w_deg}\nHumidity: {w_humidity}\
            \nTemperature: {w_temperature},\nmin.temp.: {w_temperature_min}, max.temp:{w_temperature_max},\
            \nRain: {w_rain}\nHeat index: {w_heat_index}\nClouds: {w_clouds}'''
    except:
        final_str = 'Oops! There was a problem\n retrieving that information'

    return final_str


def get_weather(choice_city:str) -> object|None:
    '''
    Function which get request from OWM service
    '''
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    
    try:
        observation = mgr.weather_at_place(choice_city)
        return observation.weather
    except:
        return None


def update_label_text(current_weather:str, label:object):
    '''
    Function which update info label for user
    '''
    label.config(text=format_response(get_weather(current_weather)))
