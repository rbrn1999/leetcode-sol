# link: https://leetcode.com/problems/deepest-leaves-sum/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional        
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_level = -1
        nodes_sum = 0
        def traverse(root, level):
            nonlocal max_level, nodes_sum
            if root is None:
                return
            traverse(root.left, level+1)
            traverse(root.right, level+1)
            if level > max_level:
                max_level = level
                nodes_sum = 0
            if level == max_level:
                nodes_sum += root.val
            
        traverse(root, 0)
        return nodes_sum
        