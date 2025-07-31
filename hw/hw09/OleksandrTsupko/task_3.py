import tkinter as tk
import config
from pyowm import OWM
import requests


owm = OWM(config.API_KEY)
mgr = owm.weather_manager()

WIDTH = 500
HEIGHT = 600

def format_response(weather):
    try:
        observation = mgr.weather_at_place('London,GB')
        w = observation.weather
        name = weather['name']
        description = weather['weather'][0]['description']
        temperature = round((weather['main']['temp']-32)/1.8, 2)
        wind = weather['wind']['speed']
        detailed_info = w.detailed_status
        final_str = (f'City: {name}\n'
                     f'Conditions: {description}\n'
                     f'Temperature: {temperature} C \n'
                     f'Wind: {wind} m/s\n'
                     f'Detailed information: {detailed_info}')
    except:
        final_str = '''Oops!!! There was a problem\nretreiving that information.'''

    return final_str

def get_weather(city):
    weather_key = config.API_KEY
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params)
    weather = response.json()
    print('The weather is: ', weather)
    format_response(weather)

    label['text'] = format_response(weather)

HEIGHT = 500
WIDTH = 600

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, bg="#606060", fg='white', font=('Calibri', 15))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="black", 
                   font=('Calibri', 14), 
                   command=lambda: get_weather(entry_field.get())
                   )
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#0066CC', bd=2)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Calibri', 16))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
