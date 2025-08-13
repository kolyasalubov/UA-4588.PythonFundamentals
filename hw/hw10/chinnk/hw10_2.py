# I. Ball-super-ball

class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

ball1 = Ball()
ball2 = Ball("super")

print(ball1.ball_type)
print(ball2.ball_type)


#II. Color-ghost

import random

class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


ghost1 = Ghost()
ghost2 = Ghost()
print(ghost1.color)
print(ghost2.color)

#III. Basic-subclasses-Adam-and-Eve

class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return [Man(), Woman()]


adam, eve = God()
print(isinstance(adam, Man))
print(isinstance(eve, Woman))


#IV. Classy-classes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name}s age is {self.age}"


p1 = Person("John", 34)
print(p1.info)


# V. Building Spheres

import math

class Sphere:
    _FOUR_THIRDS_PI = 4 / 3 * math.pi

    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round(Sphere._FOUR_THIRDS_PI * self.radius ** 3, 5)

    def get_surface_area(self):
        return round(2 * math.tau * self.radius ** 2, 5)

    def get_density(self):
        volume = self.get_volume()
        return round(self.mass / volume, 5)


ball = Sphere(2, 50)
print(ball.get_radius())        # 2
print(ball.get_mass())          # 50





# VI. Dynamic Classes

def class_name_changer(cls, new_name):
    if not new_name.isalnum() or not new_name[0].isupper():
        raise Exception("Change the name")
    cls.__name__ = new_name





