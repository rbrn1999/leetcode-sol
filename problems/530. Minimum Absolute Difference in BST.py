# link: https://leetcode.com/problems/minimum-absolute-difference-in-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = float('-inf')
        diff = float('inf')
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            nonlocal prev
            nonlocal diff
            diff = min(diff, node.val-prev)
            prev = node.val
            dfs(node.right)

        dfs(root)
        return diff

