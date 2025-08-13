# Task2. 
# Create a class Human, everyone has a name, 
# create a method in the class that displays a welcome message to each person. 
# Create a class method in the class that returns information that it is a species of "Homosapiens". 
# And in the class create a static method that returns an arbitrary message


class Human:
    def __init__(self, name):
        self.name = name
    
    def greeting(self):
        print(f"Hello {self.name}!")
    
    @classmethod
    def about_species(cls):
        return 'The species is "Homosapiens"'
    
    @staticmethod
    def info_about_humans():
        return("Humans are cool!")
    

human1 = Human("Bob")
human2 = Human("Ron")

human1.greeting()
human2.greeting()

print(Human.about_species())
print(human1.info_about_humans())
