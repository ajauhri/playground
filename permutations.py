#!/usr/bin/env python
import sys
def main(argv):
    listPermutations("", argv[1])

def listPermutations(sofar, rest):
    if rest is "":
        print sofar
    else:
        for i in xrange(0,len(rest)):
            next = sofar + rest[i]
            remaining = rest[:i]+rest[i+1:]
            listPermutations(next, remaining)
            

if __name__ == "__main__":
    main(sys.argv)
    
