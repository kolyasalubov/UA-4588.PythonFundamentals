from math import pow, pi

def rectangle (a, b):
    s = a * b
    return s


def triangle (h, a):
    s = 0.5 * h * a
    return s


def circle (r):
    s = pi * pow(r)
    return s