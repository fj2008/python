#파일 복사기능
'''
-파일복사란?>
-원본 파일에 들어있는 데이터를 읽어와서 변수에 저장한 뒤
 새로운 파일에 저장하는 것

#데이터의 종류
- 텍스트 데이터 : 문자로 이루어진 데이터 /주로 휴먼이 사용한다
- 바이너리 데이터 : 0과 1로만 이루어진 데이터 / 주로 컴퓨터가 사용하는 데이터
  (바이너리 = 이진)
  음악,동영상,이미지 등이 주로 바이너리 데이터로 이루어져 있다.


로 크게 두가지로 나뉜다
'''
#r= 입력스트림 연결
#w,a = 출력스트림 연결

#t - 텍스트 데이터를 위한 스트림,
#b - 바이너리 데이터를 위한 스트림

#rt - 텍스트 데이터를 위한 입력스트림
#wt #at- 텍스트 데이터를 위한 출력스트림
#tb -바이너리 데이터를 위한 입력스트림
#wb #ab - 바이너리 데이터를 위한 출력스트림

# 운영 체제 마다, 프로그래밍 언어 마다 줄바꿈 문자가 다름
#윈도우 - \n\r
#리눅스 - \n
#유닉스, MacOs
#그래서 그런 줄바꿈 문자를 운영체제에 상관없이 헨들링하기위해서
#텍스트데이터와 바이너리데이터를 나눠서 표현함


#파일 복사
#원본 데이터를 읽어서 변수에 저장하고
#새로운 파일에 변수에 저장되어있는 원본 데이터를 저장한다.
'''
with open("C:/Users/ITPS/Desktop/source.mp4", "rb") as source :
    print("원본 파일 오픈")
    #readline은 한줄한줄 읽는것인데  바이너리데이터는 텍스트데이터가 아니기때문에 주로 read를 사용한다

    with open("C:/Users/ITPS/Desktop/destination.mp4", "wb") as destination:
        print("복사 파일 오픈")

        print("복사 시작")

        while True :
            buffer = source.read(1024)

            if not buffer :
                break

            destination.write(buffer)

        print("복사 끝")
    print("원본 파일 스트림 닫음")'''
#이렇게 원본데이터를 변수에 저장한뒤 출력하였다
#바이너리 타입의 데이터가 제대로 복사가 됐는지 확인하려면 파일의 크기를 보면 알수있다
#크기가 같으면 잘 복사된거라고 볼 수 있다.
with open("C:/Users/ITPS/Desktop/test.txt", "rt") as test :
    with open("C:/Users/ITPS/Desktop/copy.txt" "wt") as copy :
        while True :
            test1 = test.readline()

            if test1 == "" :
                break

            copy.write(copy)



