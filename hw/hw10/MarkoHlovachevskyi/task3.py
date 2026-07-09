class Employee:
    """Class representing an employee with name and salary."""
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    @classmethod
    def total_employees(cls):
        print(f"Total employees: {cls.count}")

e1 = Employee("Alice", 5000)
e2 = Employee("Bob", 6000)

e1.display_info()
e2.display_info()
Employee.total_employees()

print("Base class:", Employee.__base__)
print("Namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Docstring:", Employee.__doc__)