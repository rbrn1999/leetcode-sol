# link: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = 0
        def dfs(node, seen):
            if node is None:
                return

            if node.val in seen:
                seen.remove(node.val)
            else:
                seen.add(node.val)

            if node.left is None and node.right is None:
                if len(seen) <= 1:
                    nonlocal count
                    count += 1
                return

            dfs(node.left, seen.copy())
            dfs(node.right, seen.copy())

        dfs(root, set())
        return count

