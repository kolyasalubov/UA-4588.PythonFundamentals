from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather(city):
    """Повертає інформацію про погоду у вигляді тексту"""
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather

        result = (
            f"Status: {w.detailed_status}\n"
            f"Wind: {w.wind()}\n"
            f"Humidity: {w.humidity}%\n"
            f"Temperature: {w.temperature('celsius')['temp']} °C\n"
            f"Clouds: {w.clouds}%\n"
        )
    except Exception as e:
        result = f"Error: {e}"

    return result




