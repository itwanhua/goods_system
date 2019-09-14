from flask import Flask, render_template, request
import good_operation, goods

app = Flask(__name__)

@app.route("/home", methods=["GET", "POST"])
def find():
    if request.method == "GET":
        return render_template("home.html")
    else:
        f = request.form.get("selected")
        w = request.form.get("way")
        print(f, w)
        if f == "get_all":
            print(1)
            gs = good_operation.get_all()
            print(gs)
        elif f == "get_byid":
            g = goods.good()
            g.set_gid(w)
            gs = good_operation.get_byid(g)
            gs = (gs, )
            print(gs)
        else:
            g = goods.good()
            g.set_gname(w)
            gs = good_operation.get_byname(g)
            gs = (gs, )
        return render_template("home.html", gs=gs)


if __name__ == "__main__":
    app.run(port="80", debug="True")