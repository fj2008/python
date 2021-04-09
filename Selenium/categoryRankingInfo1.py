from datetime import datetime
import argparse

today = datetime.now()
today = today.strftime("%Y%m%d")

parser = argparse.ArgumentParser()
parser.add_argument("--date", type=str, default=today)

args = parser.parse_args()
today = args.date

todayCategory = {}

with open("C:/Users/yicha/Desktop/app_rank/"+today+".tsv", "r", encoding="UTF-8") as file:
    file.readline()

    rank = 0

    while True:
        rank = rank + 1

        line = file.readline()
        if line == "":
            break

        line = line.split("\t")

        appId = line[0]
        appName = line[1]
        category = line[5]
        categoryElement = {"rank": rank, "id": appId, "name": appName}

        categoryList = todayCategory.get(category)
        if categoryList is None:
            categoryList = []

        categoryList.append(categoryElement)

        todayCategory[category] = categoryList

keys = todayCategory.keys()
for key in keys:
    print("===== [ " + key + " ] =====")

    values = todayCategory[key]
    for value in values:
        print("\t"+str(value))

    print()




