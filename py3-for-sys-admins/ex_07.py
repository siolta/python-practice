import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', dest='file', required=True, help='the name of the file to print from')
parser.add_argument('-l', '--linenumber', type=int, required=True, help='the line number to print')

args = parser.parse_args()
line_list = []

try:
    with open(args.file) as f:
        for line in f:
            line_list.append()
except FileNotFoundError as e:
    print(f"Error: {e}")

if len(line_list) > 0:
    try:
        print(line_list[args.linenumber])
    except IndexError as e:
        print(f"Error: {e}")

