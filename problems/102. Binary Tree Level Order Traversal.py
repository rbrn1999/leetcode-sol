# link: https://leetcode.com/problems/binary-tree-level-order-traversal/

# queue solution (FIFO)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        result = [[]]
        cur_lvl = deque([root])
        nxt_lvl = deque()
        while cur_lvl:
            node = cur_lvl.popleft()
            result[-1].append(node.val)
            if node.left:
                nxt_lvl.append(node.left)
            if node.right:
                nxt_lvl.append(node.right)
            if len(cur_lvl) == 0 and len(nxt_lvl) > 0:
                cur_lvl, nxt_lvl = nxt_lvl, deque()
                result.append([])
                
        return result

# recursion solution
# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         result = []
#         self.myFunc(root, 0, result)
#         return result
    
#     def myFunc(self, root, level, result):
#         if root is None:
#             return
#         if len(result) <= level:
#             result.append([])
#         result[level].append(root.val)
#         self.myFunc(root.left, level + 1, result)
#         self.myFunc(root.right, level + 1, result)