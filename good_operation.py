#!/etc/bin/python3
# -*- coding: utf-8 -*-

import pymysql
import goods


def get_all():
    conn = pymysql.Connect(host="localhost", user="wh", passwd="wh123", db="goodsdb")
    cur = conn.cursor()
    cur.execute("select * from good")
    rows = cur.fetchall()
    conn.close()
    return rows

def get_byid(g):
    conn = pymysql.Connect(host="localhost", user="wh", passwd="wh123", db="goodsdb")
    cur = conn.cursor()
    cur.execute("select * from good where gid = %s", (g.get_gid(), ))
    row = cur.fetchone()
    conn.close()
    return row

def get_byname(g):
    conn = pymysql.Connect(host="localhost", user="wh", passwd="wh123", db="goodsdb")
    cur = conn.cursor()
    cur.execute("select * from good where gname = %s", (g.get_gname(), ))
    row = cur.fetchone()
    conn.close()
    return row

def add_good(g):
    conn = pymysql.Connect(host="localhost", user="wh", passwd="wh123", db="goodsdb")
    cur = conn.cursor()
    try:
        cur.execute("insert into good values(null, %s, %s, %s)", (g.get_gname(), g.get_gprice(), g.get_gnum(), ))
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()

def update_good(g):
    conn = pymysql.Connect(host="localhost", user="wh", passwd="wh123", db="goodsdb")
    cur = conn.cursor()
    try:
        cur.execute("update good set gname = %s, gprice = %s, gnum = %s where gid = %s", (g.get_gname(), g.get_gprice(), g.get_gnum(), g.get_gid(), ))
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()

def delete_good(g):
    conn = pymysql.Connect(host="localhost", user="wh", passwd="wh123", db="goodsdb")
    cur = conn.cursor()
    try:
        cur.execute("delete from good where gid = %s", (g.get_gid(), ))
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()

#通过id查找
# g = goods.good()
# g.set_gid(1001)
# print(get_byid(g))
# exit(1)

#通过name查找
# g = goods.good()
# g.set_gname("飞旺")
# print(get_byname(g))

# 添加商品
# g = goods.good()
# g.set_gname("百事可乐")
# g.set_gprice(3.00)
# g.set_gnum(95)
# add_good(g)
# print(get_all())

# 更新商品
# g = goods.good()
# g.set_gid(1003)
# g.set_gname("百事可乐")
# g.set_gprice(3.00)
# g.set_gnum(80)
# add_good(g)
# print(get_all())

#删除商品
g = goods.good()
g.set_gid(1004)
delete_good(g)
print(get_all())






 