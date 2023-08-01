#!/usr/bin/env python3
"""flask app implements babel"""

from flask import Flask
from flask import render_template
from flask_babel import Babel
from config import Config


app = Flask(__name__)
babel = Babel(app)
babel.BABEL_DEFAULT_LOCALE = Config.BABEL_DEFAULT_LOCALE
babel.BABEL_DEFAULT_TIMEZONE = Config.BABEL_DEFAULT_TIMEZONE
app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def home() -> str:
    """Returns an html page"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
