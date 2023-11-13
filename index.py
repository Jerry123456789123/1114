from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>立翰Python網頁</h1>"
    homepage += "<a href=/myweb>個人網頁</a><br>"
    homepage += "<a href=/mis>MIS相關工作介紹</a><br>"
    homepage += "<a href=/test>職涯探索</a><br>"
    homepage += "<a href=/profile>履歷表</a><br>"
    return homepage

@app.route("/myweb")
def myweb():
    return render_template("myweb.html")

@app.route("/mis")
def mis():
    return render_template("mis.html")

@app.route("/test")
def test():
    return render_template("test.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")    

#if __name__ == "__main__":
    #app.run()
    