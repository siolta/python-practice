#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="Tests out the functionality of argparse")
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')



# 1 Get help with -h / --help

# 2 three flag arguments that don't take arguments

# 3 three argumements that take options, and set a variable

# 4 positional arguments 
