'''
html
데이터를 공유하기위해 만든 프로그래밍 언어
'''
import requests

url = ""
param_dic = {}


fullURL = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"
fullURL = fullURL.split("?")

url = fullURL[0]

parameter = fullURL[1]
parameter = parameter.split("&")
for param in parameter :
    param = param.split("=")
    print(param)

    param_dic.setdefault(param[0],param[1])



#URL에서 ?뒤에 오는 것들을 파라메터(Parameter)
#자원이 사용할 재료

#파라메터는 이름=값 으로 구성되어 있음
#이름과 값은  & 기호를 사용해서 구분함
#'ie=utf8 = query로 검색된 글자의 분석'&'query검색'='%ED%8C%8C%EC%9D%B4%EC%8D%AC파이썬이라는 글자를 표현' 위 파라미터가 일반적으로 사용하는 파라메터
#https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC

reponse = requests.get(url, param_dic)

print("응답코드 = {}".format(reponse.status_code))
print(reponse.text)