from flask import Flask, render_template, url_for
from sqlalchemy import true
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("main.html",text1="OWO")

@app.route("/sec")
def name():
    return render_template("sec.html", text1 = "hello_owo")

if __name__=="__main__":
    app.run(host="127.0.0.1", port="5000", debug=true)
    