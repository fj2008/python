from selenium import webdriver
from selenium.webdriver import ActionChains
import APP
import time
from datetime import datetime

driverPath ="C:/Users/ITPS/Desktop/driver/chromedriver.exe"
URL = "https://play.google.com/store?hl=ko"

driver = webdriver.Chrome(executable_path=driverPath)
driver.get(url=URL)
driver.implicitly_wait(10)
#원하는 데이터가 있는 곳으로 가는 코드
element = driver.find_element_by_css_selector("#fcxH9b > div:nth-child(2) > c-wiz.Knqxbd.tzLNed.Mfkobe > ul > li.uQeS5e.qKjvAb.iZhiic > a > span > span.pvVVcb")

element.click()

element = driver.find_element_by_css_selector("#fcxH9b > div:nth-child(2) > c-wiz:nth-child(3) > c-wiz > div > div > div > div:nth-child(4) > div > a")

element.click()

element = driver.find_element_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > c-wiz > div > div > c-wiz > c-wiz:nth-child(1) > c-wiz > div > div.Z3lOXb > div.W9yFB > a")

element.click()
'''페이지에 들어가자마자 50위 수집'''
#순위를 수집하는 코드
firstElementList = driver.find_elements_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz:nth-child(6) > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > div")
#수집한 순위의 마지막 요소를 선택
LastElement = firstElementList[-1]

#마지막 요소로 스크롤을 이동시켜라
ActionChains(driver).move_to_element(LastElement).perform()
#스크롤을 내리고 3초 쉬게 한다 요소가 불러올시간을 주기위함

'''스크롤을 내림으로써 새롭게 생긴 태그를 다시한번 불러온다'''

for i in range(1,4) :
    time.sleep(3)

    elementList = driver.find_elements_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz:nth-child(6) > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > c-wiz")
    LastElement = elementList[-1]
    ActionChains(driver).move_to_element(LastElement).perform()
#firstElementList -1 ~50까지 앱 요소
#elementList - 51~200위 까지 앱 요소
elementList = firstElementList + elementList

appInfoList = []

for element in elementList :

    appName = element.find_element_by_css_selector(".WsMG1c.nnK0zc")
    appName = appName.text

    companyName = element.find_element_by_css_selector(".KoLSrc")
    companyName = companyName.text

    imgPath = element.find_element_by_css_selector(".T75of.QNCnCf")
    imgPath = imgPath.get_property("src")

    star =element.find_element_by_css_selector("div.pf5lIe div")
    star = star.get_attribute("aria-label")
    star = star[10:13]

    appInfo = APP.APPInfo(appName, companyName,imgPath,star)

    appInfoList.append(appInfo)


today = datetime.now()#현제날짜와 시간을 가지고있음
today = today.strftime("%Y%m%d")#년 월 일  Ex)20210407
#복습할땐 jason형식으로 저장을 해보자

with open("C:/Users/ITPS/Desktop/app_rank/"+today+".tsv","w",encoding="UTF-8") as file:
    file.write("앱 이름\t서비스 회사\t앱이미지\t별점\t카테고리\t리뷰작성자의수\t별점5의비율\t별점4의비율\t별점3의비율\t별점2의비율\t별점1의비율\n")

    for appInfo in appInfoList :
        appName = appInfo.getAppName()
        company = appInfo.getCompany()
        imgPath = appInfo.getimgPath()
        star = appInfo.getstar()
        cotegory = ""
        reviewPeople = ""
        star5Rate = ""
        star4Rate =""
        star3Rate = ""
        star2Rate = ""
        star1Rate = ""

        file.write(appName+ "\t"+company+"\t"+imgPath+"\t"+star+"\t"+cotegory+"\t"+reviewPeople+"\t"+star5Rate+"\t"+star4Rate+"\t"+star3Rate+"\t"+star2Rate+"\t"+star1Rate+"\t"+"\n")




driver.close()