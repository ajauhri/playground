#!/usr/bin/env python
import sys
import functools

def ret1st(*largs):
    return largs[0]

def group_anagrams(array):
    """
    Finds and groups anagrams from a list of words
    :param array - list of words 
    :return anagrams
    """
    return functools.reduce(lambda h,x: ret1st(h, h.setdefault("".join(sorted(x)), [ ]).append(x)), array, { }).values()

if __name__ == "__main__":
    array = 'cat rat bat vase cart ract art bart brat dart'.split()
    print(group_anagrams(array))

# input = ['cart rat tar art CaRt']
# output = [['rat', 'tar', 'art'], ['cart', 'CaRt']] 
