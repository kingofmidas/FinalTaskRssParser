from bs4 import BeautifulSoup
import feedparser
import json
import logging
from datetime import date


# Set basic configs for logging
logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG,
                    handlers=[logging.FileHandler("parser.log", "a", encoding="utf-8")])


# function for parsing news
def getEntries(url, json, verbose, limit):
    '''
    1. set object of feedparser library
    2. set news limit
    3. on each iteration of loop 
        3.1 cache news
        3.2 log news
        3.3 print news in sdtout or json format
    '''
    channel = feedparser.parse(url)
    print("Feed: ", channel.feed.title, '\n')

    limit = limit or len(channel.entries)

    for item in channel.entries:

        if (limit > 0):
            cacheNews(item)
            loggingItems(item)

            if (json):
                print(getJSON(item))

            else:
                printNews(item)
        else:
            break
        limit -= 1


# checks if there is media content
def checkMediaContent(item):
    media_content = ' '
    if('media_content' in item.keys()):
        media_content = item.media_content[0]['url'] + '\n'
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


# return news in json format
def getJSON(item):
    return json.dumps({
        'Title: ': item.title,
        'Date: ': item.published,
        'Link: ': item.link,
        'Description: ': getDescription(item.description)
    })


# return description without html tags
def getDescription(item):
    return BeautifulSoup(item, features="html.parser").getText()


# print news
def printNews(item):
    print("Title: ", item.title)
    print("Date: ", item.published)
    print("Link: ", item.link, '\n')
    print("Description: ", getDescription(item.description), '\n')
    print("Links:", "\n[1]: ", item.link, "(link)\n[2]: ",
    checkMediaContent(item), '\n')


# pring logs
def printLogs():
    with open('parser.log', 'r') as f:
        for line in f:
            print(line)
