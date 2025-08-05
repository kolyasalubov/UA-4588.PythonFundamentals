class Employee:
    """This class represents employee object"""
    __all_employees = []

    def __init__(self, name, lastname, salary):
        self.__name = name
        self.__lastname = lastname
        self.__salary = salary
        Employee.__all_employees.append(self)

    def __del__(self):
        Employee.__all_employees.remove(self)

    @property
    def name(self):
        """Get first name"""
        return self.__name

    @property
    def lastname(self):
        """Get last name"""
        return self.__lastname

    @property
    def salary(self):
        """Get salary"""
        return self.__salary

    @classmethod
    def amount_of_employees(cls):
        """Total amount of employees"""
        return f"The amount of employees in the company: {len(cls.__all_employees)}"

    @classmethod
    def about_all_employees(cls):
        if not cls.__all_employees:
            return "No employee's present."

        info = ["Details:", f"{'Full name':<18} {'Salary':<18}", "-" * 25]
        for emp in cls.__all_employees:
            info.append(f"{emp.name + ' ' + emp.lastname:<18} {str(emp.salary) + '$':<18}")
        return "\n".join(info)


if __name__ == "__main__":
    print(Employee.amount_of_employees())
    print(Employee.about_all_employees())
    print("-" * 25)

    em1 = Employee("Valerie", "Black", 3200)
    em2 = Employee("Hayong", "Jun", 4000)

    print(Employee.amount_of_employees())
    print(Employee.about_all_employees())
    print(f"__base__: {Employee.__base__}")
    print(f"__dict__: {Employee.__dict__}")
    print(f"__name__: {Employee.__name__}")
    print(f"__module__: {Employee.__module__}")
    print(f"__doc__: {Employee.__doc__}")