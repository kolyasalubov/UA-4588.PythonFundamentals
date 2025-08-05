class Employee:
    """
    The Employee class represents an employee with a name and salary.
    It also keeps track of the total number of employees.
    """

    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    @classmethod
    def print_employee_count(cls):
        print(f"Total number of employees: {cls.employee_count}")

    def display_info(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")


e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)
e3 = Employee("Charlie", 70000)

e1.display_info()
e2.display_info()
e3.display_info()

Employee.print_employee_count()


print("\n--- Class Attributes ---")
print("Base classes (__base__):", Employee.__base__)
print("Class namespace (__dict__):", Employee.__dict__)
print("Class name (__name__):", Employee.__name__)
print("Module name (__module__):", Employee.__module__)
print("Class documentation (__doc__):", Employee.__doc__)
