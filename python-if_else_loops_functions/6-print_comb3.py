#!/usr/bin/python3
# Outer loop for the first digit (0 to 9)
for i in range(10):

    for j in range(10):

        if i < j:

            if i == 8 and j == 9:

                print("{}{}".format(i, j))
            else:

                print("{}{}, ".format(i, j), end="")
