from tkinter import *
from tkinter.messagebox import showinfo
import csv
import time
import random

def raise_frame(frame):
    frame.tkraise()

# de functie voor het inloggen
def inloggen():

    list = []
    wachtwoordList = []
    naamList = []

    with open("login.csv", "r") as myCSVFile:
        reader = csv.reader(myCSVFile, delimiter=";")
        for row in reader:
            for field in row:
                list.append(field)
        myCSVFile.close()

    teller = 0
    teller2 = 1

    while teller2 < len(list):
        wachtwoordList.append(list[teller2])
        naamList.append(list[teller])
        teller += 2
        teller2 += 2

    naam = gebruikersnaam.get()
    wachtwoord = wachtwd.get()

    if wachtwoord in wachtwoordList and naam in naamList:
        teller = naamList.index(naam)
        if wachtwoord == wachtwoordList[teller]:
            raise_frame(mainMenu)

        else:
            print("Het wachtwoord of de gebruikersnaam is fout2")

    else:
        print("het wachtwoord of de gebruiksnaam is fout")

# de functie voor het aanmaken van een nieuwe gebruiker/speler
def nieuwUser():
    list = []

    with open("login.csv", "r") as myCSVFile:
        reader = csv.reader(myCSVFile, delimiter=";")
        for row in reader:
            for field in row:
                list.append(field)
        myCSVFile.close()


        if len(nWachtwrd.get()) ==0 or len(cWachtwrd.get()) ==0:
            showinfo(title='attentie!', message='vul bijde wachtwoorden in!')
        else:
            if nWachtwrd.get() == cWachtwrd.get():
                while True:
                    naam = nGebruiksnaam.get()
                    wachtwoord = ''

                    if naam in list:
                        showinfo(title='attentie!', message='uw gekozen naam is al gekozen, kiest u alstublieft een andere.')
                        break

                    else:
                        wachtwoord = nWachtwrd.get()
                        with open("login.csv", "a") as meCSVFile:
                            writer = csv.writer(meCSVFile, delimiter=";")
                            writer.writerow((naam, wachtwoord))
                            raise_frame(inlog)
                        break


# de knop om de hoghscore lijst van "score" naar "Tijd" te veranderen
def highscoretoggle():
    global test_text
    test_text ='testtest'
    raise_frame(highscores)
    return


# functie voor het toevoegen van een nieuwe score
def newHighScore():
        score = random.randint(0,25)
        naam = gebruikersnaam.get()
        localtime = time.asctime( time.localtime(time.time()) )

        with open("highscore.csv", "a") as meCSVFile:
                writer = csv.writer(meCSVFile, delimiter=";")
                writer.writerow((localtime, naam, score))





# main code en opbouw van de GUI
root = Tk()

inlog = Frame(root)
aanmelden = Frame(root)
mainMenu = Frame(root)
game = Frame(root)
highscores = Frame(root)


for frame in (inlog,aanmelden, mainMenu, game, highscores):
    frame.grid(row=0, column=0, sticky='news')

# frame inlog
Label(inlog, text='Super-Wonder-Captain', font='bold 20').pack(pady=5)
logo = PhotoImage(file=r'superman.gif')
Label(inlog, image=logo,).pack()
Label(inlog, text='click op de knop om de game te starten').pack(pady=10)

gebruikersnaam = Entry(inlog)                                                                                               # invoeren gebruikersnaam
wachtwd = Entry(inlog)                                                                                                      # invoeren wachtwoord
gebruikersnaam.pack()                                                                                                       # het realisieren van de entrybox in de gui
wachtwd.pack()                                                                                                              # het realiseren van de entrybox wachtwoord in de gui
Button(inlog, text='login',command=lambda:inloggen()).pack(pady=10)                                                         # toevoegen van de button "login" en de verwijzing naar de functie inloggen()
Button(inlog, text= "aanmelden", command=lambda:raise_frame(aanmelden)).pack(pady=10)                                       # toevoegen van de button "aanmelden" met commando om het volgende scherm aanmelden op te roepen


#frame aanmelden
Label(aanmelden, text='super-woman-Captain', font='bold 20').pack(pady=5)
logo1 = PhotoImage(file=r'superman.gif')
Label(aanmelden, image=logo1,).pack()
Label(aanmelden, text= "voer gebruikers naam en wachtwoordt in.").pack()
Label(aanmelden, text= 'gebruikersnaam').pack()
nGebruiksnaam = Entry(aanmelden)
nGebruiksnaam.pack()
Label(aanmelden, text= 'wachtwoord').pack()
nWachtwrd = Entry(aanmelden)
nWachtwrd.pack()
Label(aanmelden, text= 'bevestig wachtwoord').pack()
cWachtwrd = Entry(aanmelden)
cWachtwrd.pack()

Button(aanmelden, text= "aanmelden", command=lambda:nieuwUser()).pack(pady=10)
Button(aanmelden, text= "terug", command=lambda:raise_frame(inlog)).pack(pady=10)

#frame main menu
logo2= PhotoImage(file=r'batman.gif')
Label(mainMenu, image=logo2).pack()
Label(mainMenu, text='the game, you lost').pack()
Button(mainMenu, text='start game', command=lambda:raise_frame(game)).pack()
Button(mainMenu, text='highscore', command=lambda:raise_frame(highscores)).pack()
Button(mainMenu, text='uitloggen', command=lambda:raise_frame(inlog)).pack()
Button(mainMenu, text='exit', command=lambda:sys.exit()).pack()

#frame game
Label(game, text='gues the people', font='bold 20').pack(pady= 5)
Button(game, text='submit', command=lambda:raise_frame(mainMenu)).pack()
Button(game, text='test knop highscore toevoegen (submit)', command=lambda:newHighScore()).pack()

#frame highscores
highscoresB1 = Button(highscores, text='switch test ding', command=lambda:highscoretoggle()).pack(pady=10)
highscoreL1 = Label(highscores, text='hier komen de highscores').pack(pady=10)
highscoresB2 = Button(highscores, text='Go to to frame 1', command=lambda:raise_frame(mainMenu)).pack(pady=10)

raise_frame(inlog)
root.mainloop()
