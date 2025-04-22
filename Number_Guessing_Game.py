#!/usr/bin/env python

import random

random_num = random.randint(1,10)
n = 3

print("You have three chances to win this game")


for i in range(n):
    user_input = int(input("Enter your guess number (1-10): "))
    if user_input == random_num:
        print(f"Hurray! You guessed the right number, it's {random_num}.")
        break
    else:
        print(f"Number did not matched, you left with {(n-1)-i} guess")

if user_input != random_num:
    print(f"Sorry, you have used all attempts. The number was {random_num}.")

