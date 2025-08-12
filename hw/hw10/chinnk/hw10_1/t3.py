class Employee:
    _count = 0

    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = float(salary)
        Employee._count += 1

    @classmethod
    def total_employees(cls) -> int:
        return cls._count

    def info(self) -> str:
        return f"Employee(name={self.name}, salary={self.salary:.2f})"


# quick demo
e1 = Employee("Bob", 1200)
e2 = Employee("Eve", 1500)
print("Task3 → total:", Employee.total_employees())
print("Task3 →", e1.info())
print("Task3 →", e2.info())

print("Task3 → base classes:", Employee.__bases__)
print("Task3 → namespace keys (part):", list(Employee.__dict__.keys())[:8])
print("Task3 → class name:", Employee.__name__)
print("Task3 → defined in module:", Employee.__module__)
print("Task3 → docstring:", Employee.__doc__)
