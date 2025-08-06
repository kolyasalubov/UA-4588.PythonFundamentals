from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'

owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather(city='London,GB'):
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        status = w.detailed_status
        temp = w.temperature('celsius')['temp']
        humidity = w.humidity
        result = f"{city}\n{status.capitalize()}\nTemperature: {temp}°C\nHumidity: {humidity}%"
        return result
    except Exception as e:
        return f"Error: {e}"





