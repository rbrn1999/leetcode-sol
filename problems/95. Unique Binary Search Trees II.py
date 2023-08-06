# link: https://leetcode.com/problems/unique-binary-search-trees-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n):
        dp = {}
        def generate(i,j):
            if (i, j) in dp:
                return dp[(i, j)]
            if j-i < 0:
                return [None]
            if j-i == 0:
                return [TreeNode(i)]

            dp[(i, j)] = []
            for mid in range(i,j+1):
                lefts = generate(i,mid-1)
                rights = generate(mid+1,j)
                for l in lefts:
                    for r in rights:
                        root = TreeNode(mid, l, r)
                        dp[(i, j)].append(root)
                        
            return dp[(i, j)]

        return generate(1,n)