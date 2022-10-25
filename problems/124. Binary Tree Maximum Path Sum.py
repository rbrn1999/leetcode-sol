# link: https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            val = node.val + max((left if left > 0 else 0), (right if right > 0 else 0))
            nonlocal res
            res = max(res, node.val + (left if left > 0 else 0) + (right if right > 0 else 0))
            return val

        dfs(root)
        return res

