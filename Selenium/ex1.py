'''
웹크롤링 - selenium
프로그램을 테스트하는 프레임워크
Web Driver와 Selenium설치 필요
크롬을 통해서하는게 좋다
크롬브라우저 버전 확인(최신버전확인)
http://chromedriver.chromium.org/downloads에서 크롬버전에 맞는webdriver다운
명령프롬프트에서 pip install selenium 적고 다운
'''
from selenium import webdriver
'''
driverPath = "웹드라이버의 경로"
URL = "데이터를 긁어올 페이지의 주소"
'''
driverPath ="C:/Users/ITPS/Desktop/driver/chromedriver.exe"
URL = "https://www.naver.com/"

driver = webdriver.Chrome(executable_path=driverPath)
driver.get(url=URL)

