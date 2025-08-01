import math


class Polygon:
    def __init__(self, *args):
        self.sides_of_shape = list(args)

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
    pass

p = Polygon(5, 5, 5, 5, 5)
# p.calculate_triangle()
# print(p.calculate_rectangle())
print(p.calculate_pentagon())

# The area of a square is
# Area≈1.7204774×s2
# lack of source data