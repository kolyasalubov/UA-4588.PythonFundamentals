class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


import random
class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])



class Human:
    pass
class Man(Human):
    pass
class Woman(Human):
    pass
def God():
    return [Man(), Woman()]




class Person:
    def __init__(self, name, age):
        # Зберігаємо дані в атрибуті info
        self.info = f"{name}s age is {age}"




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
        volume = (4 / 3) * math.pi * (self.radius ** 3)
        return round(volume, 5)

    def get_surface_area(self):
        area = 4 * math.pi * (self.radius ** 2)
        return round(area, 5)

    def get_density(self):
        density = self.mass / ((4 / 3) * math.pi * (self.radius ** 3))
        return round(density, 5)
    



def class_name_changer(cls, new_name):
    # Перевіряємо, чи нова назва починається з великої літери
    # та складається лише з букв і цифр
    if not (new_name and new_name[0].isupper() and new_name.isalnum()):
        raise Exception("Invalid class name!")
    
    # Змінюємо ім'я класу
    cls.__name__ = new_name