#!/usr/bin/env python3

try :
    num = float(input("Give me a number: "))
    if num == int(num) :
        print("This number is an integer.")
    else :
        print("This number is a decimal.")
except ValueError :
    pass