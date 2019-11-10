import os
import re
from dominate.tags import div, h2, img, p, link
from datetime import datetime
import html

import news_parser
import logger
import topdf


def createHtmlStructure(url, channel, limit, html_document, html_path, pdf_path):
    '''
    1. in loop create html structure
    2. create html document or convert html structure into pdf
    '''
    #uncomment if u want html with styles
    # with html_document.head:
    #     styles = os.path.abspath('style.css')
    #     link(rel='stylesheet', href=styles)

    for index, item in enumerate(channel.entries):
        if (index == limit):
            break
        with html_document:
            with div():
                h2("Title: " + html.unescape(item.title))
                p("Link: " + item.link)
                media_content = news_parser.checkMediaContent(item)
                if (media_content):
                    img(src=media_content)
                description = news_parser.getDescription(item.description)
                if (description):
                    p("Description: " + description)

    if (html_path):
        intoHTML(html_document, html_path, url)
    else:
        intoPDF(html_document, pdf_path, url)


def intoHTML(html_document, html_path, url):
    '''
    1. create folder with html file
    2. write html structure in file
    '''
    if not os.path.exists(html_path):
        os.makedirs(html_path)
    time_name = datetime.strftime(datetime.now(), "%H%M%S")
    html_file = html_path + '/' + getSiteName(url) + '-' + time_name + '.html'

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(str(html_document))
        logger.logging.info("Successfull converting into html")


def getSiteName(url):
    regex = re.search(r"^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?([a-z0-9]+[\-\.]{1}[a-z0-9]+)*(\.[a-z]{2,5})(\/.*)?$", url)

    return ''.join(filter(None,regex.group(2,3)))


def intoPDF(doc, pdf_path, url):
    '''
    1. create folder with pdf file
    2. convert html into pdf
    '''
    if not os.path.exists(pdf_path):
        os.makedirs(pdf_path)
    time_name = datetime.strftime(datetime.now(), "%H%M%S")
    pdf_file = pdf_path + '/' + getSiteName(url) + '-' + time_name + '.pdf'

    topdf.convertHtmlToPdf(str(doc), pdf_file)
    logger.logging.info("Successfull converting into pdf")
