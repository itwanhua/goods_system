#!/etc/bin/python3
# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, request, redirect, session
import good_operation, goods, users

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route('/')
def index():
    return redirect('/login')

@app.route("/home", methods=["GET", "POST"])
def home_find():
    '''
    功能：查询商品（查找所有、ID查找、名称查找、）
    返回值：模板home.html
    
    '''
    username = session.get("username")
    if request.method == "GET":
        return render_template("home.html", username=username)
    elif request.method == "POST":
        f = request.form.get("selected")
        w = request.form.get("way")
        if f == "get_all":
            gs = good_operation.get_all()
        elif f == "get_byid":
            g = goods.good()
            g.set_gid(w)
            gs = good_operation.get_byid(g)
            gs = (gs, )

        else:
            g = goods.good()
            g.set_gname(w)
            gs = good_operation.get_byname(g)
            gs = (gs, )
        return render_template("home.html", gs=gs, username=username)


@app.route("/home_add", methods=["GET", "POST"])
def home_add():
    '''
    功能：增加商品
    返回值：模板home_add.html
    
    '''
    username = session.get("username")
    if request.method == "GET":
        return render_template("home_add.html", username=username)
    elif request.method == "POST":
        gname = request.form.get("gname")
        gprice = request.form.get("gprice")
        gnums = request.form.get("gnums")
        g = goods.good()
        g.set_gname(gname)
        g.set_gprice(gprice)
        g.set_gnum(gnums)
        good_operation.add_good(g)
        gs = good_operation.get_byname(g)
        gs = (gs, )
        return render_template("home_add.html", gs = gs, username=username)

@app.route("/home_upd", methods=["GET", "POST"])
def home_upd():
    '''
    功能：增加商品
    返回值：模板home_upd.html
    
    '''
    username = session.get("username")
    if request.method == "GET":
        return render_template("home_upd.html", username=username)
    elif request.method == "POST":
        gid = request.form.get("gid")
        gname = request.form.get("gname")
        gprice = request.form.get("gprice")
        gnums = request.form.get("gnums")
        g = goods.good()
        g.set_gid(gid)
        g.set_gname(gname)
        g.set_gprice(gprice)
        g.set_gnum(gnums)
        good_operation.update_good(g)
        gs = good_operation.get_byid(g)
        gs = (gs, )
        return render_template("home_upd.html", gs = gs, username=username)

@app.route("/home_del", methods=["GET", "POST"])
def home_del():
    '''
    功能：增加商品
    返回值：模板home_del.html
    
    '''
    username = session.get("username")
    if request.method == "GET":
        return render_template("home_del.html", username=username)
    elif request.method == "POST":
        gid = request.form.get("gid")
        g = goods.good()
        g.set_gid(gid)
        gs = good_operation.get_byid(g)
        good_operation.delete_good(g)
        gs = (gs, )
        return render_template("home_del.html", gs = gs, username=username)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        row = users.login_check(username, password)
        if row:
            session["username"] = username
            return render_template("home.html", username=username)
        else:
            return render_template("login.html", feedback="登录失败！")

@app.route("/reg", methods=["GET", "POST"])
def reg():
    if request.method == "GET":
        return render_template("reg.html")
    elif request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        phone = request.form.get("phone")
        email = request.form.get("email")
        print(username, password, phone, email)
        users.user_reg(username, password, phone, email)
        return render_template("reg.html", feedback="注册成功！")



if __name__ == "__main__":
    app.run(port="80", debug="True")