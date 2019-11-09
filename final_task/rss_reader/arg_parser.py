import argparse
import version

def createArgparser():
    '''Add argument commands'''
    arguments = argparse.ArgumentParser(description='Pure Python command-line RSS reader')

    arguments.add_argument('source', type=str, help='RSS URL')
    arguments.add_argument('--version', action='version', version=f'{version.VERSION}',
                            help='Print version info')
    arguments.add_argument('--json', action='store_true', help='Print result as JSON in stdout')
    arguments.add_argument('--verbose', action='store_true', help='Outputs verbose')
    arguments.add_argument('--limit', action='store', type=int, help='Limit news topics')
    arguments.add_argument('--date', action='store', help='Print news from the specified day')
    arguments.add_argument('--tohtml', action='store', help='Convert news in html format')
    arguments.add_argument('--topdf', action='store', help='Convert news in pdf format')

    return arguments.parse_args()