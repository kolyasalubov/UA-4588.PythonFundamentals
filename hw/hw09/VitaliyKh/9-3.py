import tkinter as tk
from tkinter import font
from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()


HEIGHT = 350
WIDTH = 450

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

def get_weather():
    observation = mgr.weather_at_place(entry_field.get())
    w = observation.weather
    rain_info = f"Rain: {w.rain}" if w.rain else ""
    text_output.set(
        f"{w.detailed_status}\n"
        f"Temprature: {round(w.temperature('celsius')['temp'])}°C\n"
        f"Wind: {w.wind()['speed']}m/s\n"
        f"Humidity: {w.humidity}%\n"  
        f"{rain_info}"
        )

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


text_output = tk.StringVar()
text_output.set("")
label = tk.Label(lower_frame, font=('Courier', 14), textvariable=text_output)
label.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()