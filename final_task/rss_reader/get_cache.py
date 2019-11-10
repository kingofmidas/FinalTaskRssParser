import dominate
from dominate.tags import div, h2, img, p, link
import sqlite3
from datetime import datetime
import time
import os
import base64

import logger
import converter
import rss_reader


def dateToStamp(arg_date):
    '''
    1. convert --date into timestamp
    '''
    arg_date = str(arg_date)
    arg_date = time.mktime(datetime.strptime(arg_date, '%Y%m%d').timetuple())
    return arg_date


def convertCache(url, arg_date, limit, html_path, pdf_path):
    '''
    1. connect to database
    2. select from table news with published date equals --date
    3. convert news into html or pdf if there are --tohtml or --topdf arguments
    3. or print news in stdout
    '''
    conn = sqlite3.connect("newsdatabase.db")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT title, link, image, description FROM news WHERE pub_date_stamp >= ? and pub_date_stamp < ? ",
                    (dateToStamp(arg_date), dateToStamp(int(arg_date) + 1)))
    except sqlite3.OperationalError as e:
        print("No such table")
        logger.logging.error(str(e))

    records = cursor.fetchall()

    if (html_path is None and pdf_path is None):
        for index, row in enumerate(records):
            if(limit and index == limit):
                break
            print("\nTitle: ", row[0])
            print("Link: ", row[1], '\n')
            if (row[3]):
                print("Description: ", row[3], '\n')
    else:
        createHtmlStructure(records, limit, html_path, pdf_path, url)

        cursor.close()
        conn.close()


def createHtmlStructure(records, limit, html_path, pdf_path, url):
    '''
    1. in loop create html structure
    2. create html document or convert html structure into pdf
    '''
    html_document = dominate.document(title="HTML document")
    #uncomment if u want html with styles
    # with html_document.head:
    #     styles = os.path.abspath('style.css')
    #     link(rel='stylesheet', href=styles)

    for index, row in enumerate(records):
        if(limit and index==limit):
            break
        with html_document:
            with div():
                h2("Title: " + row[0])
                p("Link: " + row[1])
                if (row[2]):
                    img(src="data:image/jpg;base64," + base64.b64encode(row[2]).decode('ascii'))
                if (row[3]):
                    p("Description: " + row[3])

    if (html_path):
        converter.intoHTML(html_document, html_path, url)
    elif (pdf_path):
        converter.intoPDF(html_document, pdf_path, url)