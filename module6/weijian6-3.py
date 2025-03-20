'''
File: weijian6-3.py
Authors: David
Date: 2025-03-10
Class: CS_5002, Spring_2025
Description: 
Solving dice game problems
'''

import random
import matplotlib.pyplot as plt

def game(strategy):
    """
    Simulates a dice game where the player rolls two dice and wins if the sum is 7 or 11.
    Args:
        None
    Returns:
        str: The result of the dice game
    """
    score = 0
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    while dice1!= 4 and dice2 != 4:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if score > strategy:
            # print(f'The score is {score}, You win!')
            return score
        score += dice1 + dice2
    # print(f'The score is {score}, You lose!')
    return 0



def test_game_times(times, strategy):
    """
    Test the dice game for a given number of times.
    Args:
        times (int): The number of times to test the dice game
    Returns:
        float: The expected value of the dice game
    """
    score_list = []
    for i in range(times):
        score_list.append(game(strategy))
    expected_score = sum(score_list)/len(score_list)
    return expected_score


def draw_plot():
    """
    test the game with stretegy number 1 to 30 and draw the plot
    make sure you have matplotlib installed
    """
    x = list(range(1, 31))
    y = [test_game_times(10000, i) for i in x]
    plt.plot(x, y)
    plt.xlabel('strategy')
    plt.ylabel('EV')
    plt.title('EV of strategy')
    plt.show()

if __name__ == "__main__":
    draw_plot()
    # print(f"the EV of strategy is {test_game_times(1000, 100)}")
