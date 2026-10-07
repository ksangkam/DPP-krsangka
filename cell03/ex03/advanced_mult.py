#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    print("none")
    sys.exit()

i = 0
while i <= 10:
    print("Table de "+ str(i) + ": ", end="")
    j = 0
    while j <= 10:
        print(i * j , end=" ")
        j += 1
    print()
    i += 1
