# link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import defaultdict
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        d = defaultdict(lambda: [])

        def preorder(root, level):
            if root is None:
                return

            d[level].append(root)
            preorder(root.left, level+1)
            preorder(root.right, level+1)

        preorder(root, 0)

        for nodes in d.values():
            for i in range(len(nodes)-1):
                nodes[i].next = nodes[i+1]
        
        return root