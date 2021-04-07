from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driverPath ="C:/Users/ITPS/Desktop/driver/chromedriver.exe"
URL = "https://play.google.com/store?hl=ko"

driver = webdriver.Chrome(executable_path=driverPath)
driver.get(url=URL)
driver.implicitly_wait(10)

element = driver.find_element_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz > div > div.N4FjMb.Z97G4e.QeUCtb > div > c-wiz > c-wiz:nth-child(1) > c-wiz > div > div.ZmHEEd.fLyRuc > div:nth-child(1) > c-wiz > div > div > div.uzcko > div > div > a")

#ActionChains -> 연속적인 동작을 할 수 있게 해주는 모듈
#위 모듈은 쌓어있던 코드를 일괄적으로 실행하게 해야하는데 그럴때 perform을불러준다
ActionChains(driver).move_to_element(element).perform()
time.sleep(1)



