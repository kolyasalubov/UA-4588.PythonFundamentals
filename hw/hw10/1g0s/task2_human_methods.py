"""
Task 2 — Human: instance, class, and static methods

Practice instance methods vs. class methods vs. static methods.
"""


class Human:
    """Human class demonstrating instance, class, and static methods."""
    
    species = "Homosapiens"
    
    def __init__(self, name: str) -> None:
        """Initialize human with a name.
        
        Args:
            name: Name of the human
        """
        self.name = name
    
    def welcome(self) -> str:
        """Instance method returning a welcome message.
        
        Returns:
            Welcome message with the person's name
        """
        return f"Welcome, {self.name}!"
    
    @classmethod
    def info(cls) -> str:
        """Class method returning species information.
        
        Returns:
            Information about the class species
        """
        return f"This class models species: {cls.species}"
    
    @staticmethod
    def random_message() -> str:
        """Static method returning a fixed message.
        
        Returns:
            Fixed arbitrary message
        """
        return "Be kind."


if __name__ == "__main__":
    # Create two Human objects with different names
    human1 = Human("Alice")
    human2 = Human("Bob")
    
    # Call and print welcome() for each human
    print("Instance method calls:")
    print(f"  {human1.welcome()}")
    print(f"  {human2.welcome()}")
    print()
    
    # Call and print class method
    print("Class method call:")
    print(f"  {Human.info()}")
    print()
    
    # Call and print static method
    print("Static method call:")
    print(f"  {Human.random_message()}")