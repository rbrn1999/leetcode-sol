# link: https://leetcode.com/problems/delete-leaves-with-a-given-value/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(root) -> bool:
            '''
            return: delete node or not
            '''
            if root is None:
                return False
            
            
            if root.left and dfs(root.left):
                root.left = None
            
            if root.right and dfs(root.right):
                root.right = None
            
            if root.left is None and root.right is None:
                return root.val == target
            else:
                return False
        
        if dfs(root):
            return None
        else:
            return root