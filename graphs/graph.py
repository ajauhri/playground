#!/usr/bin/env python
import sys
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

#Book-keeping data for finding the strong components
S=[]
i=0

def strong(u):
"""Finds the strong components in a graph starting at u

:param u: Starting vertex of the graph
"""
    global S, i
    i = i+1
    u.num = i
    u.lowlink = i   
    S.append(u)
    for edge in u.edges:
        if edge.num == 0:
            strong(edge)
            u.lowlink = min(u.lowlink, edge.lowlink)
        elif edge.num < u.num:   #back-edge or cross-edge
            if edge in S: 
                 u.lowlink = min(u.lowlink, edge.lowlink)
    if u.num == u.lowlink:
        print 'Strong component:',
        while S and S[-1].num >= u.num:
            print S.pop().key ,
        print 

if __name__ == "__main__":
    s = construct(sys.argv[1])
    #dfs(s)
    strong(s)
