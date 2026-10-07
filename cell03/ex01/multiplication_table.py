#!/usr/bin/env python3

try :
    num = int(input("Enter a number\n"))
except ValueError :
    exit()

for i in range(10) :
    print(i, "x", num, "=", i * num)
    i += 1
