class polygon:
    def __init__(self, num_of_sides):
        self.num_of_sides = num_of_sides
        
class rectangle(polygon): 
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        super().__init__(4)
    
    def area(self):
        return self.side1 * self.side2
    