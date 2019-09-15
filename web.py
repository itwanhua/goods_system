from flask import Flask, render_template, request
import good_operation, goods

app = Flask(__name__)

@app.route("/home.html", methods=["GET", "POST"])
def find():
    '''
    功能：查询商品（查找所有、ID查找、名称查找、）
    返回值：模板home.html
    
    '''
    if request.method == "GET":
        return render_template("home.html")
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
        return render_template("home.html", gs=gs)


@app.route("/home_add.html", methods=["GET", "POST"])
def home_add():
    '''
    功能：增加商品
    返回值：模板home_add.html
    
    '''
    if request.method == "GET":
        return render_template("home_add.html")
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
        return render_template("home_add.html", gs = gs)

@app.route("/home_upd.html", methods=["GET", "POST"])
def home_upd():
    '''
    功能：增加商品
    返回值：模板home_upd.html
    
    '''
    if request.method == "GET":
        return render_template("home_upd.html")
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
        return render_template("home_upd.html", gs = gs)

@app.route("/home_del.html", methods=["GET", "POST"])
def home_del():
    '''
    功能：增加商品
    返回值：模板home_del.html
    
    '''
    if request.method == "GET":
        return render_template("home_del.html")
    elif request.method == "POST":
        gid = request.form.get("gid")
        g = goods.good()
        g.set_gid(gid)
        gs = good_operation.get_byid(g)
        good_operation.delete_good(g)
        gs = (gs, )
        return render_template("home_del.html", gs = gs)



if __name__ == "__main__":
    app.run(port="80", debug="True")