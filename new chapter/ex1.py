'''
사용자함수
세탁기같은 기계처럼
반복적인 동작을 실행할때
'''

#학생 5명의 국어점수를 각 변수에 저장하세요
'''
kor1 = 0
while True:

    print("첫 번째 학생의 국어 점수 : ", end="")

    kor1 = int(input())
    if 0 <= kor1 and kor1 <= 100:
        break
    else :
        print("0~100점 사이로 입력해 주세요")
'''
#이렇게하면 똑같은 소스코드가 5개가 필요함 kor1변수가 학생마다 바뀌기때문

#그래서 이렇게 함수를 만들어서 반복되는동작을 함수가 수행하도록 해줌

#inputKor은 소스코드뭉치에 이름을 붙여준것
def inputKor():
    while True:

        print("학생의 국어 점수 : ", end="")

        kor1 = int(input())
        if 0 <= kor1 and kor1 <= 100:
            break
        else:
            print("0~100점 사이로 입력해 주세요")
    return kor1

kor1 =inputKor()
kor2 =inputKor()
kor3 =inputKor()
kor4 =inputKor()
kor5 =inputKor()

#위와같이 반복적인 상황의 동작을 함수를사용해서 소스코드를 굉장히 줄여줬다