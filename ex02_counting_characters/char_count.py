"""
“Create a program that prompts for an input string and displays output that shows the input string and the number of characters the string contains.”

Excerpt From: Brian P. Hogan. “Exercises for Programmers (for Tamara Temple).” iBooks.

"""

import functools


def by_len(s):
    # this is cheating
    return len(s)


def by_counting(s):
    # this is proper
    l = 0
    for x in s:
        l += 1
    return l


def by_reduce(s):
    # this is cool
    return functools.reduce(lambda count, char: count + 1, s, 0)
