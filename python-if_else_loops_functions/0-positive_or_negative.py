#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:  # number must be less than 0
    print(f"{number} is negative")
