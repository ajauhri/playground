#! /usr/bin/env python

import random

def miss_int(arr):
    k = 0
    for i in range(len(arr)):
        k = k^i^arr[i]
    print k^(i+1)

if __name__ == "__main__":
    arr = random.sample(xrange(10), 9)
    print arr
    miss_int(arr)
