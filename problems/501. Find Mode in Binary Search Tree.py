# link: https://leetcode.com/problems/find-mode-in-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> list[int]:
        max_freq = 0
        freq = 0
        num = -1
        ans = []
        def dfs(node):
            if node is None:
                return

            dfs(node.left)

            nonlocal max_freq, freq, num
            if node.val == num:
                freq += 1
            else:
                freq = 1
                num = node.val
            if freq > max_freq:
                ans.clear()
                max_freq = freq
            if freq == max_freq and (not ans or ans[-1] != node.val):
                ans.append(node.val)
            
            dfs(node.right)
        
        dfs(root)
        return ans