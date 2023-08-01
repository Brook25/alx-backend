#!/usr/bin/env python3
"""flask app that returns simple header"""
from flask import Flask, render_template
import flask


app = Flask(__name__)


@app.route('/')
def home():
    """returns html page with simple header"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
