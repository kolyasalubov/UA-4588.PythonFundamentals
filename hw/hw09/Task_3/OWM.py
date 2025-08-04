from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()


def get_weather(city):
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather

        clouds = w.detailed_status       # 'clouds'
        wind_data = w.wind()             # {'speed': 4.6, 'deg': 330}
        speed = wind_data['speed']
        deg = wind_data['deg']
        humid = w.humidity               # 87
        temp = w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        rain = w.rain                    # {}
        if w.heat_index is not None:
            heat = w.heat_index
        else:
            heat = "Немає спеки"         # None (немає спеки, якщо низька температура повітря)
        c = w.clouds                     # 75

        res = (
            f"Погода: {clouds}\n"
            f"Швидкість вітру: {speed}\n"
            f"Напрямок вітру: {deg}°\n"
            f"Вологість: {humid}%\n"
            f"Температура: {temp['temp']} °C\n"
            f"Дощ: {rain}\n"
            f"Індекс спеки: {heat}\n"
            f"Хмарність: {c}%\n"
        )
        return res
    except Exception as e:
        return f"Місто не знайдено\n або сталася помилка."
