# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(q, p):
            if q is None and p is None:
                return True
            if (q and not p) or (not q and p):
                return False
            
            return (q.val == p.val) and sameTree(q.left, p.left) and sameTree(q.right, p.right)
        
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            if node.val == subRoot.val and sameTree(node, subRoot):
                return True
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
                
        return False