import tkinter as tk
from tkinter import font
import config
from pyowm import OWM
import requests


owm = OWM(config.API_KEY)
mgr = owm.weather_manager()

WIDTH = 500
HEIGHT = 600

def format_response(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temperature = round((weather['main']['temp']-32)/1.8, 2)
        final_str = f'City: {name}\nConditions: {description}\nTemperature: {temperature} C'
    except:
        final_str = '''Oops!!! There was a problem\nretreiving that information.'''

    return final_str

def get_weather(city):
    weather_key = config.API_KEY
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params)
    weather = response.json()
    print('The weather is: ', weather.__dir__)
    format_response(weather)

    label['text'] = format_response(weather)

# Search for current weather in London (Great Britain) and get details
# observation = mgr.weather_at_place('London,GB')
# w = observation.weather

# print(w.detailed_status)         # 'clouds'
# print(w.wind())                  # {'speed': 4.6, 'deg': 330}
# print(w.humidity)                # 87
# print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# print(w.rain)                    # {}
# print(w.heat_index)              # None
# print(w.clouds)                  # 75



HEIGHT = 350
WIDTH = 450

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Calibri', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="black", 
                   font=('Courier', 9), 
                   command=lambda: get_weather(entry_field.get())
                   )
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()
