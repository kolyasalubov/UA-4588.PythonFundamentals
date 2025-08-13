class Employee:
    '''
    Class Employee
    '''
    # special value of count employees
    _count_instance = 0


    def __init__(self, name:str, age:int, position:str, salary:int):
        '''
        Initial instance method

        Arguments:
        name: str
        age: int
        position: str
        salary: int
        '''
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

        # increase count employees
        Employee._count_instance += 1


    @classmethod
    def count_employees(cls):
        '''
        Class method which print count of all employees in company
        '''
        print(f'Into this company {cls._count_instance} employees')


    def info_employee(self):
        '''
        Instance method which show information about current employee
        '''
        print(f'{self.name} is working at {self.position}position. He get\'s {self.salary} dollars a year.')


    @classmethod
    def info_class(cls):
        '''
        Class method which print information about Class
        '''
        print()
        print(f'Employee Base class: {cls.__base__}')
        print(f'Employee Namespace: {cls.__dict__}')
        print(f'Employee Name class: {cls.__name__}')
        print(f'Docomentation with {cls.__module__} module:\n {cls.__doc__}')


    @staticmethod
    def name_company():
        print('SoftServe')



if __name__ == '__main__':

    # list of data about persons
    persons = [('Mark', 32, 'CEO', 320.500),
               ('Jeff', 25, 'Developer', 250.300),
               ('Adam', 38, 'Manager', 180.800)]

    for person in persons:
        employee = Employee(name=person[0],
                            age=person[1],
                            position= person[2],
                            salary=person[3])
        # information about employee
        employee.info_employee()

    # number of Employees in company
    Employee.count_employees()

    # information about class
    Employee.info_class()

    # name company
    Employee.name_company()
