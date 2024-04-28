# link: https://leetcode.com/problems/find-all-the-lonely-nodes/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        lonelyNodes = []
        if root.left is None and root.right is not None:
            lonelyNodes.append(root.right.val)
        if root.left is not None and root.right is None:
            lonelyNodes.append(root.left.val)
        return lonelyNodes + self.getLonelyNodes(root.left) + self.getLonelyNodes(root.right)
