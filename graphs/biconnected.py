#! /usr/bin/env python
__version__ = '1.0'
__author__ = 'Abhinav Jauhri<abhinavjauhri@gmail.com>'
__all__ = ['bic']

S = []
i = 0
a_c = set() 
def bic(v,u):
    """ Print all articulation points in graph, if any
    :param v: An entry vertex to a graph
    :param u: Parent of the entry vertex. None in case of root 
    """
    global S, i
    i = i+1
    v.num = i
    v.lowpt = i
    for edge in v.edges:
        if edge.num == 0:
            bic(edge,v)
            v.lowpt = min(edge.lowpt, v.lowpt)
            if edge.lowpt >= v.num:
                a_c.add(v.key) 
        elif edge.num < v.num and edge != u:
            v.lowpt = min(v.lowpt, edge.num)
    return a_c   

