#!/usr/bin/env python3
"""
module contains Flask app
"""
from flask import (
    Flask,
    render_template,
    request,
    g
)
from flask_babel import Babel
from typing import (
    Dict,
    Union
)


class Config(object):
    """
    Class configuration for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
    funciton returns user dictionary or None if ID value can't be found
    """
    id = request.args.get('login_as', None)
    if id and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """
    func adds user to flask.g if user is found
    """
    usr = get_user()
    g.user = usr


@babel.localeselector
def get_locale():
    """
    func selects and returns best language match based on supported languages
    """
    locn = request.args.get('locale')
    if locn in app.config['LANGUAGES']:
        return locn
    if g.user:
        locn = g.user.get('locale')
        if locn and locn in app.config['LANGUAGES']:
            return locn
    locn = request.headers.get('locale', None)
    if locn in app.config['LANGUAGES']:
        return locn
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    func handles '/' route
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
