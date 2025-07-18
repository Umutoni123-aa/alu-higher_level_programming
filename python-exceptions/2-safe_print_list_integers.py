#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elements_printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            elements_printed += 1
        except (ValueError, TypeError):
            pass # Skip non-integers silently
        except IndexError:
            break # Stop if out of bounds
    print()
    return elements_printed
