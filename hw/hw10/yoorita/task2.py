class Human:
    __species = "Homo sapiens"
    def __init__(self, name):
        self.__name = name

    def welcome(self):
        print(f"Hello, {self.__name}!")

    @classmethod
    def species(cls):
        return cls.__species

    @staticmethod
    def call_static():
        return "Result of the static method"


if __name__ == "__main__":
    human1 = Human("Alex")
    human2 = Human("Bill")

    human1.welcome()
    human2.welcome()

    print(human1.species())
    print(human2.call_static())