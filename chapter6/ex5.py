import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cnt&date=20210401"
param_dic = {}
response = requests.get(url,param_dic)
movieman = []
html = response.text
soup = BeautifulSoup(html, "html.parser")

movie_list = soup.find_all("td", class_ = "title")
    #td 클래스테그안에 있는 title를 가져와
for movie in movie_list :
    name = movie.text
    movieman.append(name.strip())

rangeList = []
movie_list1 = soup.find_all("td", class_= "range")
for rangeTag in movie_list1 :
    rangeList.append(rangeTag.text)

for i in range(0,len(movie)) :
    if int(rangeList[i]) !=0 :

        print("{}위 : {} / {}".format(i+1,movie[i],rangeList[i]))

