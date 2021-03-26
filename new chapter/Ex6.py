def year (year1):
    """
    docString - 함수를 설명하는 주석
    :param year : 태어난 연도
    :return : 없음
    """

    age =2021 -  year1
    print("%d 년도생은 나이가 %d살 입니다."% (year1,age))

print("태어난 연도 : ", end="")
year1 = int(input())

year(year1)


#위문제에 코드를 매개변수가 있는 함수를 만들어보자