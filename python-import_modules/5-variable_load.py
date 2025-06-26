#!/usr/bin/python3
# This script imports a variable 'a' from 'variable_load_5.py'
# and prints its value.

# The __name__ == "__main__" block ensures this code only runs
# when the script is executed directly, not when imported as a module.
if __name__ == "__main__": 
    a = __import__('variable_load_5').a

    print(a) 
