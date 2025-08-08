import practical_task_09_1 as guess_functions

import tkinter as tk
from tkinter import font

# ----------------------------------- Random -----------------------------------
rand_num = guess_functions.random_num()
attempts = 10


def check_guess(guess_entry, result_label):
    '''
    Function which checking all valid values of user number and compare it with random number
    '''
    global rand_num
    global attempts

    # Get user data
    user_input = guess_entry.get()
    
    # Check if the input is number
    if guess_functions.check_user_input_is_digit(user_input) is False:
        result_label.config(text='Please enter correct integer number.')
    else:
        # Convert to integer
        user_input = int(user_input)

    # Check if the number in the range from 1 to 100
    if guess_functions.check_user_input_range(user_input) is False:
        result_label.config(text='Enter number of range from 1 to 100.')
    
    # Continue checking
    else:
        attempts -= 1
        # Flag for game over
        flag = False

        if attempts != 0:
            if user_input  == rand_num:
                result_label.config(text='Congratulation!')
                flag = True
            elif user_input < rand_num:
                result_label.config(text='The number is more than you entered. Try again...')
            elif user_input > rand_num:
                result_label.config(text='The number is less than you entered. Try again...')
        else:
            result_label.config(text='Your attempts over')
            flag = True

        if flag:
            guess_entry.config(state=tk.DISABLED)
            button.config(state=tk.DISABLED)

# ----------------------------------- tkinter -----------------------------------
HEIGHT = 30
WIDTH = 300

root = tk.Tk()
root.title("Guess number Application")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

custom_font = font.Font(family="Verdana", size=12, weight="normal")

info_frame = tk.Frame(root, bg="deep sky blue", bd=5)
info_frame.pack(pady=5)

info_label = tk.Label(info_frame, font=custom_font, 
                      text='Hi! Let\'s play a game\n in which you try to guess a number\n that I chose in the range from 1 to 100.\n You have 10 attempts.')
info_label.pack()


input_frame = tk.Frame(root, bg="blue", bd=5)
input_frame.pack()

guess_label = tk.Label(input_frame, font=custom_font, text='Enter your guess number here')
guess_label.pack(side='left', padx=5)

guess_entry = tk.Entry(input_frame, font=custom_font)
guess_entry.pack(side='left', padx=5)


result_frame = tk.Frame(root, bg='gold', bd=10)
result_frame.pack(pady=10)

result_label = tk.Label(result_frame, font=custom_font, height=5, width=40)
result_label.pack()

button = tk.Button(root, 
                   text="Guess number", font=custom_font,
                   bg="light green", fg="black",
                   command=lambda: check_guess(guess_entry, result_label))
button.pack(pady=5)

root.mainloop()