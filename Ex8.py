'''
야바위 게임
3개의 컵 중 하나에 상금을 숨겨 두었다
컵을 무작위로 섞어서 3초 내에 상금을 찾으면
상금 획득 ㄱㅇㄷ
'''

import random
import time

#3개의 컵, 상금이 들어있는 컵은 True가 됨
cups = [False,False,False]
#3개의 컵 중 어느 컵에 상금을 숨길지 결정
right = random.randint(0,2)
cups[right] = True

print("상금은 %d번 컵에 넣었습니다."% (right+1 ))

print("컵을 몇번 섞겠습니까?", end="")
suffleCount = int(input())

while True :
    number1 = random.randint(0,2)
    number2 = random.randint(0,2)

    temp = cups[number1]
    temp1 = cups[number2]
    temp = temp1
    temp1 = temp

    print("%d번 컵과 %d번 컵을 바꿨습니다" % (number1,number2))

    suffleCount = suffleCount -1
    if suffleCount ==0 :
        break
    else:
        sleepTime = random.randint(1,10)/10
        time.sleep((sleepTime))

#time.time()  메서드는 유닉스 타임스탬프를 구해주는 기능
#유닉스 타임스탬프 - 유닉스 운영체제가 만들어지고 나서부터 경과한 초
#유닉스 타임스탬프로 시간을 통일화 시킨다
start = time.time()

#시작된 시간

print("상금은 몇번 컵에 있을까요?")
print("3초 내로 입력해 주세요")
print("정답 :", end="")
right = int(input())

end = time.time()
#끝난 시간
#시간에대한 조건 부여
if end - start > 3:
    print("시간초과")
else :
    if cups[right -1]:
        print("상금을 차지했습니다!")
    else :
        print("상금 없음 ㅅㄱ")