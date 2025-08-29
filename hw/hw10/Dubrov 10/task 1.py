class Polygon:
    def __init__(self, sides):
        self.sides = sides 

    def perimeter(self):
        return sum(self.sides)


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width, length, width])
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


length = float(input("Enter the length of your rectangle: "))
width = float(input("Enter the width of your rectangle: "))

rect = Rectangle(length, width)

print("Perimeter:", rect.perimeter())  
print("Area:", rect.area())        
