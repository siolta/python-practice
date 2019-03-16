#!/usr/bin/env python3

import sys

args = sys.argv

print(len(sys.argv))
print(args)

if "-h" in args:
    print(f"""this is the help message""")

if "-a1" in args:
    print(f"test arg_1 is: -a1  | Val is: {args[args.index('-a1') + 1]}")

if "-a2" in args:
    print(f"test arg_1 is: -a2  | Val is: {args[args.index('-a2') + 1]}")

if "-a3" in args:
    print(f"test arg_1 is: -a3  | Val is: {args[args.index('-a3') + 1]}")


print(f"the last arg is: {args[len(args)-1]}")
