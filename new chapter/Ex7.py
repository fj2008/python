'''
def num(num1,num2) :

    if num1>num2 :
        print(num1)
    else:
        print(num2)

num(10,12)

def su(su1) :


    if su % 2 ==0:
        print("짝수")
    else:
        print("홀수")

su(12)


'''
#두 정수중 작은수를 출력하라
def su(su1,su2):
    if su1 >su2 :
        print(su2)
    else :
        print(su1)

#세 정수중 가장큰수를 출력하라
def num(num1,num2,num3) :

    #max가장 큰수를 미리 정해놓고 진행한다
    max = num1
    if num2 > max:
        max = num2
    if num3 > max:
        max = num3
    print("최대값은 ", max,"입니다")

num(1,2,3)
num(2,1,3)
num(3,2,1)

#네 정수 중 큰 수를 출력하는 함수를 만드세요
def maximum4 (num1,num2,num3,num4):
    max = num1

    if num2 >max :
        max = num2
    if num3 >max :
        max = num3
    if num4 > max :
        max = num4

    print(max)
num1 = 10
num2 = 23
num3 = 33
num4 = 44


maximum4(num1,num2,num3,num4)

#매개변수에 인자에 있는값을 전달할때 값이 그대로 올라가는게 아니라 '새로운 저장소'에 '복사'가 되는 개념이다

def swap(var1,var2):
    temp = var1
    var1 = var2
    var2 =temp
    

num1 =10
num2 = 20

swap(num1,num2)



