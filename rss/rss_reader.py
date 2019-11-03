import argparse
import get_cache
import converter
import version
import feedparser
import parse_news

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


# def setParser(source):
#     channel = feedparser.parse(source)
#     print("Feed: ", channel.feed.title, '\n')
#     return channel


if not(args.limit):
    args.limit = 0


if (args.version):
    print(version.VERSION)

elif(args.verbose):
    parse_news.printLogs()

elif(args.date):
    get_cache.getCache(args.date)

elif(args.tohtml or args.topdf):

    if(args.tohtml):
        args.topdf = False
    elif(args.topdf):
        args.tohtml = False
    if not(args.limit):
        args.limit = 0

    converter.makeConvertion(args.source, args.tohtml, args.topdf, int(args.limit))

else:
    parse_news.printNews(args.source, args.json, int(args.limit))


# fast paste in argument
# source = "https://news.yahoo.com/rss"
# source1 = "https://news.google.com/rss"
# source2 = "https://www.theguardian.com/world/rss"
