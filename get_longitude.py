from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def get_longitude(self, driver,location):
    driver.find_element_by_xpath('//*[@id="localvalue"]').send_keys(location)
    driver.find_element_by_xpath('//*[@id="localsearch"]').click()

    result = driver.find_element_by_xpath('//*[@id="no_0"]').text
    print(result)

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://api.map.baidu.com/lbsapi/getpoint/index.html?qq-pf-to=pcqq.group")
time.sleep(5)
location = "西便门内大街55号"
driver.find_element_by_xpath('//*[@id="localvalue"]').send_keys(location)
driver.find_element_by_xpath('//*[@id="localsearch"]').click()

result = driver.find_element_by_xpath('//*[@id="no_0"]').text

print(result)
driver.quit()




