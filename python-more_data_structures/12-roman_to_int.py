#!/usr/bin/python3
# Roman to Integer conversion module


def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    for i in range(len(roman_string)):
        current_val = roman_dict.get(roman_string[i], 0)

        # Check if the next character exists and is greater than current
        next_val = roman_dict.get(roman_string[i + 1], 0) if i + 1 < \
            len(roman_string) else 0

        if next_val > current_val:
            total -= current_val
        else:
            total += current_val

    return total
