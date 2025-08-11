# Create a Car class with the attributes
# name, kind, model and methods of start and stop,
# which indicate information that the car started or stoped accordingly

class Car:
    def __init__(self, name, kind, model):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(kind, str):
            raise TypeError("kind must be a string")
        if not isinstance(model, (int, str)):
            raise TypeError("model must be int or string")

        self.name = name
        self.kind = kind
        self.model = model

    def start(self):
        print(
            f"Car with name {self.name}, kind {self.kind} and model {self.model} is START")

    def stop(self):
        print(
            f"Car with name {self.name}, kind {self.kind} and model {self.model} is STOP")
