# Створіть клас Людина, у кожного є ім'я, створіть метод у класі, який відображає вітальне 
# повідомлення кожній людині. Створіть метод класу в класі, який повертає інформацію про 
# те, що це вид "Homosapiens". І в класі створіть статичний метод, який повертає

class Human:
    __species = 'Homosapiens'
    def __init__(self, name):
        self.__name = name

    def hello(self):
        return f'Hello, {self.__name}'
    
    @classmethod
    def species(cls):
        return cls.__species
    
    @staticmethod
    def arbitrary():
        return "Hello, world"
    
############ Test ############
# person = Human('Andrii')
# print(person.hello())
# print(person.species())
# print(person.arbitrary())