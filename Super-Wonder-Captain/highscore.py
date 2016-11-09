import csv

def newHighScore():
        score = raw_input("punten: ")
        naam = raw_input("naam: ")

        with open("highscore.csv", "a") as meCSVFile:
                writer = csv.writer(meCSVFile, delimiter=";")
                writer.writerow((naam, score))

def highScoresPoints():

        highScoreList = []
        pointsList = []
        finalList = []

        with open("highscore.csv", "r") as myCSVFile:
            reader = csv.reader(myCSVFile, delimiter=";")
            for row in reader:
                for field in row:
                    highScoreList.append(field)
            myCSVFile.close()

        print(str(highScoreList))
        tellerHigh = 1

        while tellerHigh < len(highScoreList):
            pointsList.append(highScoreList[tellerHigh])
            tellerHigh += 2
        pointsList.sort(key=int, reverse=True)

        print(str(pointsList))
        sortingTeller = 0

        while sortingTeller < len(pointsList):
            sortingteller2 = highScoreList.index(pointsList[sortingTeller])
            sortingteller3 = highScoreList.index(pointsList[sortingTeller]) - 1
            finalList.append(highScoreList[sortingteller3])
            finalList.append(highScoreList[sortingteller2])
            sortingTeller += 1

        print(str(finalList))

        finalTeller = 0
        finalTeller2 = 1

        with open("highscore.csv", "w") as iCSVFile:
                writer = csv.writer(iCSVFile, delimiter=";")
                while finalTeller < len(finalList):
                    writer.writerow((finalList[finalTeller], finalList[finalTeller2]))
                    finalTeller += 2
                    finalTeller2 += 2

while True:
    print("1. newhighscore")
    print("2. nieuwe gebruiker")
    print("3. quit")
    keuze = input("keuze: ")

    if keuze == 1:
        newHighScore()
    elif keuze == 2:
        highScoresPoints()
    elif keuze == 3:
        break
