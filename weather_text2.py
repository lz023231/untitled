import requests
import time
import random
import socket
import http.client
import csv
# import pymysql
from bs4 import BeautifulSoup


def getContent(url,  data=None):
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
    print(type(ifo1[3]))
    temp.extend([location, ifo1[2], e[0], weather[0], '2.00'])
    st = '=@@='.join(temp)
    print(type(temp))
    with open('C:\weather.txt', 'a') as f:
        f.write(st)
        f.write('\n')

def main():
    url_beijing = 'http://www.weather.com.cn/weather/101010100.shtml'
    html_beijing = getContent(url_beijing)
    getData(html_beijing, '北京')

    url_shanghai = 'http://www.weather.com.cn/weather/101020100.shtml'
    html_shanghai = getContent(url_shanghai)
    getData(html_shanghai, '上海')

    url_guangzhou = 'http://www.weather.com.cn/weather/101280101.shtml'
    html_guangzhou = getContent(url_guangzhou)
    getData(html_guangzhou, '广州')

    url_shenzhen = 'http://www.weather.com.cn/weather/101280601.shtml'
    html_shenzhen = getContent(url_shenzhen)
    getData(html_shenzhen, '深圳')


while True:
    main()
    time.sleep(30)