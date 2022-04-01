# importing libraries 

import tkinter as tk
from tkinter import ttk

# title name

root = tk.Tk()
root.title("GUI")

# label

name_label = ttk.Label(root, text = "Moiz")
name_label.pack()

email_label = ttk.Label(root, text = "email")
email_label.pack()

address_label = ttk.Label(root, text = "address")
address_label.pack()

# we use pack() to place the widgets in the window
# but we can also use grid()
# difference between pack() and grid() is that pack() is used to place widgets in the window 
# and grid() is used to place widgets in the grid
# we can use only one of them

root.mainloop()