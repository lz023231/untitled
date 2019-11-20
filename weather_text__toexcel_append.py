import requests
import time
import random
import socket
import http.client
from xlutils.copy import copy
import csv
import pymysql
import xlrd
import xlwt
from bs4 import BeautifulSoup


def getContent(url, data=None):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh_CN,zh,q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    timeout = random.choice(range(80, 180))
    while True:
        try:
            rep = requests.get(url, headers=header, timeout=timeout)
            rep.encoding = 'utf-8'
            break
        except socket.timeout as e:
            print('3:', e)
            time.sleep(random.choice(range(8, 15)))

        except socket.error as e:
            print('4:', e)
            time.sleep(random.choice(range(20, 60)))

        except http.client.BadStatusLine as e:
            print('5:', e)
            time.sleep(random.choice(range(30, 80)))

        except http.client.IncompleteRead as e:
            print('6:', e)
            time.sleep(random.choice(range(5, 15)))
    print('request success')
    return rep.text


def getData(html_text, location):
    temp = []
    bs = BeautifulSoup(html_text, "html.parser")
    body = bs.body
    # print(body.prettify())
    # print(bs)
    data = body.find('div', {'id': '7d'})
    # print(data)
    input = data.find('input')
    # print(input.prettify())
    ifo = input['value']
    ifo1 = ifo.split()
    weather = ifo1[3].split("/")
    hei = weather[1]
    e = hei.split("°")
    print(weather)
    print('---')
    print(ifo1)
    print(type(e[0]))
    temp.extend([location, ifo1[2], e[0], weather[0], '2.00'])
    print(temp)
    # 写入Excel是有下面一行，如果不写入Excel，将下面一行注释
    return temp

    '''
    下面的内容是修改编写SQL语句，供方法write_to_mysql（）使用，写入到MySQL中
    x = '(' + "'" + location + "'"+ ',' + "'" + ifo1[2] + "'" + ',' + "'" + e[0] + "'" + ',' +"'" +  weather[0] + "'" + ',' + "'" + '2.00' + "'" + ')'
    print(x)
    sql = "insert into weather(city, weather, lowest, highest, fix) values" + x

    print(sql)
    print(type(sql))
    return sql
    '''
    '''
    写入到文件中用下面注释的内容
    st = '=@@='.join(temp)
    print(type(temp))
    with open('C:\weather.txt', 'a') as f:
        f.write(st)
        f.write('\n')
    '''


def data_write(file_path, datas):
    workbook = xlrd.open_workbook(file_path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    rows_old = worksheet.nrows
    new_workbook = copy(workbook)
    new_worksheet = new_workbook.get_sheet(0)
    j = 0
    i = 0
    for data in datas:
        #for j in range(0, len(datas[i])):
        new_worksheet.write(i+rows_old, j, data)
        j = j + 1
    new_workbook.save(file_path)





def write_to_mysql(sql_text):
    conn = pymysql.connect(host='192.168.10.4', user='root', password='123456', database='data', charset='utf8')
    cursor = conn.cursor()
    # sql = 'insert into weather(city, weather, lowest, highest, fix) values(北京,晴,7,-4,2.00)'
    cursor.execute(sql_text)
    conn.commit()
    cursor.close()
    conn.close()


def main():
    url_beijing = 'http://www.weather.com.cn/weather/101010100.shtml'
    html_beijing = getContent(url_beijing)
    # sql_beijing = getData(html_beijing, '北京')
    datas_beijing = getData(html_beijing, '北京')
    # write_to_mysql(sql_beijing)
    data_write(r'C:\Users\赵泽雷\Desktop\直播数据\weather.xls', datas=datas_beijing)

    url_shanghai = 'http://www.weather.com.cn/weather/101020100.shtml'
    html_shanghai = getContent(url_shanghai)
    # sql_shanghai = getData(html_shanghai, '上海')
    # write_to_mysql(sql_shanghai)
    datas_shanghai = getData(html_shanghai, '上海')
    data_write(r'C:\Users\赵泽雷\Desktop\直播数据\weather.xls', datas=datas_shanghai)

    url_guangzhou = 'http://www.weather.com.cn/weather/101280101.shtml'
    html_guangzhou = getContent(url_guangzhou)
    # sql_guangzhou = getData(html_guangzhou, '广州')
    # write_to_mysql(sql_guangzhou)
    datas_guangzhou = getData(html_guangzhou, '广州')
    data_write(r'C:\Users\赵泽雷\Desktop\直播数据\weather.xls', datas=datas_guangzhou)

    url_shenzhen = 'http://www.weather.com.cn/weather/101280601.shtml'
    html_shenzhen = getContent(url_shenzhen)
    # sql_shenzhen = getData(html_shenzhen, '深圳')
    # write_to_mysql(sql_shenzhen)
    datas_shenzhen = getData(html_shenzhen, '深圳')
    data_write(r'C:\Users\赵泽雷\Desktop\直播数据\weather.xls', datas=datas_shenzhen)


while True:
    main()
    time.sleep(1000)