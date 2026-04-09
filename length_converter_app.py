from tkinter import *

def convert():
    try:
        meters = float(entry_value.get())
        feet = meters * 3.28
        
        result_label.config(text=f"{meters} Meters = {feet:.2f} Feet", fg="#27ae60")
    except ValueError:
        result_label.config(text="Please enter a valid number!", fg="red")

root = Tk()
root.geometry("400x400")
root.title("Length Converter App")
root.configure(bg="#fdfefe") 

title = Label(root, text="Meter to Feet Converter", font=("Arial", 16, "bold"), bg="#fdfefe", fg="#2c3e50")
title.grid(row=0, column=0, columnspan=2, pady=20)

Label(root, text="Enter Meters:", bg="#fdfefe", font=("Arial", 10)).grid(row=1, column=0, padx=20, pady=10, sticky="e")
entry_value = Entry(root, font=("Arial", 10))
entry_value.grid(row=1, column=1, padx=10, pady=10, sticky="w")

btn_convert = Button(root, text="Convert", command=convert, bg="#3498db", fg="white", width=15)
btn_convert.grid(row=2, column=0, columnspan=2, pady=20)

result_label = Label(root, text="Result will appear here", font=("Arial", 12), bg="#fdfefe")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
