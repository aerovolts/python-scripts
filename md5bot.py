"""
md5bot.py -- Twitter bot that tweets the current time as an md5 value
"""

import time
import hashlib
import tweepy

CONSUMER_KEY = 'xxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxx' 
ACCESS_KEY = 'xxxxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxxxx'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def checkTime():
	ts = time.time()
	m = hashlib.md5()
	m.update(str(ts))
	return m.hexdigest()

def postStatus():
	currentTime = checkTime()
	api.update_status(currentTime)

int = 0
while int == 0:
	postStatus()
	time.sleep(3600) #Sleep for one hour
