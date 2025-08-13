from pyowm import OWM
from pyowm.commons.exceptions import NotFoundError, APIRequestError

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

_owm = OWM(API_KEY)
_mgr = _owm.weather_manager()

def get_weather(place: str) -> dict:
    observation = _mgr.weather_at_place(place)
    w = observation.weather
    t = w.temperature("celsius")
    wind = w.wind()
    return {
        "place": place,
        "status": w.detailed_status,
        "temp": t.get("temp"),
        "temp_min": t.get("temp_min"),
        "temp_max": t.get("temp_max"),
        "humidity": w.humidity,
        "wind_speed": wind.get("speed"),
        "wind_deg": wind.get("deg"),
        "clouds": w.clouds,
    }

if __name__ == "__main__":
    print(get_weather("London,GB"))



