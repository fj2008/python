#인코딩: 0과1밖에 모르는 컴퓨터가 사람이 다루는 데이터를 이해할 수 있도록 변화해 주는작업
#사진 인코딩: 이미지를 컴퓨터가 이해할 수 있도록 0과1로 변환하는 과정
#동영상 인코딩 : 동영상을 컴퓨터가이해할 수 있도록 0과1로 변환하는 과정
#디코딩 : 0과1을 사람이 볼 수 있는 데이터로 변환해 주는 과정
#문자 인코딩 : 문자를 컴퓨터가 이해할 수 있도록 변환하는 과정
#ASCII, UTF-8, EUC-KR, CP494 등등
#전세계적으로 모든 문자를 인코딩할때는 UTF-8이 사용된다
#인코딩과 디코딩 모두 같은 방식으로 사용해야함
#우리가사용하는 사용하는 인코딩은 CP494이고 웹페이지는 UTF-8이다
#그래서 디코딩할때 UTF-8로 하라고 명령해야함

'''
css선택자
태크 선택자
아이디 선택자
클래스 선택자
속성을 선택할 수 있는 선택자
'''
import requests
from bs4 import BeautifulSoup
#나홀로 집에 영화에 작성된 리뷰를 가져오기
#1. 파이썬 코드를 통해 나홀로집에 영화 페이지에 접근
    #1-1. 나홀로집에 영화 페이지에 직접 들어가서 영화 페이지의 url과 파라메터 파악
    #1-2. requests모듈을 사용해서 나홀로집에 영화 페이지에 접근
    #   이때 1-1에서 파악한 영화 페이지의 url과 파라메터를 파악
#2.영화 페이지 내 리뷰 데이터에 접근
    #2-1 개발자 모드(f12)를 사용해서 영화 페이지 내 리뷰 데이터의 html코드,css선택자 등을 파악
    #2-2 requests로 접근한 웹페이지 데이터를 bs4를 사용해서 분석할수 있도록 파싱
    #2-3 find 또는 find_all메서드를 사용해서 리뷰 데이터들을 선택
#3.리뷰 데이터를 출력
    #3-1 리뷰들을 불러왔으므로 for문을 사용해서 리뷰들을 하나 하나씩 출력
    #3-2

url = "https://movie.naver.com/movie/bi/mi/basic.nhn?code=10016"
param_dic = {"code" : 10016}

response = requests.get(url,param_dic)

try :
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    review_list = soup.find_all("div", class_ = "score_reple")
    #findall은 div와 score_reple이을 갖고있는 클래스들을 호출함

    for review in review_list :

        reviewContent = review.find("p")
        reviewContent = reviewContent.text
        reviewContent = reviewContent.strip()
        print(review.get_text())
except :
    print("데이터를 불러오지 못했습니다.")
