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
import time

'''
driverPath = "웹드라이버의 경로"
URL = "데이터를 긁어올 페이지의 주소"
'''
driverPath ="C:/Users/ITPS/Desktop/driver/chromedriver.exe"
URL = "https://play.google.com/store?hl=ko"

driver = webdriver.Chrome(executable_path=driverPath)
driver.get(url=URL)

'''
서버 : 서비스를 제공하는컴퓨터
서버프로그램 :서버에서 구동되는 프로그램
클라이언트: 서비스를 사용하는 컴퓨터
클라이언트 프로그램 : 클라이언트에서 구동되는프로그램

클라이어트(내 컴퓨터)> 클라이언트 프로그램(크롬)>서버컴퓨터>서버프로그램(naver)
'''

#셀레니움의 기본 대기시간은 0초
driver.implicitly_wait(10)
#셀레니움의 기본 대기 시간을 10초로 설청
#10초내에 웹페이지가 안뜨면 그다음에 동작을 해라라는뜻
#10초내에 웹페이지가 뜨면 바로 동작을 실행함
#셀레니움에게 대기시간을 지정하는 메서드


#driver라는 객체는 '현제 페이지의 정보'를 가지고있다
#find라는 메서드로 우리가 원하는 요소를 찾는것
#element 요소를 찾을때
#elements 요소들을 찾을때
#팁 ctrl+/ 주석할때 개꿀임
# elemont = driver.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz/div/div[2]/div/c-wiz/c-wiz[2]/c-wiz/div/div[2]/div[3]/c-wiz/div/div/div[1]/div/div/a')
# print(elemont)
#
# elemont = driver.find_element_by_xpath('/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/c-wiz/c-wiz[2]/c-wiz/div/div[2]/div[3]/c-wiz/div/div/div[1]/div/div/a')
# print(elemont)
#
elemont = driver.find_element_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz > div > div.N4FjMb.Z97G4e.QeUCtb > div > c-wiz > c-wiz:nth-child(2) > c-wiz > div > div.ZmHEEd.fLyRuc > div")



#driver라는 객체 사용법
#현제페이지의 정보 라고 생각하고 해석할것

#현제 찾은 요소를 클릭해라
elemont.click()
time.sleep(2)
print("현제 페이지에서 뒤로가기")
driver.back()
time.sleep(2)
print("현제 페이지에서 앞으로 가기")
driver.forward()
time.sleep(2)
print("현제 페이지 새로고침")
driver.refresh()
time.sleep(2)
print("현재 페이지의 스크린샷 저장")#저장공간이 없으면 save.png라는 파일을그 자리에저장
driver.save_screenshot("save.png")
time.sleep(2)
print("브라우저 닫기")
#현재 보고있는 탭을 닫음
#브라우저 내 탭이 하나였다면 탭을 닫으면서 브라우저도 닫힘
driver.close()

#브라우저 자체를 아예 닫아버림 (탭이 여러개 있었으면 강제로 다 닫힘)
#driver.quit()



# elemontList = driver.find_elements_by_css_selector('#fcxH9b > div.WpDbMd > c-wiz > div > div.N4FjMb.Z97G4e.QeUCtb > div > c-wiz > c-wiz:nth-child(1) > c-wiz > div > div.ZmHEEd.fLyRuc > div')
# for elemont in elemontList :
#     print(elemont,"\n")
#
# print("\n\n")
# elemontList = driver.find_elements_by_css_selector('#fcxH9b > div.WpDbMd > c-wiz > div > div.N4FjMb.Z97G4e.QeUCtb > div > c-wiz > c-wiz:nth-child(2) > c-wiz > div > div.ZmHEEd.fLyRuc > div')
# for elemont in elemontList :
#     print(elemont,"\n")
#
#
# print("\n\n")
# elemontList = driver.find_elements_by_xpath('/html/body/div[1]/div[4]/c-wiz/div/div[2]/div/c-wiz/c-wiz[2]/c-wiz/div/div[2]/div[1]')
# for elemont in elemontList :
#     print(elemont)

