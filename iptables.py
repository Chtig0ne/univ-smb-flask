# save this as app.py
from flask import Flask, render_template, request,Response
import base64

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

def check(aut_header):
    username="bon"
    password ="jour"
    encoded_uname_pass=aut_header.split() [-1]
    if encoded_uname_pass==base64.b64decode(username + ":" + password) :
        return True

@app.route('/auth')
def auth():
    aut_header=request.header.get('Auth')
    if aut_header and check(aut_header):
        return "page confidentielle"
    else:
        resp=Response()
        resp.headers['WWW-Authenticate']='Basic'
        return resp, 401


@app.route('/mdp',methods=['GET','POST'])
def mdp():
    return render_template("mdp.html")