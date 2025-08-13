"""
Task 3 — Employee class + class counter + class metadata

Models employees, tracks total count via a class-level counter, 
and inspects class metadata.
"""


class Employee:
    """
    Employee class that tracks the total number of employees created
    and provides employee information management.
    """
    
    count = 0  # Class attribute to track number of employees
    
    def __init__(self, name: str, salary: float) -> None:
        """Initialize employee with name and salary.
        
        Args:
            name: Employee name
            salary: Employee salary
            
        Raises:
            ValueError: If salary is negative
        """
        if salary < 0:
            raise ValueError("Salary must be non-negative")
            
        self.name = name
        self.salary = salary
        Employee.count += 1  # Increment class counter
    
    @classmethod
    def total(cls) -> int:
        """Return total number of employees created.
        
        Returns:
            Current count of employees
        """
        return cls.count
    
    def info(self) -> str:
        """Return employee information.
        
        Returns:
            Formatted string with employee name and salary
        """
        return f"Employee: {self.name}, Salary: {self.salary}"


if __name__ == "__main__":
    # Create three Employee instances
    emp1 = Employee("Alice Johnson", 75000.0)
    emp2 = Employee("Bob Smith", 82000.0)
    emp3 = Employee("Carol Davis", 68000.0)
    
    # Print total count and info for each employee
    print(f"Total employees: {Employee.total()}")
    print()
    
    print("Employee Information:")
    print(f"  {emp1.info()}")
    print(f"  {emp2.info()}")
    print(f"  {emp3.info()}")
    print()
    
    # Introspection output - show class metadata
    print("Class Introspection for Employee:")
    print(f"  Base classes: {Employee.__bases__}")
    print(f"  Namespace keys: {list(Employee.__dict__.keys())}")
    print(f"  Class name: {Employee.__name__}")
    print(f"  Module name: {Employee.__module__}")
    print(f"  Docstring: {Employee.__doc__}")
    print()
    
    # Demonstrate error handling
    try:
        invalid_emp = Employee("Invalid", -1000)
    except ValueError as e:
        print(f"Error creating invalid employee: {e}")