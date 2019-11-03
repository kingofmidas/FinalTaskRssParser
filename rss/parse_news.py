from bs4 import BeautifulSoup
import feedparser
import json
import logging
from datetime import date


# Set basic configs for logging
logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG,
                    handlers=[logging.FileHandler("parser.log", "a", encoding="utf-8")])


# return object of feedparser
def setParser(source):
    channel = feedparser.parse(source)
    print("Feed: ", channel.feed.title, '\n')
    return channel


# print news
def printNews(source, isJson, limit):
    '''
    1. set objects of feedparser
    2. set news limit
    3. on each iteration of loop 
        3.1 cache news
        3.2 log news
        3.3 print news in sdtout or json format
    '''
    channel = setParser(source)
    limit = limit or len(entries)

    for index, item in enumerate(channel.entries):
        if (index == limit):
            break
        cacheNews(item)
        loggingItems(item)
        if (isJson):
            print(getJSON(item))
        print("Title: ", item.title)
        print("Date: ", item.published)
        print("Link: ", item.link, '\n')
        print("Description: ", getDescription(item.description), '\n')
        print("Links:", "\n[1]: ", item.link, "(link)\n[2]: ",
        checkMediaContent(item), '\n')


# return news in json format
def getJSON(source, limit):
    return json.dumps({
            'Title: ': item.title,
            'Date: ': item.published,
            'Link: ': item.link,
            'Description: ': getDescription(item.description)
            })


# checks if there is media content
def checkMediaContent(item):
    media_content = ' '
    if('media_content' in item.keys()):
        media_content = item.media_thumbnail[0]['url'] + '\n'
    return media_content


# news caching in 'cache_news.txt'
def cacheNews(item):
    today = date.today().strftime("%Y-%m-%d")

    with open('cache_news.txt', 'a', encoding="utf-8") as f:
        f.write(today + '\n' +
                "Title: " + item.title + '\n' +
                "Link: " + item.link + '\n' +
                "Description: " + getDescription(item.description) + '\n')


# logs news in 'parser.log'
def loggingItems(item):
    logging.debug("Title: " + str(item.title))
    logging.debug("Date: " + str(item.published))
    logging.debug("Link: " + str(item.link) + '\n')
    logging.debug("Description: " + getDescription(item.description) + '\n')
    logging.debug("Links:"+"\n[1]: " + str(item.link) +
                "(link)\n[2]: " + str(checkMediaContent(item))+'\n')


# return description without html tags
def getDescription(item):
    return BeautifulSoup(item, features="html.parser").getText()


# pring logs
def printLogs():
    with open('parser.log', 'r') as f:
        for line in f:
            print(line)
