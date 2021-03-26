print("교통카드 충전 금액을 입력하시오",end="")

card = int(input())
price =1350

while card >= price:
    #break키워드를 만나는 순간
    #break 키워드가 속한 반복문에서 빠져나감
    if card <price :
        break
    card = card - price

    print("잔액 : %d"%card)

print("프로그램 종료")

#바뀔가능성이 큰 값들을 주로 변수에 저장을 한다

'''
반복문 = break 키워드
반복문으 흐름을 조절할 때 사용
반복문의 조건식을 만족하기 전에 끝내고 싶을때
반복문을 끝내는 조건이 두개가 되는것

'''

