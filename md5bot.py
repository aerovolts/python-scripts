#!/usr/bin/env python

__author__ = "Patrick Guelcher"
__copyright__ = "(C) 2016 Patrick Guelcher"
__license__ = "MIT"
__version__ = "1.0"

"""
A bot for Twitter that checks the time and then posts it as an md5 hash value.
"""

import time
import hashlib
import tweepy

# Configuration (Twitter API Settings)
CONSUMER_KEY = 'xxxxxxxxxxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxx'
ACCESS_TOKEN = 'xxxxxxxxxxxxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxxxxxxxxxxxx'
sleep_time = 3600 # Time is in seconds (Default 3600)

# Do not edit beyond this comment
def main():
    index = 0
    while index == 0:
        post_status()
        time.sleep(sleep_time) # Sleep for one hour

def check_time():
    time_stamp = str(time.time())
    encode_time = time_stamp.encode('utf-8')
    md = hashlib.md5()
    md.update(encode_time)
    return md.hexdigest()

def post_status():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    current_time = check_time()
    api.update_status(current_time)
    print(current_time)

if __name__ == '__main__':
    main()
