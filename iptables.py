# save this as app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("TP3_Peytraud_Benoit.html")

@app.route("/start")
def start():
    return render_template("TP3_Peytraud_Benoit.html")

@app.route("/rules_nat")
def rules_nat():
    return render_template("Regle_de_NAT.html")
    
@app.route("/rules_nat_add")
def rules_nat_add():
    return render_template("Ajout_de_NAT.html")