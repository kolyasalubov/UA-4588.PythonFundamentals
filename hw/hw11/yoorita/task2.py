
days_of_week = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}

while True:
    try:
        number = int(input('Enter the number: '))
        print(days_of_week[number])
    except ValueError:
        print('ValueError: Entered input is not a number')
    except KeyError:
        print('KeyError: You\'re trying to find a day of week that doesn\'t exists')
    finally:
        running = input('Exit - press Enter\nContinue - press any key\n')