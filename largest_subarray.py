#! /usr/bin/env python

def largest_subset(arr):
    s = 0;
    M = 0;
    for i in arr:
        s += i
        if s > M:
            M = s
        if s < 0:
            s = 0
    return M

if __name__ == "__main__":
    print(largest_subset([-3,7,-12,1,6,-3,5,-2]))
