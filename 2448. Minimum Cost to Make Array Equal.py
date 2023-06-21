# link: https://leetcode.com/problems/minimum-cost-to-make-array-equal/

class Solution:
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        num_cost = sorted(zip(nums, cost))
        curSum = 0
        preSum = []
        for num, _ in num_cost:
            curSum += num
            preSum.append(curSum)


        # initailize the base cost 
        result = 0
        for num, curCost in num_cost:
            result += curCost * (num-num_cost[0][0])

        curCost = result
        suffixCost = sum(cost) - num_cost[0][1]
        prefixCost = num_cost[0][1]

        for i in range(1, len(num_cost)):
            num, cost = num_cost[i]
            diff = num - num_cost[i-1][0]
            curCost += diff * prefixCost - diff * suffixCost
            result = min(result, curCost)
            prefixCost += cost
            suffixCost -= cost
        
        return result
            