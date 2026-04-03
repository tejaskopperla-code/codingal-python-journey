import tkinter as tk

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        product = num1 * num2
        
        result_text.delete("1.0", tk.END) 
        result_text.insert(tk.END, f"The product is: {product}")
    except ValueError:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Please enter valid numbers!")

root = tk.Tk()

root.geometry("400x300")

root.title("Getting Started with Widgets")

desc_label = tk.Label(root, text="Description: This app takes two numbers and calculates their product.")
desc_label.pack(pady=5)

label1 = tk.Label(root, text="Enter Number 1:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack(pady=5)

label2 = tk.Label(root, text="Enter Number 2:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack(pady=5)

calc_button = tk.Button(root, text="Calculate", command=calculate_product, bg="blue", fg="white")
calc_button.pack(pady=10)

result_text = tk.Text(root, height=2, width=30)
result_text.pack(pady=5)

root.mainloop()
