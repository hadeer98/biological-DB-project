from flask import Flask, render_template, request
from screens import screen

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/Lalignment",methods=["POST"])
def Lalignment():
    fseq=request.form.get("fseq")
    secseq=request.form.get("secseq")
    r=screen(fseq,secseq)
    return render_template("result.html",r=r)
