# link: https://leetcode.com/problems/minimum-distance-between-bst-nodes/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        minDiff = float('inf')
        prev = -1
        def dfs(node):
            if node is None:
                return
            if node.left:
                dfs(node.left)

            nonlocal minDiff
            nonlocal prev
            if prev != -1:
                minDiff = min(minDiff, node.val - prev)
            prev = node.val

            if node.right:
                dfs(node.right)

        dfs(root)
        return minDiff
