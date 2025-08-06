# Створіть клас співробітників. Кожен працівник має такі характеристики, як ім'я та зарплата. 
# Клас повинен мати лічильник, який обчислює загальну кількість працівників, а також метод, 
# який друкує загальну кількість працівників, і метод, який відображає інформацію

# Про кожного працівника зокрема, а саме ім'я та зарплату. На додаток до створення класу, 
# відобразіть інформацію про базові класи, від яких успадковується клас працівника (__base_), 
# простір імен класу (_dict__), ім'я класу (name_, ім'я модуля, в якому визначено клас (module_), документацію (_doc_)

class Employee:
    """
    Represents an employee.
    
    Class attributes:
        __counter (int): Number of employees created.
        __employees (list): List of all employees (as strings).
    """
    __counter = 0
    __employees = []

    def __init__(self, name, salary):
        """
        Initializes a new employee.

        Args:
            name (str): Employee name.
            salary (float | int): Employee salary.
        """
        self.__name = name
        self.__salary = salary
        Employee.__counter += 1
        Employee.__employees.append(f'Name: {name}, salary: {salary}')

    @classmethod
    def getAmountEmployees(cls):
        """
        Initializes a new employee.

        Args:
            name (str): Employee name.
            salary (float | int): Employee salary.
        """
        return cls.__counter
    
    @classmethod
    def getAllEmployees(cls):
        """
        Returns all employees as a string.

        Returns:
            str: List of employees, each on a new line.
        """
        return "\n".join(employee for employee in Employee.__employees)
    
print(f'__base__: {Employee.__base__}')
print(f'__dict__: {Employee.__dict__}')
print(f'__name__: {Employee.__name__}')
print(f'__module__: {Employee.__module__}')
print(f'__doc__: {Employee.__doc__}')

############ Test ############
# empl1 = Employee('Andrii', 86000)
# empl2 = Employee('Svitlana', 82000)

# print(Employee.getAmountEmployees())
# print(Employee.getAllEmployees())
