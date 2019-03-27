#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="Tests out the functionality of argparse")
parser.add_argument('--arg1', action='store_true', help='sets arg1')
parser.add_argument('--arg2', action='store_true', help='sets arg2')
parser.add_argument('--arg3', action='store_true', help='sets arg3')
parser.add_argument('--opt1', help='an optional string to print')
parser.add_argument('--opt2', help='an optional string to print')
parser.add_argument('--opt3', help='an optional string to print')
parser.add_argument('--files', nargs='+', help='files to read out')

args = parser.parse_args()

if args.arg1:
    print('Arg1 set')

if args.arg2:
    print('Arg2 set')

if args.arg3:
    print('Arg3 set')

if args.opt1:
    print(f'Opt1 set to {args.opt1}')

if args.opt2:
    print(f'Opt2 set to {args.opt2}')

if args.opt3:
    print(f'Opt3 set to {args.opt3}')

if args.files:
    for file in args.files:
        with open(file) as f:
            for line in f:
                print(line.strip())
