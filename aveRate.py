import pytesseract
from PIL import Image,ImageEnhance
import isapi


def getRate():
    global a
    sum =0
    t = 0
    for i in range(1, 104):
        if i < 10:
            a = '0000{}'.format(i)
        if 10 < i < 100:
            a = '000{}'.format(i)
        if 100 < i < 1000:
            a = '00{}'.format(i)
        if 1000 < i < 10000:
            a = '0{}'.format(i)
        path = "C:/Users/赵泽雷/Desktop/直播测试素材/1030-1100-移动-720576" + "/Screenshot-" + a + '.jpg'
        im = Image.open(path)
        img = im.crop((464, 471, 515, 496))
        b = str(i)
        path2 = "c:/count/" + b + ".png"
        img.save(path2)
        image1 = Image.open(path2)
        x = pytesseract.image_to_string(image1)
        q = x.split()
        o = "".join(q)
        print(o)

        y = int(o)
        print(y)
        if i == 1:
            if y > t:
                t = y
        else:
            if y > t:
                t = y

        sum =sum + y
        print("sum =", sum)
        ave = sum/103
        print("平均码率：" , ave)
        print("码率峰值：" , t)
getRate()
