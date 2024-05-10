# link: https://leetcode.com/problems/binary-tree-paths/

# recursion
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        result = []
        path = []

        def dfs(node):
            if not node:
                return

            path.append(node)
            dfs(node.left)
            dfs(node.right)
            if node.left is  None and node.right is None:
                path_str = '->'.join(str(node.val) for node in path)
                result.append(path_str)
            path.pop()

        dfs(root)
        return result

# iterative
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        if not root:
            return []

        result = []
        stack = [(root, [root])]

        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                path_str = '->'.join(str(node.val) for node in path)
                result.append(path_str)

            if node.left:
                stack.append((node.left, path.copy() + [node.left]))
            if node.right:
                stack.append((node.right, path.copy() + [node.right]))


        return result
