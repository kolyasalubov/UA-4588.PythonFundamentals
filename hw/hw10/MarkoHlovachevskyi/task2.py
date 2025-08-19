class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def get_species(cls):
        return f"This is a species of {cls.species}"

    @staticmethod
    def random_message():
        return "Keep learning, keep growing!"


person = Human("Марко")
person.welcome()
print(Human.get_species())
print(Human.random_message())