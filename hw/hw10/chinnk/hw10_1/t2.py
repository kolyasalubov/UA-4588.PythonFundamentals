class Human:
    species = "Homosapiens"

    def __init__(self, name: str) -> None:
        self.name = name

    def welcome(self) -> str:
        return f"Welcome, {self.name}!"

    @classmethod
    def get_species(cls) -> str:
        return cls.species

    @staticmethod
    def random_fact() -> str:
        return "Humans dream for about two hours per night on average."


# quick demo
alice = Human("Alice")
print("Task2 →", alice.welcome())
print("Task2 → species:", Human.get_species())
print("Task2 → fact:", Human.random_fact())
