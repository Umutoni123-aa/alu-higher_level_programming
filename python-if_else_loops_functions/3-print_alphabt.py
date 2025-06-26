#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    char_to_print = chr(i)
    
    if char_to_print == 'q' or char_to_print == 'e':
        continue 
    
    print("{}".format(char_to_print), end="")
