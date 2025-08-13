import math



class Poligon:
    '''
    Main class for figurs
    '''

    def __init__(self, number_of_sides:int):
        '''
        Initial method
        '''
        self.number_of_sides = number_of_sides
        self.sides = []


    @staticmethod
    def check_input(string:str) -> float:
        '''
        Method which check user input
        '''
        try:
            string_to_float = float(string)
        except ValueError:
            raise ValueError('You must enter number')
        
        return string_to_float


    def input_sides(self):
        '''
        Method which reacive sides of figure
        '''
        for i in range(self.number_of_sides):
            self.sides.append(self.check_input((input(f'Enter side {i + 1}: '))))


    def check_sides(self):
        '''
        Method which compare count input sides with needed
        '''
        try:
            len(self.sides) == self.number_of_sides
        except ValueError:
            ValueError('You must enter all sides')


    def show_sides(self):
        '''
        Method which show all sides
        '''
        print(f'Sides: {self.sides}')


    @classmethod
    def find_square(self):
        '''
        Method which must realice into subclases
        '''
        raise NotImplementedError('You must use this method into subclases')



class Rectangle(Poligon):
    '''
    Class for Rectangles
    '''

    def __init__(self):
        '''
        Initialize number of sides in rectangle
        '''

        print('Created Rectangle')
        super().__init__(4)


    def possible_to_constract(self):
        '''
        Method which checking if possible to constract Rectangle
        '''
        if self.sides[0]!= self.sides[2] and self.sides[1] != self.sides[3]:
            raise TypeError('It is impossible to construct a rectangle with such sides')


    def find_square(self):
        '''
        Method which find square of Rectangle
        '''
        # Check if input all sides
        self.check_sides()

        # Check posible to constraction
        self.possible_to_constract()

        print(f'Square of Rectangle: {self.sides[0] * self.sides[1]}')
    

    def find_perimeter(self):
        '''
        Method which find perimeter of Rectancle
        '''
        # Check if input all sides
        self.check_sides()

        # Check posible to constraction
        self.possible_to_constract()

        print(f'Perimeter of Rectangle: {math.prod(self.sides)}')



class Triangle(Poligon):
    '''
    Class for Triangels
    '''
    def __init__(self):
        '''
        Initialize number of sides in triangle
        '''
        print('Created Triangle')
        super().__init__(3)


    @staticmethod
    def possible_to_constract(formula:int):
        '''
        Method which checking if possible to constract Triangle
        '''
        if formula < 0:
            raise TypeError('It is impossible to construct a triangle with such sides')


    def find_square(self):
        '''
        Method which find square of Triangle
        '''
        # Check if input all sides
        self.check_sides()

        a, b, c = self.sides
        sum_sides = (a + b + c) / 2
        formula = sum_sides * (sum_sides - a) * (sum_sides - b) * (sum_sides - c)
        
        # Check posible to constraction
        self.possible_to_constract(formula)
        
        area = round(math.sqrt(formula), 2)
        
        print(f'Square of Triangle: {area}')



class Circle:
    '''
    Class for Circles
    '''
    def __init__(self):
        '''
        Initialize radius
        '''
        print('Created Circle')
        self.radius = 0


    @staticmethod
    def check_radius(radius:str) -> int:
        '''
        Method which checking correct input
        '''
        try:
            radius = int(radius)
        except ValueError:
            raise ValueError('Enter integer, please')
        
        return radius


    def input_radius(self):
        '''
        Metgod which reacive radius from user
        '''
        self.radius = self.check_radius(input('Enter radius: '))


    def find_area(self):
        '''
        Methon which calculate area of Circle
        '''
        print(f'Area of Circle: {round(math.pi * math.pow(self.radius, 2), 2)}')


if __name__ == '__main__':
    print()

    # rectangle = Rectangle()
    # rectangle.input_sides()
    # rectangle.show_sides()

    # rectangle.find_square()
    # rectangle.find_perimeter()
    
    # triangle = Triangle()
    # triangle.input_sides()
    # triangle.show_sides()

    # triangle.find_square()

    # circle = Circle()
    # circle.input_radius()
    # circle.find_area()
