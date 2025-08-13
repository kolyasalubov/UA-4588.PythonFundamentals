# Task 1 - Ball-super-ball
class Ball:
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type

# Task 2 - Color Ghost
import random

class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

# Task 3 - Basic subclasses - Adam and Eve
class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    pass
    
class Woman(Human):
    pass

def God():
   return [Man('Adam'), Woman('Eve')]

# Task 4 - Classy Classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"

    @property
    def set_info(self):
        return self.info
    
# Task 5 - Building Spheres
import math

class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = (4/3) * math.pi * (self.radius ** 3)
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * math.pi * (self.radius ** 2)
        return round(surface_area, 5)

    def get_density(self):
        density = self.mass / self.get_volume()
        return round(density, 5)
    
# Task 6 - Python's Dynamic Classes #1
def class_name_changer(cls, new_name):
    if not new_name[0].isupper():
        raise ValueError("Class name must start with an uppercase letter.")
    if not new_name.isalnum():
        raise ValueError("Class name must be alphanumeric.")
    
    cls.__name__ = new_name
    return cls