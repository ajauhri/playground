#! /usr/bin/env python

from functools import reduce
class cache:
    def __init__(self, *args):
        self._root = node(args[0])
        self._limit = 10
        self._size = 0
         

    def add(self, value):
        leaf = self.search(self._root, value)
        if value <= leaf.value:
            leaf.left = node. 
        else: 
            leaf.right = new_node 
        self._size += 1
        
    def search(self, root, value):
        if not root:
            return None
        result = self.search(root.left, value) if value <= root.value else self.search(root.right, value)
        return root if not result else result 

   #### - Need to do this stuff http://www.algolist.net/Data_structures/Binary_search_tree/Removal ### 
    def delete(self, value):
        parent = self.find(self._root, value)
        # if one leaf
        if value < parent.value:
            operation(parent.left)
            

        def operatio(node):

        child = parent.left if parent.value < value else parent.right
        if (not child.left and not child.right) or (not child.left or not child.right):
            if parent.value < value:
                parent.left = None
            else:
                parent.right = None

        elif child.left and child.right:
            if child.right.left:
                low = self.lowest_sub_tree(child.right)
            else:
                parent
            child.value = low.value


        def lowest_sub_tree(self, node):
            while node.left:
                parent = node 
                node = node.left
            return parent 
####

    def find(self, root, value):
        if not root:
            return None
        if root.value == value:
            return None
        elif value < root.value:
             result = self.find(root.left, value)
        elif value > root.value:
            result = self.find(root.right, value)

        return root if not result else result

    def print(self):
        """
        BFS Traversal
        """
        thislevel = [self._root] 
        while thislevel:
            nextlevel = list()
            for n in thislevel:
                print(n.value,end=" ")
                if n.left: nextlevel.append(n.left)
                if n.right: nextlevel.append(n.right)
            print()
            thislevel = nextlevel

def ret1st(*largs):
    return largs[0]
        
class node:
    def __init__(self, *args):
        self.value = args[0]
        self.counter = 0
        self.left = None
        self.right = None


if __name__ == "__main__":
    c = cache(6)
    c.add(2)
    c.add(5)
    c.add(1)
    c.add(7)
    c.add(34)
    c.print()

    
