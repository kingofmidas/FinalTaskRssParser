import urllib.request
import random
import feedparser
import os
from bs4 import BeautifulSoup
import dominate
from dominate.tags import *
import pdfkit
import webbrowser  


# make convertion of news into pdf or html
def makeConvertion(url, html_path, pdf_path, limit):
    '''
    1. create object of feedparser library
    2. create object of dominate library for creating html files
    3. on each iteration 
        3.1 check if there is media content
        3.2 write html tags
        3.3 convert format of file
    '''
    channel = feedparser.parse(url)
    doc = dominate.document(title="HTML document")

    for index, item in enumerate(channel.entries):
        if(index == limit):
            break

        random_name = random.randint(1, 120)
        media_file_name = checkMediaContent(item, random_name)

        with doc:
            with div():
                h2(item.title)
                p("Date: " + item.published)
                if (media_file_name):
                    img(src=os.path.abspath(media_file_name))
                p("Description: " + getDescription(item.description))

    
    if(html_path):
        intoHTML(html_path, doc, random_name)

    elif(pdf_path):
        intoPDF(pdf_path, doc, random_name)


# return description of news without html tags
def getDescription(item):
    return BeautifulSoup(item, features="html.parser").getText()


def checkMediaContent(item, random_name):
    '''
    1. create folder with images and return name of image 
    if there is media content in news
    2. or return nothing
    '''
    media_content = ''
    if('media_content' in item.keys()):
        media_content = item.media_content[0]['url']
    
        if not os.path.exists('images/'):
            os.makedirs('images/')
        filename_ = 'images/' + str(random_name) + '.jpg'
        urllib.request.urlretrieve(media, filename_)
        return filename_

    return media_content  


def intoHTML(html_path, doc, random_name):
    '''
    1. read file with styles for html
    2. write styles in html
    3. create folder for html file if not exists
    4. write html file
    5. open browser with html
    '''
    with open('style.css') as file:
            css_file = file.read()

    with doc.head:
        style(css_file)

    if not os.path.exists(html_path):
        os.makedirs(html_path)
    html_file = html_path + str(random_name) + '.html'

    with open(html_file, 'w') as f:
        f.write(str(doc))

    webbrowser.open(html_file, new=2)


def intoPDF(pdf_path, doc, random_name):
    '''
    1. create folder for pdf files if not exists
    2. write pdf file
    '''
    if not os.path.exists(pdf_path):
            os.makedirs(pdf_path)
    pdf_file = pdf_path + str(random_name) + '.pdf'

    pdfkit.from_string(str(doc), pdf_file)