import tkinter as tk
from pyowm import OWM
from pyowm.utils.config import get_default_config

# --- API CONFIG ---
API_KEY = 'ef2206ff5da67de63306d0b143e20872'

# Можна змінити мову на українську
config_dict = get_default_config()
config_dict['language'] = 'en'  # або 'ua' для української, якщо підтримується

owm = OWM(API_KEY, config_dict)
mgr = owm.weather_manager()

# --- GUI ---
HEIGHT = 350
WIDTH = 450

def get_weather():
    city = entry_field.get()
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        temp = w.temperature('celsius')['temp']
        status = w.detailed_status
        humidity = w.humidity
        wind = w.wind()['speed']
        
        result = (f"Погода в {city}:\n"
                  f"Стан: {status}\n"
                  f"Температура: {temp}°C\n"
                  f"Вологість: {humidity}%\n"
                  f"Вітер: {wind} м/с")
    except Exception as e:
        result = f"Помилка: не вдалося отримати дані для '{city}'"

    label['text'] = result


# --- TKINTER GUI ---
root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 12), anchor='nw', justify='left')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
