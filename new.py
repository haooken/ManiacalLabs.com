#!/usr/bin/env python

from __future__ import print_function

import sys
import os
from datetime import datetime
import re


abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


def get_valid_filename(s):
    s = str(s).strip().replace(' ', '_')
    return re.sub(r'(?u)[^-\w.]', '', s)


valid_types = ['post', 'posts', 'buildlog', 'project', 'projects', 'product', 'products']


new_type = sys.argv[1].lower()
title = sys.argv[2]
title_path = get_valid_filename(title)
year = datetime.now().year
month = datetime.now().month

if new_type not in valid_types:
    if (new_type + 's') in valid_types:
        new_type = new_type + 's'
    else:
        print('{} is invalid type! Use one of {}'.format(new_type, ', '.join(valid_types)))
        sys.exit(1)


path = '{}/{}/{}/{}/index.md'.format(new_type, title_path, year, month)

res = os.system('hugo new {}'.format(path))

if res:
    print('Error running hugo new!')
    sys.exit(res)

new_path = './content/{}'.format(path)

# with open(new)
