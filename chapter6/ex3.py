import  requests

url = ""
a_dic = {}
#fullURL = "https://movie.naver.com/movie/bi/mi/basic.nhn?code=161967"
fullURL = "https://movie.naver.com/movie/sdb/rank/rpeople.nhn"
fullURL = fullURL.split("?")
try :
    url = fullURL[0]

    parameter = fullURL[1]

    parameter = parameter.split("&")
    for a in parameter :
        a = a.split("=")
        print(a)

        a_dic.setdefault(a[0],a[1])
except IndexError:
    print("IndexError: list index out of range")

response = requests.get(url,a_dic)


print(response.text)

file = open("C:/Users/ITPS/Desktop/index.html","w",encoding="UTF-8")
file.write(response.text)
file.close()



