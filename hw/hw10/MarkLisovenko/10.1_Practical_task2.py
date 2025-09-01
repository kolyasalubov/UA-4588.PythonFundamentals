class Human :
    species = "Homosapiens"

    def __init__(self, name) :
        self.name = name

    def welcome_message(self) :
        print(f"Hello {self.name}!")

    @classmethod
    def species_belonging(cls) :
        return f"Objects of {cls.__name__} class belong to {cls.species}"
    
    @staticmethod
    def static_method() :
        return "I love Python!"
    

####################---MainProgram---####################


person_1 = Human("Mark")

person_1.welcome_message()

print(Human.species_belonging())

print(person_1.static_method())