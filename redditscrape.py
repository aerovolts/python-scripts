#!/usr/bin/env python

__author__ = "Patrick Guelcher"
__copyright__ = "(C) 2016 Patrick Guelcher"
__license__ = "MIT"
__version__ = "2.0"

"""
Scrapes the list of provided subreddits for images and downloads them to a local directory
"""

import os
import praw
import wget
import urllib.error

# Configuration
root_path = 'scrape' # Download folder (Default: scrape)
sub_list = ['vexillology', 'mapporn', 'pics'] # Subreddit list
post_limit = 50 # Sumbission limit to check and download
user_agent = 'Image Scraper 2.0 by /u/aeroblitz' # Use your own reddit username

# Do not edit beyond this comment
def main():
    create_folders()

def create_folders():
    os.mkdir(root_path)
    for sub in sub_list:
        os.mkdir(os.path.join(root_path,str(sub)))
    download_images()

def download_images():
    u = praw.Reddit(user_agent=user_agent)

    for sub in sub_list:
        post_list = u.get_subreddit(sub).get_hot(limit=post_limit)
        path = root_path + '/' + sub
        for post in post_list:
            if post.url is not None:
                file_name = post.url
                extension = post.url[-4:]
                if extension == '.jpg' or extension == '.png':
                    print (post.url)
                    wget.download(post.url, path)
        else:
            continue
    else:
        print("Scrape Comleted.")
        
if __name__ == '__main__':
    main()
