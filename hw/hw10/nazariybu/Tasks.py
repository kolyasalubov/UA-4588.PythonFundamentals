# Task1.
# Create a polygon class and a rectangle class that inherits
#  from the polygon class and finds the square of rectangle.

# class Polygon():
#     def __init__(self, num_of_sides):
#         self.num_of_sides = num_of_sides
#         self.sides = [0 for i in range(num_of_sides)]
 
#     def inputSides(self):
#         self.sides = [float(input(f'Enter side {str(i+1)}: ')) for i in range(self.num_of_sides)]

# class Rectangle(Polygon):
#     def __init__(self):
#         super().__init__(2)

#     def findArea(self):
#         a, b = self.sides
#         area = a * b
#         print(f'The area of the rectangle is {area} ')

# r = Rectangle()
# r.inputSides()
# r.findArea()

# --------------------------------------------------------

# Task 2.
# Create a class Human, everyone has a name,
# create a method in the class
#  that displays a welcome message to each person.
# Create a class methodin the class 
#  that returns information that it is a species of "Homosapiens".
# And in the class create a static method that returns an arbitrary message.

# class Human:
#     def __init__(self, name):
#         self.name = name
    
#     def welcome(self):
#         return f'Welcome {self.name}'
    
#     @classmethod
#     def species(self):
#         return "Homosapiens"
    
#     @staticmethod
#     def info():
#         return "You know that you are a human. Do you know it or not?"
    

# h1 = Human('Peter')
# print(h1.welcome())
# print(Human.species())
# print(h1.info())

# ------------------------------------------------------------------------

# Task3.
# Create an employee class.
# Each employee has characteristics such as name and salary.
# The class should have a counter that calculates the total number of employees,
#  as well as a method that prints the total number of employees
#  and a method that displays information about each employee in particular,
#  namely the name and salary.

# In addition to creating a class,
#  display information about the base classes 
#  from which the employee class is inherited (__base__),
#  the class namespace (__dict__),
#  the class name (__name__),
#  the module name in which the class is defined (__module__),
#  the documentation bar ( __doc__)


# class Employee:
#     ''' Employee with name and salary."""'''

#     employee_count = 0

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.employee_count += 1
  
#     def info(self):
#         return f'Name: {self.name} \nSalary: {self.salary}'
    
#     @classmethod
#     def show_counter(cls):
#         return f"Total number of employees: {cls.employee_count}"
    

# e1 = Employee("Tom", 1000)
# e2 = Employee("Ana", 1500)

# print(e1.info())
# print(e2.info())
# print(Employee.show_counter())

# print("Base classes (__base__):", Employee.__base__)
# print("Class namespace (__dict__):", Employee.__dict__)
# print("Class name (__name__):", Employee.__name__)
# print("Module name (__module__):", Employee.__module__)
# print("Class documentation (__doc__):", Employee.__doc__)