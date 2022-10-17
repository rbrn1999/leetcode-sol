# link: https://leetcode.com/problems/maximum-binary-tree/

# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(start, end): # [start, end)
            max_index = start + nums[start:end].index(max(nums[start:end]))
            node = TreeNode(nums[max_index])
            if max_index != start:
                node.left = dfs(start, max_index)
            if max_index != end-1:
                node.right = dfs(max_index+1, end)
            return node
        return dfs(0, len(nums))
