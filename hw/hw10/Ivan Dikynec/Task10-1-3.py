class Employee:
    count = 0
    
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary
        Employee.count += 1

    def display_count(self):
        print(f"Загальна кількість працівників: {Employee.count}")

    def display_employee(self):
        print(f"Ім'я: {self.name}, Зарплата: {self.salary}")



emp1 = Employee("Аліса", 5000)
emp2 = Employee("Володимир", 7600)


emp1.display_employee()
emp2.display_employee()


emp1.display_count()

print("\nІнформація про клас:")
print(f"Базові класи: {Employee.__base__}")
print(f"Простір імен класу (__dict__): {Employee.__dict__}")
print(f"Назва класу: {Employee.__name__}")
print(f"Назва модуля: {Employee.__module__}")
print(f"Документація (__doc__): {Employee.__doc__}")



###################################################################
# class Employee:

#     count = 0

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.count += 1


#     def display_count(self):
#         print(f"Загальна кількість працівників: {Employee.count}")

#     def display_employee(self):
#         print(f"Ім'я: {self.name}, Зарплата: {self.salary}")


# employees = []

# n = int(input("Скільки працівників додати? "))

# for i in range(n):
#     print(f"\nВведіть дані для працівника №{i+1}:")
#     name = input("Ім'я: ")
#     salary = float(input("Зарплата: "))
#     employees.append(Employee(name, salary))


# print("\nШтформація про працівників: ")
# for emp in employees:
#     emp.display_employee()


# employees[0].display_count()


# print("\nІнформація про класи:")
# print(f"Базові класи: {Employee.__base__}")
# print(f"Простір імен класу (__dict__): {Employee.__dict__}")
# print(f"Назва класа: {Employee.__name__}")
# print(f"Назва модуля: {Employee.__module__}")
# print(f"Документація (__doc__): {Employee.__doc__}")