import csv
import datetime
import math

def newHighScore():
        score = input("punten: ")
        naam = input("naam: ")
        localtime = datetime.date.today()

        with open("highscore.csv", "a", newline='') as meCSVFile:
                writer = csv.writer(meCSVFile, delimiter=";")
                writer.writerow((localtime, naam, score))

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

        #print(str(highScoreList))
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
        print(str(finalList))

def highScoresPointsTime():

        highScoreListTime = []
        pointsListTime = []
        finalListTime = []

        with open("highscore.csv", "r") as myCSVFile:
            reader = csv.reader(myCSVFile, delimiter=";")
            for row in reader:
                for field in row:
                    highScoreListTime.append(field)
            myCSVFile.close()

        print(str(highScoreListTime))
        tellerHigh = 3

        while tellerHigh < len(highScoreListTime):
            math.ceil(highScoreListTime[tellerHigh]*100)/100
            pointsListTime.append(highScoreListTime[tellerHigh])
            tellerHigh += 4
        pointsListTime.sort(key=int, reverse=True)

        print(str(pointsListTime))
        sortingTeller = 0

        while sortingTeller < len(pointsListTime):
            sortingteller2 = highScoreListTime.index(pointsListTime[sortingTeller])
            sortingteller3 = highScoreListTime.index(pointsListTime[sortingTeller]) - 1
            sortingteller4 = highScoreListTime.index(pointsListTime[sortingTeller]) - 2
            sortingteller5 = highScoreListTime.index(pointsListTime[sortingTeller]) - 3
            finalListTime.append(highScoreListTime[sortingteller4])
            finalListTime.append(highScoreListTime[sortingteller3])
            finalListTime.append(highScoreListTime[sortingteller2])
            finalListTime.append(highScoreListTime[sortingteller5])
            highScoreListTime.remove(highScoreListTime[sortingteller5])
            highScoreListTime.remove(highScoreListTime[sortingteller5])
            highScoreListTime.remove(highScoreListTime[sortingteller5])
            highScoreListTime.remove(highScoreListTime[sortingteller5])
            sortingTeller += 1

        print(str(finalListTime))

        finalTeller = 0
        finalTeller2 = 1
        finalTeller3 = 2
        finalTeller4 = 3

        with open("highscore.csv", "w") as iCSVFile:
                writer = csv.writer(iCSVFile, delimiter=";")
                while finalTeller < len(finalListTime):
                    writer.writerow((finalListTime[finalTeller], finalListTime[finalTeller2], finalListTime[finalTeller3], finalListTime[finalTeller4]))
                    finalTeller += 4
                    finalTeller2 += 4
                    finalTeller3 += 4
                    finalTeller4 += 4
done = False
while not done:
    print("1. voeg nieuwe score toe")
    print("2. sorteer scores")
    print("3. quit")
    keuze = input("keuze: ")

    if keuze == '1':
        newHighScore()
    elif keuze == '2':
        highScoresPoints()
    elif keuze == '3':
        done = True
