# Task 1.
# Write a game script that randomly generates a number from a range of
# 1 to 100 and asks the user to guess that number in 10 tries.
# The program reads the numbers entered by the user and prompts the user
# whether the guessed number is greater or less than the number entered by the
# user. The game must continue until the user has used 10 attempts and guessed
# the number. If the user guessed the number, the program prints a
# congratulatory message, and if 10 attempts have been exhausted and the user
# did not have time to guess the number, then the corresponding message is
# displayed.
# (to perform the task, you need to import the random module,
# and from it the randint() function)

# import random

# number = random.randint(1,100)

# attempts = 0
# while attempts < 10:
#     user_input = input("What is my number?\n")

#     if not user_input.isdigit():
#         print("Enter a valid number!")
#         continue

#     user_number = int(user_input)

#     if number == user_number:
#         print("You win!")
#         break
#     else:
#         print("Nope! Try again.\n")
#     attempts += 1

# if attempts == 10:
#     print(f"You Lost. The number was {number}.")
