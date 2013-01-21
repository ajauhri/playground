#! /usr/bin/env python
import random
def rotate(M,m,n):
    if m == 0 or n == 0:
        return []
    else:
        new_array = [[0 for i in range(m)] for j in range(n)]
        print new_array
        for i in range(m):
            for j in range(n):
                print n-1-j,i, ' ' , i, j
                new_array[j][m-1-i] = M[i][j]
        print new_array

if __name__ == "__main__":
    M = [random.sample(range(9),4) for x in xrange(3)]
    print M
    rotate(M,3,4)

