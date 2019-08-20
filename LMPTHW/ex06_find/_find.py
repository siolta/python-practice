#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys
from pathlib import Path

def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument('dir', nargs=1, help='directory to search in')
    parser.add_argument('-n', '--name', help='name of file or directory to look for')
    parser.add_argument('-t', '--type', choices=['file', 'directory'], help='type of file: executable, or directory')
    parser.add_argument('-e', '--exec', help='command to run on each file')

    return parser.parse_args()

def find_by_name(_dir, args):
    for f in _dir.rglob(args.name):
        print(f)

def find_by_type(_dir, args):
    if args.type not in ['directory', 'file']:
        print(f'Unknown type: {args.type}')
        sys.exit(1)

    for f in Path(f'{_dir}').rglob(args.name or '*'):
        if args.type == 'file' and f.is_file():
            print(f)
        elif args.type == 'directory' and f.is_dir():
            print(f)

def run_exec(args):
    _exec = subprocess.run([f'{args.exec}'], capture_output=True)
    return _exec.stdout.splitlines()

def find_the_things(args):
    _dir = Path(args.dir[0])

    if args.name and not args.type:
        find_by_name(_dir, args)
    elif args.type:
        find_by_type(_dir, args)
    else:
        print("You need either --name or --type")
        sys.exit(1)    


find_the_things(parse_args())
