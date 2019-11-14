from  selenium.webdriver.common.keys import Keys
import time
import re
import requests
import pytesseract
from PIL import Image,ImageEnhance
from selenium import webdriver

from selenium.webdriver.common.by import By

class Login():
    def login(self, driver, username, password):
        driver.find_element_by_xpath('//*[(@id = "username")]').clear()
        driver.find_element_by_xpath('//*[(@id = "username")]').send_keys(username)
        driver.find_element_by_xpath('//*[(@id = "passwd")]').clear()
        driver.find_element_by_xpath('//*[(@id = "passwd")]').send_keys(password)

        #screenImg = "C:/image/screenImg.png"

        #driver.find_element_by_name("username").send_keys(username)
        #driver.find_element_by_name("username").send_keys(Keys.TAB)
        #driver.find_element_by_name("password").clear()
        #driver.find_element_by_name("password").send_keys(password)
        #driver.find_element_by_name("password").send_keys(Keys.TAB)
        #driver.find_element_by_xpath('//div[contains(text(),"登  录")]').click()


