# link: https://leetcode.com/problems/construct-string-from-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        result = ""
        def preorder(node):
            if node is None:
                return
            nonlocal result
            result += str(node.val)
            if node.left:
                result += '('
                preorder(node.left)
                result += ')'
            if node.right:
                if node.left is None:
                    result += "()"
                result += '('
                preorder(node.right)
                result += ')'
        preorder(root)
        return result
