from tkinter import *

root = Tk('test')

label = Label(master= root, text= 'hellowworld', background='blue')
label.pack()

button = Button(master= root, text='druk op mij, me likes')
button.pack(pady=20)

entry = Entry(master= root)


root.mainloop()


