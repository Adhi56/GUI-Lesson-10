from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Times Table')

def geneatetable():
    table = ''
    value = endVal.get()
    num = theNum.get()
    for i in range(value + 1):
        #5*0 = 5
        table += str(num)+" X "+str(i)+" = "+str(num*i) + "\n"
    answers.config(text = table)


frame = Frame(root)
frame.pack()

maintitlelabel = Label(frame, text = 'Maths Table')
maintitlelabel.grid(row = 0, column = 1, padx = 5, pady = 5)

rangelabel = Label(frame, text = 'Number and Range: ')
rangelabel.grid(row = 1, column = 0, padx = 5, pady = 5)

theNum = IntVar()
numbers = Combobox(frame, textvariable= theNum, width = 5)
numbers['values'] = tuple(range(101))
numbers.grid(row = 1, column = 1, padx = 5, pady = 5)

endVal = IntVar()
r10 = Radiobutton(frame,text = '10', variable=endVal, value=10)
r20 = Radiobutton(frame, text = '20', variable =endVal, value=20)
r30 = Radiobutton(frame,text = '30', variable= endVal, value = 30)

r10.grid(row = 1, column = 2, padx = 5, pady = 5)
r20.grid(row = 2, column = 2, padx = 5, pady = 5)
r30.grid(row = 3, column = 2, padx = 5,pady = 5)

endVal.set(10)

generatebutton = Button(frame, text = 'Generate', command = geneatetable)
generatebutton.grid(row = 4, column = 1, padx = 5, pady = 5)

answers = Label(frame)
answers.grid(row = 5, column = 1, pady  =5, padx = 5)
























root.mainloop()