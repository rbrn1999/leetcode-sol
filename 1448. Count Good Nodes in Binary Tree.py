# link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def dfs(path, node):
            if node is None:
                return

            good = True
            for parentVal in path:
                if parentVal > node.val:
                    good = False
                    break

            if good:
                nonlocal result
                result += 1

            path.append(node.val)
            dfs(path.copy(), node.left)
            dfs(path.copy(), node.right)


        dfs([], root)
        return result
