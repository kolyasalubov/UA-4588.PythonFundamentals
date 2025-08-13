class Polygon:
    def __init__(self, sides):
        self.sides = sides      

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__([width, height])
    
    def areaOfRectangle(self):
        a, b = self.sides
        return a * b
    

############ Test ############

# rect1 = Rectangle(2, 3)
# print(rect1.areaOfRectangle())

# rect2 = Rectangle(4, 5)
# print(rect2.areaOfRectangle())