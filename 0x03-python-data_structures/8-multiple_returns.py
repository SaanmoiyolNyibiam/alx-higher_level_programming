#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string
    and its first character
    Parameters:
    - sentence: The sequence to be evaluated

    Return:
    - A tuple
    """
    if not sentence:
        res = (len(sentence), None)
    else:
        res = (len(sentence), sentence[0])
    return res
