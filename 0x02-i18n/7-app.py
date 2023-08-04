#!/usr/bin/env python3
"""Choose a locale based on a passed parameter in the url
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _
import pytz
from datetime import datetime

class Config(object):
    """app configuration class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """returns best match to the accept languages header"""
    req_locale = request.args.get('locale')
    if req_locale and req_locale in app.config['LANGUAGES']:
        return req_locale
    try:
        if g.user.get('locale') in app.config['LANGUAGES']:
            return g.user.get('locale')
    except AttributeError:
        if 'Accept-Language' in request.headers:
            return request.accept_languages.best_match(app.config['LANGUAGES'])



@babel.timezoneselector
def get_timezone():
    """returns a prefered time zone from a URL parameter or user settings"""
    try:
        return pytz.timezone(request.args.get('timezone')).zone
    except pytz.exceptions.UnknownTimeZoneError:
        try:
            return pytz.timezone(g.user.get('timezone')).zone
        except AttributeError or pytz.exceptions.UnknownTimeZoneError:
            pass
    return pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE']).zone




def get_user(user_id):
    """gets and returns a user from users if user_id is provided"""
    if user_id and int(user_id) in users:
        return users.get(int(user_id))


@app.before_request
def before_request():
    """makes a user globally visible if logged in with user id"""
    user = get_user(request.args.get('login_as'))
    if user:
        g.user = user


@app.route('/')
def index():
    """returns and displays html page with possible user login"""
    fmt = "%m %d, %Y, %H:%M:%S %z"
    return render_template('7-index.html', current_time=datetime.now().strftime(fmt))


if __name__ == "__main__":
    app.run(port='5000', host="0.0.0.0", debug=True)
