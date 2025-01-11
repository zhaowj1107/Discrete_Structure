'''
this program will convert one base number represetation to another
Author: David Zhao
Date: 2025-01-06

'''

def represetation_tranfer(base1,base2):
    print(f"We will trafer a number from base{base1} to base{base2}")
    base1_num = int(input(f"Enter a base{base1} number: "))
    decimal = 0
    base2_num = 0
    order = 0
    # transfer base1 number to decimal number
    while base1_num > 0:
        remainder = base1_num % 10
        base1_num = base1_num // 10
        decimal = (base1 ** order)*remainder + decimal
        #print(decimal)
        #print(remainder)
        #print(order)
        #print("-----------")
        order = order + 1
    print(f"the decimal number is {decimal}")

    # transfer decimal number to base2 number
    order = 0
    remainder = 0
    while decimal > 0:
        remainder = decimal % base2
        decimal = decimal // base2
        base2_num = (10 ** order)*remainder + base2_num
        #print(base2_num)
        #print(remainder)
        #print(order)
        #print("-----------")
        order = order + 1
    print(f"the base{base2} number is {base2_num}")
