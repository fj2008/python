'''
두 앱의 특정 월의 랭킹 비교 (막대그래프)
'''
from datetime import datetime
import argparse
import calendar
import matplotlib.pyplot as plt

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]

def makeRanking(name, start, end):
    ranking = []

    for i in range(start, end + 1):
        day = str(i)
        if len(day) == 1:
            day = "0" + day

        today = year + month + day
        rank = 0

        try:
            with open("C:/Users/yicha/Desktop/app_rank/" + today + ".tsv", "r", encoding="UTF-8") as file:
                file.readline()

                while True:
                    line = file.readline()
                    if line == "":
                        break

                    line = line.split("\t")
                    rank = rank + 1

                    if line[1].find(name) >= 0:
                        ranking.append(rank)
                        break

            if len(ranking) != i:
                ranking.append(0)
        except FileNotFoundError:
            ranking.append(0)

    return ranking

today = datetime.now()
today = today.strftime("%Y%m")

parser = argparse.ArgumentParser()
parser.add_argument("--name1", type=str, default=None)
parser.add_argument("--name2", type=str, default=None)
parser.add_argument("--date", type=str, default=today)

args = parser.parse_args()
name1 = args.name1
name2 = args.name2
today = args.date

year = int(today[0:4])
month = int(today[4:])
monthrange = calendar.monthrange(year, month)

year = str(year)
month = str(month)
if len(month) == 1:
    month = "0" + month

start = 1
end = monthrange[1]

name1Ranking = makeRanking(name1, start, end)
name2Ranking = makeRanking(name2, start, end)

dayList = []
for i in range(start, end+1):
    dayList.append(i)

plt.rc('font', family='NanumGothic')
plt.xlabel("날짜")
plt.ylabel("순위")
plt.axis([start, end, 0, 200])
plt.title(name1 + "    |    " + name2)

value_a_x = create_x(2, 0.8, 1, len(name1Ranking))
value_b_x = create_x(2, 0.8, 2, len(name1Ranking))

ax = plt.subplot()
ax.bar(value_a_x, name1Ranking)
ax.bar(value_b_x, name2Ranking)

middle_x = [(a+b)/2 for (a, b) in zip(value_a_x, value_b_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(dayList)

plt.show()

