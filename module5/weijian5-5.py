'''
File: weijian5-5.py
Authors: John/Sia/David
Date: 2025-02-14
Class: CS_5002, Spring_2025
Description: 
solve combination and pascal tri with recursion
-----------------
'''

def combination(n, k):
    '''
    combinations of n items taken k
    Args:
        n (int): Total number of items
        k (int): Number of items to choose
    Returns:
        int: Number of combinations
    >>> combination(5, 2)
    10
    >>> combination(10, 3)
    120
    >>> combination(7, 0)
    1
    >>> combination(7, 7)
    1
    '''
    if k == 0:
        return 1
    else:
        return n * combination(n - 1, k - 1) // k

def pascal_tri(n = None):
    '''
    Generates and prints Pascal's Triangle up to row n, and calculates combinations.
    Args:
        n (int): The number of rows to generate in Pascal's Triangle
    Returns:
        None
    >>> pascal_tri(3)
    c(6, 3) = 20
    The result by using pascal triangle is 20
    20
    >>> pascal_tri(2)
    c(4, 2) = 6
    The result by using pascal triangle is 6
    6
    >>> pascal_tri(4)
    c(8, 4) = 70
    The result by using pascal triangle is 70
    70
    '''
    if n is None:
        n = int(input("please fill a positive int below 50:"))
    while n > 50 or n < 0 :
        n = int(input("please fill a int below 50:"))
    result_direct = combination(2 * n, n)
    print(f"c({2 * n}, {n}) = {result_direct}")
    result_indirect = 0
    n_stable = n
    while n >= 0:
        result_indirect = result_indirect + combination(n_stable, n) ** 2
        n = n - 1
    print(f"The result by using pascal triangle is {result_indirect}")
    return result_indirect


if __name__ == "__main__":
    import doctest
    doctest.testmod()