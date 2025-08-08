class Employee:
    ''' employee with name and salary'''
    employee_count = 0
    employees = []
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
        Employee.employees.append(self)
        
    @classmethod
    def counter(cls):
        return f'Total number of employees: {cls.employee_count}'
    
    def info(self):
        return f'Name: {self.name}\nSalary: {self.salary}'  

#e1 = Employee("vi", 2000)
#e2 = Employee("dante", 3000)

#e1.display_info()
#e2.display_info()
#Employee.print_total()

#print("Base class:", Employee.__base__)
#print("Bases:", Employee.__bases__)
#print("Namespace (keys):", list(Employee.__dict__.keys())[:10])
#print("Class name:", Employee.__name__)
#print("Module:", Employee.__module__)
#print("Doc:", Employee.__doc__)      