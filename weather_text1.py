import requests
import time
import random
import socket
import http.client
import csv
# import pymysql
from bs4 import BeautifulSoup


def getContent_beijing(url, data=None):
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


def getContent_shanghai(url, data=None):
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


def getContent_guangzhou(url, data=None):
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


def getContent_shenzhen(url, data=None):
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


def getData_beijing(html_text):
    final = []
    a = '=@@='
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
    hei = weather[1][0:1]
    print(weather)
    print('---')
    print(ifo1)
    print(type(ifo1[3]))
    temp.extend(['北京', ifo1[2], hei, weather[0], '2.00'])
    st = '=@@='.join(temp)
    print(type(temp))
    with open('C:\weather.txt', 'a') as f:
        f.write(st)
        f.write('\n')


def getData_shanghai(html_text):
    final = []
    a = '=@@='
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
    hei = weather[1][0:1]
    print(weather)
    print('---')
    print(ifo1)
    print(type(ifo1[3]))
    temp.extend(['上海', ifo1[2], hei, weather[0], '2.00'])
    st = '=@@='.join(temp)
    print(type(temp))
    with open('C:\weather.txt', 'a') as f:
        f.write(st)
        f.write('\n')


def getData_guangzhou(html_text):
    final = []
    a = '=@@='
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
    hei = weather[1][0:1]
    print(weather)
    print('---')
    print(ifo1)
    print(type(ifo1[3]))
    temp.extend(['广州', ifo1[2], hei, weather[0], '2.00'])
    st = '=@@='.join(temp)
    print(type(temp))
    with open('C:\weather.txt', 'a') as f:
        f.write(st)
        f.write('\n')


def getData_shenzhen(html_text):
    final = []
    a = '=@@='
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
    hei = weather[1][0:1]
    print(weather)
    print('---')
    print(ifo1)
    print(type(ifo1[3]))
    temp.extend(['深圳', ifo1[2], hei, weather[0], '2.00'])
    st = '=@@='.join(temp)
    #print(type(temp))
    with open('C:\weather.txt', 'a') as f:
        f.write(st)
        f.write('\n')


'''
    div1 = div.find('div')
    a = div1.find('a')
    p = a.find_all('p')

    for day in p:
        #temp = []
        temp.append('北京')
        p1 = day[1].string
        temp.append(p1)
        p2 = day[2].string
        temp.append(p2)


        inf = day.find_all('p')
        weather = inf[0].string
        temp.append(weather)
        temperature_highest = inf[1].find('span').string
        temperature_low = inf[1].find('i').string
        temp.append(temperature_low)
        temp.append(temperature_highest)


        #final.append(temp)
    print('getData success')
    return temp


def writeData(data, name):
    with open(name, 'a', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(data)
    print('write_csv success')
'''
if __name__ == '__main__':
    url_beijing = 'http://www.weather.com.cn/weather/101010100.shtml'
    url_shanghai = 'http://www.weather.com.cn/weather/101020100.shtml'
    url_guangzhou = 'http://www.weather.com.cn/weather/101280101.shtml'
    url_shenzhen = 'http://www.weather.com.cn/weather/101280601.shtml'
    html_beijing = getContent_beijing(url_beijing)
    getData_beijing(html_beijing)

    html_shanghai = getContent_shanghai(url_shanghai)
    getData_shanghai(html_shanghai)

    html_guangzhou = getContent_guangzhou(url_guangzhou)
    getData_guangzhou(html_guangzhou)

    html_shenzhen = getContent_shenzhen(url_shenzhen)
    getData_shenzhen(html_shenzhen)
    # writeData(result, 'C:/weather.csv')
    print('my frist python file')