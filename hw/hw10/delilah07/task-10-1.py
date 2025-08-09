# Task 1

class Polygon:
    def __init__(self, num_of_sides):
        self.num_of_sides = num_of_sides

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__([ width, height, width, height])
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(5, 3)
print(f"Area of rectangle: {rect.area()}")
print(rect.num_of_sides)

# Task 2
class Human:
    species = "Homosapiens" 

    def __init__(self, name):
        self.name = name
    
    def welcome_msg(self):
        return f"Welcome, {self.name}!"
    
    @classmethod
    def get_species(cls):
        return f"You are {cls.species}!"
    
    @staticmethod
    def arbitrary_message():
        return "Have a great!"
    
person1 = Human("Alice")
person2 = Human("Bob")

print(person1.welcome_msg())     
print(person2.welcome_msg())    

print(person1.get_species())           
print(person2.get_species()) 

print(person1.arbitrary_message())     
print(person2.arbitrary_message())     

# Task 3
class Employee:
    ''' class that return number of employees 
    and their name and salary'''
    
    num_of_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num_of_employees += 1

    @classmethod
    def num_of_employees_msg(cls):
        return f'Total Employees: {cls.num_of_employees}'
    
    def employee_info(self):
        return (f"Name: {self.name}, Salary: {self.salary}")
    
emp1 = Employee("Alice", 5000)
emp2 = Employee("Bob", 7000)

print(emp1.employee_info())
print(emp2.employee_info())

print(Employee.num_of_employees_msg())

print("Class Metadata:")
print("Base classes:", Employee.__base__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation string:", Employee.__doc__)