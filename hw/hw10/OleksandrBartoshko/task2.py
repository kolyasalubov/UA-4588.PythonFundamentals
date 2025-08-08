class Human:
    def __init__(self, name):
        self.name = name
    def welcome(self):
        return f'Welcome {self.name}'
    @classmethod
    def species():
        return "Homosapiens"    
    
    @staticmethod
    def message():
        return "Good for u, that you are human :)"