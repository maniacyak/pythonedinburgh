from flask import Blueprint, render_template

mod = Blueprint('base', __name__)

def get_tweets():
    return []


def upcoming_events():
    return []


@mod.route('/')
def home():
    return render_template(
        'home.html',
        tweets=get_tweets(),
        upcoming_events =upcoming_events())
