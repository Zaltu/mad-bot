"""
Functions for all possible actions
"""
import random

def nyx():
    """
    Generate a random Nyx quote

    :returns: one of Nyx's final battle quotes.
    :rtype: str
    """
    return random.sample({
        "Celebrate life's grandeur. Its brilliance. Its magnificence.",
        "There is both joy and wonder in coming to understand another.",
    }, 1)


def owo():
    """
    NYI
    See Sagiri's owo command implementation

    :returns: "OwO"
    :rtype: str
    """
    return "OwO"
