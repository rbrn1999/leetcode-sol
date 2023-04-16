# link: https://leetcode.com/problems/most-frequent-subtree-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        sum_count = defaultdict(int)
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            cur_sum = node.val + dfs(node.left) + dfs(node.right)
            sum_count[cur_sum] += 1
            return cur_sum

        dfs(root)
        max_value = max(sum_count.values())
        return [treeSum for treeSum in sum_count.keys() if sum_count[treeSum] == max_value]

