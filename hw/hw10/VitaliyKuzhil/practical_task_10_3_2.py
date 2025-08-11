class Animals():
    '''
    Main class for Animals
    '''
    def __init__(self, name, species, legs):
        '''
        Initial method

        name: str
        species: str
        legs: int
        '''
        self.name = name
        self.species = species
        self.legs = legs


    @classmethod
    def make_sound(self):
        '''
        Class method that overriden in the subclasses
        '''


class Mammal(Animals):
    '''
    Class Mammal
    '''
    def give_birth(self):
        '''
        Method give_birth in class Mammal 
        '''
        pass


    def make_sound(self):
        '''
        Method that return a sound of Mammal
        '''
        return 'Roar'


class Bird(Animals):
    '''
    Class Bird
    '''
    def lay_eggs(self):
        '''
        Method lay_eggs in class Bird
        '''
        pass


    def make_sound(self):
        '''
        Method that return a sound of Bird
        '''
        return 'Squawk'


class Reptile(Animals):
    '''
    Class Reptile
    '''
    def shed_skin(self):
        '''
        Method shed_skin in class Reptile
        '''
        pass


    def make_sound(self):
        '''
        Method that return a sound of Reptile
        '''
        return 'Hiss'
