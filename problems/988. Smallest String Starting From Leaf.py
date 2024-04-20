# link: https://leetcode.com/problems/smallest-string-starting-from-leaf/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        result = ""
        stack = []
        def dfs(node):
            if not node:
                return
                
            stack.append(chr(ord('a') + node.val))
            if not node.left and not node.right:
                s = ''.join(stack[::-1])
                nonlocal result
                if result == "" or s < result:
                    result = s
            else:
                dfs(node.left)
                dfs(node.right)

            stack.pop()
        
        dfs(root)
        return result