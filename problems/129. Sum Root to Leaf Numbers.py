# link: https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        answer = 0
        stack = []
        def dfs(root: Optional[TreeNode]):
            if root is None:
                return
            stack.append(root.val)
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            if root.left is None and root.right is None:
                nonlocal answer
                answer += int(''.join([str(val) for val in stack]))
            stack.pop()

        dfs(root)
        return answer

