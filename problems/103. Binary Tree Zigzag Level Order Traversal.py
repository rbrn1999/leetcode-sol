# link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        reverse = False
        zigzag = []
        queue = deque()
        queue.append(root)

        while queue:
            cur_level = deque()
            for _ in range(len(queue)):
                node = queue.popleft()
                if reverse:
                    cur_level.appendleft(node.val)
                else:
                    cur_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            zigzag.append(cur_level)
            reverse = not reverse

        return zigzag

