import math

class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
    
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        self.volume = 4 / 3 * math.pi * pow(self.radius, 3)
        return round(self.volume, 5)
    
    def get_surface_area(self):
        self.surface_area = 4 * math.pi * pow(self.radius, 2)
        return round(self.surface_area, 5)
    
    def get_density(self):
        self.density = self.mass / self.volume
        return round(self.density, 5)
    
    