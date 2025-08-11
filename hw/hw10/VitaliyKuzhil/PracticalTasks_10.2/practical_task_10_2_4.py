class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
        self.info=f'{self.name}s age is {self.age}'

names=['John','Matt','Alex', 'Mike']
ages=[16,25,57,39]

for i in range(4):
    person = Person(names[i], ages[i])
    print(person.info)