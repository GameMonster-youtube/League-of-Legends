#-*- coding: utf-8 -*-
from flask import Flask, render_template
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/introduce')
def introduce():
    return render_template('introduce.html')

@app.route('/Renekton')
def Renekton():
    return render_template('Renekton.html')

@app.route('/Sett')
def Sett():
    return render_template('Sett.html')

@app.route('/Yasuo')
def Yasuo():
    return render_template('Yasuo.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
