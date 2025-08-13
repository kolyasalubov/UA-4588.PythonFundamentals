class Employee:
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

# 🔹 Створення об'єктів
emp1 = Employee("Dmytro", 36000)
emp2 = Employee("Olena", 4500)

emp1.display_info()
emp2.display_info()
Employee.total_employees()

# 🔍 Інформація про клас
print("\nClass info:")
print("Base classes:", Employee.__bases__)
print("Namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Doc string:", Employee.__doc__)
