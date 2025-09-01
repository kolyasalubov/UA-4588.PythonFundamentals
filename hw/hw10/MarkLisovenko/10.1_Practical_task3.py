class Employee :
    """
    This class is destined to create different objects for each employee with necessary attributes and methods.
    """
    
    counter = 0

    def __init__(self, name : str, salary : float) :
        self.name = name
        self.salary = salary
        Employee.counter += 1

    @classmethod
    def number_of_employees(cls) :
        return cls.counter
    
    def dispEmployeeInfo(self) :
        print(f"Name: {self.name}, Salary: {self.salary}")


####################---MainProgram---####################


employee_1 = Employee("Mark", 1000)
employee_1.dispEmployeeInfo()
print(f"The total number of employees is {Employee.number_of_employees()}")

employee_2 = Employee("Bohdan", 3000)
employee_2.dispEmployeeInfo()
print(f"The total number of employees is {Employee.number_of_employees()}")

employee_3 = Employee("Artem", 2000)
employee_3.dispEmployeeInfo()
print(f"The total number of employees is {Employee.number_of_employees()}")


print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)