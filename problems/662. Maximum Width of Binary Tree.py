# link: https://leetcode.com/problems/maximum-width-of-binary-tree/

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root, 1))
        max_width = 0
        while q:
            start = q[0][1]
            end = q[-1][1]
            for _ in range(len(q)):
                node, index = q.popleft()
                if node.left:
                    q.append((node.left, index*2))
                if node.right:
                    q.append((node.right, index*2+1))
            max_width = max(max_width, end-start + 1)

        return max_width

