#!/usr/bin/env python

__version__ ='1.0'
__author__ = 'Abhiav Jauhri<abhinavjauhri@gmail.com>'

import math

"""Deterministic Select
Given a list of numbers, finds the kth largest number using a deterministing linear-time algorithm
"""


def pivot(arr):
    arr_groups = chunks(arr, 5)
    medians = cal_medians(arr_groups)
    if len(medians) > 5:
        p = pivot(medians) 
    else:
        return cal_median(medians)
    return p

def cal_medians(arr_groups):
    medians = []
    for group in arr_groups:
        medians.append(cal_median(group))
    return medians

def cal_median(arr):
    arr.sort()
    index = int(math.ceil(len(arr)/2))
    return arr[index]

# Yields successive n-sized chunks
def chunks(arr, n):
    for i in xrange(0, len(arr), n):
        yield arr[i:i+n]

def quick_select(arr, k):
    p = pivot(arr)
    less_array = filter(lambda x: x < p, arr)
    greater_array = filter(lambda x: x > p, arr)
    L = len(less_array)
    if L == k - 1:
        return p 
    elif L > k - 1:
        return quick_select(less_array, k)
    elif L < k - 1:
        return quick_select(greater_array, k - L - 1)

if __name__ == "__main__":
    str_array = raw_input('Input the list of number: ').split()
    arr = map(lambda x: int(x), str_array)
    k = input('kth largest element to find ') 
    print quick_select(arr, k)

