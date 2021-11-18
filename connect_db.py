# -*- coding: utf-8 -*-
"""
@Time : 2021/11/18 14:20
@FileName : connect_db.py
@Description : 
"""

import pymysql

def get_conn():
    conn = pymysql.Connect(host="localhost", user="test", passwd="123456", db="goodsdb")
    return conn

