# Task1. 
# Create a polygon class and a rectangle class that inherits from the polygon class 
# and finds the square of rectangle


class Polygon:
    def __init__(self, number_of_sides: int):
        self.number_of_sides = number_of_sides
        self.sides = [0 for i in range(number_of_sides)]
    
    def set_sides(self):
        self.sides = [float(input(f"Please enter side {i + 1}: ")) for i in range(self.number_of_sides)]

    def about_polygon(self):
        print(f"This polygon has {self.number_of_sides} sides")
        for i in range(self.number_of_sides):
            print(f"Side {i + 1}: {self.sides[i]}")


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(4)
        self.length = 0
        self.width = 0

    
    def set_sides(self):
        self.length = float(input("Please enter length: "))
        self.width = float(input("Please enter width: "))
        self.sides = [self.length, self.width, self.length, self.width]
    
    def get_area(self):
        return self.length * self.width
