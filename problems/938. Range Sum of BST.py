# link: https://leetcode.com/problems/range-sum-of-bst/description/

Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        def dfs(node):
            if node is None:
                return
            if node.val > low:
                dfs(node.left)
            if node.val >= low and node.val <= high:
                nonlocal result
                result += node.val
            if node.val < high:
                dfs(node.right)

        dfs(root)
        return result
