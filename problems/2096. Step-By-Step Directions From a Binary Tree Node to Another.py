# link: https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        root_to_start = []
        root_to_end = []

        def dfs(node, target, path, final_path):
            if node is None:
                return
            if node.val == target:
                final_path[:] = path.copy()
                return
            
            path.append('L')
            dfs(node.left, target, path, final_path)
            path.pop()

            path.append('R')
            dfs(node.right, target, path, final_path)
            path.pop()
        
        dfs(root, startValue, [], root_to_start)
        dfs(root, destValue, [], root_to_end)

        i = 0
        n = min(len(root_to_start), len(root_to_end))
        while i < n and root_to_start[i] == root_to_end[i]:
            i += 1
        
        return 'U' * (len(root_to_start)-i) + ''.join(root_to_end[i:])

        
        
