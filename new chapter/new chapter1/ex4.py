'''
스트림  open함수 실습
csv형식
comma-separated values 는 데이터를 쉼표(,)로 구분한 덱스트 데이터이다.,
확장자는.csv이며 MIME형식은 tex/csv이다.
비슷한 포맷으로 탭으로 구분하는'tab-separated values;(TSV)가 있음
파일의 확장자와 실제 파일의 내용과는 무관
'''

with open("C:/Users/ITPS/Desktop/covid.csv","r") as file:
    file.readline()
   #월별 검사 진행자의 수
    add= 0
    #월별 검사 진행자 수
    monthAddList = [-1,0,0,0,0,0,0,0,0,0,0,0,0]


        #split메서드로 ","를 기준으로 분리를시켜라라고 명령함
    while True:
        contents = file.readline()

        if contents == "" :

            break
        dataList = contents.split(",")
        dateInfo = dataList[0].split("-")

        #covid.csv파일의 데이터를 읽어서
        #월별 검사 진행자의 수를 출력하세요.
        year = int(dateInfo[0])
        month = int(dateInfo[1])
        day = int(dateInfo[2])
        monthAddList[month] = monthAddList[month] +[int(dataList[3])]
        add = add + int(dataList[3])


    print("전체 검사 진행자의 수 = ", add)

    for i in range(1,13) :
        print("%d월 검사 진행자의 수 =%d"%(i,monthAddList[i]))
