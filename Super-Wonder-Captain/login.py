import csv

with open("login.csv", "w") as iCSVFile:
                writer = csv.writer(iCSVFile, delimiter=";")

def nieuwe_gebruiker():

    list = []

    with open("login.csv", "r") as myCSVFile:
        reader = csv.reader(myCSVFile, delimiter=";")
        for row in reader:
            for field in row:
                list.append(field)
        myCSVFile.close()

        naam = input("wat voor gebruikersnaam wilt u: ")
        wachtwoord = input("wat voor wachtwoord wilt u: ")

        if naam in list:
            print("deze naam is al in gebruik")

        else:
            with open("login.csv", "a", newline="") as meCSVFile:
                writer = csv.writer(meCSVFile, delimiter=";")
                writer.writerow((naam, wachtwoord))

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

    print(str(list))
    teller = 0
    teller2 = 1

    while teller2 < len(list):
        wachtwoordList.append(list[teller2])
        naamList.append(list[teller])
        teller += 2
        print(str(wachtwoordList))
        teller2 += 2
        print(str(naamList))
    naam = input("wat is de gebruikersnaam: ")
    wachtwoord = input("wat is het wachtwoord: ")

    if wachtwoord in wachtwoordList and naam in naamList:
        teller = wachtwoordList.index(wachtwoord)
        if teller == naamList.index(naam):
            print("Uw bent ingelogt")

        else:
            print("Het wachtwoord of de gebruikersnaam is fout2")

    else:
        print("het wachtwoord of de gebruiksnaam is fout")

while True:
    print("1. inloggen")
    print("2. nieuwe gebruiker")
    print("3. quit")
    keuze = input("")

    if keuze == "2":
        nieuwe_gebruiker()
    elif keuze == "1":
        inloggen()
    elif keuze == "3":
        break
