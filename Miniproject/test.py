from tkinter import *


def gameStart():
    root = Tk()


    root.mainloop()

def highscoreTijd():
    root= Tk()

    root.mainloop()

def highscoreScore():
    root = Tk()

    labelhiscore = Label(master= root, text="dere\r derede\r")
    labelhiscore.pack()

    root.mainloop()



root = Tk()
root.wm_title("Hello, world")

logo = PhotoImage(file=r'''C:\\Users\\Dennis\\PycharmProjects\\Git\\Miniproject\\superman.gif''')
p1 = Label(master=root, image=logo)
p1.pack()


label = Label(master=root, text="super-woman-Captain", font="bold 20")
label.pack(pady=20)

button = Button(master=root, text='Start game', command=gameStart)
button.pack(pady=5)
button1 = Button(master=root, text='Highscore op tijd', command=highscoreTijd)
button1.pack(pady=5)
button1 = Button(master=root, text='Highscore op score', command=highscoreScore)
button1.pack(pady=5)


#label1 = label
#entry = Entry(master=root, text='test')
#entry.pack(pady=20)


root.mainloop()

