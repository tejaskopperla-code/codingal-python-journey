from tkinter import *

def calculate_interest():
    try:
        p = float(p_entry.get())  
        r = float(r_entry.get())  
        t = float(t_entry.get())  
        
        si = (p * r * t) / 100
        ci = p * (pow((1 + r / 100), t)) - p
        
        result_label.config(text=f"Simple Interest: {si:.2f}\nCompound Interest: {ci:.2f}", fg="blue")
    except ValueError:
        result_label.config(text="Please enter numbers only!", fg="red")

root = Tk()
root.geometry("400x400")
root.title("Age Calculator App") 
root.configure(bg="#fdfefe")

Label(root, text="Principle Amount:", bg="#fdfefe").grid(row=0, column=0, padx=20, pady=10, sticky="w")
p_entry = Entry(root)
p_entry.grid(row=0, column=1)

Label(root, text="Time (years):", bg="#fdfefe").grid(row=1, column=0, padx=20, pady=10, sticky="w")
t_entry = Entry(root)
t_entry.grid(row=1, column=1)

Label(root, text="Rate of Interest (%):", bg="#fdfefe").grid(row=2, column=0, padx=20, pady=10, sticky="w")
r_entry = Entry(root)
r_entry.grid(row=2, column=1)

btn = Button(root, text="Calculate Interest", command=calculate_interest, bg="orange", fg="white")
btn.grid(row=3, column=0, columnspan=2, pady=20)

result_label = Label(root, text="", font=("Arial", 11, "bold"), bg="#fdfefe")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
