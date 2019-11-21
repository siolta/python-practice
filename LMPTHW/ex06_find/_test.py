#!/usr/bin/env python3

import subprocess


_out = subprocess.Popen(['ls', '-lah', '.'], 
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.STDOUT,
                        universal_newlines=True)

stdout, stderr = _out.communicate()

print(stdout)
print(stderr)
