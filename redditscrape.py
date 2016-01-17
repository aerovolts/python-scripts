#!/usr/bin/env python

__author__ = "Patrick Guelcher"
__copyright__ = "(C) 2016 Patrick Guelcher"
__license__ = "MIT"
__version__ = "1.0"

"""
Scrapes the list of provided subreddits for images and downloads them to a local directoy
"""

import os
import praw
import wget
import urllib.error

# Configuration
path = 'images' # Download folder (Default: images)
sub_list = ['vexillology', 'mapporn', 'pics'] # Subreddit list
post_limit = 100 # Sumbission limit to check and download
user_agent = 'Image Scraper 1.0 by /u/aeroblitz' # Use your own reddit username

# Do not edit beyond this comment
def main():
    create_folder()

def create_folder():
    os.mkdir(path)
    download_images()

def download_images():
    u = praw.Reddit(user_agent=user_agent)

    for sub in sub_list:
        posts = u.get_subreddit(sub).get_hot(limit=post_limit)
        for post in posts:
            if post.url is not None:
                file_name = post.url
                extension = post.url[-4:]
                if extension == '.jpg' or extension == '.png':
                    try:
                        print (' File Name ' + file_name)
                        print (' Path ' + path)
                        wget.download(file_name, path)
                    except urllib.error.HTTPError as err:
                        if err.code == 404:
                            pass
                        else:
                            continue
            else:
                pass

if __name__ == '__main__':
    main()
