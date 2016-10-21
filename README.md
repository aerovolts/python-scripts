# Python-Scripts

This is a central repository for miscellaneous python scripts I have written, and will write, over time that don't merit their own repository. Explanations for each script inside this repository are listed below.

These scripts are all written and tested in Python 3 (as reflected by the shebang line at the top of each file).

## degrees_converter.py

This simple script automates the conversion of Decimal Degrees and Degrees Minutes Seconds. Prompts are

## md5bot.py

Generates an md5 hash of the current time and posts to Twitter using the tweepy library and Twitter API.

To use this script install the tweepy library using `pip install tweepy`. Go to the Twitter developer site and register a new application. Add the consumer key/secret and access token/secret from your application into the script.

The script runs in an infinite loop to post, there are better ways to do this (like a cron job) but I haven't learned those yet.

## twitterqtr.py

This script uses a spreadsheet of pre-selected quotes on Google Drive to post to twitter. The quotes are randomly selected and then sent to Twitter via ttweepy and the Twitter API.

This is probably broken however, I haven't used it in a long time.

## redditscrape.py

A script for downloading images from a list of user-defined subreddits up to a user-defined limit. Configuration can be found in the Configuration block near the top of the file.

Two Python packages are requiered to run this script (`praw` and `wget`). They can be installed via pip with the following commands:

* `pip install praw`
* `pip install wget`

To-Do List:

* [ ] Clean-up .tmp files from broken downloads
* [ ] Check if image already exists to prevent duplicate downloads
* [ ] Fix download of non-direct image likes (ie. imgur galleries)
