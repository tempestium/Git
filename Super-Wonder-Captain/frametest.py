from tkinter import *


def raise_frame(frame):
    frame.tkraise()

def inlog():
    return

root = Tk()

inlog = Frame(root)
aanmelden = Frame(root)
mainMenu = Frame(root)
game = Frame(root)
highscores = Frame(root)


for frame in (inlog,aanmelden, mainMenu, game, highscores):
    frame.grid(row=0, column=0, sticky='news')

# frame inlog
Label(inlog, text='super-woman-Captain', font='bold 20').pack(pady=5)
logo = PhotoImage(file=r'superman.gif')
Label(inlog, image=logo,).pack()
Label(inlog, text='click op de knop om de game te starten').pack(pady=10)

gebruikersnaam = Entry(inlog).pack()
wachtwoord = Entry(inlog).pack()
Button(inlog, text='login',command=lambda:raise_frame(mainMenu)).pack(pady=10)
Button(inlog, text= "aanmelden", command=lambda:raise_frame(aanmelden)).pack(pady=10)


#frame aanmelden
Label(aanmelden, text='super-woman-Captain', font='bold 20').pack(pady=5)
logo1 = PhotoImage(file=r'superman.gif')
Label(aanmelden, image=logo1,).pack()
Label(aanmelden, text= "voer gebruikers naam en wachtwoordt in.").pack()
Label(aanmelden, text= 'gebruikersnaam').pack()
Entry(aanmelden).pack()
Label(aanmelden, text= 'wachtwoord').pack()
Entry(aanmelden).pack()
Label(aanmelden, text= 'bevestig wachtwoord').pack()
Entry(aanmelden).pack()

Button(aanmelden, text= "aanmelden", command=lambda:raise_frame(inlog)).pack(pady=10,side='left')
Button(aanmelden, text= "terug", command=lambda:raise_frame(inlog)).pack(pady=10,side='right')

#frame main menu
logo2= PhotoImage(file=r'batman.gif')
Label(mainMenu, image=logo2).pack()

Label(mainMenu, text='the game, you lost').pack()
Button(mainMenu, text='start game', command=lambda:raise_frame(game)).pack()
Button(mainMenu, text='highscore', command=lambda:raise_frame(highscores)).pack()
Button(mainMenu, text='uitloggen', command=lambda:raise_frame(inlog)).pack()
Button(mainMenu, text='exit', command=lambda:sys.exit()).pack()

#frame game
Label(game, text='FRAME 3').pack()
Button(game, text='Go to frame 4', command=lambda:raise_frame(highscores)).pack()

#frame highscores
Label(highscores, text='FRAME 4').pack()
Button(highscores, text='Go to to frame 1', command=lambda:raise_frame(inlog)).pack()

raise_frame(inlog)
root.mainloop()
