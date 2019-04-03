#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', dest='file', required=True, help='the name of the file to print from')
parser.add_argument('-l', '--linenumber', type=int, required=True, help='the line number to print')

args = parser.parse_args()

try:
    lines = open(args.file).readlines()
    line = lines[args.linenumber -1]
except FileNotFoundError as e:
    print(f"Error: {e}")
except IndexError as e:
    print(f"Error: {e}")
else:
    print(line)
