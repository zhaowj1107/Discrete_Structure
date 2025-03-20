import doctest

"""
File: weijian8-5.py
Author: Weijian Zhao(David)
Date: 2025-03-20
Class: CS_5002, Spring_2025
Description: 
homework 8-5:sorting algorithms
"""

def swap(x, y):
    """
    Swap the values of x and y.
    >>> swap(1, 2)
    (2, 1)
    >>> swap('a', 'b')
    ('b', 'a')
    """
    temp = x
    x = y
    y = temp
    return x, y

def bubble_sort(list_n):
    """
    Sort the list using bubble sort algorithm.

    Args:
    list_n: List of elements to be sorted.

    >>> bubble_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> bubble_sort([3, 1, 4, 1, 5])
    [1, 1, 3, 4, 5]
    """
    length = len(list_n)
    while length > 1: #first loop
        for index_i in range(length-1): #second loop
            if list_n[index_i] > list_n[index_i + 1]:
                list_n[index_i], list_n[index_i + 1] = swap(list_n[index_i], list_n[index_i + 1])
        length -= 1
        print(list_n)
    return list_n


def insert_sort(list_n):
    length = len(list_n)
    for idx_i in range(length):
        while idx_i != 0:
            if list_n[idx_i] < list_n[idx_i - 1]:
                list_n[idx_i], list_n[idx_i - 1] = swap(list_n[idx_i], list_n[idx_i - 1])
            idx_i -= 1
        print(list_n)
    return list_n


def merge_sort(list_n):
    

if __name__ == "__main__":
    # doctest.testmod()

    list_a = [5, 4, 3, 2, 1]
    print("Here is the bubble sort.")
    bubble_sort(list_a)
    list_a = [5, 4, 3, 2, 1]
    print("\nHere is the bubble sort.")
    insert_sort(list_a)