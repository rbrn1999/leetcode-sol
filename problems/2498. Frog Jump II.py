# link: https://leetcode.com/problems/frog-jump-ii/

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        n = len(stones)
        maxCost = 0
        left = right = 0
        for i in range(1, n):
            maxCost = max(maxCost, stones[i] - stones[left])
            left, right = right, i

        return maxCost
