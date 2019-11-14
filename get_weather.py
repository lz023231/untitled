#! /usr/bin/env python


from PIL import Image
from selenium import webdriver
import time
import os
import pytesseract

while True:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.get("http://www.weather.com.cn/weather/101010100.shtml")
    time.sleep(2)
    js1 = "document.documentElement.scrollTop=50"
    driver.execute_script(js1)

    time.sleep(3)
    now = time.strftime("%Y-%m-%d_%H_%M")
    print(now)

    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    print(PROJECT_ROOT)
    filePath = PROJECT_ROOT + '\\weather_preview\\' + now + ".png"
    print(filePath)
    driver.save_screenshot(filePath)

    im = Image.open(filePath)
    img = im.crop((208, 392, 1202, 775))
    filePath2 = PROJECT_ROOT + '\\weather_exact\\' + now + ".png"
    img.save(filePath2)
    img1 = Image.open(filePath2)
    text = pytesseract.image_to_string(img1)

    text = text.encode('utf-8').decode("utf-8")
    print(text)



    driver.quit()
    time.sleep(1197)