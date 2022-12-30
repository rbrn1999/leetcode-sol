# link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, maxVal=float('-inf')):
            if node is None:
                return
            if node.val >= maxVal:
                maxVal = node.val
                nonlocal count
                count += 1
            
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)

        dfs(root)
        return count