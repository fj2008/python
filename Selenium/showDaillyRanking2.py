from datetime import datetime
from datetime import timedelta
import argparse

today = datetime.now()
today = today.strftime("%Y%m%d")
#argqarse 모듈을 사용해서 프로그램실행시 전달하는 값(argument) 를 전달받을 수 있음
parser = argparse.ArgumentParser()
#첫번째 매개변수 = argument의 이름
#두번째 매개변수 = argument의 타입
#세번째 매개변수 = argument의 기본값
parser.add_argument("--date", type=str, default=today)

args = parser.parse_args()
today = args.date

todayRanking = []
prevRanking = []


with open("C:/Users/ITPS/Desktop/app_rank/"+today+".tsv","r",encoding="UTF-8") as file:
    file.readline()

    while True :
        line = file.readline()
        if line == "":
            break

        line = line.split("\t")
        todayRanking.append(line[0])
#어제의 날짜를 계산
#문자열인 today변수를 datetiime 객체로 변환
# 2021.04.08
year = int(today[0:4])
month = int(today[4:6])
day = int(today[6:])
today = datetime(year,month,day)

yesterday = today - timedelta(days=1)
yesterday = yesterday.strftime("%Y%m%d")

#어제의 랭킹 데이터 파일을 열어
with open("C:/Users/ITPS/Desktop/app_rank/"+yesterday+".tsv","r",encoding="UTF-8") as file:
    file.readline()

    while True :
        line = file.readline()
        if line == "":
            break

        line = line.split("\t")
        prevRanking.append(line[0])
#어제의 랭킹을 저장


start = 0
end = 20

while True :
    #i =>todayRanking에서 n번째
    for i in range(start,end):
        #todayRanking에서 n번째 앱의 순위
        thisRank = i + 1
        #todayRanking에서 n번째 앰의 어제 순위
        prevRanking = 0
        #j =>현재(n번째)앱의 어제 순위를 찾아 저장
        for j in range(0,len(prevRanking)):
            if todayRanking[i] == prevRanking[j]:
                prevRank = j+1
                break
        #현재앰의 어제 랭킹이 없었다면은
        if prevRank ==0:
            diff = "new"
        else :
        #현재앱의 어제 랭킹이 있었다면
            diff = thisRank-prevRank

        if diff ==0:
            diff = "-"

        elif diff <0:
            diff = "▲" +str(abs(diff))#abs는 절댓값을 취하는것
        elif diff >0:
            diff ="▼" + str(abs(diff))



        print("{},({}){}".format(thisRank, diff, todayRanking[i]))

    if start == 0 :
        print("[ 1. 다음 순위 ({}위~{}위)]".format(start+21,end+20))
        print("[ 2. 종료 ]")
    elif start >= 20 and end < 200:
        print("[ 1. 다음 순위 ({}위~{}위)]".format(start+21,end+20))
        print("[ 2. 이전 순위 ({}위~{}위)]".format(start-19,end-20))
        print("[ 3. 종료 ]")
    elif end >= 200 :
        print("[ 1. 이전 순위 ({}위~{}위)]".format(start-19,end-20))
        print("[ 2. 종료 ]")


    menu = int(input())
    if menu == 1:
        if end == 200:
            start = start -20
            end = end-10

            start = start+ 20
            end = end + 20
        else :
            start =start+20
            end =end + 20
    elif menu == 2:
        if start ==0:
            print("프로그램을 종료합니다.")
            break
        else:
            start = start-20
            end = end - 20
    else :
        if 20 <= start and start <=160:
            break
        else:
            print("존재하지 않는 메뉴입니다.")