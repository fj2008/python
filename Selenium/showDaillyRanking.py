from datetime import datetime
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

ranking = []

with open("C:/Users/ITPS/Desktop/app_rank/"+today+".tsv","r",encoding="UTF-8") as file:
    file.readline()

    while True :
        line = file.readline()
        if line == "":
            break

        line = line.split("\t")
        ranking.append(line[0])


start = 0
end = 20

while True :
    for i in range(start,end):
        print("{},{}".format(i+1, ranking[i]))

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