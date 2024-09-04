# link: https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def dfs(self, root: 'Node', result: list[int]) -> None:
        if root is None:
            return

        for child in root.children:
            self.dfs(child, result)

        result.append(root.val)
        return

    def postorder(self, root: 'Node') -> list[int]:
        result = []
        self.dfs(root, result)
        return result
