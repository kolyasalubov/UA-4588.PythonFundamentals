def get_day_of_week():
   
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    try:
        number = int(input("Enter a number from 1 to 7: "))

        if number in days:
            print(f'{number} is {days[number]}')
        else:
            raise ValueError("Error: Please enter a number between 1 and 7.")
        
    except ValueError as e:
        print(e)


get_day_of_week()