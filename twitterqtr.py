"""
twitterqtr.py -- A Twitter bot that takes quotes input into Google Drive and posts them to Twitter.
"""

import tweepy
import gspread

#Twitter API Settings
CONSUMER_KEY = 'xxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxx' 
ACCESS_KEY = 'xxxxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxxxx'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#Google Drive Settings
gc = gspread.login('username@gmail.com', 'password')

#Quote Fetcher
def fetchQuote():
	wks = gc.open("Spreadsheet Name").sheet1
	
	quotes_list = filter(None, (wks.col_values(3))) #Filter empty lines
	quotes_list.pop(0) #Remove column heading
	
	qn = 1
	for q in quotes_list:
		api.update_status(q)
		print str(qn) + " " + q
		qn = qn + 1
		time.sleep(3600) #Sleep for one hour

#Initiate
fetchQuote()
