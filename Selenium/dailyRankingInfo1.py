'''
오늘의 랭킹 데이터를 불러와 출력
'''
from datetime import datetime

today = datetime.now()
today = today.strftime("%Y%m%d")

ranking = []

with open("C:/Users/yicha/Desktop/app_rank/"+today+".tsv", "r", encoding="UTF-8") as file:
    file.readline()

    while True:
        line = file.readline()
        if line == "":
            break

        line = line.split("\t")
        ranking.append(line[1])

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
        print("{}. {}".format(i+1, ranking[i]))

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

