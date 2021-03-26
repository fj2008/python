'''
n = 1
while n <= 10 :
    print(n)

    n+=1'''
#반복문을 짤때 언제 시작해서 어떤조건으로 어떻게 끝나는지 계산을 해야한다
'''
hit = 0

while hit < 10:
    hit = hit +1
    print("나무를 %d번 찍었습니다" % hit)

    if hit ==10:
        print("나무가 넘어간다.")
'''
#끝이 정해져 있는 반복문을 횟수 반복문이라고 한다
#끝이 정해져있는 반복문은 while문에 어울리지 않는다
#while문에 어울리는 프로그램
'''
특정조건을 만족할 땨까지 주사위를 굴리는 프로그램
경품 추첨 이벤트 프로그램
로또당첨 번호 선정 프로그램

앞선 예제를 while문으 ㅣ용도에 맞게 수정해보자
'''


import random
#주사위를 한번 굴림
dice = 0
#random.randint로 값을 넣어줄 것이기 때문에 dice를 0으로 설정
while dice != 4:
    dice = random.randint(1,6)

    print("dice = %d"%dice)
#1~6사이에 수중에서 임의의 수를 얻어 낼 수 있다
#randint는 rand.int로 int타입의 데이터 타입을 가진다
#while문은 그 조건을 걸어서 while을 빠져나갈 수 있는 코드를 꼭 작성해야한다

