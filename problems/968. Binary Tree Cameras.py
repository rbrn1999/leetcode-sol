# link: https://leetcode.com/problems/binary-tree-cameras/
# solution: https://leetcode.com/problems/binary-tree-cameras/discuss/2160386/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
from typing import Optional
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # val 0: not monitored, val 1: camera node, val 2: monitored, val 3: leaf
        def dfs(node):
            if node is None:
                return 0
            count = dfs(node.left) + dfs(node.right)
            cur = min(node.left.val if node.left else 3, node.right.val if node.right else 3)
            
            match cur:
                case 0: # children not monitored, place camera
                    node.val = 1
                    count += 1
                case 1: # has children with camera, already monitored
                    node.val = 2
                
                # 2, 3: children monitored but node current node, let the parent monitor current node latter    
            return count
        
        return dfs(root) + (root.val==0) # if root not monitored: place camera
            
        