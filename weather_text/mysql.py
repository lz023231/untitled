import pymysql

def write_to_mysql():
    conn = pymysql.connect(host = '192.168.10.4', user = 'root', password = '123456', database = 'data', charset = 'utf8')
    cursor = conn.cursor()
    sql = "insert into weather(city, weather, lowest, highest, fix) values ('北京','晴','7','-4','2.00')"
    sql2 = 'insert into weather(city) value ("北京")'

    cursor.execute("insert into weather(city, weather, lowest, highest, fix) values ('北京','晴','7','-4','2.00')")

    conn.commit()


    cursor.close()
    conn.close()

write_to_mysql()