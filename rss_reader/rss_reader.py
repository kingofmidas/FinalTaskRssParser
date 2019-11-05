import argparse
import feedparser
import os
import pdfkit
import random
import dominate
from dominate.tags import *
from datetime import date

import parse_news
import get_cache
import logger
import version
import converter


arguments = argparse.ArgumentParser(description='Pure Python command-line RSS reader')

arguments.add_argument('source', action='store', help='RSS URL')
arguments.add_argument('--version', action='store_true', help='Print version info')
arguments.add_argument('--json', action='store_true', help='Print result as JSON in stdout')
arguments.add_argument('--verbose', action='store_true', help='Outputs verbose')
arguments.add_argument('--limit', action='store', help='Limit news topics')
arguments.add_argument('--date', action='store', help='Print news from the specified day')
arguments.add_argument('--tohtml', action='store', help='Convert news in html format')
arguments.add_argument('--topdf', action='store', help='Convert news in pdf format')

args = arguments.parse_args()

try:
    # set object of feedparser library
    channel = feedparser.parse(args.source)
    print("Feed: ", channel.feed.title, '\n')
    
    # if no limit - take all news in channel
    if not (args.limit):
        args.limit = len(channel.entries)
    limit = int(args.limit)

    if (args.version):
        print(version.VERSION)

    elif (args.verbose):
        # Create file if not exist
        with open('parser.log', 'r') as f:
            for line in f:
                print(line)

    elif (args.date):

        if (len(args.date)==8):
            print(get_cache.getCache(int(args.date)))
        else:
            print("Length of date should be equals 8")

    elif (args.tohtml or args.topdf):

        # set object of html converter library
        doc = dominate.document(title="HTML document")
        random_name = random.randint(1, 120)

        for index, item in enumerate(channel.entries):
            if (index == limit):
                break
            
            media_content = parse_news.checkMediaContent(item)
          
            # create html structure
            with doc:
                with div():
                    h2(item.title)
                    p("Date: " + item.published)
                    if (media_content):
                        img(src=media_content)
                    p("Description: " + parse_news.getDescription(item.description))

        if (args.tohtml):
           converter.intoHTML(args.tohtml, doc, random_name)

        elif (args.topdf):
            converter.intoPDF(args.topdf, doc, random_name)

    else:

        for index, item in enumerate(channel.entries):
            if (index == limit):
                break

            # create folder for cache
            today = date.today().strftime("%Y%m%d")
            if not os.path.exists('cache/'):
                os.makedirs('cache/')
            cache_file = 'cache/' + today + '.txt'

            # cache news
            with open(cache_file, 'a', encoding="utf-8") as f:
                f.write("Title: " + item.title + '\n' +
                        "Link: " + item.link + '\n' +
                        "Description: " + parse_news.getDescription(item.description) + '\n')
     
            # log news
            logger.logging.debug("Title: " + str(item.title))
            logger.logging.debug("Date: " + str(item.published))
            logger.logging.debug("Link: " + str(item.link))
            logger.logging.debug("Description: " + parse_news.getDescription(item.description))
            logger.logging.debug("Links:"+"\n[1]: " + str(item.link) +
                        "(link)\n[2]: " + str(parse_news.checkMediaContent(item)))

            if (args.json):
                print(parse_news.intoJson(item))

            # print news
            print("Title: ", item.title)
            print("Date: ", item.published)
            print("Link: ", item.link, '\n')
            print("Description: ", parse_news.getDescription(item.description), '\n')
            print("Links:", "\n[1]: ", item.link, "(link)\n[2]: ",
                parse_news.checkMediaContent(item), '\n')

except ValueError as e:
    print("--limit or --date argument should be number")
    logger.logging.error("ValueError: " + str(e))

except AttributeError as e:
    print("AttributeError: " + str(e))
    print("Maybe check your source")
    logger.logging.error("AttributeError: " + str(e))

# fast paste in argument
# source = "https://news.yahoo.com/rss"
# source1 = "https://news.google.com/rss"
# source2 = "https://www.theguardian.com/world/rss"
