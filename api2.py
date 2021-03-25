# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 09:57:59 2020

@author: Mooncat
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask test"

@app.route("/test")
def test():
    return "Hello Flask test"

if __name__=="__main__":
    app.run()