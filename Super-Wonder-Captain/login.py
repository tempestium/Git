import csv

def nieuwe_gebruiker():

    list = []

    with open("login.csv", "r") as myCSVFile:
        reader = csv.reader(myCSVFile, delimiter=";")
        for row in reader:
            for field in row:
                list.append(field)
        myCSVFile.close()

        while True:
            naam = raw_input("wat voor gebruikersnaam wilt u: ")

            if naam in list:
                print("deze naam is al in gebruik")

            else:
                wachtwoord = raw_input("wat voor wachtwoord wilt u: ")
                with open("login.csv", "a") as meCSVFile:
                    writer = csv.writer(meCSVFile, delimiter=";")
                    writer.writerow((naam, wachtwoord))
                    break

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

    naam = raw_input("wat is de gebruikersnaam: ")
    wachtwoord = raw_input("wat is het wachtwoord: ")

    if wachtwoord in wachtwoordList and naam in naamList:
        teller = naamList.index(naam)
        if wachtwoord == wachtwoordList[teller]:
            print("Uw bent ingelogt")

        else:
            print("Het wachtwoord of de gebruikersnaam is fout2")

    else:
        print("het wachtwoord of de gebruiksnaam is fout")

while True:
    print("1. inloggen")
    print("2. nieuwe gebruiker")
    print("3. quit")
    keuze = input("keuze: ")

    if keuze == 2:
        nieuwe_gebruiker()
    elif keuze == 1:
        inloggen()
    elif keuze == 3:
        break

