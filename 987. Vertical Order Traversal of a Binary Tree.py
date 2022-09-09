# link: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cmp_to_key
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []
        minCol = maxCol = 0
        def compare(lhs, rhs):
            if lhs[1][0] < rhs[1][0]:
                return -1
            elif lhs[1][0] > rhs[1][0]:
                return 1
            else:
                return lhs[0] - rhs[0]

        def dfs(node, ind): # ind: (row, col)
            if node is None:
                return
            else:
                nodes.append((node.val, ind))
                nonlocal minCol, maxCol
                minCol = min(minCol, ind[1])
                maxCol = max(maxCol, ind[1])
            if node.left:
                dfs(node.left, (ind[0]+1, ind[1]-1))
            if node.right:
                dfs(node.right, (ind[0]+1, ind[1]+1))


        dfs(root, (0, 0))

        # create unsort vertical level 2d-list m*(-1)
        result = [ [] for _ in range(maxCol-minCol+1)]
        for node in nodes:
            result[node[1][1]-minCol].append(node)

        for i, col in enumerate(result):
            col.sort(key=cmp_to_key(compare))
            result[i] = [v[0] for v in col]
        return result
