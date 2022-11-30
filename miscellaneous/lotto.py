# This script is a simple lotto game. It generates 6 random numbers
# between 1 and 49 and asks the user to guess them. The user has 3
# chances to guess the numbers. If the user guesses all 6 numbers
# correctly, he wins the jackpot. If the user guesses 5 numbers
# correctly, he wins the second prize. If the user guesses 4 numbers
# correctly, he wins the third prize. If the user guesses 3 numbers
# correctly, he wins the fourth prize. If the user guesses 2 numbers
# correctly, he wins the fifth prize. If the user guesses 1 number
# correctly, he wins the sixth prize. If the user guesses 0 numbers
# correctly, he wins the seventh prize. The user can play the game
# as many times as he wants.

# import random

# # Generate 6 random numbers
# def generate():
#     lotter_list = []
#     for i in range(6):
#         lotter_list.append(random.randint(1, 49))
#     print("The winning numbers are: ", lotter_list)
#     return lotter_list
# def display(lotter_list):
#     for i in (lotter_list):
#         print(i)
# lotter_list = generate()
# display(lotter_list)

# import random
# picks =  int (input("How Many Picks ?: "))

# for i in range (picks):
#     num_list = random.sample(range(1, 49), 5,)
#     num_list.sort()
#     bonus_num = random.sample(range(1, 49), 1)
# print("Lucky Numbers :", num_list, "for ", "Jordan :", bonus_num)

import random
picks =  int (input("How Many Picks ?: "))

for i in range (picks):
    num_list = random.sample(range(1, 45), 6,)
    num_list.sort()
    joker_num = random.sample(range(1, 20), 1)
    print("Lucky Numbers :", num_list, joker_num)