import argparse
import rss_parser
import get_cache
import tohtml
import topdf

parser = argparse.ArgumentParser(description='Pure Python command-line RSS reader')

parser.add_argument('source', action='store', help='RSS URL')
parser.add_argument('--version', action='store_true', help='Print version info')
parser.add_argument('--json', action='store_true', help='Print result as JSON in stdout')
parser.add_argument('--verbose', action='store_true', help='Outputs verbose status messages')
parser.add_argument('--limit', action='store', help='Limit news topics')
parser.add_argument('--date', action='store', help='Print news from the specified day')
parser.add_argument('--tohtml', action='store', help='Convert news in html format')
parser.add_argument('--topdf', action='store', help='Convert news in pdf format')


args = parser.parse_args()


if (args.version):
    version = 1.0
    print(version)

elif(args.verbose):
    rss_parser.printLogs()

elif(args.date):
    get_cache.getCache(args.date)

elif(args.tohtml):
    if not(args.limit):
        args.limit = 0
    tohtml.getHTML(args.source, args.tohtml, int(args.limit))

elif(args.topdf):
    if not(args.limit):
        args.limit = 0
    topdf.getPDF(args.source, args.topdf, int(args.limit))

else:
    if not(args.limit):
        args.limit = 0

    rss_parser.getEntries(args.source, args.json, args.verbose, int(args.limit))

