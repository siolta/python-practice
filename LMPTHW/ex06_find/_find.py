#!/usr/bin/env python3

import argparse
import os
import subprocess
import glob # rewrite to use Path from pathlib?

def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--directory', default='.', help='directory to search in')
    parser.add_argument('-n', '--name', help='name of file or directory to look for')
    parser.add_argument('-t', '--type', choices=['file', 'directory'], default='file', help='type of file: executable, or directory')
    parser.add_argument('-e', '--exec', help='command to run on each file')
    parser.add_argument('-p', '--print', action='store_true', help='print out each file')

    return parser.parse_args()

def find_files(args):
    return glob.glob(f'{args.directory}/{args.name}')

def find_directories(args):
    return glob.glob(f'{args.directory}/**/')

def run_exec(args):
    _exec = subprocess.run([f'{args.exec}'], capture_output=True)
    return _exec.stdout.splitlines()

def run():
    args = parse_args()
    if args.type == 'file':
        items = find_files(args)
    elif args.type == 'directory':
        items = find_directories(args)

    for item in items:
        if args.print:
            print(item)
        if args.exec is not None:
            output = run_exec(args)
            for line in output:
                print(line.decode("utf-8"))


run()
