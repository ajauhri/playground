#! /usr/bin/env python
import sys
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def comm_ancestor(node_1, node_2, root):
    """Finds the common ancestor of two nodes in a tree
    :param node_1, node_2: Two nodes for finding the ancestor
    :param root: Starting point for the tree
    :type node_1, node_2, root:trees.bst
    """

    node_1_path = []
    node_2_path = []
    root_cp = root

    if not root:
        return []

    # construct path for node_1
    while node_1.data != root.data:
        node_1_path.append(root.data)
        if node_1.data < root.data:
                root = root.left
        else:
            root = root.right

    root = root_cp

    # constrcut path for node_2
    while node_2.data != root.data:
        node_2_path.append(root.data)
        if node_2.data < root.data:
            root = root.left
        else:
            root = root.right

    # if any one of the path are empty then common ancestor does not exist
    if len(node_1_path) == 0 or len(node_2_path) == 0:
        return [] 

    # # check for the first node where the paths differ, or the last node a path, which ever comes first
    print("rer") 

def construct_tree(arr):
    root = Node(arr[0])
    for val in arr[1:]:
        r = root
        while True:
            if val <= r.val:
                if r.left:
                    r = r.left
                else:
                    r.left = Node(val)
                    break
            
            elif val > r.val:
                if r.right:
                    r = r.right
                else:
                    r.right = Node(val)
                    break
    return root
                
if __name__ == "__main__":
    arr = list(map(lambda x: int(x), sys.argv[1].split()))
    root = construct_tree(arr)

    comm_ancestor(2, 4, root)
