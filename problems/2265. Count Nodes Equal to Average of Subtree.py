# link: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node) -> (int, int, int):
            '''
            node: Optional TreeNode
            return value: (number of nodes, sum of node values, number of nodes statisfied the requirement)
            '''
            if node is None:
                return (0, 0, 0)
            left_count, left_total, left_ans = dfs(node.left)
            right_count, right_total, right_ans = dfs(node.right)
            count = left_count + right_count + 1
            total = left_total + right_total + node.val
            ans = left_ans + right_ans + int(total // count == node.val)

            return (count, total, ans)
        
        return dfs(root)[2]