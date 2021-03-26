#함수 - 함수의 호출 과정 및 변수의 범위



def mul(a,b) :
    c =a* b
    return c

def add(a,b) :
    c = a+b
    print(c)
    d = mul(a,b)
    print(d)

x=10
y=20


add(x,y)

'''
            RAM 
mul     함수의 정보
add     함수의 정보
x       10
y       20

    ram상에서 add함수만의 공간
a       10
b       20
c       30

    ram상에서 mul함수만의 공간
a       10
b       20
c       200


'''