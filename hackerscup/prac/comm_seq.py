#! /usr/bin/env python
import random

def comm_seq(arr_1, arr_2):
    if len(arr_1) == 0 or len(arr_2) == 0:
        return []
    
    m = len(arr_1) - 1
    n = len(arr_2) - 1
    
    if arr_1[m] == arr_2[n]:
        return comm_seq(arr_1[:-1], arr_2[:n]) + [arr_1[m]]

    elif arr_1[m] < arr_2[n]:
        return comm_seq(arr_1, arr_2[:-1])

    elif arr_1[m] > arr_2[n]:
        return comm_seq(arr_1[:-1], arr_2)


if __name__ == "__main__":
    arr_1 = [random.randrange(0,5) for _ in xrange(10)]
    arr_2 = [random.randrange(0,5) for _ in xrange(10)]
    arr_1.sort()
    arr_2.sort()
    print 'arr_2 = ',arr_2
    print 'arr_1 = ',arr_1
    print comm_seq(arr_1, arr_2)
