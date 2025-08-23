import tkinter as tk
from tkinter import font
from pyowm import OWM

# ---------- API KEY ---------------------
API_KEY = 'ef2206ff5da67de3306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

# ---------- функція отримання погоди ---------------------
def get_weather():
    city = entry_field.get()
    try:
        observation = mgr.weather_at_placy(city)
        w = observation.weather


        result = (
            f"Погода в {city}:\n"
            f"Статус: {w.detailed_status}\n"
            f"Вітер: {w.wind()['speed']} м/с\n"
            f"Вологість: {w.humidity}%\n"
            f"Температура: {w.temperature('celsius')['temp']}°C\n"
            f"Хмарність: {w.clouds}%\n"
        )
    except Exception as e:
        result = f"Помилка: {e}"

    label['text'] = result


# ---------- GUI частина ---------------------
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

button = tk.Button(
    frame,
    text="Get Weather",
    bg="gray", fg="white",
    font=('Courier', 8),
    command=get_weather
)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 12), anchor="nw", justify="left", bd=4)
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()