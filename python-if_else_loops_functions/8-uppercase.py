#!/usr/bin/python3
def uppercase(str):
    for char in str:
        char_ascii = ord(char)
        if char_ascii >= ord('a') and char_ascii <= ord('z'):
            uppercase_ascii = char_ascii - 32
        else:
            uppercase_ascii = char_ascii
        print("{}".format(chr(uppercase_ascii)), end="")
    print("")
