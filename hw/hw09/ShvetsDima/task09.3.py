import tkinter as tk
from tkinter import font
from pyowm import OWM
from pyowm.utils.config import get_default_config

# Weather API setup
API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

# GUI constants
HEIGHT = 350
WIDTH = 450

def format_response(weather):
    try:
        description = weather.detailed_status
        temperature = weather.temperature('celsius')["temp"]
        wind = weather.wind()["speed"]
        humidity = weather.humidity
        return f"Condition: {description}\nTemperature: {temperature}°C\nWind: {wind} m/s\nHumidity: {humidity}%"
    except:
        return "There was a problem retrieving that information"

def get_weather(city):
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        label['text'] = format_response(w)
    except:
        label['text'] = "City not found"

# GUI setup
root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=('Courier', 12),
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='light yellow', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 12), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()