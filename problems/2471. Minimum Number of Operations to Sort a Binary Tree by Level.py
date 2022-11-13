# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def minimumSwaps(arr):
            pos = sorted(list(enumerate(arr)), key=lambda x: x[1])
            count = 0
            
            for i in range(len(arr)):
                while True:
                    if pos[i][0] == i:
                        break
                    count += 1
                    swap_ind = pos[i][0]
                    pos[i], pos[swap_ind] = pos[swap_ind], pos[i]
            return count
        
        count = 0
        q = deque([root])
        while q:
            curLevel = []
            for _ in range(len(q)):
                node = q.popleft()
                curLevel.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            count += minimumSwaps(curLevel)
            # count += seleSortCost(curLevel)
        
        return count
        
        