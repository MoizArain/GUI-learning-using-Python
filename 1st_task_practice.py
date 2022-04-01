# importing librries from tkinter
import tkinter as tk
from tkinter import ttk

# title name
root = tk.Tk()
root.title("my first GUI")

# label

name_label = ttk.Label(root, text = "hi my name is Moiz")
name_label.pack()

second_name_label = ttk.Label(root, text= "and this is my 1st gui im working on")
second_name_label.pack()


root.mainloop()