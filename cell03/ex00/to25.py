#!/usr/bin/env python3

try :
    num = int(input("Enter a number less than 25\n"))
except ValueError :
    exit()

if num > 25 :
    print("Error")
else :
    while num <= 25 :
        print("Inside the loop, my variable is ", num)
        num += 1
