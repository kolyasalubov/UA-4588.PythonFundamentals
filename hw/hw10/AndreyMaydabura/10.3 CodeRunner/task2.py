class Animal:
    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs

    def make_sound(self):
        return "animal sound"


class Mammal(Animal):
    def make_sound(self):
        return "Roar"

    def give_birth(self):
        return f"{self.name} is giving birth."


class Bird(Animal):
    def make_sound(self):
        return "Squawk"

    def lay_eggs(self):
        return f"{self.name} is laying eggs."


class Reptile(Animal):
    def make_sound(self):
        return "Hiss"

    def shed_skin(self):
        return f"{self.name} is shedding its skin."
