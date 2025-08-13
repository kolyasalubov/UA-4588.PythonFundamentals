class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Hello, {self.name}! Welcome!")

    @classmethod
    def species(cls):
        return "Species: Homo sapiens"

    @staticmethod
    def message():
        return "Have a great day!"

# 🔹 Приклад використання
person = Human("Alice")
person.welcome()
print(Human.species())       # ➤ Species: Homo sapiens
print(Human.message())       # ➤ Have a great day!
