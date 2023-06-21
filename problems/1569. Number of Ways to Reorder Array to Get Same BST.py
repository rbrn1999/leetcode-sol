# link: https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

import math

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def numOfWays(self, nums: List[int]) -> int:

        # construct binary search tree
        root = Node(nums[0])
        for i in range(1, len(nums)):
            node = root
            while True:
                if nums[i] < node.val:
                    if node.left:
                        node = node.left
                    else:
                        node.left = Node(nums[i])
                        break
                else:
                    if node.right:
                        node = node.right
                    else:
                        node.right = Node(nums[i])
                        break

        def dfs(root, low=1, high=len(nums)) -> int:
            if high - low < 2:
                return 1

            left = (root.val - low)
            right = (high - root.val)
            combs = math.comb(left+right, left) * dfs(root.left, low, root.val-1) * dfs(root.right, root.val+1, high)
            return combs % (10 ** 9 + 7)

        return dfs(root) - 1

