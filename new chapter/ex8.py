'''
함수를 정의하는 방법

def 함수이름(매개변수) :
    소스코드1
    소스코드2
    ,,,
    소스코드n

'''
'''
#return이 포함된 함수!!
#1더하기 1을 출력하는 함수를 만드세요
def add0():
    print(1+1)
#1+1 의 결과를 반환(return)하는 함수를 만드세요
def add1():
    return  1+1
#두 수를 더한 결과를 출력하는 함수를 만드세요
def add2(num1,num2) :
    print(num1 + num2)

#두 수를 더한 결과를 출력(print)하고 돌려(return)주는 함수
def add2(num1,num2) :
    print(num1 + num2)
    return (num1+ num2)

#두 정수 중 큰 수를 반환하는 함수를 만드세요

def add3(num1,num2) :
    max= num1
    if num2> max :
        max = num2

    return max
#두 정수 중 작은 수를 반환하는 함수를 만드세요
def minimum(num1,num2):
    if num1 < num2:
        return num1
    else:
        return num2
#세 정수 중 가운뎃 수를 반환하는 함수를 만드세요

def mid(num1,num2,num3):

    if num1>= num2:
        if num2>= num3:
            return num2
        elif num1 <= num3:
            return num1
        else :
            return  num3
    elif num1 > num3 :
    #elif num2 > num3 :
        return num3
    else :
        return  num2

#국,영,수 점수를 전달받아 합계와 평균을 반환하는 함수를 만드세요

def calcScore(kor,eng,mat) :
    sum = kor + eng+ mat
    avg = sum /3

    #합계와 평균을 반환하는 return 문을 완성하시요
    #한개의 값을 리턴하는게 아닌 데이터들을 반환하는 방법이 필요하다
#    return (sum,avg)
#or
    return {"합계" : sum, "평균" : avg}
#   return [sum,avg]

#이렇게 시퀀스 객체들을 사용해서 데이터'들'을 반환할 수 있다.
result = calcScore(1,2,3)
print(result["합계"])
print(result["평균"])

#return은 이 함수의 끝을 의미함
#함수를 수행하다가 return을 만나면 그즉시 제어가 함수를 호출했던 곳으로 돌아감
#종료될때 결과값을가지고 제어가 돌아가게 돼있음

add0()

result = add1()
print("add1 함수의 결괏값 = ", result)

print("add2 함수의 결괏값=",add2(1,1))
'''
#두  수와 산술 연산자 중  한 연산자를 전달 받아
#두 수를 사용자가 원하는 산술 연산한 결과를 반환하는 함수를 반드세요

def num (num1,num2,yun) :
    print("첫번째 수 :" ,end="")
    num1 = int(input())
    print("두번째 수 :" , end="")
    num2 = int(input())
    var1 = num1 + num2
    var2 = num1 - num2
    var3 = num1 * num2
    var4 = num1 / num2
    print("연산자 (+,-,*,/) :",end="")
    yun = input()

    if yun == "+" :
        print("첫번째 수와 두번째 수의 연산 결과는 %d 입니다."%var1)
        return var1
    if yun == "-" :
        print("첫번째 수와 두번째 수의 연산 결과는 %d 입니다."%var2)
        return var2
    if yun == "*" :
        print("첫번째 수와 두번째 수의 연산 결과는 %d 입니다."%var3)
        return  var3
    if yun == "/" :
        print("첫번째 수와 두번째 수의 연산 결과는 %d 입니다."%var4)
        return var4
    else :
        print("연산자를 잘못 입력 하셨습니다.")
num(2,3,"+")