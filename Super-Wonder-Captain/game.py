from tkinter import *
from tkinter.messagebox import showinfo
import csv
import time
import random
import json
import winsound
from marvel_heroes_xml import create_marvel_xml

def raise_frame(frame):
    frame.tkraise()

def start_game():
    raise_frame(game)
    setup_game()

def setup_game():
    global held_naam
    global comics_lijst
    global stories_lijst
    global series_lijst
    global events_lijst
    global hidden_naam
    global hint_counter
    global score
    global start_tijd
    score = 25
    hint_counter = 0
    label_hint.config(text='')
    label_score.config(text=str(score))
    start_tijd = time.time()

    #create_marvel_xml()
    with open('marvel.json') as marvelJSONfile:
        filestr = marvelJSONfile.read()
        filedict = json.loads(filestr)
        held_naam = filedict['data']['results'][0]['name']
        comics_lijst = [i['name'] for i in filedict['data']['results'][0]['comics']['items']]
        stories_lijst = [i['name'] for i in filedict['data']['results'][0]['stories']['items']]
        series_lijst = [i['name'] for i in filedict['data']['results'][0]['series']['items']]
        events_lijst = [i['name'] for i in filedict['data']['results'][0]['events']['items']]

    hidden_naam = ''
    for i in held_naam:
        if i not in ' ':
            hidden_naam += '*'
        else:
            hidden_naam += ' '
    label_held.config(text=hidden_naam)

def invoer():
    global start_tijd
    global eind_tijd
    eind_tijd = time.time() - start_tijd
    newHighScore()



# de knop om een hint te laten zien
def show_hint():
    global hint_counter
    global held_naam
    global hidden_naam
    global score

    hint_counter += 1

    if hint_counter == 1:
        hintt = 'Held komt voor in deze comics: '
        for i in comics_lijst:
            hintt += i + '\n'
        label_hint.config(text=hintt)
        score -= 1
    elif hint_counter == 2:
        hintt = 'Held komt voor in deze stories: '
        for i in stories_lijst:
            hintt += i + '\n'
        label_hint.config(text=hintt)
        score -= 1
    elif hint_counter == 3:
        hintt = 'Held komt voor in deze series: '
        for i in series_lijst:
            hintt += i + '\n'
        label_hint.config(text=hintt)
        score -= 1
    elif hint_counter == 4:
        hintt = 'Held komt voor in deze events: '
        for i in events_lijst:
            hintt += i + '\n'
        label_hint.config(text=hintt)
        score -= 1
    elif hint_counter > 4 and ((hint_counter-4) < (len(held_naam) + 1)):
        word_counter = hint_counter - 4
        if hidden_naam[word_counter - 1] == ' ':
            word_counter += 1
            hint_counter += 1
        hidden_naam = held_naam[:word_counter] + hidden_naam[word_counter:]
        label_held.config(text=hidden_naam)
        score -= 2

    label_score.config(text='Score: ' + str(score))

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
            showinfo(title='ATTENTIE!', message='u heeft een foute gebruikersnaam of wachtwoord ingevuldt.')
    elif len(wachtwoord) == 0:
        showinfo(title='ATTENTIE!', message='vul een wachtwoordt in!')

    else:
        showinfo(title='ATTENTIE!', message='uw gebruikersnaam bestaat niet')

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

                    if ' ' in naam and len(naam) == 0:
                        showinfo(title='ATTENTIE!', message='spaties zijn niet toegestaan in uw gebruikersnaam!')
                        break

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

# de knop om de highscore lijst te printen
def highscoreframe():


    hidden_naam = ''
    for i in held_naam:
        if i not in ' ':
            hidden_naam += '*'
        else:
            hidden_naam += ' '
    label_held.config(text=hidden_naam)

# functie voor het toevoegen van een nieuwe score
def newHighScore():
        global score
        global eind_tijd
        naam = gebruikersnaam.get()
        localtime = time.asctime( time.localtime(time.time()) )

        with open("highscore.csv", "a") as meCSVFile:
                writer = csv.writer(meCSVFile, delimiter=";")
                writer.writerow((localtime, naam, score, eind_tijd))





# main code en opbouw van de GUI
root = Tk()

inlog = Frame(root)
aanmelden = Frame(root)
mainMenu = Frame(root)
game = Frame(root)
highscores = Frame(root)


for frame in (inlog,aanmelden, mainMenu, game, highscores):
    frame.grid(row=0, column=0, sticky='news')

# aanmaken van de variablen voor de GUI inlogscherm
titel =Label(inlog, text='Super-Wonder-Captain', font='bold 20')
logo = PhotoImage(file=r'superman.gif')
inlogPicture = Label(inlog, image=logo)
inlogLabel = Label(inlog, text='click op de knop om de game te starten')
gebruikersnaam = Entry(inlog)
wachtwd = Entry(inlog)                                                                                                                                                                                                            # het realiseren van de entrybox wachtwoord in de gui
inlogButton = Button(inlog, text='login',command=lambda:inloggen())
inlogButton1 = Button(inlog, text= "aanmelden", command=lambda:raise_frame(aanmelden))


# Aanmaken van de GUI inlogscherm
titel.pack(pady=10)
inlogPicture.pack(pady=10)
inlogLabel.pack(pady=10)
gebruikersnaam.pack()
wachtwd.pack()
inlogButton.pack(pady=10)
inlogButton1.pack(pady=10)
winsound.PlaySound('marvelsound.wav',winsound.SND_ASYNC)

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
Button(aanmelden, text= 'exit', command=lambda: sys.exit()).pack()

#frame main menu
logo2= PhotoImage(file=r'batman.gif')
Label(mainMenu, image=logo2).pack()
Label(mainMenu, text='the game, you lost').pack()
Button(mainMenu, text='start game', command=lambda:start_game()).pack()
Button(mainMenu, text='highscore', command=lambda:raise_frame(highscores)).pack()
Button(mainMenu, text='uitloggen', command=lambda:raise_frame(inlog)).pack()
Button(mainMenu, text='exit', command=lambda:sys.exit()).pack()

#frame game
Label(game, text='Raad de held!', font='bold 20').pack(pady= 5)
Button(game, text='submit', command=lambda:raise_frame(mainMenu)).pack()
Button(game, text='test knop highscore toevoegen (submit)', command=lambda:newHighScore()).pack()
Button(game, text='Laat hint zien!', command=lambda:show_hint()).pack()
label_held = Label(game, text='', font='bold 20')
label_hint = Label(game, text='')
label_score = Label(game, text='Score: 25')
entry_held = Entry(game)
label_score.pack(pady=5)
label_held.pack(pady=5)
Button(game, text='Voer held in:', command=lambda:invoer()).pack(pady=5)
entry_held.pack()
label_hint.pack(pady=5)

#frame highscores
highscoresB1 = Button(highscores, text='switch test ding', command=lambda:highscoretoggle()).pack(pady=10)
highscoreL1 = Label(highscores, text='hier komen de highscores').pack(pady=10)
highscoresB2 = Button(highscores, text='Go to to frame 1', command=lambda:raise_frame(mainMenu)).pack(pady=10)

raise_frame(inlog)
root.mainloop()
