from selenium import webdriver
from selenium.webdriver import ActionChains
import APP

driverPath ="C:/Users/ITPS/Desktop/driver/chromedriver.exe"
URL = "https://play.google.com/store?hl=ko"

driver = webdriver.Chrome(executable_path=driverPath)
driver.get(url=URL)
driver.implicitly_wait(10)
#셀레니움이 css요소를 잘 못찾으면 그 요소에 들어가기위한 다른 css선택자를 찾아서 들어가면된다
element = driver.find_element_by_css_selector("#fcxH9b > div:nth-child(2) > c-wiz.Knqxbd.tzLNed.Mfkobe > ul > li.uQeS5e.qKjvAb.iZhiic > a > span > span.pvVVcb")

element.click()

element = driver.find_element_by_css_selector("#fcxH9b > div:nth-child(2) > c-wiz:nth-child(3) > c-wiz > div > div > div > div:nth-child(4) > div > a")

element.click()

element = driver.find_element_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz:nth-child(5) > div > c-wiz > div > div > c-wiz > c-wiz:nth-child(1) > c-wiz > div > div.Z3lOXb > div.W9yFB > a")

element.click()

elementList = driver.find_elements_by_css_selector("#fcxH9b > div.WpDbMd > c-wiz:nth-child(6) > div > c-wiz > div > c-wiz > c-wiz > c-wiz > div > div.ZmHEEd > div")

appInfoList = []

for element in elementList :
    #요소에있는 글씨만 text맴버변수에 들어있는데 그것을 text메소드를 활용해서 출력한다
    appName = element.find_element_by_css_selector(".WsMG1c.nnK0zc")
    appName = appName.text

    companyName = element.find_element_by_css_selector(".KoLSrc")
    companyName = companyName.text

    appInfo = APP.APPInfo(appName, companyName)
    appInfoList.append(appInfo)

print("가져온 앱의 개수  = ", len(appInfoList))

for appInfo in appInfoList :

    print("%s / %s "% (appInfo.getAppName(),appInfo.getCompany()))