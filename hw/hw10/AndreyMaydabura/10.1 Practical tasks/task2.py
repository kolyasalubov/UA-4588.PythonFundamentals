class Human:

    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def species_info(cls):
        return f"This species is {cls.__name__} and belongs to Homosapiens."

    @staticmethod
    def random_message():
        return "An arbitrary message"


person1 = Human("Alice")
person2 = Human("Bob")

for person in [person1, person2]:
    print(person.welcome())
    print(person.species_info())
    print(person.random_message())
