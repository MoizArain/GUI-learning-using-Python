import tkinter as tk
from tkinter import ttk

# tittle name

root = tk.Tk()
root.title("GUI")

# label with element without assining position

name_label = ttk.Label(root, text = "Hello Python")
name_label.grid(row = 1, column = 1)

email_label = ttk.Label(root, text = "email")
email_label.grid(row = 2, column = 1)

address_label = ttk.Label(root, text = "address")
address_label.grid(row = 3, column =1)

# entry box of button submit

name = tk.StringVar() #creating variable for entry box
name_box = ttk.Entry(root, width= 16, textvariable = name) #entry box
name_box.grid(row = 1, column = 2) # layout// position //button

# entry box and now we are assinging element position
name_box = ttk.Entry(root)
name_box.grid(row = 1, column = 2)

email_box = ttk.Entry(root)
email_box.grid(row = 2, column = 2)

address_box = ttk.Entry(root)
address_box.grid(row = 3, column =2)

# button 
def action():
    print("Button Pressed")
    
submit_button = ttk.Button(root, text="Submit", command = action)
submit_button.grid(row=4,column = 1)
                 
root.mainloop()