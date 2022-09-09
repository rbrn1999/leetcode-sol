# link: https://leetcode.com/problems/binary-tree-pruning/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node) -> bool:
            if node is None:
                return False
            if node.left and not dfs(node.left):
                node.left = None
            if node.right and not dfs(node.right):
                node.right = None
            return node.val == 1 or dfs(node.left) or dfs(node.right)

        if dfs(root):
            return root
        else:
            return None
