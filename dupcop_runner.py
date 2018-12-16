# -*- coding: utf-8 -*-

import logging
import argparse
import sys

from dupcop.dupcop import DupCop

def main():



    argparser = argparse.ArgumentParser(description='Delete identically duplicate files in a filesystem')
    argparser.add_argument('-s', '--source', help='Directory to deduplicate contents', required=True)
    argparser.add_argument('-dd', '--depth', help='Maxmimum directory depth to traverse (use 1 for current dir)', type=int, const=None, required=False)
    argparser.add_argument('--regex-ignore', help='Ignore files matching provided regex pattern', const=None, type=str, required=False)
    argparser.add_argument('--regex-whitelist', help='Only deduplicate files matching provided regex pattern', const=None, required=False)
    argparser.add_argument('--dry-run', help='Show what changes the script will make without deleting duplicates from the filesystem', action='store_true', required=False)
    argparser.add_argument('-d', '--debug', help='Enable debugging logging', action='store_true', required=False)
    argparser.add_argument('--only-remove-whitelist', help="Only remove files matching expression", const=None, type=str, required=False)

    args = argparser.parse_args()

    if args.debug:
        logging.basicConfig(steam=sys.stdout, level=logging.DEBUG)

    else:
        logging.basicConfig(steam=sys.stdout, level=logging.INFO)

    log = logging.getLogger('dupcop_runner')

    dcop = DupCop(logger=log)

    dcop.run(args.source, args.depth, args.regex_ignore, args.regex_whitelist, args.dry_run, args.only_remove_whitelist)

if __name__ == '__main__':
    main()
