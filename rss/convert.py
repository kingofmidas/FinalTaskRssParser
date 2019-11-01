import urllib.request
import random
import feedparser
import os
from bs4 import BeautifulSoup
import dominate
from dominate.tags import *
import pdfkit
import webbrowser


def getDescription(item):
    return BeautifulSoup(item, features="html.parser").getText()


def checkMediaContent(item):
    media_content = '\n'
    if(item.has_key('media_content')):
        media_content = item.media_content[0]['url']
    return media_content    


def makeConvertion(url, html_path, pdf_path, limit):

    channel = feedparser.parse(url)
    doc = dominate.document(title="HTML document")

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

    if(html_path):
        with open('test.css') as file:
            css = file.read()

        with doc.head:
            style(css)

        if not os.path.exists(html_path):
            os.makedirs(html_path)
        html_file = html_path + str(rand) + '.html'
        with open(html_file, 'w') as f:
            f.write(str(doc))
        webbrowser.open(html_file, new=2)

    elif(pdf_path):
        if not os.path.exists(pdf_path):
            os.makedirs(pdf_path)
        pdf_file = pdf_path + str(rand) + '.pdf'
        pdfkit.from_string(str(doc), pdf_file)
