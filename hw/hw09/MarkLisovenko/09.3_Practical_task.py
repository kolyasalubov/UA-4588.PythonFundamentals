import tkinter as tk
from pyowm import OWM
import config

API_KEY = config.KEY
owm = OWM(API_KEY)
mgr = owm.weather_manager()

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

def get_weather():
    city = entry_field.get()
    observation = mgr.weather_at_place(city)
    w = observation.weather

    info = f"Weather in {city}:\n" \
           f"Status: {w.detailed_status}\n" \
           f"Temperature: {w.temperature('celsius')['temp']}°C\n" \
           f"Feels like: {w.temperature('celsius')['feels_like']}°C\n" \
           f"Wind: {w.wind()['speed']} m/s, {w.wind()['deg']}°\n" \
           f"Humidity: {w.humidity}%\n" \
           f"Clouds: {w.clouds}%\n" \
           f"Rain: {w.rain if w.rain else 'No'}\n" \
           f"Heat index: {w.heat_index if w.heat_index else None}"
    label['text'] = info

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 12), justify='left')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()