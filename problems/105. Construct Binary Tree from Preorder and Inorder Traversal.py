# link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        node = TreeNode(preorder.pop(0))
        rootInd = inorder.index(node.val)
        node.left = self.buildTree(preorder, inorder[:rootInd])
        node.right = self.buildTree(preorder, inorder[rootInd+1:])
        return node
