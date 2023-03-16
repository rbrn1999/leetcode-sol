# link: https://leetcode.com/problems/check-completeness-of-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        isFull = True
        while queue:
            node = queue.popleft()
            if node is None:
                isFull = False
            elif not isFull:
                return False
            else:
                queue.extend([node.left, node.right])

        return True


# DFS
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        maxDepth = 0
        isFull = True
        cur = root
        while cur:
            maxDepth += 1
            cur = cur.left
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop()

            if node is None or (node.left is None and node.right is None):
                if node is None:
                    depth -= 1

                if isFull and maxDepth-1 == depth:
                    isFull = False
                    maxDepth -= 1
                    isFull = False
                elif depth != maxDepth:
                    return False
            
            if node:
                stack.extend([(node.right, depth+1), (node.left, depth+1)])
                    
        
        return True