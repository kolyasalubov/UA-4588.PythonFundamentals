days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}
class MyError(Exception):
      pass

try:
    day = input("Please enter a number: ") 

    if isinstance(day, float):
            raise ValueError
    
    day = int(day)

    if day in days:
          print(f'{day} is a{days[day]}')
    else:
          print(MyError(f"{day} is not correct"))
except ValueError:
         print(MyError(f"{day} is not integer"))

except:
    pass