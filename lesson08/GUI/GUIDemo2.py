import tkinter

win = tkinter.Tk()

win.title('我的視窗')
label = tkinter.Label(win, text='Hello', fg='yellow', bg='red', fount_='Arial', 12)
label2 = tkinter.Label(win, text='Hello2')
button1 = tkinter.Button(win, text='Hello3')
label4 = tkinter.Label(win, text='Hello4')
button2 = tkinter.Button(win, text='Hello5')
label.grid(column=0, row=0, padx=20)
label2.grid(column=1, row=0, pady=20)
button1.grid(column=2, row=3)
label4.grid(column=0, row=1)
button2.grid(column=2, row=5)
win.geometry('300x300')

win.mainloop()
