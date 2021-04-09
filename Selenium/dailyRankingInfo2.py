'''
어제, 오늘의 랭킹 데이터를 불러와
오늘의 랭킹 데이터를 출력할 때
어제 보다 몇 단계 올랐는지 함께 출력해주는 프로그램
'''
from datetime import datetime
from datetime import timedelta
import argparse

today = datetime.now()
today = today.strftime("%Y%m%d")

parser = argparse.ArgumentParser()
parser.add_argument("--date", type=str, default=today)

args = parser.parse_args()
today = args.date

todayRanking = []
prevRanking = []

with open("C:/Users/yicha/Desktop/app_rank/"+today+".tsv", "r", encoding="UTF-8") as file:
    file.readline()

    while True:
        line = file.readline()
        if line == "":
            break

        line = line.split("\t")
        todayRanking.append(line[1])

year = int(today[0:4])
month = int(today[4:6])
day = int(today[6:])
today = datetime(year, month, day)

yesterday = today - timedelta(days=1)
yesterday = yesterday.strftime("%Y%m%d")
with open("C:/Users/yicha/Desktop/app_rank/"+yesterday+".tsv", "r", encoding="UTF-8") as file:
    file.readline()

    while True:
        line = file.readline()
        if line == "":
            break

        line = line.split("\t")
        prevRanking.append(line[1])

print("===== [ 사용방법 ] =====")
print("특정 월의 일별 랭킹을 보고 싶다면")
print("프로그램 실행 시 첫 번째 옵션으로")
print("%Y%m%d 형식의 날짜를 입력하세요.")
print("----- -----")
print("메뉴는 번호로 입력을 하고")
print("Enter키를 누르면 해당 메뉴가 실행됩니다.")
print("===== " * 4)

start = 0
end = 20

while True:
    for i in range(start, end):
        thisRank = i + 1
        prevRank = 0
        for j in range(0, len(prevRanking)):
            if todayRanking[i] == prevRanking[j]:
                prevRank = j+1
                break

        if prevRank == 0:
            diff = "new"
        else:
            diff = thisRank - prevRank

            if diff == 0:
                diff = "-"
            elif diff < 0:
                diff = "▲ " + str(abs(diff))
            else:
                diff = "▼ " + str(abs(diff))

        print("{}. ({}){}".format(thisRank, diff, todayRanking[i]))

    if start == 0:
        print("[ 1. 다음 순위 ({}위 ~ {}위) ]".format(start + 21, end + 20))
        print("[ 2. 종료 ]")
    elif start >= 20 and end < 200:
        print("[ 1. 다음 순위 ({}위 ~ {}위) ]".format(start+21, end+20))
        print("[ 2. 이전 순위 ({}위 ~ {}위) ]".format(start-19, end-20))
        print("[ 3. 종료 ]")
    elif end >= 200:
        print("[ 1. 이전 순위 ({}위 ~ {}위) ]".format(start-19, end-20))
        print("[ 2. 종료 ]")

    menu = int(input())
    if menu == 1:
        if end == 200:
            start = start - 20
            end = end - 20
        else:
            start = start + 20
            end = end + 20
    elif menu == 2:
        if start == 0 or end == 200:
            print("프로그램을 종료합니다.")
            break
        else:
            start = start - 20
            end = end - 20
    else:
        print("프로그램을 종료합니다.")
        break



