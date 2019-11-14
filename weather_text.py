
import requests
import time
import random
import socket
import http.client
import csv
import pymysql
from bs4 import BeautifulSoup

def getContent(url, data =None):
    header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh_CN,zh,q=0.8',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    timeout = random.choice(range(80,180))
    while True:
        try:
            rep = requests.get(url,headers = header,timeout = timeout)
            rep.encoding = 'utf-8'
            break
        except socket.timeout as e:
            print('3:', e)
            time.sleep(random.choice(range(8,15)))

        except socket.error as e:
            print('4:', e)
            time.sleep(random.choice(range(20,60)))

        except http.client.BadStatusLine as e:
            print('5:', e)
            time.sleep(random.choice(range(30,80)))

        except http.client.IncompleteRead as e:
            print('6:', e)
            time.sleep(random.choice(range(5,15)))
    print('request success')
    return rep.text

def getData(html_text):
    final = []
    bs = BeautifulSoup(html_text, "html.parser")
    body = bs.body
    print(body)
    #print(bs)
    data = body.find('div',{'id': '7d'})
    ul = data.find('ul')
    li = ul.find_all('li')

    for day in li:
        temp = []
        temp.append('北京')
        date = day.find('h1').string
        temp.append(date)
        inf = day.find_all('p')
        weather = inf[0].string
        temp.append(weather)
        temperature_highest = inf[1].find('span').string
        temperature_low = inf[1].find('i').string
        temp.append(temperature_low)
        temp.append(temperature_highest)
        final.append(temp)
    print('getData success')
    return final


def writeData(data, name):
    with open(name, 'a', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)
    print('write_csv success')

if __name__ == '__main__':
    url = 'http://www.weather.com.cn/weather/101010100.shtml'
    html = getContent(url)
    result = getData(html)
    writeData(result, 'C:/weather.csv')
    print('my frist python file')