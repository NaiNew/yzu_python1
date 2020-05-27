import tkinter

win = tkinter.Tk()

win.title('我的視窗')
label = tkinter.Label(win, text='Hello')
label.pack(side=tkinter.LEFT)
label2 = tkinter.Label(win, text='Bye')
label2.pack(side=tkinter.RIGHT)
win.geometry('300x300')

win.mainloop()
