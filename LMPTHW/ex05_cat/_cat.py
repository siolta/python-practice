#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()

parser.add_argument(nargs='+', dest='files', help="a list of files to print lines from")
parser.add_argument('-n', action="store_true", dest='number')
parser.add_argument('-b', action="store_true", dest='blank_number')
parser.add_argument('-s', action="store_true", dest='squeeze', help="Not currently working as expected")

files = parser.parse_args().files
number = parser.parse_args().number
blank_number = parser.parse_args().blank_number
squeeze = parser.parse_args().squeeze
print(files)

line_count = 1

for file in files:
    with open(file) as f:
        lines = f.readlines()
        prev_line = lines[0]
        for line in lines:
            if number:
                print(f"{line_count} : {line.strip()}")
                line_count += 1
            elif blank_number:
                if line.strip():
                    print(f"{line_count} : {line.strip()}")
                    line_count += 1
                else:
                    print(f"  : {line.strip()}")
            elif squeeze:
                if not line.strip() and prev_line.strip():
                    print(line.strip())
                    prev_line = line
                    pass
                else:
                    print(line.strip())

            else:
                print(line.strip())


