day = int(input("Enter the day of the month: "))
match day:
    case 1:
        print("its monday")
    case 2:
        print("its tuesday")
    case 3:
        print("its wednesday")
    case 4:
        print("its thursday")   
    case 5:
        print("its friday")             
    case 6:
        print("its saturday")    
    case 7:
        print("its sunday")
    case _:
        raise ValueError("Invalid day of the month. Please enter a number between 1 and 7.")      