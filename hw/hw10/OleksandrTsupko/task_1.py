import math
import tkinter as tk
from pyowm import OWM
import requests
from tkinter import ttk
from tkinter import font


# class Polygon:
#     def __init__(self, *args):
#         self.sides_of_shape = list(args)

#     def calculate_circle(self):
#         return math.pi * math.pow(self.sides_of_shape[0], 2)

#     def calculate_triangle(self):
#         side1 = self.sides_of_shape[0]
#         side2 = self.sides_of_shape[1]
#         side3 = self.sides_of_shape[2]

#         # Check for valid triangle inequality: The sum of the lengths of any two
#         # sides of a triangle must be greater than the length of the third side.
#         if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
#             print("Error: The given side lengths do not form a valid triangle.")
#             # return 0.0
#         else:
#             # Step 1: Calculate the semi-perimeter (s)
#             s = (side1 + side2 + side3) / 2
#             # Step 2: Apply Heron's formula
#             area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
#             # return area
#             print(area)

#     def calculate_rectangle(self):
#         side1 = self.sides_of_shape[0]
#         side2 = self.sides_of_shape[1]
#         return side1 * side2
    
#     def calculate_pentagon(self):
#         if sum(self.sides_of_shape) <= 0:
#             return 0.0
#         else:
#             area = ((1/4) * math.sqrt(5 * 
#                     (5 + 2 * math.sqrt(5))) * 
#                     (sum(self.sides_of_shape) ** 2))
#             return area


# class Rectangle(Polygon):
#     pass

# p = Polygon(5)
# p.calculate_triangle()
# print(p.calculate_rectangle())
# print(p.calculate_pentagon())
# print(p.calculate_circle())

# def display_text(entry_field, label):
#     """
#     Handles the button click event.
#     Retrieves text from the entry field and updates the label.
#     """
#     user_input = entry_field.get()
    
#     if not user_input:
#         label.config(text="Please enter some text")
#         return
    
#     # Print the text to the console
#     print(f"User entered: {user_input}")

#     # Update the label with the text from the entry field
#     label.config(text=f"You entered:\n{user_input}")

# WIDTH = 600
# HEIGHT = 500

# root = tk.Tk()

# canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
# root.title("Area calculator")
# canvas.pack()

# lower_frame = tk.Frame(root, bg="#690A0A", bd=2)
# lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# label = tk.Label(lower_frame, bg="#690A0A", fg="#717171", font=('Calibri', 18))
# label.place(relx=0, rely=0, relwidth=1, relheight=1)

# frame = tk.Frame(root, bg="#A8A8A8", bd=2)
# frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# entry_field_text = tk.Entry(frame, bg="#E1E1E1", fg="#343434", font=('Calibri', 18))
# entry_field_text.place(relx=0, rely=0, relwidth=0.65, relheight=1)

# entry_field_shape = tk.Entry(frame, bg="#E1E1E1", fg="#343434", font=('Calibri', 18))
# entry_field_shape.place(relx=0.5, rely=0.5, relwidth=0.65, relheight=1)

# button_get_text = tk.Button(frame, 
#                    text="Get Text", 
#                    bg="gray", fg="#343434",
#                    font=('Calibri', 16), 
#                    command=lambda: display_text(entry_field_text, label)
#                    )
# button_get_text.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

# button_get_shape = tk.Button(frame, 
#                    text="Get Shape", 
#                    bg="gray", fg="#343434",
#                    font=('Calibri', 16), 
#                    command=lambda: display_text(entry_field_shape, label)
#                    )
# button_get_shape.place(relx=0.7, rely=0.5, relwidth=0.3, relheight=1)


BG_COLOUR = "#cccccc"
FONT_COLOUR = "#515151"

root = tk.Tk()
root.title('Area Shape Calculator')
root.geometry('800x600')

right_frame = tk.Frame(root, bg=BG_COLOUR, bd=2)
right_frame.place(relx=0.5, rely=0, relwidth=1, relheight=1)

label = tk.Label(right_frame, bg=BG_COLOUR, fg=FONT_COLOUR, font=('Calibri', 18))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

left_frame = tk.Frame(root, bg=BG_COLOUR)
left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)

buttons = [
    tk.Button(left_frame, text="Circle", font=('Calibri', 28), fg=FONT_COLOUR),
    tk.Button(left_frame, text="Triangle", font=('Calibri', 28), fg=FONT_COLOUR),
    tk.Button(left_frame, text="Rectangle", font=('Calibri', 28), fg=FONT_COLOUR),
    tk.Button(left_frame, text="Pentagon", font=('Calibri', 28), fg=FONT_COLOUR)
]

for btn in buttons:
    btn.pack(fill='both', expand=True, padx=10, pady=10)

root.mainloop()