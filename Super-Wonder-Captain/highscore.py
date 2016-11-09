import csv
import time

def newHighScore():
        score = raw_input("punten: ")
        naam = raw_input("naam: ")
        localtime = time.asctime( time.localtime(time.time()) )

        with open("highscore.csv", "a") as meCSVFile:
                writer = csv.writer(meCSVFile, delimiter=";")
                writer.writerow((localtime, naam, score))

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
        tellerHigh = 2

        while tellerHigh < len(highScoreList):
            pointsList.append(highScoreList[tellerHigh])
            tellerHigh += 3
        pointsList.sort(key=int, reverse=True)

        print(str(pointsList))
        sortingTeller = 0

        while sortingTeller < len(pointsList):
            sortingteller2 = highScoreList.index(pointsList[sortingTeller])
            sortingteller3 = highScoreList.index(pointsList[sortingTeller]) - 1
            sortingteller4 = highScoreList.index(pointsList[sortingTeller]) - 2
            finalList.append(highScoreList[sortingteller4])
            finalList.append(highScoreList[sortingteller3])
            finalList.append(highScoreList[sortingteller2])
            sortingTeller += 1

        print(str(finalList))

        finalTeller = 0
        finalTeller2 = 1
        finalTeller3 = 2

        with open("highscore.csv", "w") as iCSVFile:
                writer = csv.writer(iCSVFile, delimiter=";")
                while finalTeller < len(finalList):
                    writer.writerow((finalList[finalTeller], finalList[finalTeller2], finalList[finalTeller3]))
                    finalTeller += 3
                    finalTeller2 += 3
                    finalTeller3 += 3

while True:
    print("1. voeg nieuwe score toe")
    print("2. sorteer scores")
    print("3. quit")
    keuze = input("keuze: ")

    if keuze == 1:
        newHighScore()
    elif keuze == 2:
        highScoresPoints()
    elif keuze == 3:
        break
