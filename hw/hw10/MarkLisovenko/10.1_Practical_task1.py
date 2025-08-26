class Polygon :
    def __init__(self, number_of_sides) :
        self.number_of_sides = number_of_sides
        self.values_of_sides = [0 for i in range(number_of_sides)]
    
    def inputSides(self) :
        for i in range(len(self.values_of_sides)) :
            self.values_of_sides[i] = float(input(f"Enter the side number {str(i+1)}: "))

    def displaySides(self) :
        for i in range(self.number_of_sides) :
            print(f"Side {str(i+1)} is {self.values_of_sides[i]}")
        
    
class Rectangle(Polygon) :
    def __init__(self) :
        super().__init__(4)
    
    def findArea(self) :
        side_1, side_2 = set(self.values_of_sides)
        area_of_the_rectangle = side_1 * side_2
        print(f"Area of the rectangle is equal to {area_of_the_rectangle}")


####################---MainProgram---####################


rectangle = Rectangle()

rectangle.inputSides()

rectangle.displaySides()

rectangle.findArea()