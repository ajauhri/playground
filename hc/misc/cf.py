#! /usr/bin/env python
from __future__ import division
import sys
import functools

real = 0

def update(tuple):
    global real
    real = tuple[1]/real
    return tuple[0]

def do_it():
    global real
    l = [0]
    l.extend(list(map(lambda x: update(divmod(1,real)), range(8))))
    return l

if __name__ == "__main__":
    global real
    real = float(sys.argv[1])
    print(do_it())
