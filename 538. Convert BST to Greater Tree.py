# link: https://leetcode.com/problems/convert-bst-to-greater-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    # my inorder attemp
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def sumTree(node):
            if node:
                return sumTree(node.left) + node.val + sumTree(node.right)
            else:
                return 0
        
        def addCurSum(node, sumList):
            if node:
                addCurSum(node.left, sumList)
                sumList[0] -= node.val
                node.val += sumList[0]
                addCurSum(node.right, sumList)
        
        curSum = sumTree(root)
        addCurSum(root, [curSum])
        
        return root
    
    # inverse inorder attemp (faster)
    # def convertBST(self, root):
    #     if root is not None:
    #         self.convertBST(root.right)
    #         self.total += root.val
    #         root.val = self.total
    #         self.convertBST(root.left)
    #     return root