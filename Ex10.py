'''
range 실습
'''

for forward in range(2,6):
    for backward in range(1,10):
        print("%d *%d = %d"% (forward,backward, forward* backward))

'''
for backward in range(1,10,1):
    forward = 2
    for num1 in range(1,10):
        result = num1 * forward
    result= forward *backward
print("%d * %d = %d" %(num1,backward,result))

'''
'''
interviewResult = [
    ("홍길동", "sbs@naver.com",45),
    ("심봉사", "academy@gmail.com",79),
    ("철수" , "coumperter@naver.com",85),
    ("영희" , "art@naver.com", 99),
    ("이몽룡", "accds@naver,com", 69)
]
#name = 0번인댁스 email = 1번인덱스 point = 2번인덱스
for (name, email, point) in interviewResult :
    if point < 80: continue

    print("\n")
    print("발신자 : <sbs아카데미 컴퓨터아트 학원>")
    print("수신자 : <{0}>".format(email))
    print("내용 : ")
    print("\t 축하드립니다., %s님은 %d점으로 면접에 합격하셨습니다!"%(name,point))
    print("="*50)
'''