

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return (True, -1)
            left = dfs(root.left)
            right = dfs(root.right)
            return (left[0] and right[0] and abs(left[1] - right[1]) <= 1, max(left[1], right[1]) + 1)
        return dfs(root)[0]


# or 

class Solution:
    def height(self, root):
        if root is None:
            return -1
        return max(self.height(root.left), self.height(root.right)) + 1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.height(root.left) - self.height(root.right)) <= 1