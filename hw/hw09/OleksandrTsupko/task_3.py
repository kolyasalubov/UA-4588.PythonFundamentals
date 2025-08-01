import tkinter as tk
import config
from pyowm import OWM
import requests


WIDTH = 500
HEIGHT = 600

def format_response(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temperature = round((weather['main']['temp']-32)/1.8, 2)
        wind = weather['wind']['speed']
        final_str = (f'City: {name}\n'
                     f'Conditions: {description}\n'
                     f'Temperature: {temperature} C \n'
                     f'Wind: {wind} m/s\n')
    except:
        final_str = '''Oops!!! There was a problem\nretreiving that information.'''

    return final_str

def get_weather(city):
    weather_key = config.API_KEY
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params)
    weather = response.json()
    format_response(weather)

    label['text'] = format_response(weather)

HEIGHT = 500
WIDTH = 600

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

frame = tk.Frame(root, bg="#A8A8A8", bd=2)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, bg="#E1E1E1", fg="#343434", font=('Calibri', 18))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="#343434",
                   font=('Calibri', 16), 
                   command=lambda: get_weather(entry_field.get())
                   )
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="#A8A8A8", bd=2)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, fg='#343434', font=('Calibri', 18))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
