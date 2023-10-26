# link: https://leetcode.com/problems/find-largest-value-in-each-tree-row/

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        ans = []
        q.append(root)
        while q:
            val = -float('inf')
            for _ in range(len(q)):
                node = q.popleft()
                val = max(val, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(val)
        
        return ans