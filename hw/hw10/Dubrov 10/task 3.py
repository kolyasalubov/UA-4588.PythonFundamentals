class Employee:
    """Class for describing an employee"""
    count = 0  

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    @classmethod
    def total_employees(cls):
        print(f"Total employees: {cls.count}")

    def display_employee(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

employees = [] 

n = int(input("How many employees do you want to add?? "))

for i in range(n):
    name = input(f"Enter the employee's name {i+1}: ")
    salary = float(input(f"Enter the employee's salary {i+1}: "))
    emp = Employee(name, salary)
    employees.append(emp)

print("\n--- List of employees ---")
for emp in employees:
    emp.display_employee()

Employee.total_employees()

print("\n--- Information about class Employee ---")
print("Base classes:", Employee.__base__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)