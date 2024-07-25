# link: https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import itertools

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        result = 0
        def helper(node: Optional[TreeNode]) -> list[int]:
            if node is None:
                return []
            
            if node.left is None and node.right is None:
                return [0]
            
            left_leaves = [d+1 for d in helper(node.left) if d+1 < distance]
            right_leaves = [d+1 for d in helper(node.right) if d+1 < distance]

            nonlocal result
            for left_leaf, right_leaf, in itertools.product(left_leaves, right_leaves):
                if left_leaf + right_leaf <= distance:
                    result += 1
            
            return left_leaves + right_leaves
        
        helper(root)
        return result