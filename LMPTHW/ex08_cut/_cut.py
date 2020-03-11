#!/usr/bin/env python3

import argparse


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('file')
    parser.add_argument('-d', dest='delim')

    return parser.parse_args()

args = parse_args()

with open(args.file) as f:
    for line in f.readlines():
        print(line.split(args.delim))
    

print(args)
