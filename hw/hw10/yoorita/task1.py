import math

class Polygon:
    def __init__(self, sides: list):
        self.__sides = sides
        self.__s0 = sides[0]

    @property
    def sides(self):
        return self.__sides

    def area(self):
        return round((self.__perimeter() * self.__apothem()) / 2, 2)

    def __perimeter(self):
        return len(self.__sides) * self.__s0 # counting the polygon has the same side length

    def __apothem(self):
        return round(self.__s0 / (2 * math.tan(180 / len(self.__sides))), 2)


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__([width, height])

    def area(self):
        a, b = self.sides
        return a * b


if __name__ == "__main__":
    rect = Rectangle(2, 3)
    print(rect.area())