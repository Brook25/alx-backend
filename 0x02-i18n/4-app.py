#!/usr/bin/env python3
"""Choose a locale based on a passed parameter in the url
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config(object):
    """app configuration class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """returns best match to accept languages header"""
    req_locale = request.args.get('locale')
    if req_locale and req_locale in app.config['LANGUAGES']:
        return req_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """returns an html page"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(port='5000', host="0.0.0.0", debug=True)
