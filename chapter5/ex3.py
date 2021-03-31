# time 모듈 = 시간과 관련된 함수들을 갖고 있는 모듈
import  time
#datetime 모듈 -> 날짜와 시간 관련된 함수들을 갖고 있는 모듈
import datetime
#now -> 메서드, 클래스안에 들어있는것, datetime 클래스 안에 들어있는 함수
#현재 날짜와 시간을 반환
#시간 -> 마이크로초 단위까지 계산
#밀리초 = 1/1000,마이크로초 = 1/1000000,나노초 ->1/100000000

print(datetime.datetime.now())

#유닉스 타임스탬프 : 유닉스OS 개발된 시점을 0초로 초를 세는 체계
#시간은 세계적으로 봤을때 상대적인것이기 때문에 프로그래밍에서는 유닉스 타임스탬프로
#시간을 통일한다
#time > 유닉스 타임스탬프를 반환

print(time.time())
#ctime > 우리가 아는 시간을 반환
#ISO (국제표준기구)에서 정한 표준 형태의 시간을 출력
print(time.ctime())

# strftime ->형식화된 시간 반환
# %y,%Y -> 2자리 또는 4자리 연도 출력
# %m -> 2자리 숫자로 월 표시 /01~12
# %o -> 2자리 숫자로 일 표시 / 01~09~10~31
# %H -> 2자리 숫자로 시간 표시
# %M -> 2자리 숫자로 분 표시
# %S -> 2자리 숫자로 초 표시
#위에있는것보 훨신 많이 있으니 필요에 따라 찾아서 사용하면됨
print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(time.strftime("%Y년-%m월-%d일 %H시:%M분:%S초"))

print("슬립전")
#sleep -> 프로그램을 잠시 멈추는 기능(테스트용)
time.sleep(3)
print("슬립 후")


