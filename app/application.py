import logging
import re

from django.utils.html import urlize

from flask import Flask
from flask import render_template
import ical
from jinja2 import Markup
import tweepy

app = Flask(__name__)


class TwitterCredentials(db.Model):
    consumer_key = db.StringProperty(required=True)
    access_token = db.StringProperty(required=True)
    consumer_secret = db.StringProperty(required=True)
    access_secret = db.StringProperty(required=True)


@app.route('/')
def home():
    return render_template('home.html',
            tweets=get_tweets(),
            upcoming_events =ical.upcoming_events());





app.secret_key = '7%@0g6y!hu^flbmkcfb$@zxs9ftmh=t0blgnog-ibh52za$6nu'
