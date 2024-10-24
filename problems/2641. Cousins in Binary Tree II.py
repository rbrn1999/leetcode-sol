# link: https://leetcode.com/problems/cousins-in-binary-tree-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        total = root.val
        q = deque()
        q.append(root)

        while q:
            next_total = 0
            for _ in range(len(q)):
                node = q.popleft()
                node.val = total - node.val
                sibling_sum = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
                if node.left:
                    next_total += node.left.val
                    node.left.val = sibling_sum
                    q.append(node.left)
                if node.right:
                    next_total += node.right.val
                    node.right.val = sibling_sum
                    q.append(node.right)
            
            total = next_total
        
        return root
            