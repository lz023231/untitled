#! /usr/bin/env python

from PIL import Image
from selenium import webdriver
import time
import os
import win32con
import pyautogui
from pymouse import *

while True:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    #driver.get("http://map.baidu.com/fwmap/zt/traffic/?city=beijing")
    driver.get("https://www.369.me/bj/")
    #driver.refresh()
    time.sleep(2)
    '''
    m = PyMouse()
    #将鼠标定位到屏幕中心
    m.move(960,610)
    time.sleep(2)
    #鼠标滑轮向上滚动
    pyautogui.scroll(1)
    #win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,1)
    #driver.find_element_by_xpath("//*[@id='mapContenter']/div[6]/div[2]/div[1]").click()
    time.sleep(3)
    '''

    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    print(PROJECT_ROOT)
    now = time.strftime("%Y-%m-%d_%H_%M")
    filePath = PROJECT_ROOT + '\\road_preview\\' + now + ".png"
    print(filePath)
    driver.save_screenshot(filePath)

    im = Image.open(filePath)
    img = im.crop((372, 175, 966, 736))
    filePath2 = PROJECT_ROOT + '\\road_exact\\' + now + ".png"
    img.save(filePath2)



    driver.quit()
    time.sleep(113)