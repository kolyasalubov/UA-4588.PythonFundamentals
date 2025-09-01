class NumberOutOfBoundError(Exception) :
    def __init__(self, message) :
        self.message = message


def day_of_week() :
    number = input("Enter the number: ")

    try :
        number = int(number)

        match number :
            case 1 :
                print("Monday")
            case 2 :
                print("Tuesday")
            case 3 :
                print("Wednesday")
            case 4 :
                print("Thursday")
            case 5 :
                print("Friday")
            case 6 :
                print("Saturday")
            case 7 :
                print("Sunday")
            case _ :
                if number > 7 :
                    raise NumberOutOfBoundError("Number can not be greater than 7")
    
    except NumberOutOfBoundError as e :
        print(e)
    
    except ValueError :
        print("You entered not a number")


####################---MainProgram---####################


day_of_week()