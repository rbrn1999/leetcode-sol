# Time Limit Exceeded
class Solution:
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        res = float('inf')
        for i, target in enumerate(nums):
            curCost = 0
            for j in range(len(nums)):
                if i == j:
                    continue
                curCost += abs(nums[j]-target)*cost[j]
                if curCost >= res:
                    break
            res = min(res, curCost)
        return res