class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(sides=4)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Example usage
rect = Rectangle(5, 3)
print("Rectangle area:", rect.area())