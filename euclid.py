#! /usr/bin/env python
import sys

def gcd(a,b):
    while b>0:
        r = a%b
        a = b
        b = r
    print(a)

if __name__ == "__main__":
    gcd(int(sys.argv[1]),int(sys.argv[2]))
