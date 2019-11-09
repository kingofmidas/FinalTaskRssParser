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
        converter.createHtmlStructure(channel, limit, html_document, args.tohtml, args.topdf)
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
                print("Description: ", news_parser.getDescription(item.description), '\n')
                print("Links:", "\n[1]: ", item.link, "(link)\n[2]: ",
                      news_parser.checkMediaContent(item), '\n')


def checkArguments():
    '''Check if in argument are --version or --help'''
    if ('--version' in sys.argv or '--help' in sys.argv or '-h' in sys.argv):
        return False
    else:
        return True


def checkConnection(source):
    '''Check connection to server'''
    source = Request(source)
    try:
        response = urlopen(source)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
        logger.logging.error("HTTPError: " + str(e))
        sys.exit()
    except URLError as e:
        print('Failed to reach a server.')
        print('Reason: ', e.reason)
        logger.logging.error("URLError: " + str(e))
        sys.exit()
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
            checkConnection(args.source)
            # set object of feedparser library
            channel = feedparser.parse(args.source)
            print("Feed: ", channel.feed.title, '\n')
            limit = args.limit or len(channel.entries)

            main(channel, limit)

# for faste paste
# python rss_reader.py https://news.yahoo.com/rss
# python rss_reader.py https://news.google.com/rss
# python rss_reader.py https://www.theguardian.com/world/rss
