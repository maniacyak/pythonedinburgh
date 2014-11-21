# -*- coding: utf-8 -*-

from __future__ import print_function

import logging
from os import environ
from re import compile

from jinja2 import Markup
from jinja2.utils import urlize
from tweepy import OAuthHandler, API, TweepError

def twitterfy(tweet):
    tweet = urlize(tweet)

    # find hashtags
    # pattern = compile(r"(?P<start> ?)#(?P<hashtag>[A-Za-z0-9\-_]+)(?P<end>.?)")

    # replace with link to search
    link = (r'\g<start>#<a href="http://search.twitter.com/search?q=\g<hashtag'
            '>"  title="#\g<hashtag> search Twitter">\g<hashtag></a>\g<end>')
    #text = pattern.sub(link, tweet)
    text = tweet

    # find usernames
    pattern = compile(r"(?P<start>.?)@(?P<user>[A-Za-z0-9_]+)(?P<end>.?)")

    # replace with link to profile
    link = (r'\g<start>@<a href="http://twitter.com/\g<user>"  title="#\g<user'
            '> on Twitter">\g<user></a>\g<end>')
    text = pattern.sub(link, text)

    return Markup(text)


class TwitterCredentials(object):
    def __init__(self,
                 consumer_key, consumer_secret, access_token, access_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_secret = access_secret

    @classmethod
    def from_env(cls):
        values = [
            environ.get(key) for key in [
                'TWITTER_CONSUMER_KEY', 'TWITTER_CONSUMER_SECRET',
                'TWITTER_ACCESS_TOKEN', 'TWITTER_ACCESS_SECRET'
            ]]
        if all(values):
            return cls(*values)
        else:
            return None


class TweetWrapper(object):
    def __init__(self, tweet):
        self.tweet = tweet

    @property
    def markup(self):
        return twitterfy(self.tweet.text)

    @property
    def author(self):
        if hasattr(self.tweet, 'retweeted_status'):
            return self.tweet.retweeted_status.user
        else:
            return self.tweet.user

    @property
    def profile_image(self):
        return self.author.profile_image_url


class Twitter(object):
    def __init__(self, credentials=None):
        self.api = None

        if credentials is None:
            credentials = TwitterCredentials.from_env()

        if credentials is not None:
            auth = OAuthHandler(credentials.consumer_key,
                                credentials.consumer_secret)
            auth.set_access_token(credentials.access_token,
                                  credentials.access_secret)
            self.api = API(auth_handler=auth)

    def get_tweets(self, screen_name, count=5):
        if self.api is None:
            logging.error("No Twitter credentials were found.")
            # We don't have login stuff, bail.
            return []

        try:
            statuses = self.api.user_timeline(screen_name, count=count)
        except TweepError:
            logging.error("Failed to read timeline.")
            return []

        return [TweetWrapper(status) for status in statuses]
