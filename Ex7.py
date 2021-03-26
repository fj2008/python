'''
반복문 continue
break 문과 마찬가지로
반복문의 안에서 흐름을 조절할 때 사용
특정코드 뭉치들을 실행하지 않고 다시 조건을 비교하고자 할때
'''
'''
print("수 써라" , end="")
num1 = int(input())

if num1 == 0 :
    while num1 >=1 :
        if num1 % 3 != 0:
            print(num1)
        num1 +=1

elif num1 <0 :
    while num1 <=1:
        if num1 % 3 != 0:
            print(num1)
        num1 +=1
'''


num2 = 0


while num2 <= 73 :
    if num2 % 10 ==3 :
        num2+=1

        print(num2)


