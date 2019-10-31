import argparse
import iter1
import iter3

parser = argparse.ArgumentParser(description='Pure Python command-line RSS reader')

parser.add_argument('source', action='store', help='RSS URL')
parser.add_argument('--version', action='store_true', help='Print version info')
parser.add_argument('--json', action='store_true', help='Print result as JSON in stdout')
parser.add_argument('--verbose', action='store_true', help='Outputs verbose status messages')
parser.add_argument('--limit', action='store', help='Limit news topics if this parameter provided')
parser.add_argument('--date', action='store', help='Print news from the specified day')

args = parser.parse_args()


if (args.version):
    version = 1.0
    print(version)

elif(args.verbose):
    iter1.printLogs()

elif(args.date):
    iter3.getCache(args.date)

else:
    if not(args.limit):
        args.limit = 0
    iter1.getEntries(args.source, args.json, args.verbose, int(args.limit))

