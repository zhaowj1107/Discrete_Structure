"""
File: weijian8-5.py
Author: David/Icho/Xiang
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
    """
    Sort the list using insert sort algorithm.
    args:
    list_n: List of elements to be sorted.

    >>> insert_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> insert_sort([3, 1, 4, 1, 5])
    [1, 1, 3, 4, 5]
    """
    length = len(list_n)
    for idx_i in range(length):
        while idx_i != 0:
            if list_n[idx_i] < list_n[idx_i - 1]:
                list_n[idx_i], list_n[idx_i - 1] = swap(list_n[idx_i], list_n[idx_i - 1])
            idx_i -= 1
        print(list_n)
    return list_n


def split(list_n):
    """
    Split the list into two parts.
    args:
    list_n: List of elements to be split.
    
    >>> split([1,2,3,4,5,6,7,8])
    ([1, 2, 3, 4], [5, 6, 7, 8])
    >>> split([1,2,3,4,5,6,7])
    ([1, 2, 3], [4, 5, 6, 7])
    """
    mid = 0 + (0 + len(list_n))//2
    return list_n[:mid], list_n[mid:]

def merge(list1,list2):
    """
    Merge two sorted lists into one sorted list.
    the args are two sorted lists.
    args:
    list1: List of elements to be merged."
    """
    list3 = []
    i, j = 0, 0
    while len(list3) != len(list1) + len(list2):
        if list1[i] >= list2[j]:
            list3.append(list2[j])
            if j < len(list2) - 1:
                j += 1
            else:
                for x in list1[i:]:
                    list3.append(x)
        elif list1[i] < list2[j]:
            list3.append(list1[i])
            if i < len(list1) - 1:
                i += 1
            else:
                for y in list2[j:]:
                    list3.append(y)
        print(list3)
    return list3


def merge_sort(list_n):
    """
    Sort the list using merge sort algorithm.
    use recursion to split the list into two parts and merge them with merge function.
    args:
    list_n: List of elements to be sorted.
    """
    if len(list_n) == 1:
        print(list_n)
        return list_n
    else:
        list_left, list_right = split(list_n)
        return merge(merge_sort(list_left), merge_sort(list_right))


if __name__ == "__main__":
    list_a = [5, 4, 3, 2, 1]
    print("Here is the bubble sort.")
    bubble_sort(list_a)
    list_a = [5, 4, 3, 2, 1]
    print("\nHere is the bubble sort.")
    insert_sort(list_a)

    list_n = [100,3,5,7,2,4,6,8,1]
    merge_sort(list_n)
    
    # list1 = [1,3,5,7]
    # list2 = [2,4,6,8]
    # merge(list1,list2)


