# link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                prev_right_root, root.right, root.left = root.right, root.left, None
                last_leaf = root.right
                while last_leaf and last_leaf.right:
                    last_leaf = last_leaf.right
                    
                last_leaf.right = prev_right_root
            root = root.right