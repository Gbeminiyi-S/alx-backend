#!/usr/bin/env python3
"""This module sets up a basic Flask app"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Creates a Config class with the LANGUAGES attribute"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route('/')
def index_page():
    """This function defines a route for the root URL ('/')"""
    return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """Selects a language translation to use for request by order of priority
    """
    url_match = request.args.get('locale', None)
    best_match = request.accept_languages.best_match(app.config['LANGUAGES'])
    global_match = g.user.get('locale', None)

    locales = [url_match, best_match, global_match]

    for locale in locales:
        if locale and locale in Config.LANGUAGES:
            return locale
    return Config.BABEL_DEFAULT_LOCALE

def get_user():
    """Returns a user dictionary"""
    user_id = request.args.get('login_as')

    if user_id:
        try:
            user_id = int(user_id)
            if user_id in users:
                return users[user_id]
            return None
        except Exception:
            return None


@app.before_request
def before_request():
    """Finds the user"""
    g.user = get_user()

