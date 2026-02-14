def print_last_digit(number):
    # Get the absolute value to handle negative numbers, then modulo 10
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit
