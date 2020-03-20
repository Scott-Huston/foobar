"""
Ion Flux Relabeling
===================

Oh no! Commander Lambda's latest experiment to improve the efficiency of her LAMBCHOP doomsday 
device has backfired spectacularly. She had been improving the structure of the ion flux converter 
tree, but something went terribly wrong and the flux chains exploded. Some of the ion flux converters 
survived the explosion intact, but others had their position labels blasted off. She's having her 
henchmen rebuild the ion flux converter tree by hand, but you think you can do it much more quickly -
quickly enough, perhaps, to earn a promotion!

Flux chains require perfect binary trees, so Lambda's design arranged the ion flux converters to form 
one. To label them, she performed a post-order traversal of the tree of converters and labeled each 
converter with the order of that converter in the traversal, starting at 1. For example, a tree of 7 
converters would look like the following:

   7
 3   6
1 2 4 5

Write a function solution(h, q) - where h is the height of the perfect tree of converters and q is a
list of positive integers representing different flux converters - which returns a list of integers 
p where each element in p is the label of the converter that sits on top of the respective converter 
in q, or -1 if there is no such converter.  For example, solution(3, [1, 4, 7]) would return the 
converters above the converters at indexes 1, 4, and 7 in a perfect binary tree of height 3, which 
is [3, 6, -1].

The domain of the integer h is 1 <= h <= 30, where  h = 1 represents a perfect binary tree containing 
only the root, h = 2 represents a perfect binary tree with the root and two leaf nodes, h = 3 represents 
a perfect binary tree with the root, two internal nodes and four leaf nodes (like the example above), 
and so forth.  The lists q and p contain at least one but no more than 10000 distinct integers, all of 
which will be between 1 and 2^h-1, inclusive.
"""

from math import pow

def solution(h, q):
    def num_nodes(h):
        """
        Returns how many nodes are in a binary tree of height h
        """
        return pow(2,h)-1

    def find_top(h,n):
        """
        Returns the place of the parent node to node n in a post-order traversal of a binary tree of h height.
        n is the place of the input node in a post-order traversal.
        """
        node_count = num_nodes(h)
    
        # if node is top-most node, return -1
        if n == node_count:
            return -1

        top = node_count
        level = 1
    
        # work down the binary tree until n and top are found
        while True:
            right = top-1
            # subtract number of nodes in right subtree from number of right node 
            # to find number of left node
            left = right - num_nodes(h-level)
    
            # if n is the left or the right node, return top
            if n==left or n==right:
                return top
            
            # otherwise set new top to be left or right node and increment level
            level += 1
            if n>left:
                top = right
            else:
                top = left

    # check h is in expected range
    if h<1 or h>30:
        raise ValueError('Height of tree expected to be between 1 and 30 inclusive')

    # cache answers for efficiency
    cache = {}
    solution = []

    # loop through nodes and find top from cache or function
    for node in q:
        # check node value is valid
        if node<1 or node>num_nodes(h):
            raise ValueError('Node in q is out of valid range from 1 to total number of nodes inclusive')

        if node in cache:
            top = cache[node]
        else:
            top = find_top(h,node)
    
        solution.append(int(top))
    
    return solution