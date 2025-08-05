import tkinter as tk
from pyowm import OWM

# API settings
API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

# Window size
HEIGHT = 350
WIDTH = 450

# Weather fetching function with city parameter


def get_weather(city):
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather

        temp = w.temperature('celsius')['temp']
        wind = w.wind()['speed']
        humidity = w.humidity
        clouds = w.clouds
        status = w.detailed_status

        weather_info = f"Weather in {city}:\n" \
            f"Status: {status}\n" \
            f"Temperature: {temp}°C\n" \
            f"Wind: {wind} m/s\n" \
            f"Humidity: {humidity}%\n" \
            f"Clouds: {clouds}%"
    except:
        weather_info = "Error: Could not retrieve data.\nPlease check the city name."

    label['text'] = weather_info


# GUI setup
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
                   command=lambda: get_weather(entry_field.get()))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,
                  relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 12),
                 justify='left', anchor='nw', bg='white')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
