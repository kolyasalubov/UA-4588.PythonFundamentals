# 1

# def check_age():
#     try:
#         age = int(input("Enter your age: "))

#         if age < 0:
#             raise ValueError("Age cannot be negative")
        
#         print("Even" if age % 2 == 0 else "Odd")

#     except ValueError as e:
#         print(e)

# if __name__ == "__main__":
#     check_age()




# 2

# try:

#     user = int(input("Enter a number from 1 to 7: "))

#     days = {1: "Monday",
#         2: "Tuesday",
#         3: "Wednesday", 
#         4: "Thursday", 
#         5: "Friday", 
#         6: "Saturday", 
#         7: "Sunday"}

#     print(days[user])

# except KeyError as k:
#     print(f"{k}: wrong number")
# except ValueError as v:
#     print(f"{v}: you must enter a number")

