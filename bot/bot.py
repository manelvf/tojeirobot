# -*- coding: UTF-8 -*-
import os
import random
import json
import re
from datetime import datetime, timedelta

from twitter import Twitter, OAuth
from BeautifulSoup import BeautifulSoup

from config import TWITTER, PHRASES_FILE


def twitter_login(config_file):
    with open(config_file) as f:
        config = json.load(f)

    return Twitter(auth=OAuth(
        TWITTER["token"],
        TWITTER["token_key"],
        TWITTER["con_secret"],
        TWITTER["con_secret_key"]
    ))

    
def load_phrases_file(filename):
    lines = []
    with open(filename) as f:   
        for l in f.readlines():
            lines.append(l)

    return lines


def choose_random_phrase(phrases):
    return random.choice(phrases)


def tweet(t):
    phrases = load_phrases_file(PHRASES_FILE)
    phrase = choose_random_phrase(phrases)

    t.statuses.update(status=phrase)
    print(phrase)


if __name__ == "__main__":
    tweet(twitter_login)
