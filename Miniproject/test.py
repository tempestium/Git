from tkinter import *
import time

def clicked1():
    root1 = Tk()

    root1.mainloop()



root = Tk()
root.wm_title("Hello, world")

label = Label(master= root, text="hellow world")
label.pack(pady= 20)

button = Button(master= root, text='druk op mij, me likes', command=clicked1)
button.pack(pady=5)
button1= Button(master= root, text='test')
button1.pack(pady=5)
button1= Button(master= root, text='test')
button1.pack(pady=5)


label1= label
entry = Entry(master= root, text='test')
entry.pack(pady=20)


root.mainloop()

