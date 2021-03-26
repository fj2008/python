'''
클래스
c언어에는 클래스가 없다.
이말은 클래스가 없어도 프로그래밍이 가능하다는 것
파이썬으로 만든 프로그램들 중에는 클래스를 사용하지 않고 만든 프로그램도있다
꼭 필요한 요소는 아니지만 알고 사용하면 프로그래밍에 날개를 달아준다.
'''
#연관있는 변수와 연관있는 함수를 하나로 묶는 방법 : 클래스
#클래스로 묶은 변수 - 요소,속성,멤버 변수
#클래스로 묶은 함수 - 기능 , 함수,멤버 메서드
#Calculator 클래스를 '정의'했다. '선언'했다 라고 표현함
class Calculator :

    #계산기를 위한 클래스를 만든다
    #속성 - 값1,값2, 연산자, 연산결과...등등
    def __init__(self):
        self.num1
        self.num2
        self.op
        self.result
        self.color
        self.brand

    #기능 - 덧셈,뻴셈,곱하기,나누기 등등

    def add(num1, num2):
        return num1 + num2

    def minus(num1, num2):
        return num1 - num2

    def div(num1, num2):
        return num1 * num2

    def mul(num1, num2):
        return num1 / num2


#Calculator() >클래스의 인스턴스를 만든다.
#클래스의 인스턴스를 만든다.= 쿠키 틀을 먹을 순 없다. 쿠키틀로 찍어낸 쿠키를 먹을수 있는것 처럼
#클래스를 정의해뒀다고 해서 그 클래스를 사용할 수 있는건 아님
#클래스의 인스턴스를 만들어야지 클래스 안에 정의해둔 속성(멤버 변수)과 기능(멤버 메서드)을
#사용할 수 있다.


#redCal 객체
redCal =Calculator()
redCal.num1 = 10
redCal.num2 = 25
redCal.add(1,1)

#blueCal 객체

blueCal =Calculator()
blueCal.color = "blue"
blueCal.add(1,2)

#blackCal 객체

blackCal = Calculator()
blackCal.color = "black"
blackCal.add(2,23)


while True :
    print("====== 무야호~ ======")
    print("연산하고자 하는 두 수 를 입력 후")
    print("연산자를 입력하세요.")
    print("연산은 +,-,*,/ 만 가능합니다")
    print("프로그램을 종료하려면 연산자에 0을 입력하세요.")
    print("======= ======= ========")

    print("입력 :", end="")
    number1 = int(input())

    print("입력2 :", end="")
    number2 = int(input())

    print("연산자 : ", end="")
    op = input()
    if op == 0 :
        break
    if op == "+" :
        add(number1,number2)
    elif op == "-" :
        miner(number1,number2)
    elif op == "*" :
        div(number1,number2)
    elif op == "/" :
        mul(number1,number2)
