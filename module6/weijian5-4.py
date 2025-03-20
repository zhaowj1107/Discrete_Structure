'''
File: weijian5-5.py
Authors: Dayu/Lionel/David
Date: 2025-02-28
Class: CS_5002, Spring_2025
Description: 
Solving limit problems
'''

def limitation_flip_coin(n):
    """
    Calculates the probability of getting heads in a recursive coin flip scenario.
    The probability alternates between being based on the previous flip's outcome.
    Args:
        n (int): The number of recursive flips to calculate
    Returns:
        float: The probability of getting heads after n recursive flips
    >>> limitation_flip_coin(0)  # Base case
    0.5
    >>> limitation_flip_coin(1)  # 1 - (0.5/2)
    0.75
    >>> limitation_flip_coin(2)  # 1 - (0.75/2)
    0.625
    >>> limitation_flip_coin(3)  # 1 - (0.625/2)
    0.6875
    """
    if n == 0:
        return 1/2
    else:
        return 1 - (limitation_flip_coin(n - 1) / 2)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(round(limitation_flip_coin(20),6))
