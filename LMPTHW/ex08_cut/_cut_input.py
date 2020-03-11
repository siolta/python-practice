#!/usr/bin/env python3

import sys

_, delim, fields = sys.argv
split_at = [int(x) for x in field.split(',')]

def lines_of_input():
    try:
        while True:
            yield input()
    except EOFError:
        raise StopIteration

split_lines = (line.split(delim) for line in lines_of_input())

cuts = (line[split_at[0] for line in split_lines])

print("\n".join(cut for cut in cuts))
