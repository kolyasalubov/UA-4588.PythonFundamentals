# Task 1

def check_age():
    try:
        age = input('Enter your age:\n')
       
        if age < 0:
            raise ValueError('You enter negative value')
        if age % 2 == 0:
            return f'Entered age {age} is even'
        else:
            return f'Entered age {age} is odd'
    except ValueError as e:
        return f"Error: {e}"

print(check_age())

# Task 2
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
        day = int(input('Enter a number for day of the week (1-7):\n'))
        if 1 <=  day <= 7:
            return days[ day]
        else:
            raise ValueError('Number out of range. Please enter a number from 1 to 7.')
    except ValueError as e:
        return f"Error: {e}"
    
print(get_day_of_week())