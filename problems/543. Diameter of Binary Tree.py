# link: https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def dfs(node):
            if node is None:
                return 0
            nonlocal result
            left = dfs(node.left)
            right = dfs(node.right)
            result = max((left + right), result)
            return max(left, right) + 1
        
        dfs(root)
        return result
        