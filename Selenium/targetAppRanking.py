from datetime import  datetime
import argparse
import  calendar
import matplotlib.pyplot as plt

today = datetime.now()
today = today.strftime("%Y%m")

parser = argparse.ArgumentParser()
parser.add_argument("--name", type = str, default= None)
parser.add_argument("--date", type = str, default= today)

args = parser.parse_args()
name = args.name
today = args.date
#name 앱의 일별 순위
ranking  = []

year = int(today[0:4])
month = int(today[4:])
#해당 년 월의1일부터 마지막날까지의 날짜를 구해짐 range
monthrange = calendar.monthrange(year,month)

year = str(year)
month = str(month)
if len(month) == 1 :
    month = "0" + month

start = 1#해당월의 첫째날
end = monthrange[1]#해당 달의 마지막날짜


for i in range(start,end+1):
    day = str(i)
    if len(day) == 1:
        day = "0" + day

    today = year + month + day
    rank = 0

    try :
        with open("C:/Users/ITPS/Desktop/app_rank/"+today+".tsv","r",encoding="UTF-8") as file:
            file.readline()

            while True:
                line = file.readline()
                if line == "":
                    break

                line = line.split("\t")
                rank = rank+1

                if line[0].find(name) != 0: #find를 매개변수로 전달하면 매개변수와 일치하는 값을찾아줌

                    ranking.append(rank)
                    break


        if len(ranking) != i:
            ranking.append(0)
    except FileNotFoundError:
        ranking.append(0)

dayList = []
for i in range(start,end+1):
    dayList.append(i)

plt.plot(dayList,ranking)
plt.xlabel("date")
plt.ylabel("rank")
plt.axis([start,end,0,200])
plt.show()