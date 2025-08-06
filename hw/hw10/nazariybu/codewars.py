# I. Ball-super-ball
# Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

class Ball(object):
  def __init__(self, type = "regular"):
    self.ball_type = type

# -------------------------------------------------------

# II. Color-ghost
# Create a class Ghost
# Ghost objects are instantiated without any arguments.
# Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated

# import random

# class Ghost(object):  
#     def __init__(self):
#         colors = ["white", "yellow", "purple","red"]
#         self.color = random.choice(colors)


# ---------------------------------------------------------

# III. Basic-subclasses-Adam-and-Eve
# According to the creation myths of the Abrahamic religions,
# Adam and Eve were the first Humans to wander the Earth.
# You have to do God's job.
# The creation method must return an array of length 2 containing objects (representing Adam and Eve).
# The first object in the array should be an instance of the class Man.
# The second should be an instance of the class Woman.
# Both objects have to be subclasses of Human.
# Your job is to implement the Human, Man and Woman classes.

# def God():
#     return [Man(), Woman()]

# class Human():
#     pass

# class Man(Human):
#     pass

# class Woman(Human):
#     pass

# --------------------------------------------------------

# IV. Classy-classes
# Your task is to complete this Class, the Person class has been created.
# You must fill in the Constructor method to accept a name as string and an age as number,
# complete the get Info property and getInfo method/Info getter which should return johns age is 34

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.info= f"{self.name}s age is {self.age}"

# -----------------------------------------------------

# V. Building Spheres
# Arguments for the constructor
# radius -> integer or float (do not round it)
# mass -> integer or float (do not round it)

# Methods to be defined
# get_radius()       =>  radius of the Sphere (do not round it)
# get_mass()         =>  mass of the Sphere (do not round it)
# get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
# get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
# get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)

# import math

# class Sphere(object):
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
        
#     def get_radius(self):
#         return self.radius
    
#     def get_mass(self):
#         return self.mass
    
#     def get_volume(self):
#         volume = (4/3) * math.pi * math.pow(self.radius, 3)
#         return round(volume, 5)
    
#     def get_surface_area(self):
#         area = 4 * math.pi * math.pow(self.radius, 2)
#         return round(area, 5)
    
#     def get_density(self):
#         density = self.mass / ((4/3) * math.pi * math.pow(self.radius, 3))
#         return round(density, 5)

# ------------------------------------------------------

# VI. Dynamic Classes
# Although Timmy had no idea why changing name is so important for his boss,
# he realized, that it's not the end, so he turned to you, his guru,
# to help him and asked you to prepare some function, which could change name of given class.
# Note: Proposed function should allow only names with alphanumeric chars (upper & lower letters plus ciphers),
# but starting only with upper case letter. In other case it should raise an exception.

# import re

# def class_name_changer(cls, new_name):
#     if not re.match(r'^[A-Z][A-Za-z0-9]*$', new_name):
#         raise ValueError("Invalid class name!")
        
#     cls.__name__ = new_name
#     return cls