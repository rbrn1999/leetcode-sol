# link: https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        result = []
        queue = deque()
        if root is None:
            return result
        queue.append(root)
        while queue:
            node = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(node.val)
        
        return result
                