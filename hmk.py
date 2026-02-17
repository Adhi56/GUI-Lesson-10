from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Student Registration')

def enroll_student():
    course = course_combobox.get()
    batch = batch_var.get()
    if course and batch:
        result_label.config(text=f"Registered for {course} in the {batch}")
    else:
        result_label.config(text="Select course and batch!")

frame = Frame(root)
frame.pack()

course_combobox = Combobox(frame)
course_combobox['values'] = ('Python', 'Game Development', 'Web Design')
course_combobox.grid(row=0, column=0, padx=5, pady=5)
course_combobox.current(0)

batch_var = StringVar()
Radiobutton(frame, text='Morning Batch', variable=batch_var, value='Morning Batch').grid(row=1, column=0)
Radiobutton(frame, text='Evening Batch', variable=batch_var, value='Evening Batch').grid(row=2, column=0)

Button(frame, text='Enroll Now', command=enroll_student).grid(row=3, column=0, pady=5)

result_label = Label(frame, text='')
result_label.grid(row=4, column=0, pady=5)

root.mainloop()
