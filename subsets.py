#!/usr/bin/env python

def subsets(sofar, rest):
    if rest == "":
        print sofar

    else:
        subsets(sofar + rest[0], rest[1:])
        subsets(sofar, rest[1:])

if __name__ == "__main__":
    str = raw_input()
    subsets("", str)
