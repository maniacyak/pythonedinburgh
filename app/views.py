from flask import Blueprint, render_template

from .twitter import Twitter

mod = Blueprint('base', __name__)

twitter_client = Twitter()


def get_tweets():
    return twitter_client.get_tweets('pythonedinburgh')


def upcoming_events():
    return []


@mod.route('/')
def home():
    return render_template(
        'home.html',
        tweets=get_tweets(),
        upcoming_events =upcoming_events())
