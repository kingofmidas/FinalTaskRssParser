from fpdf import FPDF
import urllib.request
import random
#import iter1
import feedparser
import os
from bs4 import BeautifulSoup


url = "https://news.yahoo.com/rss"

def getEntries(url, limit, pdf_path):

    channel = feedparser.parse(url)
    print("Feed: ", channel.feed.title, '\n')

    limit = limit or len(channel.entries)
    index = 0

    while (index < limit):
        item = channel.entries[index]
        toPdf(item, pdf_path, item.media_content[0]['url'])
        index += 1

    # for index, item in enumerate(channel.entries):

    #     if (limit > 0):
    #         toPdf(item, pdf_path, item.media_content[0]['url'])

    #     limit -= 1


pdf = FPDF()
pdf.add_page()


def toPdf(item, pdf_path, media):

    pdf.set_font('Arial', 'B', 16)
    title = item.title
    print(title)
    pdf.cell(40, 10, ln=1, txt=title)
    pdf.set_font('Arial', size=14)
    published = item.published
    pdf.cell(10, 10, ln=2, txt=published)
    description = getDescription(item.description)
    pdf.cell(10, 10, ln=3, txt=description)

    rand = random.randint(1, 120)
    if not os.path.exists('images/'):
        os.makedirs('images/')
    filename_ = 'images/' + str(rand) + '.jpg'
    urllib.request.urlretrieve(media, filename_)
    
    pdf.image(filename_)

    # name_ = item.title.split()[1]
    if not os.path.exists(pdf_path):
        os.makedirs(pdf_path)
    outfile = pdf_path + 'news' + '.pdf'
    pdf.output(r'outfile', 'F')


def getDescription(item):
    return BeautifulSoup(item, features="html.parser").getText()

def checkMediaContent(item):
    media_content = '\n'
    if(item.has_key('media_content')):
        media_content = item.media_content[0]['url']
    return media_content

getEntries(url, 2, 'pdfs/')

# file_dir = os.path.dirname(os.path.abspath(__file__))
# os.chdir(file_dir)
# print(os.getcwd())