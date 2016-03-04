#!/usr/bin/env python

__author__ = "Patrick Guelcher"
__copyright__ = "(C) 2016 Patrick Guelcher"
__license__ = "MIT"
__version__ = "3.1"

"""
Scrapes the list of provided subreddits for images and downloads them to a local directory
"""

import os, praw, wget, urllib.error

# Configuration
root_path = 'scrape' # Download folder (Default: scrape)
sub_list = [
            'vexillology',
            'mapporn',
            'pics',
            'wallpapers'
            ] # Subreddit list
post_limit = 10 # Sumbission limit to check and download
user_agent = 'Image Scraper 3.1 by /u/aeroblitz' # Use your own reddit username

# Do not edit beyond this comment
def main():
    create_folders()

def create_folders():
    os.makedirs(root_path, exist_ok=True)
    for sub in sub_list:
        os.makedirs(os.path.join(root_path,str(sub)), exist_ok=True)
#    else:
#        print("DirectoryError: Could not create directory for " + sub)
    download_images()

def download_images():
    u = praw.Reddit(user_agent=user_agent)

    for sub in sub_list:
        post_list = u.get_subreddit(sub).get_hot(limit=post_limit)
        download_path = root_path + '/' + sub
        for post in post_list:
            if post.url is not None:
                file_name = post.url
                extension = post.url[-4:]
                if extension == '.jpg' or extension == '.png':
                    print ("\n" + post.url)
                    try:
                        wget.download(post.url, download_path)
                    except (IndexError, urllib.error.HTTPError):
                        print ("\n" + "DownloadError: Skipping file download.")
                        pass
                else:
                    pass
            else:
                pass
        else:
            continue
    else:
        print("\n" + "\n" + "Scrape Completed." + "\n")

if __name__ == '__main__':
    main()
