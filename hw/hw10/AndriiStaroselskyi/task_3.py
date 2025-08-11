# Task3. Create an employee class. Each employee has characteristics such as name
# and salary. The class should have a counter that calculates the total number of
# employees, as well as a method that prints the total number of employees and a
# method that displays information about each employee in particular, namely the
# name and salary.
# In addition to creating a class, display information about the base classes from which 
# the employee class is inherited (__base__), the class namespace (__dict__), the 
# class name (__name__), the module name in which the class is defined 
# (__module__), the documentation bar ( __doc__)

class Employee:
    """
    The Employee class represents information about employees (name and salary)
    Contains the total number of employees
    """
    number_of_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.number_of_employees += 1
    
    def __del__(self):
        print(f"{self.name} has been fired :c")
        Employee.number_of_employees -= 1
    
    @classmethod
    def get_number_of_employees(cls):
        return cls.number_of_employees

    def get_employee_info(self):
        return f"Name: {self.name}\nSalary: {self.salary}"
    

empl1 = Employee("Bob", 2500)
empl2 = Employee("Beem", 4200) 

print(f"Number of employees: {Employee.get_number_of_employees()}")

print(empl1.get_employee_info())
print(empl2.get_employee_info())

del empl2

print(f"Number of employees: {Employee.get_number_of_employees()}")

print("\n" + "*" *10)
print("The Employee class is inherited from:", Employee.__base__)
print("The Employee class namespace contains:", Employee.__dict__)
print("The class name is", Employee.__name__)
print("The module name is", Employee.__module__)
print("The documentation bar of the Employee class is:", Employee.__doc__)
