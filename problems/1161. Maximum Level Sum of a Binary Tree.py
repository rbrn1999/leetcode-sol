# link: https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        level = 1
        maxSum = -float('inf')
        maxSumLevel = 0
        while q:
            curSum = 0
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                curSum += node.val

            if curSum > maxSum:
                maxSum = curSum
                maxSumLevel = level

            level += 1

        return maxSumLevel
