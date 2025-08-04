import random
import math
import re

# Regular Ball Super Ball
class Ball(object):
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type


# Color Ghost
class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


# Basic subclasses - Adam and Eve
class Human:
    def __init__(self):
        pass


class Man(Human):
    def __init__(self):
        super().__init__()


class Woman(Human):
    def __init__(self):
        super().__init__()


# def god():
#     return [Man(), Woman()]


# Classy Classes
class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def info(self):
        return f"{self.__name}s age is {self.__age}"


# Building Spheres
class Sphere(object):
    def __init__(self, radius, mass):
        self.__radius = radius
        self.__mass = mass

    def get_radius(self):
        return self.__radius

    def get_mass(self):
        return self.__mass

    def get_volume(self):
        return (4 / 3) * math.pi * math.pow(self.get_radius(), 3)

    def get_surface_area(self):
        return 4 * math.pi * math.pow(self.get_radius(), 2)

    def get_density(self):
        return self.get_mass() / self.get_volume()


# Python's Dynamic Classes #1
class MyClass:
    pass


def class_name_changer(cls, new_name):
    if not re.match(r'[A-Z][a-zA-Z0-9]{,79}$', new_name):
        raise NameError('Name is not valid')
    cls.__name__ = new_name

