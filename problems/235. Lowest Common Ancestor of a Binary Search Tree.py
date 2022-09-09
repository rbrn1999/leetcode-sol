# link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        
        while root:
            if root.val < p.val: # root is lesser than both nodes
                root = root.right
            elif root.val > q.val: # root is greater than both nodes
                root = root.left
            else:
                return root

    # assume p and q exist in the tree
    # this method works with all binary trees
    # def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
    #     if root is None or root ==  p or root == q:
    #         return root
        
    #     left = self.lowestCommonAncestor(root.left, p, q)
    #     right = self.lowestCommonAncestor(root.right, p, q)
        
    #     if left and right:
    #         return root
        
    #     return left if left is not None else right