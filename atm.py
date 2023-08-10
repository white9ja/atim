from flask import Flask, render_template,request, session, logging, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)

@app.route("/")
def hello():
     return render_template('/index.html',title='Welcome')

@app.route("/scan")
def scan():
     return render_template('/screening.html',title='Screen')

if __name__ == '__main__':
    app.run(debug=True)