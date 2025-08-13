class Human:
    '''
    Human class
    '''
    def __init__(self, name):
        '''
        Initialize method
        '''
        self.name = name

        print(f'Create person: {self.name}')


    def congratulation(self):
        '''
        Congratulation method (instanse method)
        '''
        print(f'Hello, {self.name}!')


    @classmethod
    def genus(self):
        '''
        Genus method (class method)
        '''
        print('You are "Homosapiens"')


    @staticmethod
    def ability():
        '''
        Ability method (static method)
        '''
        print('People can reasoning. And it\'s amazing!')


if __name__ == '__main__':

    persons = ['Mark', 'Jeff', 'Adam']

    for person in persons:

        person = Human(name = 'Mark')
        person.congratulation()
        person.genus()
        person.ability()
        
        print()
