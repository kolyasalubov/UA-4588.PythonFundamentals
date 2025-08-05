import tkinter as tk
from tkinter import font
from OWM import getLocationData

HEIGHT = 350
WIDTH = 450

current_weather = ''

def get_weather(label, location):
    global current_weather
    w = getLocationData(location)
    
    current_weather = f'''
{w.detailed_status.capitalize()}
Wind: speed: {w.wind()['speed']}, deg: {w.wind()['deg']}\n
Humidity: {w.humidity}\n
Temperature: min.: {w.temperature('celsius')['temp_min']}, max.: {w.temperature('celsius')['temp_max']},\n
Rain: {w.rain}\n
Heat index: {w.heat_index}\n
Clouds: {w.clouds}
    '''
    label.config(text=current_weather)
    

def main():
    root = tk.Tk()
    root.title("Weather Application")

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    frame = tk.Frame(root, bg="deep sky blue", bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.2, anchor='n')

    button = tk.Button(frame, 
                    text="Get Weather", 
                    bg="gray", fg="black", 
                    font=('Courier', 8), 
                    command=lambda: get_weather(label, entry_field.get())
                   )
    button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

    entry_field = tk.Entry(frame, font=('Courier', 12))
    entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

    lower_frame = tk.Frame(root, bg='gold', bd=10)
    lower_frame.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.6, anchor='n')


    label = tk.Label(lower_frame, font=('Courier', 14), text=current_weather)

    label.place(relx=0, rely=0, relwidth=1, relheight=1)

    root.mainloop()

if __name__ == '__main__':
    main()
    






