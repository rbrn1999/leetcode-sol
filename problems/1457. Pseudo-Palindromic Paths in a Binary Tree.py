# link: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        odd = [0] * 10
        def dfs(node) -> int:
            if node is None:
                return 0

            odd[node.val] = (odd[node.val] + 1) % 2
            if node.left is None and node.right is None:
                count = sum(odd)
                odd[node.val] = (odd[node.val] - 1) % 2
                if count <= 1:
                    return 1
                else:
                    return 0
            result = dfs(node.left) + dfs(node.right)
            odd[node.val] = (odd[node.val] - 1) % 2
            return result
        
        return dfs(root)