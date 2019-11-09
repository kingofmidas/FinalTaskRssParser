from bs4 import BeautifulSoup
import json
import os
import urllib.request
from datetime import datetime
import time
import sqlite3
import  html


def checkMediaContent(item):
    '''check if there is media content'''
    media_content = ''
    if ('media_content' in item.keys()):
        media_content = item.media_content[0]['url']
    elif ('media_thumbnail' in item.keys()):
        media_content = item.media_thumbnail[0]['url']
    return media_content


def getDescription(item):
    '''return description without html tags'''
    return BeautifulSoup(item, features="html.parser").getText()


def intoJson(item):
    '''print news in json format'''
    return json.dumps({
        'Title: ': html.unescape(item.title),
        'Date: ': item.published,
        'Link: ': item.link,
        'Description: ': getDescription(item.description),
        'Media_link': checkMediaContent(item)
        })


def cacheNews(url, channel):
    '''
    1. connect to database
    2. create table in database
    3. insert news into table
    '''
    conn = sqlite3.connect("newsdatabase.db")
    cursor = conn.cursor()

    try:
        cursor.execute("""CREATE TABLE news
                        (title text, link text, image text, 
                        description text, pub_date_stamp real,
                        UNIQUE (title, link, pub_date_stamp))
                        """)
    except:
        print("Table already exists")

    insertNewsIntoTable(channel, cursor)
    conn.commit()
    cursor.close()
    conn.close()


def insertNewsIntoTable(channel, cursor):
    '''
    1. fill table with news
    2. convert date into timestamp
    3. create folder with cache images in loop
    '''
    for index, item in enumerate(channel.entries):

        descr = getDescription(item.description)

        pub_date = getPublishedDate(item.published)
        pub_date_stamp = time.mktime(datetime.strptime(pub_date, '%d %m %Y %H:%M:%S').timetuple())

        if not os.path.exists('cache_images/'):
            os.makedirs('cache_images/')
        time_name = datetime.strftime(datetime.now(), "%H%M%S") + str(index)
        image_file_name = 'cache_images/' + time_name + '.jpg'
        if (checkMediaContent(item)):
            urllib.request.urlretrieve(checkMediaContent(item), image_file_name)

        row = (html.unescape(item.title), item.link, descr, os.path.abspath(image_file_name), pub_date_stamp)
        try:
            cursor.execute("INSERT INTO news VALUES (?,?,?,?,?)", row)
        except sqlite3.IntegrityError:
            pass


def isEmpty(cursor):
    '''
    1. check if table is empty
    '''
    cursor.execute("SELECT COUNT(*) FROM news")
    exist = cursor.fetchone()
    if not(exist[0]):
        return True
    else:
        return False


def getPublishedDate(pub_date):
    '''
    1. convert published date into --date argument format
    '''
    pub_date = ((pub_date).split(' ')[1:5])

    month = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06',
            'Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

    pub_date[1] = month[pub_date[1]]
    pub_date = ' '.join(pub_date)

    return pub_date
