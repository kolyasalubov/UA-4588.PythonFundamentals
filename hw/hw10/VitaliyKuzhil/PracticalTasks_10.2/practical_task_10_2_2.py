import random

class Ghost:
    '''
    Class Ghost
    '''
    # List of colors for Ghost instances
    colors = ['white', 'yellow', 'purple', 'red']

    def __init__(self):
        self.color = random.choice(Ghost.colors)


ghost = Ghost()
print(ghost.color)  #=> "white" or "yellow" or "purple" or "red"
