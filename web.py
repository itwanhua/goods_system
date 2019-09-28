#!/etc/bin/python3
# -*- coding: utf-8 -*-

import os, re
from flask import Flask, render_template, request, redirect, session, abort, Response
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
    if not username:
        return redirect('/login')
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
        elif f == "get_byname":
            g = goods.good()
            g.set_gname(w)
            gs = good_operation.get_byname(g)
            gs = (gs, )

        elif f == "get_blurname":
            gs = good_operation.get_blurname(w)

        return render_template("home.html", gs=gs, username=username)


@app.route("/home_add", methods=["GET", "POST"])
def home_add():
    '''
    功能：增加商品
    返回值：模板home_add.html
    
    '''
    username = session.get("username")
    if not username:
        return redirect('/login')
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

        # 若数据库中该商品名已存在，则修改商品价格并在原库存上加上新增数量
        g_tmp = good_operation.get_byname(g)
        if g_tmp:
            g.set_gnum(int(g.get_gnum()) + (g_tmp[3]))
            g.set_gid(g_tmp[0])
            good_operation.update_good(g)
            gs = good_operation.get_byname(g)
            gs = (gs, )
            return render_template("home_add.html", gs = gs, username=username)

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
    if not username:
        return redirect('/login')
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
    if not username:
        return redirect('/login')
    if request.method == "GET":
        return render_template("home_del.html", username=username)
    elif request.method == "POST":
        f = request.form.get("selected")
        w = request.form.get("way")

        if f == "get_byid":
            g = goods.good()
            g.set_gid(w)
            gs = good_operation.get_byid(g)
            good_operation.delete_good(g)
            gs = (gs, )
            return render_template("home_del.html", gs = gs, username=username)
        elif f == "get_byname":
            g = goods.good()
            g.set_gname(w)
            gs = good_operation.get_byname(g)
            good_operation.delete_good_byname(g)
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
        password1 = request.form.get("password1")
        phone = request.form.get("phone")
        email = request.form.get("email")
        print(username, password, password1, phone, email)

        if not (username and username.strip() and password and password1 and phone and email):
            return render_template("reg.html", feedback="信息不完整！")
        if users.reg_username_check(username):
            print(users.reg_username_check(username))
            abort(Response("用户名已存在！"))
        if not re.fullmatch("[a-zA-Z0-9_]{4,20}", username):
            abort(Response("用户名不合法！"))
        if not (len(password) >= 6 and len(password) <= 15 and password1 == password):
            abort(Response("密码错误！"))
        if not re.fullmatch(r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$", email):
            abort(Response("邮箱格式有误！"))

        users.user_reg(username, password, phone, email)
        return render_template("reg.html", feedback="注册成功！")

@app.route("/check_username", methods=["GET"])
def check_username():
    username = request.args.get("username")
    code = users.reg_username_check(username)
    return {"err": code}


if __name__ == "__main__":
    app.run(port="80", debug="True")