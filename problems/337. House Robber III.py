# link: https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from functools import cache
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(root, access=True):
            if root is None:
                return 0
            if not access:
                return dfs(root.left) + dfs(root.right)
            take_cost = root.val + dfs(root.left, False) + dfs(root.right, False)
            dont_take_cost = dfs(root.left) + dfs(root.right)
            return max(take_cost, dont_take_cost)

        return dfs(root)
