#!/usr/bin/env python3

import sys
import requests
import json
from argparse import ArgumentParser

parser = ArgumentParser(description="Given a url and a format, prints the content of the url to a file")

parser.add_argument('url', help='URL to fetch content from')
parser.add_argument('-f', '--out-file', dest='file', help='File to send contents to')
parser.add_argument('-t', '--content-type', dest='type', choices=['json', 'html'], default='html', help='Type of content to return')

args = parser.parse_args()

response = requests.get(args.url)

if response.status_code != 200:
    print(f"Error fetching requested url: {response.status_code}")
    sys.exit(1)

if args.type.lower() == 'json':
    try:
        content = json.dumps(response.json())
    except ValueError:
        print("Error: Content is not JSON")
        sys.exit(1)

else:
    content = response.text

with open(args.file, 'w') as f:
    f.write(content)
    print(f"Content written to '{args.file}''")


