# link: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        def dfs(node):
            if node is None:
                return False
            nonlocal s
            if node.val not in s:
                s.add(k-node.val)
                return dfs(node.left) or dfs(node.right)
            else:
                return True

        return dfs(root)
