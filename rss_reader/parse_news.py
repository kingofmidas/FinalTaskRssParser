from bs4 import BeautifulSoup
import feedparser
from datetime import date
import sys


# check if there is media content
def checkMediaContent(item):
    media_content = ''
    if ('media_content' in item.keys()):
        media_content = item.media_content[0]['url']
    elif ('media_thumbnail' in item.keys()):
        media_content = item.media_thumbnail[0]['url']
    return media_content


# return description without html tags
def getDescription(item):
    return BeautifulSoup(item, features="html.parser").getText()
