import argparse
import iter1

parser = argparse.ArgumentParser(description='Pure Python command-line RSS reader')

parser.add_argument('source', action='store', help='RSS URL')
parser.add_argument('--version', action='store_true', help='Print version info')
parser.add_argument('--json', action='store_true', help='Print result as JSON in stdout')
parser.add_argument('--verbose', action='store_true', help='Outputs verbose status messages')
parser.add_argument('--limit', action='store', help='Limit news topics if this parameter provided')

args = parser.parse_args()


if (args.version):
    version = 1.0
    print(version)

elif(args.verbose):
    iter1.printLogs()

else:
    if not(args.limit):
        args.limit = 0
    iter1.getEntries(url, args.json, args.verbose, int(args.limit))

