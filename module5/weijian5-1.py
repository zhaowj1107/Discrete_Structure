'''
File: weijian5-1.py
Authors: Weijian(David)
Date: 2025-02-13
Class: CS_5002, Spring_2025
Description: 
solve the lock permutation and combination pizzle
-----------------
The following 3 funtions are calculating the result directly.
problem_part_a(n)
problem_part_b(n)
problem_part_c(n)

The following 3 funtions are building the result list, and print the list/ return the length

problem_part_a_iter(n)
problem_part_b_iter(n)
problem_part_c_iter(n)
'''

TOTAL_DIGIT = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def problem_part_a(n = 3):
    """
    Calculate the number of possible combinations for an n-digit lock using only odd digits.
    Args:
        n (int): Number of digits in the lock combination
    Returns:
        int: Number of possible combinations using only odd digits
    >>> problem_1(1)
    5
    >>> problem_1(2)
    25
    >>> problem_1(3)
    125
    """
    if n <= 0:
        return 0
    ODD_DIGIT = list(x for x in TOTAL_DIGIT if x % 2 == 1)
    length_odd = len(ODD_DIGIT)
    print(f"The direct answer of problem a is {length_odd ** n}")
    return length_odd ** n

def problem_part_b(n = 3):
    """
    Calculate the number of possible combinations for an n-digit lock where each digit is unique.
    Args:
        n (int): Number of digits in the lock combination
    Returns:
        int: Number of possible combinations with unique digits
    >>> problem_part_b(1)
    10
    >>> problem_part_b(2)
    90
    >>> problem_part_b(3)
    720
    """
    if n <= 0:
        return 0
    length_odd = len(TOTAL_DIGIT)
    total_comb = 1
    for index in range(n):
        total_comb, length_odd = total_comb * length_odd, length_odd - 1
    print(f"The direct answer of problem b is {total_comb}")
    return total_comb

def problem_part_c(n = 3):
    """
    Calculate the number of possible combinations for an n-digit lock where digits are in strictly increasing order.
    Args:
        n (int): Number of digits in the lock combination
    Returns:
        int: Number of possible combinations with strictly increasing digits
    >>> problem_part_c(1)
    10
    >>> problem_part_c(2)
    45
    >>> problem_part_c(3)
    120
    """
    if n <= 0:
        return 0
    elif n > 9:
        print("n must be a integer between 1 and 9.")
        return None
    length_odd = len(TOTAL_DIGIT)
    total_comb = 1
    dividor = 1
    for index in range(n):
        total_comb, length_odd, dividor = total_comb * length_odd , length_odd - 1, dividor * (index + 1)
    print(f"The direct answer of problem c is {int(total_comb / dividor)}")
    return int(total_comb / dividor)



def problem_part_a_iter(n = 3):
    """
    Calculate the number of possible combinations for an n-digit lock where all digits are odd numbers.
    Uses an iterative approach to solve the problem.
    Args:
        n (int): Number of digits in the lock combination
    Returns:
        int: Number of possible combinations with all odd digits
    >>> problem_part_a_iter(1)
    5
    >>> problem_part_a_iter(2)
    25
    >>> problem_part_a_iter(3)
    125
    """
    if n <= 0:
        return 0
    ODD_DIGIT = list(x for x in TOTAL_DIGIT if x % 2 == 1)
    result_list = []
    stable_biggest_number = 10**(n)-1
    biggest_number = 10**(n)-1
    while biggest_number >= stable_biggest_number // 10 + 1:
        list_letter = list(str(biggest_number))
        if_true = 1
        for number_letter in list_letter:
            if int(number_letter) in ODD_DIGIT:
                continue
            else:
                if_true = 0
                break
        if if_true == 1:
            result_list.append(str(biggest_number))
        biggest_number -= 1
    print("Here is the set of valid codes")
    print(result_list)
    print(f"The total number of valid codes is {len(result_list)}")
    return len(result_list)
    


def problem_part_b_iter(n = 3):
    """
    Calculate the number of possible combinations for an n-digit lock where each digit is unique.
    Uses an iterative approach to solve the problem.
    Args:
        n (int): Number of digits in the lock combination
    Returns:
        int: Number of possible combinations with unique digits
    >>> problem_part_b_iter(1)
    10
    >>> problem_part_b_iter(2)
    90
    >>> problem_part_b_iter(3)
    720
    """
    result_list = []
    biggest_number = 10**(n)-1
    while biggest_number >= 0:
        if_true = 1
        for number_index in range(n-1):
            for number_index1 in range(number_index + 1, n):
                if int(str(biggest_number).zfill(n)[number_index]) != int(str(biggest_number).zfill(n)[number_index1]):
                    continue
                else:
                    if_true = 0
                    break
        if if_true == 1:
            number_str_form = str(biggest_number).zfill(n)
            result_list.append(number_str_form)
        biggest_number -= 1
    print("Here is the set of valid codes")
    print(result_list)
    print(f"The total number of valid codes is {len(result_list)}")
    return len(result_list)

def problem_part_c_iter(n = 3):
    """
    Calculate the number of possible combinations for an n-digit lock where digits are in strictly increasing order.
    Args:
        n (int): Number of digits in the lock combination
    Returns:
        int: Number of possible combinations with strictly increasing digits
    >>> problem_part_b_iter(1)
    10
    >>> problem_part_b_iter(2)
    45
    >>> problem_part_b_iter(3)
    120
    """
    result_list = []
    biggest_number = 10**(n)-1
    while biggest_number >= 0:
        if_true = 1
        for number_index in range(n-1):
            if int(str(biggest_number).zfill(n)[number_index]) < int(str(biggest_number).zfill(n)[number_index + 1]):
                continue
            else:
                if_true = 0
                break
        if if_true == 1:
            number_str_form = str(biggest_number).zfill(n)
            result_list.append(number_str_form)
        biggest_number -= 1
    print("Here is the set of valid codes")
    print(result_list)
    print(f"The total number of valid codes is {len(result_list)}")
    return len(result_list)

# Prolem A
# print(problem_part_a_iter(3))
# print(problem_part_a(3))

# Prolem B
# print(problem_part_b_iter(3))
# print(problem_part_b(3))

# Prolem C
# problem_part_c_iter(3)
# print(problem_part_c(3))