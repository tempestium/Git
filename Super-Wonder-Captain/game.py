from tkinter import *
from tkinter.messagebox import showinfo
import csv
import datetime
import time
import json
import winsound
from marvel_heroes_xml import create_marvel_xml

def raise_frame(frame):
    frame.tkraise()

def start_game():
    raise_frame(game)
    setup_game()

def show_highscores():
    raise_frame(highscores)
    highScoresPoints()

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
    global track_minscore

    track_minscore = 0
    entry_held.delete(0, 'end')
    score = 25
    hint_counter = 0
    label_hint.config(text='')
    label_score.config(text=str(score))
    start_tijd = [True, time.time()]

    create_marvel_xml()
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
    global held_naam
    invoer_held = entry_held.get()

    if invoer_held.lower() == held_naam.lower():
        eind_tijd = time.time() - start_tijd[1]
        start_tijd[0] = False
        newHighScore()
        showinfo('Attentie!', 'Gefeliciteerd, het is goed!')
        raise_frame(highscores)
    else:
        showinfo('Attentie!', 'Dit is niet het juiste antwoord!')



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
            showinfo(title='ATTENTIE!', message='u heeft een fout wachtwoord ingevuldt.')
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

# functie voor het toevoegen van een nieuwe score
def newHighScore():
        global score
        global eind_tijd
        naam = gebruikersnaam.get()
        localtime = datetime.date.today()

        with open("highscore.csv", "a", newline='') as meCSVFile:
                writer = csv.writer(meCSVFile, delimiter=";")
                writer.writerow((localtime, naam, score, eind_tijd))

# functie om highscore op punten te sorteren
def highScoresPoints():

        highScoreList = []
        pointsList = []
        finalList = []

        with open("highscore.csv", "r") as myCSVFile:
            reader = csv.reader(myCSVFile, delimiter=";")
            for row in reader:
                field_nr = 0
                for field in row:
                    field_nr += 1
                    if field_nr == 1:
                        data = field.split('-')
                        date = datetime.date(int(data[0]), int(data[1]), int(data[2]))
                        delta_date = datetime.date.today() - date
                        highScoreList.append(delta_date.days)
                    else:
                        highScoreList.append(field)
            myCSVFile.close()

        tellerHigh = 2

        while tellerHigh < len(highScoreList):
            pointsList.append(highScoreList[tellerHigh])
            tellerHigh += 4
        pointsList.sort(key=int, reverse=True)

        sortingTeller = 0

        while sortingTeller < len(pointsList):
            sortingteller2 = highScoreList.index(pointsList[sortingTeller])
            sortingteller3 = highScoreList.index(pointsList[sortingTeller]) - 1
            sortingteller4 = highScoreList.index(pointsList[sortingTeller]) - 2
            sortingteller5 = highScoreList.index(pointsList[sortingTeller]) + 1
            finalList.append(highScoreList[sortingteller4])
            finalList.append(highScoreList[sortingteller3])
            finalList.append(highScoreList[sortingteller2])
            finalList.append(highScoreList[sortingteller5])
            highScoreList.remove(highScoreList[sortingteller4])
            highScoreList.remove(highScoreList[sortingteller4])
            highScoreList.remove(highScoreList[sortingteller4])
            highScoreList.remove(highScoreList[sortingteller4])
            sortingTeller += 1

        sortingTeller = 0
        highscorestring = ''
        for i in finalList:
            if sortingTeller == 0:
                highscorestring += 'Dagen geleden: ' + str(i) + ', '
            elif sortingTeller == 1:
                highscorestring += 'Naam: ' + str(i) + ', '
            elif sortingTeller == 2:
                highscorestring += 'score: ' + str(i) + ', '
            elif sortingTeller == 3:
                highscorestring += 'tijd: ' + str(round(float(i), 2)) + '\n'
                sortingTeller = -1
            sortingTeller += 1

        highscoreL1.config(text=highscorestring)

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

# aanmaken van de variablen voor de GUI inlogscherm
titel =Label(inlog, text='Super-Wonder-Captain', font='bold 20')
logo = PhotoImage(file=r'superman.gif')
inlogPicture = Label(inlog, image=logo)
inlogLabel = Label(inlog, text='click op de knop om de game te starten')
gebruikersnaam = Entry(inlog)
wachtwd = Entry(inlog,show= '*')                                                                                                                                                                                                            # het realiseren van de entrybox wachtwoord in de gui
inlogButton = Button(inlog, text='login',command=lambda:inloggen())
inlogButton1 = Button(inlog, text= "aanmelden", command=lambda:raise_frame(aanmelden))
inlogButton3 = Button(inlog, text='Exit', command=lambda:sys.exit())

# Aanmaken van de GUI inlogscherm
titel.pack(pady=10)
inlogPicture.pack(pady=10)
inlogLabel.pack(pady=10)
gebruikersnaam.pack()
wachtwd.pack()
inlogButton.pack(pady=10)
inlogButton1.pack(pady=10)
inlogButton3.pack()
winsound.PlaySound('marvelsound.wav',winsound.SND_ASYNC)

#frame aanmelden

#Aanmaken van de variablen
aanmeldLabelTitle = Label(aanmelden, text='super-woman-Captain', font='bold 20')
logo1 = PhotoImage(file=r'ironman.gif')
aanmeldPicture = Label(aanmelden, image=logo1,)
aanmeldLabel1 = Label(aanmelden, text= "voer gebruikers naam en wachtwoordt in.")
aanmeldLabel2 = Label(aanmelden, text= 'gebruikersnaam')
nGebruiksnaam = Entry(aanmelden)
aanmeldLabel3 = Label(aanmelden, text= 'wachtwoord')
nWachtwrd = Entry(aanmelden)
aanmeldLabel4 = Label(aanmelden, text= 'bevestig wachtwoord')
cWachtwrd = Entry(aanmelden)
aanmeldButton = Button(aanmelden, text= "aanmelden", command=lambda:nieuwUser())
aanmeldButton1 = Button(aanmelden, text= "terug", command=lambda:raise_frame(inlog))


#maken van de GUI
aanmeldLabelTitle.pack(pady=5)
aanmeldPicture.pack()
aanmeldLabel1.pack()
aanmeldLabel2.pack(pady=5)
nGebruiksnaam.pack()
aanmeldLabel3.pack()
nWachtwrd.pack()
aanmeldLabel4.pack()
cWachtwrd.pack()
aanmeldButton.pack(pady=5)
aanmeldButton1.pack(pady=5)


#frame main menu

# aanamken variabelen
logo2= PhotoImage(file=r'batman.gif')
mmLabel = Label(mainMenu, image=logo2)
mmLabel1 = Label(mainMenu, text='the game, you lost')
mmButton = Button(mainMenu, text='start game', command=lambda:start_game())
mmButton2 = Button(mainMenu, text='highscore', command=lambda:raise_frame(highscores))
mmButton3 = Button(mainMenu, text='uitloggen', command=lambda:raise_frame(inlog))
mmButton4 = Button(mainMenu, text='exit', command=lambda:sys.exit())


# aanmaken GUI Main Menu
mmLabel.pack()
mmLabel1.pack()
mmButton.pack()
mmButton2.pack()
mmButton3.pack()
mmButton4.pack()


#frame game

#variableren aanmaken

gLabel = Label(game, text='Raad de held!', font='bold 20')
gButton = Button(game, text='terug naar main menu', command=lambda:raise_frame(mainMenu))
gButton1 = Button(game, text='Laat hint zien!', command=lambda:show_hint())
label_held = Label(game, text='', font='bold 20')
label_hint = Label(game, text='')
label_score = Label(game, text='Score: 25')
entry_held = Entry(game)
gButton3 = Button(game, text='Voer held in:', command=lambda:invoer())

#het maken van de GUI
gLabel.pack(pady=5)
label_score.pack(pady=5)
label_held.pack(pady=5)
gButton3.pack()
entry_held.pack(pady=10)
gButton1.pack()
label_hint.pack(pady=5)
gButton.pack()


#frame highscores
highscoreL1 = Label(highscores, text='hier komen de highscores')
highscoreL1.pack(pady=10)
highscoresB2 = Button(highscores, text='Ga terug naar menu', command=lambda:raise_frame(mainMenu)).pack(pady=10)

raise_frame(inlog)
root.mainloop()
