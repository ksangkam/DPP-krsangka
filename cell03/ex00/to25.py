#!/usr/bin/env python3

print("Enter a number less than 25")
try :
    num = int(input())
except ValueError :
    exit()

if num > 25 :
    print("Error")
else :
    while num <= 25 :
        print("Inside the loop, my variable is ", num)
        num += 1
