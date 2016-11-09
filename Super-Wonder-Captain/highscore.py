import csv

punten = 100
inlog = "hoi"

def newHighScore():
        score = punten
        naam = inlog

        highScoreList = []

        with open("highscore.csv", "r") as myCSVFile:
            reader2 = csv.reader(myCSVFile, delimiter=";")
            for row in reader2:
                for field in row:
                    highScoreList.append(field)
            myCSVFile.close()

        with open("highscore.csv", "a", newline="") as meCSVFile:
            writer = csv.writer(meCSVFile, delimiter=";")
            writer.writerow((score, naam))
