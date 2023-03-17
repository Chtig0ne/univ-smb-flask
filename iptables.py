# save this as app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start():
    return render_template("TP3_Peytraud_Benoit.html")