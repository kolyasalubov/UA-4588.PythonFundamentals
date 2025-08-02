import math
import tkinter as tk

class Polygon:
    def __init__(self, *args):
        self.sides_of_shape = list(args)

    def calculate_circle(self):
        return math.pi * math.pow(self.sides_of_shape[0], 2)

    def calculate_triangle(self):
        side1 = self.sides_of_shape[0]
        side2 = self.sides_of_shape[1]
        side3 = self.sides_of_shape[2]

        # Check for valid triangle inequality: The sum of the lengths of any two
        # sides of a triangle must be greater than the length of the third side.
        if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
            print("Error: The given side lengths do not form a valid triangle.")
            # return 0.0
        else:
            # Step 1: Calculate the semi-perimeter (s)
            s = (side1 + side2 + side3) / 2
            # Step 2: Apply Heron's formula
            area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
            # return area
            print(area)

    def calculate_rectangle(self):
        side1 = self.sides_of_shape[0]
        side2 = self.sides_of_shape[1]
        return side1 * side2
    
    def calculate_pentagon(self):
        if sum(self.sides_of_shape) <= 0:
            return 0.0
        else:
            area = ((1/4) * math.sqrt(5 * 
                    (5 + 2 * math.sqrt(5))) * 
                    (sum(self.sides_of_shape) ** 2))
            return area


class Rectangle(Polygon):
    side_a = new_entry1.get()


BG_COLOUR = "#cccccc"
FONT_COLOUR = "#515151"

root = tk.Tk()
root.title('Area Shape Calculator')
root.geometry('800x600')

right_frame = tk.Frame(root, bg=BG_COLOUR, bd=2)
right_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

radius_label = tk.Label(right_frame, text="Radius:", bg=BG_COLOUR, 
                        font=('Calibri', 20), fg=FONT_COLOUR)
side_a_label = tk.Label(right_frame, text="Side A:", bg=BG_COLOUR, 
                        font=('Calibri', 20), fg=FONT_COLOUR)
side_b_label = tk.Label(right_frame, text="Side B:", bg=BG_COLOUR, 
                        font=('Calibri', 20), fg=FONT_COLOUR)
side_c_label = tk.Label(right_frame, text="Side C:", bg=BG_COLOUR, 
                        font=('Calibri', 20), fg=FONT_COLOUR)
side_d_label = tk.Label(right_frame, text="Side D:", bg=BG_COLOUR, 
                        font=('Calibri', 20), fg=FONT_COLOUR)
side_e_label = tk.Label(right_frame, text="Side E:", bg=BG_COLOUR, 
                        font=('Calibri', 20), fg=FONT_COLOUR)

new_entry1 = tk.Entry(right_frame, font=('Calibri', 20), fg=FONT_COLOUR)
new_entry2 = tk.Entry(right_frame, font=('Calibri', 20), fg=FONT_COLOUR)
new_entry3 = tk.Entry(right_frame, font=('Calibri', 20), fg=FONT_COLOUR)
new_entry4 = tk.Entry(right_frame, font=('Calibri', 20), fg=FONT_COLOUR)
new_entry5 = tk.Entry(right_frame, font=('Calibri', 20), fg=FONT_COLOUR)

def calculate_area_and_display(shape, entry1, entry2=None):
    """
    Calculates the area based on the selected shape and input values,
    then updates the output label and prints to the console.
    """
    try:
        if shape == "circle":
            radius = float(entry1.get())
            area = math.pi * math.pow(radius, 2)
            result_text = f"The area of the circle is:\n{area:.2f}"
            print(f"Calculating area for Circle with radius: {radius}")
        elif shape == "rectangle":
            length = float(entry1.get())
            width = float(entry2.get())
            area = length * width
            result_text = f"The area of the rectangle is:\n{area:.2f}"
            print(f"Calculating area for Rectangle with length: {length}, width: {width}")
        else:
            result_text = "Calculation not implemented yet."
    except ValueError:
        result_text = "Please enter valid numbers."

    label_text_output.config(text=result_text)

def show_circle():
    label_text_output.config(text="Enter the radius of \nthe circle")
    radius_label.place(relx=0.2, rely=0.3, relwidth=0.15, relheight=0.08)
    new_entry1.place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.08)
    button_count_area.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.08)
    button_count_area.config(command=lambda: calculate_area_and_display(
                                                "circle", new_entry1, new_entry2))

def show_triangle():
    label_text_output.config(text="Enter the lengths of \nthe sides of triangle")

    side_a_label.place(relx=0.2, rely=0.23, relwidth=0.15, relheight=0.08)
    side_b_label.place(relx=0.2, rely=0.38, relwidth=0.15, relheight=0.08)
    side_c_label.place(relx=0.2, rely=0.53, relwidth=0.15, relheight=0.08)

    new_entry1.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.08)
    new_entry2.place(relx=0.2, rely=0.45, relwidth=0.6, relheight=0.08)
    new_entry3.place(relx=0.2, rely=0.6, relwidth=0.6, relheight=0.08)

    button_count_area.config(command=lambda: calculate_area_and_display(
                                            "triangle", new_entry1, new_entry2, new_entry3))
    button_count_area.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.08)


def show_rectangle():
    label_text_output.config(text="Enter the lengths of \nthe sides of rectangle")

    side_a_label.place(relx=0.2, rely=0.3, relwidth=0.15, relheight=0.08)
    side_b_label.place(relx=0.2, rely=0.5, relwidth=0.15, relheight=0.08)

    new_entry1.place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.08)
    new_entry2.place(relx=0.2, rely=0.6, relwidth=0.6, relheight=0.08)

    button_count_area.config(command=lambda: calculate_area_and_display(
                                            "rectangle", new_entry1, new_entry2))
    button_count_area.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.08)
    

label_text_output = tk.Label(right_frame, 
                 bg=BG_COLOUR, 
                 fg=FONT_COLOUR, 
                 font=('Calibri', 32), 
                 text='Choose the shape')
label_text_output.place(relx=0, rely=0.05, relwidth=1, relheight=0.2)

button_count_area = tk.Button(right_frame, 
                              text='Count the area', 
                              font=('Calibri', 20), 
                              fg=FONT_COLOUR)

left_frame = tk.Frame(root, bg=BG_COLOUR)
left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)

buttons = [
    tk.Button(left_frame, 
              text="Circle", 
              font=('Calibri', 28), 
              fg=FONT_COLOUR,
              command=show_circle),
    tk.Button(left_frame, 
              text="Triangle", 
              font=('Calibri', 28), 
              fg=FONT_COLOUR,
              command=show_triangle),
    tk.Button(left_frame, 
              text="Rectangle", 
              font=('Calibri', 28), 
              fg=FONT_COLOUR,
              command=show_rectangle),
    tk.Button(left_frame, 
              text="Pentagon", 
              font=('Calibri', 28), 
              fg=FONT_COLOUR,
              command=lambda: label_text_output.config(text="You selected: Pentagon"))
]

for btn in buttons:
    btn.pack(fill='both', expand=True, padx=10, pady=10)

root.resizable(False, False)

root.mainloop()