import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date=20210401"
param_dic = {}
response = requests.get(url,param_dic)


html = response.text
soup = BeautifulSoup(html,"html.parser")
mivelist = soup.find_all("td")