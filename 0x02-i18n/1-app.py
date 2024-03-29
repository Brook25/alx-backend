#!/usr/bin/env python3
"""configures and implements flask app and babel"""
from flask import Flask
from flask import render_template
from flask_babel import Babel


class Config(object):
    """Config class for app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def home() -> str:
    """Returns an html page"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
