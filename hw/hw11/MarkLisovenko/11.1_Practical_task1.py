class NegativeNumberAgeError(Exception) :
    def __init__(self, message) :
        self.message = message


def check_age() :
    age = int(input("Enter your age: "))
    
    try :
        if age >= 0 :
            print("Your age is even") if age % 2 == 0 else print("Your age is odd")
    
        else :
            raise NegativeNumberAgeError("Age can not be a negative number")
    
    except NegativeNumberAgeError as e :
        print(e)


####################---MainProgram---####################


check_age()