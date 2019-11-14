#! /usr/bin/env python

from PIL import Image
from selenium import webdriver
import time
import win32api
import win32con
import pyautogui
from pymouse import *

while True:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("http://map.baidu.com/fwmap/zt/traffic/?city=beijing")
    driver.refresh()
    time.sleep(2)

    m = PyMouse()
    #将鼠标定位到屏幕中心
    m.move(960,610)
    time.sleep(2)
    #鼠标滑轮向上滚动
    pyautogui.scroll(1)
    #win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,1)
    #driver.find_element_by_xpath("//*[@id='mapContenter']/div[6]/div[2]/div[1]").click()
    time.sleep(3)
    now = time.strftime("%Y-%m-%d_%H_%M")
    print(now)

    filePath = "C://image/road_preview/" + now + ".png"
    print(filePath)
    driver.save_screenshot(filePath)

    im = Image.open(filePath)
    img = im.crop((600, 140, 1230, 710))
    filePath2 = "C://image/road_exact/" + now + ".png"
    img.save(filePath2)



    driver.quit()
    time.sleep(113)