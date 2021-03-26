'''
반복문 for
for 변수 in 시퀀스 객체 :
    코드1
    코드2
    ...
변수안에 있는 시퀀스 객체를 다 반복하여 출력함

모든 시퀀스객체 사용가능
'''

score = [56,45,65,45,]

for word in score :
    print(word)
    if word <60 :
        print("불합격")
    elif word>= 60 :
        print("합격")
