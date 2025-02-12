'''
File: weijian3-5.py
Authors: Weijian(David)
Date: 2025-02-11
Class: CS_5002, Spring_2025
Description: 
solve the lock permutation and combination pizzle
-----------------
The following 3 funtions with default operands
problem_part_a()
problem_part_b()
problem_part_c()

'''
letter_set = ["A","G","I","L","N"]

def factorial(n):
    """
    general factorial tool function
    """
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def problem_part_a(letter_list = letter_set, word = "ALIGN") -> int:
    '''
    Calculates the lexicographical position of a given word using permutations of letters.
    Args:
        letter_list (list): List of available letters (default: Letter_set)
        word (str): The target word to find position for (default: "ALIGN")
    Returns:
        int: The lexicographical position of the word (1-based index)
    >>> problem_part_a(["A","G","I","L","N"], "ALIGN")
    1
    >>> problem_part_a(["A","G","I","L","N"], "LIGAN")
    87
    >>> problem_part_a(["A","B","C"], "CAB")
    5
    '''
    word_stamp = word
    total_length = len(word)
    letter_list.sort() # sort in alphabet order
    total_number = factorial(total_length)
    position = 0
    for letter_index in range(total_length):
        list_position = letter_list.index(word[letter_index])
        total_number = total_number // (total_length - letter_index)
        position = position + list_position * total_number
        letter_list.remove(word[letter_index])
    print(f"The position of \"{word_stamp}\" is {position + 1}.")
    return (position + 1)

letter_set = ["A","G","I","L","N"]

def problem_part_b(letter_list = letter_set, position = 87) -> str:
    '''
    Calculates the word at a given lexicographical position using permutations of letters.
    Args:
        letter_list (list): List of available letters (default: Letter_set)
        position (int): The target position to find word for (1-based index)
    Returns:
        list: The word as a list of letters at the given position
    >>> problem_part_b(["A","G","I","L","N"], 1)
    ['A', 'L', 'I', 'G', 'N']
    >>> problem_part_b(["A","G","I","L","N"], 87)
    ['L', 'I', 'G', 'A', 'N']
    >>> problem_part_b(["A","B","C"], 5)
    ['C', 'A', 'B']
    '''
    position_stamp = position
    letter_list.sort() # sort in alphabet order
    total_length = len(letter_list)
    total_number = factorial(total_length)
    letter_list = []
    position = position - 1
    while total_length > 0:
        total_number = total_number // total_length
        letter_index, position = position // total_number, position % total_number
        letter_list.append(letter_list[letter_index])
        letter_list.remove(letter_list[letter_index])
        total_length -= 1
    word = "".join(letter_list)
    print(f"The word in position {position_stamp} is \"{word}\".")
    return word

letter_set = ["A","G","I","L","N"]
VOWELS = ["A", "E", "I", "O", "U"]

def problem_part_c(letter_list = letter_set, word = "ALIGN"):
    total_length = len(letter_list)
    word_list = []
    while total_length > 0:
        word = ""
        for letter in letter_list:
            word = 
        word_list.append(str(word))
        total_length -= 1

if __name__ == "__main__":
    problem_part_a()
    problem_part_b()
    # problem_part_c()