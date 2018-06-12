import sys
import os
import glob
import re

re_search = '\[\!\[(.*)\]\((.*\))\n\]\((.*\))'


if __name__ == '__main__':
    in_dir = sys.argv[1]
    all_files = glob.glob('{}/*.md'.format(in_dir), recursive=True)
    for f in all_files:
        with open(f, 'r+', encoding="utf8") as fo:
            data = fo.read()

        matches = re.findall(re_search, data)
        if matches:
            print(f)
            replace = {}
            for m in matches:
                cap = m[0]
                thumb = m[1][:-1]
                img = m[2][:-1]
                og = '[![{}]({})\n]({})'.format(cap, thumb, img)
                rep = '{{< figure src="' + img + '" caption="' + cap + '" >}}'
                replace[og] = rep

            for k, v in replace.items():
                data = data.replace(k, v)

            with open(f, 'w', encoding="utf8") as f_out:
                f_out.write(data)
