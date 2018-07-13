#!/usr/bin/env python

from __future__ import print_function

import sys
import os
from datetime import datetime
import re
import subprocess


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def get_valid_filename(s):
    s = str(s).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', s)


valid_types = ['posts', 'buildlog', 'projects', 'products']


new_type = sys.argv[1].lower()
title = sys.argv[2]
title_path = get_valid_filename(title)
year = datetime.now().year
month = datetime.now().month

if new_type not in valid_types:
    if (new_type + 's') in valid_types:
        new_type = (new_type + 's')
    else:
        print('{} is invalid type! Use one of {}'.format(new_type, ', '.join(valid_types)))
        sys.exit(1)


path = '{}/{}/{}/{}/index.md'.format(new_type, year, month, title_path)

cmd = 'hugo new {}'.format(path)
print(cmd)

p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
output = output.decode("utf-8")
res = p.wait()
print(output)
if res:
    print('Error running hugo new!')
    sys.exit(res)

full_path = output.replace(' created\n', '')

with open(full_path, 'r+') as f:
    content = f.read()
    f.truncate()
    f.seek(0)
    f.write(content.replace('$$TITLE$$', title))
    f.flush()

print("""
New doc created @ {}
Static resources may be included in the same directory
and referenced as a relative path.
""".format(full_path))