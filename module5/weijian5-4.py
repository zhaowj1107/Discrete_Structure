'''
File: weijian5-4.py
Authors: John/Sia/David
Date: 2025-02-14
Class: CS_5002, Spring_2025
Description: 
counting the rectangle
-----------------
The following 3 funtions with default operands
problem_part_a()
problem_part_b()
problem_part_c()
'''

def problem_part_a(n: int, m: int):
    dictionary_rectangle = {}
    counter = 0
    for x1 in range(n):
        for y1 in range(m):
            for x2 in range(x1+1, n+1):
                for y2 in range(y1+1, m+1):
                    dictionary_rectangle[(x1,x2,y1,y2)] = [(x2 - x1), (y2 - y1)]
                    # The key of dictionary is the coordinator of rectangle's two sides,
                    # the value of dictionary is the length of rectangle's two sides
                    counter += 1
    print(f"the number of rectangle is {counter}.")
    return dictionary_rectangle


def problem_part_b(n: int, m: int):
    dictionary_rectangle = {}
    counter = 0
    for x1 in range(n):
        for y1 in range(m):
            for x2 in range(x1+1, n+1):
                for y2 in range(y1+1, m+1):
                    if y1 == 0 and (x2 == n):
                        # Let Y be the horizontal axis and X be the vertical axis.
                        # if y1 is in the first edge, when x1 and x2 could not reach to 8
                        continue
                    dictionary_rectangle[(x1,x2,y1,y2)] = [(x2 - x1), (y2 - y1)]
                    # The key of dictionary is the coordinator of rectangle's two sides,
                    # the value of dictionary is the length of rectangle's two sides
                    counter += 1
    print(f"the number of rectangle is {counter}.")
    return dictionary_rectangle


def problem_part_c(n: int, m: int):
    dictionary_rectangle = {}
    counter = 0
    for x1 in range(n):
        for y1 in range(m):
            for x2 in range(x1+1, n+1):
                for y2 in range(y1+1, m+1):
                    if (y1 == 0 and (x2 == n or x1 == 0)) or (y2 == 8 and (x2 == n or x1 == 0)):
                        # Let Y be the horizontal axis and X be the vertical axis.
                        # if y1 is in the left side, x2 could not reach to 8, filter the left-top/bottom cornor
                        # if y2 is in the right side, x1 could not reach to 8, filter the left-top/bottom cornor
                        continue
                    dictionary_rectangle[(x1,x2,y1,y2)] = [(x2 - x1), (y2 - y1)]
                    # The key of dictionary is the coordinator of rectangle's two sides
                    # the value of dictionary is the length of rectangle's two sides
                    counter += 1
    print(f"the number of rectangle is {counter}.")
    return dictionary_rectangle

def problem_part_d(n: int, m: int):
    dictionary_rectangle = {}
    counter = 0
    for x1 in range(n):
        for y1 in range(m):
            for x2 in range(x1+1, n+1):
                for y2 in range(y1+1, m+1):
                    if (y1 == 0 and (x2 == n)) or (y2 == 8 and (x1 == 0)):
                        # Let Y be the horizontal axis and X be the vertical axis.
                        # if y1 is in the left side, x2 could not reach to 8, filter the left-top/bottom cornor
                        # if y2 is in the right side, x1 could not reach to 8, filter the left-top/bottom cornor
                        continue
                    dictionary_rectangle[(x1,x2,y1,y2)] = [(x2 - x1), (y2 - y1)]
                    # The key of dictionary is the coordinator of rectangle's two sides
                    # the value of dictionary is the length of rectangle's two sides
                    counter += 1
    print(f"the number of rectangle is {counter}.")
    return dictionary_rectangle

if __name__ == "__main__":
    problem_part_a(8,8)
    problem_part_b(8,8)
    problem_part_c(8,8)
    problem_part_d(8,8)