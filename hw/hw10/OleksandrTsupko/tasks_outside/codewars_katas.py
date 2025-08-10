import random


# Regular Ball Super Ball

# Create a class Ball. Ball objects should accept one argument 
# for "ball type" when instantiated.
# If no arguments are given, ball objects should instantiate 
# with a "ball type" of "regular."

class Ball:
    
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


# Color Ghost

# Create a class Ghost 
# Ghost objects are instantiated without any arguments. 
# Ghost objects are given a random color attribute 
# of "white" or "yellow" or "purple" or "red" when instantiated

class Ghost:

    def __init__(self, colors=["white", "yellow", "purple", "red"]):
        self.color = random.choice(colors)