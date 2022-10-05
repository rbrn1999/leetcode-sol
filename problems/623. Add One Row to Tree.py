# link: https://leetcode.com/problems/add-one-row-to-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val, root)
            return node

        curLevel = [root]
        nextLevel = []
        curDepth = 1

        node = None
        while curLevel and curDepth < depth-1:
            node = curLevel.pop(0)
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)

            if not curLevel:
                curLevel, nextLevel = nextLevel, []
                curDepth += 1


        for node in curLevel:
            left = TreeNode(val, left=node.left)
            right = TreeNode(val, right=node.right)
            node.left = left
            node.right = right

        return root
