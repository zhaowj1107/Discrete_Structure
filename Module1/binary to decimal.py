'''
this program will convert a decimal number to binary
Author: David Zhao
Date: 2025-01-06

'''

def binary_to_decimal():
    binary = int(input("Enter a binary number: "))
    decimal = 0
    order = 0
    while binary > 0:
        remainder = binary % 10
        binary = binary // 10
        decimal = (2 ** order)*remainder + decimal
        print(decimal)
        print(remainder)
        print(order)
        print("-----------")
        order = order + 1
    print(decimal)
        
binary_to_decimal()
