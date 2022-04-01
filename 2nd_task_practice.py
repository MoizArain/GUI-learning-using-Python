# importing libraries
import tkinter as tk
from tkinter import ttk

# title
root = tk.Tk()
root.title("my 2nd GUI")

# label using grid
label_1 = ttk.Label(root, text="this is my 2nd GUI")
label_1.grid(row=1, column=1)

label_2 = ttk.Label(root,text="this is my 2nd GUI")
label_2.grid(row= 2, column = 1)

label_3 = ttk.Label(root, text = "this is my 2nd GUI")
label_3.grid(row=3, column = 1)

root.mainloop()