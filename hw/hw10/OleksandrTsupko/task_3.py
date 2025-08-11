class Employees:
    
    number_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.__class__.number_employees += 1

    def info_about_employee(self):
        print(f'Number of employee: {self.__class__.number_employees}\n' 
              f'Name: {self.name}\n'
              f'Salary: {self.salary}\n')
    
    @staticmethod
    def quantity_employee():
        print(f'Quantity of employee: {Employees.number_employees}')

    @staticmethod
    def info_about_class():
        print('__base__:', Employees.__base__)
        print('__dict__:', Employees.__dict__)
        print('__name__:', Employees.__name__)
        print('__module__:', Employees.__module__)
        print('__doc__:', Employees.__doc__)

e1 = Employees('Maksym', 5000)
e1.info_about_employee()
e1.quantity_employee()

e2 = Employees('Vadym', 4000)
e2.info_about_employee()
e2.quantity_employee()

e1.info_about_class()