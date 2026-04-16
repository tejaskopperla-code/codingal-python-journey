from tkinter import *

def check_strength():
    password = password_entry.get()
    length = len(password)
    
    if length == 0:
        result_label.config(text="Enter a password", fg="black")
    elif length <= 5:
        result_label.config(text="Strength: Weak", fg="Red")
    elif 6 <= length <= 8:
        result_label.config(text="Strength: Medium", fg="Yellow") # You might want 'Orange' for better visibility
    elif 9 <= length <= 12:
        result_label.config(text="Strength: Strong", fg="Light Green")
    else:
        result_label.config(text="Strength: Very Strong", fg="Dark Green")

root = Tk()
root.geometry("400x400")

root.title("Length Converter App")
root.configure(bg="#f0f0f0")

Label(root, text="Password Strength Checker", font=("Arial", 14, "bold"), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=20)

Label(root, text="Enter Password:", bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10)
password_entry = Entry(root, show="*") # 'show="*"' hides the password characters
password_entry.grid(row=1, column=1, padx=10, pady=10)

btn_check = Button(root, text="Check Strength", command=check_strength, bg="#3498db", fg="white")
btn_check.grid(row=2, column=0, columnspan=2, pady=20)

result_label = Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f0f0")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
