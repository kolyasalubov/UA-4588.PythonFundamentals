def number_to_day(number: int):
    match number:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            raise ValueError("Incorrect day number")
        
try:
    day_number = int(input("Please enter the number of a day: "))
    day = number_to_day(day_number)
except ValueError as e:
    print(e)
except Exception as e:
    print("Something went wrong:", e)      
else:
    print(day)
