#!/etc/bin/python3
# -*- coding: utf-8 -*-

import pymysql

def login_check(uname, password):
    conn = pymysql.Connect(host="localhost", user="wh", passwd="wh123", db="goodsdb")
    cur = conn.cursor()
    cur.execute("select * from users where uname = %s and password = %s", (uname, password, ))
    row = cur.fetchone()
    conn.close()
    return row

