from tkinter import *
from datetime import date

def calculate_age():
    
    today = date.today()
    
    try:

        user_name = name_entry.get()
        birth_year = int(year_entry.get())
        
        age = today.year - birth_year
        
        result_label.config(text=f"Hello {user_name}!\nYou are {age} years old.", fg="#2ecc71")
    except ValueError:
        result_label.config(text="Please enter a valid year!", fg="red")

root = Tk()
root.geometry("400x400")
root.title("Age Calculator App")
root.configure(bg="#f0f3f4") 

Label(root, text="Name:", bg="#f0f3f4").grid(row=0, column=0, padx=20, pady=10)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)

Label(root, text="Birth Date:", bg="#f0f3f4").grid(row=1, column=0, padx=20, pady=10)
date_entry = Entry(root)
date_entry.grid(row=1, column=1)

Label(root, text="Birth Month:", bg="#f0f3f4").grid(row=2, column=0, padx=20, pady=10)
month_entry = Entry(root)
month_entry.grid(row=2, column=1)

Label(root, text="Birth Year:", bg="#f0f3f4").grid(row=3, column=0, padx=20, pady=10)
year_entry = Entry(root)
year_entry.grid(row=3, column=1)

calc_btn = Button(root, text="Calculate Age", command=calculate_age, bg="#3498db", fg="white", font=("Arial", 10, "bold"))
calc_btn.grid(row=4, column=0, columnspan=2, pady=20)

result_label = Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f3f4")
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()