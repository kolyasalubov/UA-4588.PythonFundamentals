class Human:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}! Welcom!"
    
    @classmethod
    def species_info(cls):
        return "We are Homosapiens."
    
    @staticmethod
    def random_message():
        return "Have a great day and keep smiling!"