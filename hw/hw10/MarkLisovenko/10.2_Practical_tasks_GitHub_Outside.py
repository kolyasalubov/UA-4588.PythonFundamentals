# --- Ball-super-ball ---
class Ball :
    def __init__(self, ball_type = "regular") :
        self.ball_type = ball_type


# --- Color-ghost ---
import random

class Ghost :
    colors = ("white", "yellow", "purple", "red")
    def __init__(self) :
        self.color = random.choice(Ghost.colors)


# --- Basic-subclasses-Adam-and-Eve ---
class Human :
    def __init__(self) :
        pass
        

class Man(Human) :
    def __init__(self) :
        super().__init__()
    
    
class Woman(Human) :
    def __init__(self) :
        super().__init__()
        

def God() :
    return [Man(), Woman()]


# --- Classy-classes ---
class Person :
    def __init__(self, name : str, age : int) :
        self.name = name
        self.age = age
        
    @property    
    def info(self) :
        return f"{self.name}s age is {self.age}"


# --- Building Spheres ---
import math

class Sphere :
    def __init__(self, radius : int | float, mass : int | float) :
        self.radius = radius
        self.mass = mass
        
    def get_radius(self) :
        return self.radius
    
    def get_mass(self) :
        return self.mass
    
    def get_volume(self) :
        volume = (4 / 3) * math.pi * math.pow(self.radius, 3)
        return round(volume, 5)
        
    def get_surface_area(self) :
        surface_area = 4 * math.pi * math.pow(self.radius, 2)
        return round(surface_area, 5)
        
    def get_density(self) :
        density = self.mass / ((4 / 3) * math.pi * math.pow(self.radius, 3))
        return round(density, 5)


# --- Dynamic Classes ---
import re

def class_name_changer(cls, new_name):
    if re.search(r"^[A-Z][A-Za-z0-9]*$", new_name) :
        cls.__name__ = new_name
    else :
        raise ValueError