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

def user_reg(username, password, phone, email):
    conn = pymysql.Connect(host="localhost", user="wh", passwd="wh123", db="goodsdb")
    cur = conn.cursor()
    try:
        cur.execute("insert into users values(%s, %s, %s, %s)", (username, password, phone, email, ))
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()

def reg_username_check(username):
    conn = pymysql.Connect(host="localhost", user="wh", passwd="wh123", db="goodsdb")
    cur = conn.cursor()
    cur.execute("select * from users where uname = %s", (username, ))
    row = cur.rowcount
    conn.close()
    return row


