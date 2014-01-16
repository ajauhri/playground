#!/usr/bin/env python
import sys
def main(N):
    if N == 0:
        return N
    else:
        l = []
        while N:
            l.append(N%2)
            N >>= 1


        return l[::-1]

            

if __name__ == "__main__":
    print main(int(sys.argv[1]))
    
