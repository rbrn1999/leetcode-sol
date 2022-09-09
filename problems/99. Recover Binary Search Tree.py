# link: https://leetcode.com/problems/recover-binary-search-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    # in-order traversal
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = second = prev = None
        
        def traverse(node: Optional[TreeNode]):
            if not node:
                return
            
            traverse(node.left)
            nonlocal first, second, prev
            if first is None and (prev is None or prev.val >= node.val):
                first = prev
            if first and prev.val >= node.val:
                second = node
            prev = node
            
            traverse(node.right)
        
        traverse(root)
        first.val, second.val = second.val, first.val