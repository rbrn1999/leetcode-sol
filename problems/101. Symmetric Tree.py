# link: https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        queue = deque()
        queue.append(root)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node is None:
                    continue
                queue.extend([node.left, node.right])
            for i in range(len(queue)//2):
                if (queue[i] is None) != (queue[-i-1] is None):
                    return False
                if queue[i] and queue[-i-1] and (queue[i].val != queue[-i-1].val):
                    return False
        
        return True
