class Human:

    def __init__(self, name):
        self.name = name
        print(f'Greetings {name}!')

    @classmethod
    def class_information(cls):
        return 'Human is a species of "Homosapiens"'
    
    @staticmethod
    def static_method():
        print('Best regards')

h1 = Human('Oleks')
h2 = Human('Pavlo')