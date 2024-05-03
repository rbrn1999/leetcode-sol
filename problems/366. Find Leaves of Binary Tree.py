# link: https://leetcode.com/problems/find-leaves-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> list[list[int]]:
        result = []
        def dfs(node) -> int: # return the max distance of the current node to a leaf node
            if node is None:
                return -1

            d = 1 + max(dfs(node.left), dfs(node.right))

            # followup: actually remove the leaves
            node.left = None
            node.right = None

            if len(result) <= d:
                result.append([])
            result[d].append(node.val)

            return d

        dfs(root)
        return result
