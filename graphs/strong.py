#! /usr/bin/env python
__version__ = '1.0'
__author__ = 'Abhinav Jauhri<abhinavjauhri@gmail.com>'
__all__ = ['string']

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


