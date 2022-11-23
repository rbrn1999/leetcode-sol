# link: https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        vals = []
        ans = []
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)
        
        dfs(root)
        n = len(vals)
        for q in queries:
            ind = bisect.bisect_left(vals, q, 0, n)
            if ind == n:
                ans.append([vals[n-1], -1])
            elif ind == 0 and vals[0] != q:
                ans.append([-1, vals[0]])
            elif vals[ind] != q:
                ans.append([vals[ind-1], vals[ind]])
            else:
                ans.append([q, q])
        
        return ans