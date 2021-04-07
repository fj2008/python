from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
#키보드에 명시된 특수문자들을 선택한 요소에 전달할수 있음
driverPath ="C:/Users/ITPS/Desktop/driver/chromedriver.exe"
URL = "https://play.google.com/store?hl=ko"

driver = webdriver.Chrome(executable_path=driverPath)
driver.get(url=URL)
driver.implicitly_wait(10)

elementList = driver.find_element_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz > div > div.N4FjMb.Z97G4e.QeUCtb > div > c-wiz > c-wiz:nth-child(2) > c-wiz > div > div.ZmHEEd.fLyRuc > div")
for element in elementList :
    elementName = element.find_element_by_css_selector(".WHE7ib mpg5gc")
    element = elementName
    print(elementName,"페이지에 접속")

    element.click()

    time.sleep(1)

    driver.back()
# element = driver.find_element_by_css_selector("#gbqfq")
#
# #선택한요소에 정보를 보내어 입력하게 전송을 해줌
# element.send_keys("네이버")
#
# time.sleep(1)
# element.send_keys(Keys.ENTER)
#
#
# time.sleep(1)
# element.send_keys(Keys.BACKSPACE)
# element.send_keys(Keys.BACKSPACE)
# element.send_keys(Keys.BACKSPACE)
# #검색어 영역에 코리아교육그룹 이라고 입력하고
#
# #해당 앱을 검색하고자 함
#
# time.sleep(1)
#
# element.send_keys("코리아 교육 그룹")
#
# time.sleep(1)
#
# element.send_keys(Keys.ENTER)


# element = driver.find_element_by_css_selector("#gbqfb > span")
# element.submit()





#element.메서드 를하면 이 element가 품고있는 자식의 정보를 찾는것
#element는 내가 선택한 요소의 정보를 찾는것이다
# print(element.get_attribute("href"))
# print(element.get_property("class"))
#
# print(element.is_displayed())
# print(element.is_enabled())
# print(element.is_selected())
#
# print(element.value_of_css_property("position"))
#
# print(element.screenshot("element.png"))

# print("id = ",element.id)#html에서 말한 id가아니라 셀레니움이 공개한 id
# print("tag_name =",element.tag_name)
# print("Location = ",element.location)
# print("location_once_scrolled_into_view =",element.location_once_scrolled_into_view)
# print("size = ",element.size)
# print("rect = ",element.rect)
# print("text = ",element.text)
# print("parent = ",element.parent)


