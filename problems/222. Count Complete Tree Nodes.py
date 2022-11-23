# link: https://leetcode.com/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        prev = None
        cur = root
        depth = -1
        while cur:
            prev, cur = cur, cur.left
            depth += 1
        nodeCount = 2 ** (depth) - 1
        def dfs(node, d):
            if d == depth-1:
                nonlocal nodeCount
                nodeCount += int(node.left is not None) + int(node.right is not None)
                return node.right is not None
            elif node is not None:
                return dfs(node.left, d + 1) and dfs(node.right, d + 1)
            else:
                return False

        if depth <= 0:
            return depth + 1
        dfs(root, 0)
        return nodeCount
