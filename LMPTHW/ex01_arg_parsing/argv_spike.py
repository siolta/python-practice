#!/usr/bin/env python3

import sys

args = sys.argv

print(len(sys.argv))
print(args)

if "-h" in args:
    print(f"""this is the help message""")

if "-f1" in args:
    print(f"""this is the flag1 message""")

if "-f2" in args:
    print(f"""this is the flag2 message""")

if "-f3" in args:
    print(f"""this is the flag3 message""")

if "-a1" in args:
    print(f"test arg_1 is: -a1  | Val is: {args[args.index('-a1') + 1]}")
    position = args.index('-a1') + 2

if "-a2" in args:
    print(f"test arg_2 is: -a2  | Val is: {args[args.index('-a2') + 1]}")
    position = args.index('-a2') + 2

if "-a3" in args:
    print(f"test arg_3 is: -a3  | Val is: {args[args.index('-a3') + 1]}")
    position = args.index('-a3') + 2

if '-' not in args[len(args) -1 ]:
    for arg in range(position, len(args)):
        print(f"test posit arg_{position} is: {args[arg]}")
        position += 1
