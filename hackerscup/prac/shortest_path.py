#! /usr/bin/env python
import random
arr = [[-1 for x in xrange(5)] for x in xrange(3)]

def shortest_path(A, i, j):
    global arr
    arr[0][0] = A[0][0]
    if i<0 or j<0:
        return float('Inf')
    elif arr[i][j] >=0:
        return arr[i][j]
    else:
        result = A[i][j] + min(shortest_path(A,i-1,j), shortest_path(A,i,j-1))
    arr[i][j] = result
    return result


if __name__ == "__main__":
    A = [random.sample(range(9),3) for x in xrange(3)]
    for i in xrange(3):
        for j in xrange(3):
            print A[i][j],
        print
    print shortest_path(A, 2, 2)

