class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def get_species(cls):
        return f"Type: {cls.species}"

    @staticmethod
    def arbitrary_message():
        return "Static methods can be called without an object!"
    
    
name = input("Enter your name: ")

person1 = Human(name) 
person1.welcome()

print(Human.get_species())
print(Human.arbitrary_message())

print("-" * 40)