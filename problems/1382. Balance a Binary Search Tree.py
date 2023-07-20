# link: https://leetcode.com/problems/balance-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        def dfs(node):
            if node is None:
                return 0
            dfs(node.left)
            nodes.append(node)
            dfs(node.right)

        def buildTree(start, end):
            if start == end:
                node = nodes[start]
                node.left = node.right = None
                return node
            if start > end:
                return None
            mid = start + (end - start) // 2
            node = nodes[mid]
            node.left = buildTree(start, mid-1)
            node.right = buildTree(mid+1, end)
            return node

        dfs(root)
        return buildTree(0, len(nodes)-1)

