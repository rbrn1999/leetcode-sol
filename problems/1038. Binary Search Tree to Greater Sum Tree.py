# link: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def getSum(root: TreeNode) -> int:
            if root is None:
                return 0
            return root.val + getSum(root.left) + getSum(root.right)
        
        def inorder(root: TreeNode, total: int) -> int:
            if root is None:
                return total
            total = inorder(root.left, total)
            total -= root.val
            root.val += total
            total = inorder(root.right, total)

            return total
            
        total = getSum(root)
        inorder(root, total)

        return root
