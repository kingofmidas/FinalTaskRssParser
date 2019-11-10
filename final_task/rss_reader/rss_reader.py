import arg_parser
import feedparser
import sys
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import dominate
import html

import news_parser
import logger
import get_cache
import converter


def main(channel, limit):
    '''
    1. cache news
    2. create html or pdf document
    3. or print in stdout news in json or normal format
    '''
    news_parser.cacheNews(args.source, channel)

    if (args.tohtml or args.topdf):
        html_document = dominate.document(title="HTML document")
        converter.createHtmlStructure(args.source, channel, limit, html_document, args.tohtml, args.topdf)
    else:
        for index, item in enumerate(channel.entries):
            if (index == limit):
                break
            logger.createLogs(item)

            if (args.json):
                print(news_parser.intoJson(item))
            else:
                print("\nTitle: ", html.unescape(item.title))
                print("Date: ", item.published)
                print("Link: ", item.link, '\n')
                description = news_parser.getDescription(item.description)
                if(description):
                    print("Description: ", description, '\n')
                print("Links:", "\n[1]: ", item.link, "(link)")
                media_content = news_parser.checkMediaContent(item)
                if(media_content):
                    print("\n[2]: ", media_content, '\n')


def checkArguments():
    '''Check if in argument are --version or --help'''
    if ('--version' in sys.argv or '--help' in sys.argv or '-h' in sys.argv):
        return False
    else:
        return True


class checkConnectionException(Exception):
    pass


def checkConnection(source):
    '''Check connection to server'''
    source = Request(source)
    try:
        response = urlopen(source)
    except Exception as e:
        raise checkConnectionException(e)
    else:
        logger.logging.info('Website is working')


if __name__ == "__main__":

    args = arg_parser.createArgparser()

    if (args.verbose):
        logger.makeVerbose()

    if (args.date):
        get_cache.convertCache(args.source, args.date, args.limit, args.tohtml, args.topdf)
    else:
        if (checkArguments()):
            try:
                checkConnection(args.source)

                # set object of feedparser library
                channel = feedparser.parse(args.source)
                print("Feed: ", channel.feed.title, '\n')
                limit = args.limit or len(channel.entries)

                main(channel, limit)
            except checkConnectionException as e:
                logger.logging.error("Connection error" + str(e))
                print("Connection error: ", e)
