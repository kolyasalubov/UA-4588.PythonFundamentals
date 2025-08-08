import tkinter as tk
from tkinter import font
import OWM


HEIGHT = 350
WIDTH = 650


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


custom_font = font.Font(family="Verdana", size=12, weight="normal")


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.85, relheight=0.1, anchor='n')


entry_field = tk.Entry(frame, font=custom_font)
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)


button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="light green", fg="black",
                   font=custom_font, 
                   command=lambda: OWM.update_label_text(entry_field.get(), label))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.85, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=custom_font, justify='left')
label.place(relx=0, rely=0, relwidth=1, relheight=1)


root.mainloop()

