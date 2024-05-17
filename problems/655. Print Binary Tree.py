# link: https://leetcode.com/problems/print-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def height(root) -> int:
            if root is None:
                return -1

            return 1 + max(height(root.left), height(root.right))

        def dfs(root, row: int, col: int) -> None:
            if not root:
                return
            res[row][col] = str(root.val)
            dfs(root.left, row+1, col-2**(h-row-1))
            dfs(root.right, row+1, col+2**(h-row-1))

        h = height(root)
        res = [[""] * (2 ** (h+1)-1) for _ in range(h+1)]
        dfs(root, 0, (len(res[0])-1)//2)

        return res
