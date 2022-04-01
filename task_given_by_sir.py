import tkinter as tk
from tkinter import ttk

# title
root = tk.Tk()
root.title("Registeration of Form")

# label
label_1 = ttk.Label(root, text = "Institute of Mathematics & computer Science")
label_1.grid(row = 1, column = 1)

label_2 = ttk.Label(root, text= "Exam Registration form")
label_2.grid(row = 2, column = 1)

name_label = ttk.Label(root, text = "Name: ")
name_label.grid(row = 3, column = 1)

roll_no_label = ttk.Label(root, text = "Roll No: ")
roll_no_label.grid(row = 4, column = 1)

cast_label = ttk.Label(root, text = "Cast: ")
cast_label.grid(row = 5, column = 1)

semester_label = ttk.Label(root, text = "Semester: ")
semester_label.grid(row = 6, column = 1)

year_label = ttk.Label(root, text = "Year: ")
year_label.grid(row = 7, column = 1)


# entry box
name_1 = tk.StringVar() #creating variable for entry box
name_box = ttk.Entry(root, width= 16, textvariable = name_1) #entry box
name_box.grid(row = 3, column = 2) # layout// position //button

# entry box
name_label = ttk.Entry(root)
name_label.grid(row = 3, column = 2)

roll_no_label = ttk.Entry(root)
roll_no_label.grid(row = 4,column = 2)

cast_label = ttk.Entry(root)
cast_label.grid(row = 5, column = 2)

semester_label = ttk.Entry(root)
semester_label.grid(row = 6, column = 2)

year_label = ttk.Entry(root)
year_label.grid(row = 7, column = 2)

# button
def action():
    print("Button Pressed")

submit = ttk.Button(root, text="Submit", command = action)
submit.grid(row=8,column = 1)

root.mainloop()