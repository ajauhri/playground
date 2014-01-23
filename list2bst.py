#!/usr/bin/env python

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def lst2bst(list, start, end):
    if start < end:
        mid = (start + end) / 2
        root = Node(list[mid])
        root.left = lst2bst(list, start, mid - 1)
        root.right = lst2bst(list, mid + 1, end)
        return root
    elif start == end:
        return Node(list[start])
    return None

def in_order_traversal(root):
    if root.left != None:
        in_order_traversal(root.left)
    print root.data,
    if root.right != None:
        in_order_traversal(root.right)

if __name__ == "__main__":
    list = [1,2,3,4]
    root = lst2bst(list, 0, len(list) - 1 )
    in_order_traversal(root)
    
