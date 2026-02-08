#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.
    If the dictionary is empty or None, returns None.
    """
    if not a_dictionary:
        return None

    # max() with the dictionary's get method as the key for comparison
    return max(a_dictionary, key=a_dictionary.get)
