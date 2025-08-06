import random

class Ghost(object):
    __colors = ["white", "yellow", "purple", "red"]
    def __init__(self):
        self.color = random.choice(Ghost.__colors)