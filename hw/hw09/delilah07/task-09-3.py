from pyowm import OWM
from pyowm.commons.exceptions import NotFoundError
import tkinter as tk
from tkinter import font

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()
def get_weather():
    city = entry_field.get()
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather

        status = w.detailed_status
        wind = w.wind()
        humidity = w.humidity
        temp = w.temperature('celsius')
        rain = w.rain
        clouds = w.clouds

        result = f"""Weather in {city}:
Status: {status}
Temperature: {temp['temp']}°C (min: {temp['temp_min']}°C, max: {temp['temp_max']}°C)
Humidity: {humidity}%
Wind: {wind.get('speed', 'N/A')} m/s, {wind.get('deg', 'N/A')}°
Rain: {rain if rain else 'No rain'}
Clouds: {clouds}%"""
    except NotFoundError:
        result = "City not found. Please enter a valid city name."
    except Exception as e:
        result = f"Error: {e}"

    label['text'] = result

HEIGHT = 350
WIDTH = 450

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
                   font=('Courier', 10),
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 10), justify='left', anchor='nw')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()