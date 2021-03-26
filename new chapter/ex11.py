'''
내장함수

abs()
slice()
len():시퀀스객체의 갯수를 알려줌
max():최댓값을구해줌
round():반올림

문자열과 관련된 내장함수

chr() : 정수를 문자로 변환하는 함수(아스키코드)
eval() : 문자열로 이루어진 연산을 해주는 함수
format() : 데이터를 원하는 형식의 문자열로 변환해 주는 함수
str() : 데이터를 문자열로 변환해주는 함수

'''

print(chr(48))

print(chr(97))

#chr함수를 사용해서 Z, !를 출력하세요

print(chr(90))

print(chr(33))


#chr 함수는 파일안에 있는 프로그램을 불러올때 주로 사용함

#ord함수는 문자에서 정수로변환해주는 함수
print(ord('A'))




#eval은 문자열안에 들어있는 연산을 eval함수가 알아서 연산자와 피연산자를 계산해주는 함수
print(eval("1 + 1"))

num1 = 27
print(eval("num1 *2"))
#eval은 위와같이 문자열안에 변수를넣어도 컴퓨터가 알아서 문자열을 연산할수있게 만들어준다

#format()함수는 데이터를 형식화 한다
print(format(10000,","))
print(format(10000,"_"))


#str()어떠한 데이터를 문자화 시키도록해줌
print(str(1000))


#eval활용

print("계산식을 입력하세요 : ", end="")

expr = input()

print(expr + "=" + str(eval(expr)))



