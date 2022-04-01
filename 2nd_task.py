# libraries from tkinter

import tkinter as tk
from tkinter import ttk

# title name

root = tk.Tk()
root.title("GUI")

# label using grid()

name_label = ttk.Label(root, text = "Hello Python")
name_label.grid(row = 1, column = 1)

email_label = ttk.Label(root, text = "email")
email_label.grid(row = 2, column = 1)

address_label = ttk.Label(root, text = "address")
address_label.grid(row = 3, column =1)

root.mainloop()