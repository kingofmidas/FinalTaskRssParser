import os
import pdfkit
from dominate.tags import div, h2, img, p, link
from datetime import datetime

import news_parser
import logger


def createHtmlStructure(channel, limit, html_document, html_path, pdf_path):
    '''
    1. in loop create html structure
    2. create html document or convert html structure into pdf
    '''
    with html_document.head:
        styles = os.path.abspath('style.css')
        link(rel='stylesheet', href=styles)
    for index, item in enumerate(channel.entries):
        if (index == limit):
            break
        with html_document:
            with div():
                h2("Title: " + item.title)
                p("Link: " + item.link)
                media_content = news_parser.checkMediaContent(item)
                if (media_content):
                    img(src=media_content)
                p("Description: " + news_parser.getDescription(item.description))

    if (html_path):
        intoHTML(html_document, html_path)
    else:
        intoPDF(html_document, pdf_path)


def intoHTML(html_document, html_path):
    '''
    1. create folder with html file
    2. write html structure in file
    '''
    if not os.path.exists(html_path):
        os.makedirs(html_path)
    time_name = datetime.strftime(datetime.now(), "%H%M%S")
    html_file = html_path + '/' + time_name + '.html'

    with open(html_file, 'w') as f:
        f.write(str(html_document))
        logger.logging.info("Successfull converting into html")


def intoPDF(doc, pdf_path):
    '''
    1. create folder with pdf file
    2. convert html into pdf
    '''
    if not os.path.exists(pdf_path):
        os.makedirs(pdf_path)
    time_name = datetime.strftime(datetime.now(), "%H%M%S")
    pdf_file = pdf_path + '/' + time_name + '.pdf'

    pdfkit.from_string(str(doc), pdf_file)
    logger.logging.info("Successfull converting into pdf")
