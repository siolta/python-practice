#!/usr/bin/env python3

import argparse
import sys

# Build the parser
parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0.0')

# Parse the arguments
args = parser.parse_args()

# read the file, reverse the contents and print
try:
    f = open(args.filename)
    limit = args.limit
except FileNotFoundError as e:
    print(f"Error: {e}")
    sys.exit(2)
else:
    with open(args.filename) as f:
        lines = f.readlines()
        lines.reverse()

        if args.limit:
            lines = lines[:limit]

        for line in lines:
            print(line.strip()[::-1])
