'''
File: weijian3-5.py
Authors: Weijian(David)
Date: 2025-01-29
Class: CS_5002, Spring_2025
Description: 
The program calculates the Prob of given set with out certain digits.
'''

def user_input():
    """
    Function user_input()
    Parameters: nothing
    Returns: one int value
    Prompts the user for a valid positive integer input.
    """
    print("Please noted: any number above 8 will be extremely slow.")
    expo_number = int(input('Enter a positive interger: '))
    while expo_number < 1:
        print("Invalid input number. Please try again\n")
        expo_number = int(input('Enter a positive interger: '))
    return expo_number

def contain_5(number, digit = 5):
    """
    Function contain_5
    Parameters: number
    Returns: Boolean value
    Tell if this integer contain 5
    >>> contain_5(12345)
    True
    >>> contain_5(1234)
    False
    >>> contain_5(50505)
    True
    >>> contain_5(1234, 4)
    True
    """
    result = []
    if number == 0:
        return [0]
    while number > 0:
        number, per_digit = number // 10, number % 10
        result.append(per_digit)
    
    return (digit in result)

def main(n = None):
    """
    Function main()
    Parameters: n (optional) - positive integer representing number of digits
    Returns: float - probability of numbers containing digit 5
    
    Calculates probability of numbers containing digit 5 in range of n-digit numbers.
    If no argument provided, prompts user for input.
    
    >>> main(1)  # Testing single digit numbers (1-9)
    The total number that do not contain 5 is 8.
    The total number that contain 5 is 1.
    The range is from 1 to 10
    The prob of that is 0.111
    0.111
    >>> main(2)  # Testing two-digit numbers (10-99)
    The total number that do not contain 5 is 72.
    The total number that contain 5 is 18.
    The range is from 10 to 100
    The prob of that is 0.2
    0.2
    >>> main(3)  # Testing three-digit numbers (100-999)
    The total number that do not contain 5 is 648.
    The total number that contain 5 is 252.
    The range is from 100 to 1000
    The prob of that is 0.28
    0.28
    >>> main(4)  # Testing three-digit numbers (1000-9999)
    The total number that do not contain 5 is 5832.
    The total number that contain 5 is 3168.
    The range is from 1000 to 10000
    The prob of that is 0.352
    0.352
    """
    if n is None:
        n = user_input()
    counter_not_5 = 0
    counter_5 = 0
    total_number = len(range(10 ** (n - 1), 10 ** n))
    for number in range(10 ** (n - 1), 10 ** n):
        if contain_5(number):
            counter_5 += 1
        else:
            counter_not_5 +=1
    print(f"The total number that do not contain 5 is {counter_not_5}.")
    print(f"The total number that contain 5 is {counter_5}.")
    print(f"The range is from {10 ** (n - 1)} to {10 ** n}")
    print(f"The prob of that is {round((counter_5/total_number),3)}")
    return round((counter_5/total_number),3)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    main(4)