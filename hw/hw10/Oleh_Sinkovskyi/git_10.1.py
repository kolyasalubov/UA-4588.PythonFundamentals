# Task 1

# class Polygon:
#     def __init__(self):
#         pass

# class Rectangle(Polygon):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
    
#     def area(self):
#         return self.width * self.height


# r = Rectangle(3, 5)
# print(r.area())




# Task 2

# class Human:
#     species = "Homo sapiens"

#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         return f"Hi {self.name}!"
    
#     @classmethod
#     def s(cls, name):
#         return f"{name} is {cls.species}."
    
#     @staticmethod   
#     def staticmethod():
#         return "message"
    



# Task 3

# class Employee:

#     _counter = 0

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = float(salary)
#         Employee.counter +=1

#     @classmethod
#     def amount(cls):
#         return cls.counter

#     def info(self):
#         return f"Name - {self.name} ({self.salary:.2f}$)"
    
# print(Employee.__base__)
# print(Employee.__dict__)
# print(Employee.__name__)
# print(Employee.__module__)
# print(Employee.__doc__)


