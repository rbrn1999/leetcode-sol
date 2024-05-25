# link: https://leetcode.com/problems/distribute-coins-in-binary-tree/# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node) -> list[int]:
            # return : extra coins, used moves
            if node is None:
                return [0, 0]
            
            left = dfs(node.left)
            right = dfs(node.right)
            # abs(left/right . moves): move this many extra coins by 1 step
            moves = left[0] + abs(left[1]) + right[0] + abs(right[1])
            # positive extra_coins: must pass coins to the parent
            # negative extra_coints: must get coins from the parent
            extra_coins = left[1] + right[1] + (node.val - 1)

            return moves, extra_coins
            
        return dfs(root)[0]