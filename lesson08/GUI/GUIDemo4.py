import tkinter
from tkinter import messagebox

def myadd():
    pass

win = tkinter.Tk()
win.geometry('300x300')

label = tkinter.Label(win, text='0')
label.pack()

button = tkinter.Button(win, text='add', command=myadd)
button.pack()

win.mainloop()
