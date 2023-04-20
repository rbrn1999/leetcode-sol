# link: https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> (int, int, int): # (left, right, max)
            if node is None:
                return (-1, -1, -1)

            _, left, leftMax = dfs(node.left)
            right, _, rightMax  = dfs(node.right)
            return (left+1, right+1, max(leftMax, rightMax, left+1, right+1))

        return dfs(root)[2]

