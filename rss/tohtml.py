import urllib.request
import random
import feedparser
import os
from bs4 import BeautifulSoup
import dominate
from dominate.tags import *


def getDescription(item):
    return BeautifulSoup(item, features="html.parser").getText()


def checkMediaContent(item):
    media_content = '\n'
    if(item.has_key('media_content')):
        media_content = item.media_content[0]['url']
    return media_content    


def getHTML(url, html_path, limit):
    channel = feedparser.parse(url)
    doc = dominate.document(title='HTML document')
    index = 0

    while (index < limit):
        item = channel.entries[index]

        media = checkMediaContent(item)
        rand = random.randint(1, 120)
        if not os.path.exists('images/'):
            os.makedirs('images/')
        filename_ = 'images/' + str(rand) + '.jpg'
        urllib.request.urlretrieve(media, filename_)

        with doc:
            with div():
                h2(item.title)
                p("Date: " + item.published)
                img(src=os.path.abspath(filename_))
                p("Description: " + getDescription(item.description))

        index += 1

    if not os.path.exists(html_path):
        os.makedirs(html_path)
    html_path = html_path + str(rand) + '.html'
    with open(html_path, 'w') as f:
        f.write(str(doc))

    return html_path
