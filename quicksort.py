#!/usr/bin/env python
import random

def quick_sort(array):
    n = len(array)
    if n <= 1:
        return array
    else:
        rand = random.randint(0, n-1) 
        p = array[rand]
        less_array = filter(lambda x: x<p, array)
        equal_array = filter(lambda x: x==p, array)
        greater_array = filter(lambda x: x>p, array)
        return quick_sort(less_array) + equal_array + quick_sort(greater_array)

if __name__ == "__main__":
    int_array = map(lambda x: random.randint(0,1000), range(0,10000))
    print quick_sort(int_array)
    
