import pymysql
import goods

g = goods.good()

def get_all():
    conn = pymysql.Connect(host="localhost", user="wh", passwd="wh123", db="goodsdb")
    cur = conn.cursor()
    cur.execute("select * from good")
    rows = cur.fetchall()
    conn.close()
    return rows

def get_byid(gid):
    conn = pymysql.Connect(host="localhost", user="wh", passwd="wh123", db="goodsdb")
    cur = conn.cursor()
    cur.execute("select * from good where gid = %s" % gid)
    row = cur.fetchone()
    conn.close()
    return row

def get_byname(gname):
    conn = pymysql.Connect(host="localhost", user="wh", passwd="wh123", db="goodsdb")
    cur = conn.cursor()
    cur.execute("select * from good where gname = %s", (gname, ))
    row = cur.fetchone()
    conn.close()
    return row

def add_good(gname, gprice, gnum):
    conn = pymysql.Connect(host="localhost", user="wh", passwd="wh123", db="goodsdb")
    cur = conn.cursor()
    try:
        cur.execute("insert into good values(null, %s, %s, %s)", (gname, gprice, gnum, ))
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()

def update_good(gname, gprice, gnum, gid):
    conn = pymysql.Connect(host="localhost", user="wh", passwd="wh123", db="goodsdb")
    cur = conn.cursor()
    try:
        cur.execute("update good set gname = %s, gprice = %s, gnum = %s where gid = %s", (gname, gprice, gnum, gid, ))
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()

def delete_good(gid):
    conn = pymysql.Connect(host="localhost", user="wh", passwd="wh123", db="goodsdb")
    cur = conn.cursor()
    try:
        cur.execute("delete from good where gid = %s", (gid))
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()

update_good("飞旺", 4.50, 20, 1002)
print(get_all())
# print(get_byname("卫"))





 