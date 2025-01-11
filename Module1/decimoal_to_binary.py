'''
this program will convert a decimal number to binary
Author: David Zhao
Date: 2025-01-06

'''

def decimal_to_binary(decimal):
    binary = 0
    order = 0    
    #Check if the value is positive.
    if decimal >= 0:

        while decimal > 0:
            print(f"This is order {order}.")
            remainder = decimal % 2
            decimal = decimal // 2
            binary = (10 ** order)*remainder +  binary
            print(decimal)
            print(f"The remainder is {remainder}")
            print("-----------")
            order = order + 1
        print(f"The binary number is 0d{binary}.")
    elif decimal < -128:
        print("Since we use 8 bits to represent the twos complement negative binary number, \nWe could only transfer a negative decimal number from -128 to -1.")
    else:
        decimal = decimal * -1
        decimal = 256 - decimal
        while decimal > 0:
            print(f"This is order {order}.")
            remainder = decimal % 2
            decimal = decimal // 2
            binary = (10 ** order)*remainder +  binary
            #print(decimal)
            print(f"The remainder is {remainder}")
            print("-----------")
            order = order + 1
        print(f"We use 8 bits to represent the twos complement negative binary number, \nThe binary number is 0d{binary}.")
    
def main():
    while True:
        decimal = input("Enter a decimal number: ")
        try:
            value = int(decimal)
        except ValueError:
            error_value = type(decimal)
            print(f"Your input type is {error_value}, please enter a valid integer.")
            continue
        # check if the input is a valid positive number
        decimal_to_binary(int(decimal))
        break


if __name__ == "__main__":
    main()



'''
        # another way to transfer decimal to negative binary number
        # did not figure out how to add 1 to the filpped binary number

        decimal = decimal * -1
        while decimal > 0:    
            remainder = decimal % 2
            decimal = decimal // 2
            binary = (10 ** order)*remainder +  binary
            print(f"The remainder is {remainder}")
            print("-----------")
            order = order + 1
        print(f"The magnitude of binary number is 0d{binary}.")

        binary_str = str(binary)
        binary_str = binary_str.zfill(8)
        binary_negative = "11111111"
        binary_negative = list(binary_negative)
        for i in range(8):
                if binary_str[i] == "1":
                    binary_negative[i] = "0"
                else:
                    binary_negative[i] = "1"
        binary_negative = "".join(binary_negative)
        print(f"We use 8 bits to represent the twos complement negative binary number, \nThe binary number is 0d{binary_negative}.")
'''