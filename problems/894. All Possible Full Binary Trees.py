# link: https://leetcode.com/problems/all-possible-full-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Top-Bottom
from functools import cache
class Solution:
    @cache
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        if n == 1:
            return [TreeNode()]
        n -= 1
        for i in range(1, n, 2): # To form another full binary subtree we need to + or - 2 nodes
            lefts = self.allPossibleFBT(i)
            rights = self.allPossibleFBT(n-i)
            for l in lefts:
                for r in rights:
                    root = TreeNode(0, l, r)
                    result.append(root)
        return result


# Bottom-Up
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = defaultdict(list)
        dp[1].append(TreeNode()) # base case
        for i in range(3, n+1, 2):
            curr_n = i - 1 # minus the root node in the middle
            for left_n in range(1, curr_n, 2): 
                right_n = curr_n - left_n
                for left in dp[left_n]:
                    for right in dp[right_n]:
                        root = TreeNode(0, left, right)
                        dp[i].append(root)

        return dp[n]