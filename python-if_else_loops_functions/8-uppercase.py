#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Check if the character is lowercase
        if ord(char) >= 97 and ord(char) <= 122:
            # Convert to uppercase by subtracting 32 from its ASCII value
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
