#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()

parser.add_argument(nargs='+', dest='files', help="a list of files to print lines from")
parser.add_argument('-n', action="store_true", dest='number')
parser.add_argument('-b', action="store_true", dest='blank_number')
parser.add_argument('-s', action="store_true", dest='squeeze', help="Not currently working as expected")

args = parser.parse_args()

print(args.files)

line_number = 1

for file in args.files:
    with open(file) as f:
        lines = f.readlines()
        prev_line = lines[0]
        for line in lines:
            if args.number:
                print(f"{line_number} : {line.strip()}")
                line_number += 1
            elif args.blank_number:
                if line.strip():
                    print(f"{line_number} : {line.strip()}")
                    line_number += 1
                else:
                    print(f"  : {line.strip()}")
            elif args.squeeze:
                if not line.strip() and prev_line.strip():
                    print(line.strip())
                    prev_line = line
                    pass
                else:
                    print(line.strip())

            else:
                print(line.strip())


