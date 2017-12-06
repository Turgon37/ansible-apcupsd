#!/usr/bin/env python

import json
import os
import re
import subprocess
import sys

content=dict()

# 6.6.1p1 style formatting
# 7.2p2 style formatting
version_re = re.compile('^apcupsd\s*(?P<version>(?P<major>[0-9]+)[^ ]+)')
try:
    result = subprocess.Popen(['/usr/bin/env', 'apcupsd', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    (stdout, stderr) = result.communicate()
    match = version_re.search(stdout)
    if match:
        content['version_full'] = match.group('version')
        content['version_major'] = match.group('major')
except subprocess.CalledProcessError as e:
    content['error'] = str(e)

if len(content) == 0:
    content = None

print(json.dumps(content))
sys.exit(0)
