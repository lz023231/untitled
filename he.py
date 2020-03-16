from selenium.webdriver.common.keys import Keys
import xlrd
import time

class Get_longitude():
    def get_longitude(self,driver,location):
        driver.find_element_by_xpath('//*[@id="localvalue"]').clear()
        #time.sleep()
        driver.find_element_by_xpath('//*[@id="localvalue"]').send_keys(location)
        #time.sleep(2)
        driver.find_element_by_xpath('//*[@id="localsearch"]').click()
        time.sleep(1)
        result = driver.find_element_by_xpath('//*[@id="no_0"]').text
        return result
    def get_excel(self,path,k):
        # 读取excel文件
        Excelfile = xlrd.open_workbook(path)

        # 获取读入文件的sheet
        # 索引从0开始
        # 也可以用名字的方式读取，但是一定要注意大小写
        # sheet = Excelfile.sheet_by_name('Sheet1')
        sheet = Excelfile.sheet_by_index(0)

        # 获取行内容，索引从0开始
        rows = sheet.row_values(k)
        print(rows)
        nrows = sheet.nrows
        return rows
    def get_nrows(self, path):
        Excelfile = xlrd.open_workbook(path)
        sheet = Excelfile.sheet_by_index(0)
        nrows = sheet.nrows
        return nrows
