# link: https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxDiff = 0
        visited = []
        def dfs(node, maxVal, minVal):
            if node is None:
                return
            nonlocal maxDiff
            maxDiff = max(abs(maxVal - node.val), abs(minVal - node.val), maxDiff)
            visited.append(node.val)
            maxVal = max(maxVal, node.val)
            minVal = min(minVal, node.val)
            dfs(node.left, maxVal, minVal)
            dfs(node.right, maxVal, minVal)
            visited.pop()
            if visited and node.val == maxVal:
                maxVal = max(visited)
            if visited and node.val == minVal:
                minVal = min(visited)

        dfs(root, root.val, root.val)
        return maxDiff

