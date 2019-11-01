from bs4 import BeautifulSoup
import feedparser
import json
import re
import logging
from datetime import date


# url = "https://news.yahoo.com/rss"
# url1 = "https://news.google.com/rss"
# url2 = "https://www.theguardian.com/world/rss"


logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s', 
                    level=logging.DEBUG,
                    handlers=[logging.FileHandler("parser.log", "a", encoding="utf-8")])


def getEntries(url, json, verbose, limit, pdf_path):

    channel = feedparser.parse(url)
    print("Feed: ", channel.feed.title, '\n')

    limit = limit or len(channel.entries)

    for index, item in enumerate(channel.entries):

        if (limit > 0):
            cacheNews(item)
            loggingItems(item)

            if (json):
                print(getJSON(item))

            else:
                print("Title: ", item.title)
                print("Date: ", item.published)
                print("Link: ", item.link, '\n')
                print("Description: ", getDescription(item.description), '\n')
                print("Links:", "\n[1]: ", item.link, "(link)\n[2]: ",
                checkMediaContent(item), '\n')
        else:
            break
        limit -= 1



def checkMediaContent(item):
    media_content = '\n'
    if(item.has_key('media_content')):
        media_content = '\n' + item.media_content[0]['url'] + '\n'
    return media_content


def cacheNews(item):
    today = date.today()
    d1 = today.strftime("%Y-%m-%d")

    with open('cache_news.txt', 'a', encoding="utf-8") as f:
        f.write(d1 + '\n' +
                "Title: " + item.title + '\n' +
                "Link: " + item.link + '\n' +
                "Description: " + getDescription(item.description) + 
                checkMediaContent(item) + '\n')


def loggingItems(item):
    logging.debug("Title: " + str(item.title))
    logging.debug("Date: " + str(item.published))
    logging.debug("Link: " + str(item.link) + '\n')
    logging.debug("Description: " + getDescription(item.description) + '\n')
    logging.debug("Links:"+"\n[1]: " + str(item.link) +
                "(link)\n[2]: " + str(checkMediaContent(item))+'\n')


def getJSON(item):
    return json.dumps({
        'Title: ': item.title,
        'Date: ': item.published,
        'Link: ': item.link,
        'Description: ': getDescription(item.description)
    })


def getDescription(item):
    return BeautifulSoup(item, features="html.parser").getText()


def printLogs():
    with open('parser.log', 'r') as f:
        for line in f:
            print(line)



