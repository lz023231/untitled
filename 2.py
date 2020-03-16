from he import *
from selenium import webdriver
from openpyxl import load_workbook
import xlwt
import xlrd
from xlutils.copy import copy
import openpyxl
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://api.map.baidu.com/lbsapi/getpoint/index.html?qq-pf-to=pcqq.group")
time.sleep(5)
path = 'C:\\Users\\赵泽雷\\Desktop\\zuobiao.xls'
nrows = Get_longitude().get_nrows(path)
print(nrows)
for i in range(nrows):
    print('---------------------------')
    print(i)
    rows = Get_longitude().get_excel(path,i)
    rows = "".join(rows)
    print("ree" + rows)
    a = Get_longitude().get_longitude(driver, rows)
    print(a)
    b = a.split("\n")
    print(b)
    h = b[1]
    h2 = b[0]
    y ="".join(h)
    y2 = "".join(h2)
    l = y.find(rows)
    l2 = y.find(rows)
    if l != -1:
    '''
        改写写入文件了，计划返回不为负一的，将坐标写入第二列，为负一的写---应该追加写入，现在存在的问题是将第一条数据写入后，第二条数据会覆盖第一条数据
    '''
        return re
    wb = xlrd.open_workbook(path)
    #tt = xlwt.open
    ws = wb.sheets()[0]
    newwb = copy(wb)
    newws = newwb.get_sheet(0)
    newws.write(i,1,b[2])
    print("i=",i)

    newwb.save('C:\\Users\\赵泽雷\\Desktop\\zuobiao2.xls')



driver.quit()