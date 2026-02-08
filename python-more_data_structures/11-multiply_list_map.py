#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.
    If no score is found, returns None.
    """
    if not a_dictionary:
        return None

    # max iterates keys; key=a_dictionary.get compares their values
    return max(a_dictionary, key=a_dictionary.get)
