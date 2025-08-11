# -----Regular Ball Super Ball-----

# Create a class Ball. 
# Ball objects should accept one argument for "ball type" when instantiated.
    
# If no arguments are given, 
# ball objects should instantiate with a "ball type" of "regular."

class Ball:
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type


# -----Color Ghost-----

# Create a class Ghost
# Ghost objects are instantiated without any arguments.
# Ghost objects are given a random color attribute of 
# "white" or "yellow" or "purple" or "red" when instantiated

from random import choice

class Ghost:
    def __init__(self):
        self.color = choice(["white", "yellow", "purple", "red"]) 


# -----Basic subclasses - Adam and Eve-----

# According to the creation myths of the Abrahamic religions, 
# Adam and Eve were the first Humans to wander the Earth.

# You have to do God's job. The creation method must return an array of length 2 containing objects 
# (representing Adam and Eve). The first object in the array should be an instance of the class Man. 
# The second should be an instance of the class Woman. Both objects have to be subclasses of Human. 
# Your job is to implement the Human, Man and Woman classes.

def God():
    return [Man(), Woman()]

class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass


# -----Classy Classes-----

# Your task is to complete this Class, the Person class has been created. 
# You must fill in the Constructor method to accept a name as string 
# and an age as number, complete the get Info property and getInfo method/Info getter 
# which should return johns age is 34

class Person:
    def __init__(self, name, age):
        self.info=f"{name}s age is {age}"


# -----Building Spheres-----

# Now that we have a Block let's move on to something slightly more complex: a Sphere.

# Arguments for the constructor
# radius -> integer or float (do not round it)
# mass -> integer or float (do not round it)

# Methods to be defined
# get_radius()       =>  radius of the Sphere (do not round it)
# get_mass()         =>  mass of the Sphere (do not round it)
# get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
# get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
# get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)

from math import pi

class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
    
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return round(4/3 * pi * self.radius ** 3, 5)
    
    def get_surface_area(self):
        return round(4 * pi * self.radius ** 2, 5) 
    
    def get_density(self):
        return round(self.mass / Sphere.get_volume(self), 5)


# -----Python's Dynamic Classes #1-----
# Timmy's quiet and calm work has been suddenly stopped by 
# his project manager (let's call him boss) yelling:

# - Who named these classes?! Class MyClass? It's ridiculous! '
# 'I want you to change it to UsefulClass!

# Tim sighed, he already knew it's gonna be a long day.
# Few hours later, boss came again:
# Much better - he said - but now I want to change that class name to SecondUsefulClass,

# and went off. Although Timmy had no idea why changing name is so important for his boss, 
# he realized, that it's not the end, so he turned to you, his guru, 
# to help him and asked you to prepare some function, which could change name of given class.

def class_name_changer(cls, new_name):
    if not new_name.isalnum() or not new_name[0].isupper():
        raise Exception("The name does not meet the requirements")
    cls.__name__ = new_name
