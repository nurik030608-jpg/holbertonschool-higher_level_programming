#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
            
    return new_string

if __name__ == "__main__":
    test_no_c = no_c

    test1 = "Best School"
    print(test_no_c(test1))

    test2 = "Chicago"
    print(test_no_c(test2))

    test3 = "C is fun!"
    print(test_no_c(test3))

