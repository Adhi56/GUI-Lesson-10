from tkinter import *

root = Tk()
root.geometry('300x300')
root.title('Theme Changer')
root.config(background='white')

def change_bg():
    colour = thecolours.get()
    root.config(background=colour)
    frame.config(background=colour)

frame = Frame(root, background='white')
frame.pack()

chooselabel = Label(frame, text = 'Choose your Background Colour:', fg = 'black', bg = 'white', bd = 15)
chooselabel.grid(row = 1, column = 1, padx = 10)

thecolours = StringVar()
red = Radiobutton(frame, text = 'Red', variable= thecolours, value = 'red')
green = Radiobutton(frame, text = 'Green', variable = thecolours, value = 'green')
blue = Radiobutton(frame,text = 'Blue', variable = thecolours, value = 'blue')

red.grid(column = 1, row = 2, pady = 5)
green.grid(column = 1, row = 3)
blue.grid(column = 1, row = 4)

colourchangebutton = Button(frame, text = 'Change', fg = 'black', bg = 'white', command = change_bg)
colourchangebutton.grid(column = 1, row = 5, pady = 5)















root.mainloop()
