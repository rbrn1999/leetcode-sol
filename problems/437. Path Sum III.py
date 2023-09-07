# link: https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        pathSum_count = defaultdict(int) # count of sums from root to each node in the path
        pathSum_count[0] = 1
        count = 0
        def dfs(root, curSum):
            if root is None:
                return
            nonlocal count
            curSum += root.val
            prevSum = curSum - targetSum
            count += pathSum_count.get(prevSum, 0)
            pathSum_count[curSum] += 1
            dfs(root.left, curSum)
            dfs(root.right, curSum)
            pathSum_count[curSum] -= 1
            if pathSum_count[curSum] == 0:
                del pathSum_count[curSum]
        
        dfs(root, 0)
        return count