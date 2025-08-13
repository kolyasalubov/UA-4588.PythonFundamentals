import tkinter as tk
from tkinter import messagebox
from pyowm.commons.exceptions import NotFoundError, APIRequestError
from OWM import get_weather

HEIGHT, WIDTH = 350, 450

def format_weather(data: dict) -> str:
    return (
        f"Place: {data['place']}\n"
        f"Status: {data['status']}\n"
        f"Temp: {data['temp']} °C (min {data['temp_min']} / max {data['temp_max']})\n"
        f"Humidity: {data['humidity']}%\n"
        f"Wind: {data['wind_speed']} m/s, {data['wind_deg']}°\n"
        f"Clouds: {data['clouds']}%"
    )

def on_get_weather():
    place = entry.get().strip()
    if not place:
        messagebox.showwarning("Validation", "Enter city like 'London,GB'.")
        return
    try:
        data = get_weather(place)
        output.config(text=format_weather(data))
    except NotFoundError:
        messagebox.showerror("Error", f"City not found: {place}")
    except APIRequestError as e:
        messagebox.showerror("Error", f"API request failed:\n{e}")
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error:\n{e}")

root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=("Courier", 12))
entry.place(relx=0, rely=0, relwidth=0.65, relheight=1)
entry.insert(0, "London,GB")

btn = tk.Button(frame, text="Get Weather", bg="gray", fg="white",
                font=("Courier", 8), command=on_get_weather)
btn.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower = tk.Frame(root, bg="gold", bd=10)
lower.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

output = tk.Label(lower, font=("Courier", 12), justify="left", anchor="nw")
output.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()

