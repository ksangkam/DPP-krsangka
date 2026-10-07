#!/usr/bin/env python3

try :
    num1 = int(input("Give me the first number: "))
    num2 = int(input("Give me the second number: "))

    print("Thank you!")
    print(num1, "+", num2, "=", num1 + num2)
    print(num1, "-", num2, "=", num1 - num2)
    print(num1, "/", num2, "=", num1 / num2)
    print(num1, "*", num2, "=", num1 * num2)
except ValueError :
    pass
