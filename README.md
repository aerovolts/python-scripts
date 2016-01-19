# Python-Scripts

This is a central repository for miscellaneous python scripts I have written, and will write, over time that don't merit their own repository.

Unless otherwise noted, scripts are written in Python 3.

# Scripts

## md5bot.py

Generates an md5 hash of the current time and posts to Twitter using the tweepy library and Twitter API.

To use this script install the tweepy library using `pip install tweepy`. Go to the Twitter developer site and register a new application. Add the consumer key/secret and access token/secret from your application into the script.

The script runs in an infinite loop to post, there are better ways to do this (like a cron job) but I haven't learned those yet.

## twitterqtr.py

This script uses a spreadsheet of pre-selected quotes on Google Drive to post to twitter. The quotes are randomly selected and then sent to Twitter via ttweepy and the Twitter API.

This is probably broken however, I haven't used it in a long time.

## redditscrape.py

Downloads images from a list of user indicated subreddits up to a limit also defined by the user. These settings are located under the "Configuration" comment.

Currently broken, see issues page for details.
