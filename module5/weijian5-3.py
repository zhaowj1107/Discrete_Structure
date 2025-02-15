"""
File: weijian5-3.py
Authors: Weijian(David)
Date: 2025-02-14
Class: CS_5002, Spring_2025
Description: 
SET game
-----------------
number (1/2/3), shape (diamond/squiggle/oval), shading (solid/open/striped), and colour (red/green/purple)
"""

def is_valid_set(card1, card2, card3):
    """
    Determines if three cards form a valid set based on the game Set rules.
    A valid set is when for each of the four features (number, shape, shading, color),
    the three cards are either all the same or all different.
    Args:
        card1 (list): First card's features [number, shape, shading, color]
        card2 (list): Second card's features [number, shape, shading, color]
        card3 (list): Third card's features [number, shape, shading, color]
    Returns:
        bool: True if valid set, False otherwise
    >>> is_valid_set(['1', 'diamond', 'solid', 'red'], ['2', 'diamond', 'solid', 'red'], ['3', 'diamond', 'solid', 'red'])
    True
    >>> is_valid_set(['1', 'diamond', 'solid', 'red'], ['2', 'oval', 'striped', 'green'], ['3', 'squiggle', 'open', 'purple'])
    True
    >>> is_valid_set(['1', 'oval', 'solid', 'red'], ['2', 'oval', 'solid', 'red'], ['3', 'squiggle', 'solid', 'red'])
    False
    >>> is_valid_set(['1', 'diamond', 'solid', 'red'], ['1', 'oval', 'solid', 'green'], ['1', 'squiggle', 'solid', 'red'])
    False
    """
    count_same = 0
    count_diff = 0
    for feature in range(4):  # 4 features
        a, b, c = card1[feature], card2[feature], card3[feature]
        if (a != b and b != c and a != c):
            count_diff += 1
        elif (a == b == c):
            count_same += 1
    if (count_diff + count_same) == 4:
    # count_diff == 2 and count_same == 2:
    # count_diff == 4 and count_same == 0:
    # count_diff == 3 and count_same == 1:
    # count_diff == 1 and count_same == 3:
        return True
    else:
        return False

    # print(card_list)
def check_set(card_list):
    counter = 0
    for card_1 in range(len(card_list)):
        for card_2 in range(card_1, len(card_list)):
            for card_3 in range(card_2, len(card_list)):
                if is_valid_set(card_list[card_1], card_list[card_2], card_list[card_3]):
                    # print(card_list[card_1], card_list[card_2], card_list[card_3])
                    counter += 1
    print(counter)

def main():
    number = ["1","2","3"]
    shape = ["diamond", "squiggle", "oval"]
    shading = ["solid", "open", "striped"]
    colour = ["red", "green", "purple"]
    card_list = []
    for index_1 in number:
        for index_2 in shape:
            for index_3 in shading:
                for index_4 in colour:
                    word = [index_1, index_2, index_3, index_4]
                    # print(word)
                    card_list.append(word)
    check_set(card_list)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()