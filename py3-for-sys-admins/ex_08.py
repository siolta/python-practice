#!/usr/bin/env python3

import sys
import subprocess
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port', dest='port',
                    required=True, help='the port to search for')

port = parser.parse_args().port
cmd = ["lsof", "-n", f"-i4TCP:{port}"]

try:
    result = subprocess.run(cmd, capture_output=True)   
except subprocess.CalledProcessError as e:
    print(f"No process running on port: {port}")
    sys.exit(1)
else:
    listening = None

    for line in result.stdout.splitlines():
        if "LISTEN" in str(line):
            listening = line
            break
        
    if listening:
        # PID is second column in the output
        pid = int(listening.split()[1])
        os.kill(pid, 9)
        print(f"Killed process {pid}")
    else:
        print(f"No process listening on port {port}")
        sys.exit(1)
