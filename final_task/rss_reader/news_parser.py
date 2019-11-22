from contextlib import closing
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import sqlite3
import psycopg2
import json
import time
import html
import os

from . import logg


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
    json_news = {
        'Title: ': html.unescape(item.title),
        'Date: ': item.published,
        'Link: ': item.link
        }
    description = getDescription(item.description)
    media_link = checkMediaContent(item)
    if(description):
        json_news['Description: '] = description
    if(media_link):
        json_news['Media link: '] = media_link
    return json.dumps(json_news)


def cacheNews(url, channel):
    '''
    1. connect to database
    2. create table in database
    3. insert news into table
    '''
    try:
        with closing(psycopg2.connect(database="postgres",user='postgres',password='rssreader',
                                    host='db',port='5432')) as con:
            with con.cursor() as cur:
                cur.execute("""CREATE TABLE IF NOT EXISTS news
                                (title text, link text, image bytea,
                                description text, pub_date_stamp real,
                                UNIQUE (title, link, pub_date_stamp))
                                """)
                insertNewsIntoTable(channel, cur)
                con.commit()
    except (Exception, psycopg2.DatabaseError) as e:
        logg.logging.error(str(e))


def insertNewsIntoTable(channel, con):
    '''
    1. fill table with news
    2. convert date into timestamp
    3. create folder with cache images in loop
    '''
    for index, item in enumerate(channel.entries):

        description = getDescription(item.description)

        pub_date = getPublishedDate(item.published)
        pub_date_stamp = time.mktime(datetime.strptime(pub_date, '%d %m %Y %H:%M:%S').timetuple())

        media_content = checkMediaContent(item)
        if (media_content):
            response = requests.get(media_content)
            image = psycopg2.Binary(response.content)

        row = (html.unescape(item.title), item.link, image, description, pub_date_stamp)
        try:
            con.execute("INSERT INTO news VALUES (%s,%s,%s,%s,%s)", row)
        except (Exception, psycopg2.DatabaseError) as e:
            logg.logging.error(str(e))


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

    month = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
            'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

    pub_date[1] = month[pub_date[1]]
    pub_date = ' '.join(pub_date)

    return pub_date
