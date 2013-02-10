#! /usr/bin/env python
import math

li = lambda x: x*2              #left index
ri = lambda x: x*2 + 1          #right index 
access = lambda x,y,z: x[y(z)]

def heapify(arr):
    """
    Creates a heap in O(n) time

    :para `arr` list of arbitrary positive integers
    :rtype heap as a list 
    """
    arr.insert(0, -1)

    #look for internal nodes - all elements except leaf, hence height - 1 => lg(n) -1 
    internal_height = int(math.log(len(arr)-1,2)) - 1
    for h in range(internal_height, -1, -1):
        for i,e in reversed(list(enumerate(arr))[2**h:(2**h)*2]): 
            bubble_tree_down(e, i, arr)

    return arr

def add(elem, arr):
    """
    Adds an element to an heap 

    :param `elem` a positive integer to be added
    :param `arr` an existing heap 
    """
    arr.append(elem)
    pos = len(arr)-1
    parent = int(pos/2)

    # bubble tree up to maintain the heap property 
    while parent!=0:
        if arr[parent] > elem:
            swap(pos, parent, arr)
            pos = int(pos/2)
            parent = int(parent/2)
        else:
            break

def delete_min(arr):
    """
    Delete the min element. Overall takes O(lgn) time to retain the heap property

    :param `arr` existing heap
    :rtype min value
    :rtype new heap as a list
    """
    last_elem = arr[-1]
    min_elem = arr[1]
    arr = [-1, last_elem]+arr[2:-1]
    bubble_tree_down(last_elem, 1, arr)
    return min,arr

def bubble_tree_down(elem, pos, arr):
    """
    Maintain the heap property by percolating down

    :param `elem` integer to be percolated
    :param `pos` position of the `elem` in the heap
    :param `arr` the heap
    """
    while True:
        min_pos = pos

        # `elem` has both its children
        if len(arr) > li(pos) and len(arr) > ri(pos):
            min_elem = min(min(access(arr,li,pos), access(arr,ri,pos)), elem)
            if access(arr,li,pos) == min_elem:
                min_pos = li(pos)
            elif access(arr,ri,pos) == min_elem:
                min_pos = ri(pos) 

            if min_pos != pos:
                swap(pos, min_pos, arr)  
                pos = min_pos
            else:
                break
        
        # elem has a single child 
        elif len(arr) > li(pos):
            if access(arr,li,pos) < elem:
                min_pos = li(pos) 
            if min_pos != pos:
                swap(pos, min_pos, arr)
                pos = min_pos
            else:
                break
        
        # No children
        else:
            break

def print_heap(arr):
    """
    wrapper for printing
    """
    print(arr[1:])
           
def swap(pos_a, pos_b, arr):
    """
    In-memory swap

    :param pos_a, pos_b: positions in a list
    :type pos_a,pos_b: positive integers
    :param arr: list of integers
    """
    arr[pos_a] += arr[pos_b]
    arr[pos_b] = arr[pos_a] - arr[pos_b]
    arr[pos_a] -= arr[pos_b]

if __name__ == "__main__":
    ### test cases ###
    arr = heapify([10,7,8,25,5,11,27,16,15,4,12,6,7,23,20])
    print_heap(arr)
    add(2,arr)
    print_heap(arr)
    arr = heapify([2,5,3,9,6,11,4,17,10,8])
    add(2,arr)
    print_heap(arr)
    min_elem,arr = delete_min(arr)
    print_heap(arr)
