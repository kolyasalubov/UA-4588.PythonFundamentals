import tkinter as tk
import math

BG_COLOUR = "#cccccc"
FONT_COLOUR = "#515151"

# --- Shape Classes for calculations ---

class Polygon:
    """Base class for geometric shapes."""
    def __init__(self, *args):
        self.sides = list(args)

    def calculate_triangle(self):
        """
        Calculates the area of a triangle using Heron's formula.
        Handles invalid triangle inequality.
        """
        if len(self.sides) < 3: return 0.0
        side1, side2, side3 = self.sides[0], self.sides[1], self.sides[2]

        if (side1 + side2 <= side3) or (side1 + side3 <= side2) or (side2 + side3 <= side1):
            return "Error: Invalid Triangle"
        else:
            s = (side1 + side2 + side3) / 2
            area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
            return area

    def calculate_rectangle(self):
        """Calculates the area of a rectangle."""
        if len(self.sides) < 2: return 0.0
        return self.sides[0] * self.sides[1]
    
    def calculate_pentagon(self):
        """Calculates the area of a regular pentagon."""
        if not self.sides: return 0.0
        side = self.sides[0]
        area = (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * (side ** 2)
        return area

class Triangle(Polygon):

    def perimeter_triangle(self):
        return sum(self.sides)

class Rectangle(Polygon):

    def perimeter_rectangle(self):
        return sum(self.sides) * 2
    
class Pentagon(Polygon):

    def perimeter_pentagon(self):
        return sum(self.sides)
    
class Circle:

    def __init__(self, radius):
        self.radius = radius

    def calculate_circle(self):
        """Calculates the area of a circle."""
        return math.pi * math.pow(self.radius, 2)

# --- Tkinter functions for UI logic ---

def clear_widgets():
    """
    Hides all dynamically placed widgets to prepare for a new shape.
    """
    for widget in [radius_label, side_a_label, side_b_label, side_c_label, side_d_label, side_e_label,
                   new_entry1, new_entry2, new_entry3, new_entry4, new_entry5, button_count_area]:
        widget.place_forget()

def calculate_area_and_display(shape, *entries):
    """
    Calculates the area based on the selected shape and input values,
    then updates the output label and prints to the console.
    """
    try:
        side_values = [float(e.get()) for e in entries if e.winfo_ismapped()]
        result_text = "Calculation not implemented yet"
        circle = Circle(side_values[0])
        rectangle = Rectangle(*side_values)
        triangle = Triangle(*side_values)
        pentagon = Pentagon(*side_values)

        if shape == "circle":
            area = circle.calculate_circle()
            result_text = f"The area of the circle is:\n{area:.2f}"
            print(f"Calculating area for Circle with radius: {side_values[0]}")
        elif shape == "rectangle":
            area = rectangle.calculate_rectangle()
            result_text = f"The area of the rectangle is:\n{area:.2f}"
            print(f"Calculating area for Rectangle with sides: {side_values[0]}, {side_values[1]}")
        elif shape == "triangle":
            area = triangle.calculate_triangle()
            result_text = f"The area of the triangle is:\n{area:.2f}"
            print(f"Calculating area for Triangle with sides: {side_values}")
        elif shape == "pentagon":
            area = pentagon.calculate_pentagon()
            result_text = f"The area of the pentagon is:\n{area:.2f}"
            print(f"Calculating area for Pentagon with side: {side_values[0]}")
        
    except (ValueError, IndexError):
        result_text = "Please enter valid numbers"

    label_text_output.config(text=result_text)

def show_circle():
    clear_widgets()
    label_text_output.config(text="Enter the radius of \nthe circle")
    radius_label.place(relx=0.2, rely=0.3, relwidth=0.15, relheight=0.08)
    new_entry1.place(relx=0.4, rely=0.3, relwidth=0.5, relheight=0.08)
    button_count_area.config(command=lambda: 
                    calculate_area_and_display("circle", new_entry1))
    button_count_area.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.08)

def show_triangle():
    clear_widgets()
    label_text_output.config(text="Enter the lengths of \nthe sides of triangle")

    side_a_label.place(relx=0.2, rely=0.25, relwidth=0.15, relheight=0.08)
    side_b_label.place(relx=0.2, rely=0.39, relwidth=0.15, relheight=0.08)
    side_c_label.place(relx=0.2, rely=0.53, relwidth=0.15, relheight=0.08)
    new_entry1.place(relx=0.4, rely=0.25, relwidth=0.5, relheight=0.08)
    new_entry2.place(relx=0.4, rely=0.39, relwidth=0.5, relheight=0.08)
    new_entry3.place(relx=0.4, rely=0.53, relwidth=0.5, relheight=0.08)

    button_count_area.config(command=lambda: 
                    calculate_area_and_display("triangle", new_entry1, 
                                               new_entry2, new_entry3))
    button_count_area.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.08)

def show_rectangle():
    clear_widgets()
    label_text_output.config(text="Enter the lengths of \nthe sides of rectangle")

    side_a_label.place(relx=0.2, rely=0.3, relwidth=0.15, relheight=0.08)
    side_b_label.place(relx=0.2, rely=0.5, relwidth=0.15, relheight=0.08)
    new_entry1.place(relx=0.4, rely=0.3, relwidth=0.5, relheight=0.08)
    new_entry2.place(relx=0.4, rely=0.5, relwidth=0.5, relheight=0.08)

    button_count_area.config(command=lambda: 
                    calculate_area_and_display("rectangle", new_entry1, new_entry2))
    button_count_area.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.08)

def show_pentagon():
    clear_widgets()
    label_text_output.config(text="Enter the side length of \nthe regular pentagon")

    side_a_label.place(relx=0.2, rely=0.25, relwidth=0.15, relheight=0.08)
    side_b_label.place(relx=0.2, rely=0.34, relwidth=0.15, relheight=0.08)
    side_c_label.place(relx=0.2, rely=0.43, relwidth=0.15, relheight=0.08)
    side_d_label.place(relx=0.2, rely=0.52, relwidth=0.15, relheight=0.08)
    side_e_label.place(relx=0.2, rely=0.61, relwidth=0.15, relheight=0.08)
    new_entry1.place(relx=0.4, rely=0.25, relwidth=0.5, relheight=0.08)
    new_entry2.place(relx=0.4, rely=0.34, relwidth=0.5, relheight=0.08)
    new_entry3.place(relx=0.4, rely=0.43, relwidth=0.5, relheight=0.08)
    new_entry4.place(relx=0.4, rely=0.52, relwidth=0.5, relheight=0.08)
    new_entry5.place(relx=0.4, rely=0.61, relwidth=0.5, relheight=0.08)

    button_count_area.config(command=lambda: 
                calculate_area_and_display("pentagon", new_entry1, 
                                           new_entry2, new_entry3, 
                                           new_entry4, new_entry5))
    button_count_area.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.08)


# --- Main Application Setup ---
root = tk.Tk()
root.title('Area Shape Calculator')
root.geometry('800x600')
root.resizable(False, False)

# Left frame for buttons
left_frame = tk.Frame(root, bg=BG_COLOUR)
left_frame.place(relx=0, rely=0, relwidth=0.5, relheight=1)

# Right frame for output and entry fields
right_frame = tk.Frame(root, bg=BG_COLOUR, bd=2)
right_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

# Labels and Entry fields for input
# Initially hidden and appears after shape is chosen
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

new_entry1 = tk.Entry(right_frame, bg='white', font=('Calibri', 20), 
                      fg=FONT_COLOUR)
new_entry2 = tk.Entry(right_frame, bg='white', font=('Calibri', 20), 
                      fg=FONT_COLOUR)
new_entry3 = tk.Entry(right_frame, bg='white', font=('Calibri', 20), 
                      fg=FONT_COLOUR)
new_entry4 = tk.Entry(right_frame, bg='white', font=('Calibri', 20), 
                      fg=FONT_COLOUR)
new_entry5 = tk.Entry(right_frame, bg='white', font=('Calibri', 20), 
                      fg=FONT_COLOUR)

# Label to display the selected shape and results
label_text_output = tk.Label(right_frame, 
                 bg=BG_COLOUR, 
                 fg=FONT_COLOUR, 
                 font=('Calibri', 32), 
                 text='Choose the shape',
                 justify='left')
label_text_output.place(relx=0, rely=0.05, relwidth=1, relheight=0.2)

button_count_area = tk.Button(right_frame, 
                              text='Count the area', 
                              font=('Calibri', 20), 
                              fg=FONT_COLOUR)

# --- Buttons for shape selection ---
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
              command=show_pentagon)
]

for btn in buttons:
    btn.pack(fill='both', expand=True, padx=10, pady=10)

root.mainloop()