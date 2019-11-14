from hxzxLogin import *
import unittest
from selenium import webdriver
import time
from pykeyboard import PyKeyboard
import os
#import HTMLTestRunnerCN
#import sendMail
#import run


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://39.98.206.54:9090/login.do")

    def test_1_login(self):
        username = 'ctsing'
        password = 'admin'
        time.sleep(2)
        Login().login(self.driver,username,password)



        self.driver.save_screenshot('C://image/picture.png')

        ce = self.driver.find_element_by_id("code-image")  # 具体的id要用F12自行查看 
        print(ce.location)
        left = ce.location['x']
        top = ce.location['y']
        right = ce.size['width'] + left
        height = ce.size['height'] + top
        im = Image.open('C://image/picture.png')
        img = im.crop((1490, 660, 1650, 710))
        img.save('C://image/picture2.png')
        time.sleep(3)

        image1 = Image.open('C://image/picture2.png')
        text = pytesseract.image_to_string(image1)
        #print(text)
        self.driver.find_element_by_xpath('//*[(@id = "checkImage")]').send_keys(text)
        self.driver.find_element_by_xpath('//*[(@id = "confirm")]').click()
        time.sleep(2)
        url = self.driver.current_url
        if url == "http://39.98.206.54:9090/login.do":
            print("登录失败")


        #添加素材


        #点击素材管理
        self.driver.find_element_by_xpath('//*[@id="menu"]/a[2]').click()
        time.sleep(3)

        #点击添加更多
        self.driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "icoAdd", " " ))]').click()
        time.sleep(4)

        w = self.driver.find_element_by_xpath('//*[@id="material_add_btn"]/li[1]/a').is_enabled()
        if w == False:
            print('文本素材不可以点击')

        t = self.driver.find_element_by_xpath('//*[@id="material_add_btn"]/li[2]/a').is_enabled()
        if t ==False:
            print('天气预报不可以点击')

        tj = self.driver.find_element_by_xpath('//*[@id="material_add_btn"]/li[3]/a').is_enabled()
        if tj == False:
            print('添加表格不可以点击')

        wb = self.driver.find_element_by_xpath('//*[@id="material_add_btn"]/li[4]/a').is_enabled()
        if wb == False:
            print('外部视频源可以点击')

        fw = self.driver.find_element_by_xpath('//*[@id="material_add_btn"]/li[5]/a').is_enabled()
        if fw == False:
            print('服务器文件不可点击')

        wy = self.driver.find_element_by_xpath('//*[@id="material_add_btn"]/li[6]/a').is_enabled()
        if wy == False:
            print('网页截图不可以点击')

        tj = self.driver.find_element_by_xpath('//*[@id="material_add_btn"]/li[6]/a').is_enabled()
        if tj == False:
            print('添加模板不可以点击')

        #单素材上传
        self.driver.find_element_by_xpath('//*[@title="默认分类"]').click()
        time.sleep(2)
        #x = self.driver.find_element_by_xpath('//*[@title="默认分类"]').is_selected()
        #print(x)
        x = self.driver.find_element_by_xpath('//*[@id="material_import"]/span').is_enabled()
        if x == False:
            print("单个素材上传不能点击")
        self.driver.find_element_by_xpath('//*[@id="material_import"]/span').click()
        time.sleep(3)
        self.driver.switch_to_frame('iframe')
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="file"]').send_keys('C:\\image\\picture.png')
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@value="上传"]').click()
        time.sleep(3)
        k = PyKeyboard()
        k.tap_key(k.enter_key)













    def tearDown(self):
        time.sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()