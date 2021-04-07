ranking = []

with open("C:/Users/ITPS/Desktop/app_rank/20210407.tsv","r",encoding="UTF-8") as file:
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

    print("[ 1. 다음 순위 ]")
    print("[ 2. 이전 순위 ]")
    print("[ 3. 종료 ]")

    menu = int(input())
    if menu == 1:
        start = start+ 20
        end = end + 20
        if start > 200  :
            print("다음순위 없음")
            start = start -20
            end = end-20

    elif menu == 2:
        start = start-20
        end = end - 20
        if start < 0 :
            print("이전 순위가 없습니다")
            start = start+20
            end = end+20

    else :
               break