from flask import Flask,render_template,request

app = Flask(__name__)

#创建了网址/show/info 和函数index的对应关系
@app.route("/show/info")
def index():
    # return "flask web"
    return render_template("index.html")

@app.route("/test")
def index1():
    return render_template("test.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        user = request.form.get("user")
        pwd = request.form.get("pwd")
        gender = request.form.get("gender")
        more = request.form.get("more")
        print(user,pwd,gender,more)
        return "注册成功"

if __name__ == '__main__':
    app.run()