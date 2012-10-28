#!/usr/bin/env python

__version__ = '1.0'
__author__ = 'Abhinav Jauhri<abhinavjauhri@gmail.com>'

import sys
import biconnected,  strong
class Graph:
    def __init__(self, key):
        self.key = key      #unique id for a vertex 
        self.edges = []
        self.visited = False#required for the simple DFS
        self.lowlink = 0    #The vertex with the lowest num value reachable from u
        self.num = 0        #Sequence in which DFS traverses each node

def construct(file, s=1): 
    """Constructs a Graph using the adjaceny matrix given in the file

    :param file: path to the file with the matrix
    :param s: starting node key. Defaults to 1

    :return start vertex of the graph
    """
    d = {}
    f = open(file,'rU')
    size = int(f.readline())
    for x in xrange(1,size+1):
        d[x] = Graph(x)
    start = d[s]
    for i in xrange(0,size):
           l = map(lambda x: int(x), f.readline().split())
           node = l[0]
           for child in l[1:]:
               d[node].edges.append(d[child])
    return start

def dfs(start):
    """Depth-First traversal

    :param start: start vertex in the Graph
    """
    print start.key
    start.visited = True
    for edge in start.edges:
        if not edge.visited:
            dfs(edge) 

if __name__ == "__main__":
    s = construct(sys.argv[1])
    #dfs(s)
    strong.strong(s)
    #print biconnected.bic(s,None)
