from tkinter import *
import random

def play(user_choice):
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)
    
    if user_choice == computer_choice:
        result = f"It's a Tie!\nComputer also chose {computer_choice}"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = f"You Win!\nComputer chose {computer_choice}"
    else:
        result = f"You Lose!\nComputer chose {computer_choice}"
    
    result_label.config(text=result)

root = Tk()
root.title("Length Converter App")
root.geometry("400x400")

title_label = Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"), pady=20)
title_label.pack()

instruction_label = Label(root, text="Choose your move:", font=("Arial", 12))
instruction_label.pack(pady=10)

btn_frame = Frame(root)
btn_frame.pack(pady=20)

rock_btn = Button(btn_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = Button(btn_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = Button(btn_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

result_label = Label(root, text="", font=("Arial", 14, "italic"), fg="blue", pady=30)
result_label.pack()

root.mainloop()