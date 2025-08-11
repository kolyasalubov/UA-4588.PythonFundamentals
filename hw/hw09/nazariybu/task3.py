import tkinter as tk
from pyowm import OWM
from config import API_KEY
import requests

# ---------- API ---------------
owm = OWM(API_KEY)
mgr = owm.weather_manager()


# ------- Windows Size ---------
HEIGHT = 350
WIDTH = 450

# ---------- Functions -----------
def format_response(weather):
    try :
        name = weather['name']
        description = weather['weather'][0][ 'description' ]
        temperature = round((weather['main']['temp']-32)/1.8, 2)
        final_str = f'City: {name} \nConditions: {description} \nTemperature {temperature} C'
    except :
        final_str = '''Oops! !! There was a problem\n retrieving that information.'''

    return final_str

def get_weather(city):
    weather_key = API_KEY
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}    
    response = requests.get(url, params)
    weather = response.json()
    format_response(weather)
    
    label['text'] = format_response(weather)


# ---------- GUI ----------------
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
