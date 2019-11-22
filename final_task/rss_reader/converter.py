from dominate.tags import div, h2, img, p, link
import dominate
from datetime import datetime
import os
import html

from . import news_parser, topdf


def createHtmlStructure(channel, limit, html_path, pdf_path):
    '''
    1. in loop create html structure
    2. return html_structure or file name of pdf document
    '''
    html_document = dominate.document(title="HTML document")

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
        return str(html_document)
    else:
        return intoPDF(html_document, pdf_path)


def intoPDF(doc, pdf_path):
    '''
    1. create folder with pdf file
    2. convert html into pdf
    3. return only filename for send_from_directory function
    '''
    if not os.path.exists(pdf_path):
        os.makedirs(pdf_path)
    time_name = datetime.strftime(datetime.now(), "%H%M%S")
    file_name = 'NewsFeed' + '-' + time_name + '.pdf'
    pdf_file = os.path.join(pdf_path, file_name)

    topdf.convertHtmlToPdf(str(doc), pdf_file)
    return file_name
