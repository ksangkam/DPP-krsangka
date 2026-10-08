#!/usr/bin/env python3

import sys
import re

if len(sys.argv) != 3:
    print("none")
    sys.exit()

keyword = sys.argv[1]
text = sys.argv[2]

matches = re.findall(re.escape(keyword), text)

if not matches:
    print("none")
else:
    print(len(matches))
