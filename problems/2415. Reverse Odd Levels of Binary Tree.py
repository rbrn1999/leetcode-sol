# link: https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        levels = [[root]]
        while levels[-1]:
            if levels[-1][0].left is None:
               break
            children = []
            for node in levels[-1]:
                children.extend([node.left, node.right])
            levels.append(children)

        for i in range(len(levels)):
            if i % 2 == 1:
                levels[i].reverse()


        for i in range(len(levels)-1):
            for j in range(len(levels[i])):
                levels[i][j].left = levels[i+1][2*j]
                levels[i][j].right = levels[i+1][2*j + 1]

        return root
