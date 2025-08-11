# 1

# class Ball(object):
#     def __init__(self, ball_type = "regular"):
#         self.ball_type = ball_type



# 2

# import random

# class Ghost:
#     def __init__(self):
#         opt = ["white", "yellow", "purple", "red"]
#         self.color =  random.choice(opt)




# 3

# def God():
#     return [Man(), Woman()]

# class Human(object):
#     pass

# class Man(Human):
#     pass
    
# class Woman(Human):
#     pass




# 4

# class Person:
    
#     def __init__(self, name,age):
#         self.name = str(name)
#         self.age = int(age)
        
#     @property        
#     def info(self):
#         return f"{self.name}s age is {self.age}"




# 5 

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
#         return round((4/3)*math.pi*self.radius**3, 5)
    
#     def get_surface_area(self):
#         return round(4*math.pi*self.radius**2, 5)
    
#     def get_density(self):
#         vol = self.get_volume()
#         return round(self.mass / vol, 5)




# 6

# def class_name_changer(cls, new_name):
#     if not isinstance(new_name, str):
#         raise TypeError ("new_name must be str")
        
#     if not new_name: 
#         raise ValueError ("new_name should not be empty")
        
#     if not new_name[0].isupper():
#         raise Exception ("new_name should start with upper case")
        
#     if not new_name.isalnum():
#         raise Exception ("new_name should have only alphanumeric chars")
        
#     cls.__name__ = new_name