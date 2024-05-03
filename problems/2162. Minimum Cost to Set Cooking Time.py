# link: https://leetcode.com/problems/minimum-cost-to-set-cooking-time/

class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        min_cost = float('inf')
        def helper(minutes: int, seconds: int) -> int:
            prev = startAt
            cost = 0
            # first digit
            if minutes > 9:
                if minutes // 10 != prev:
                    cost += moveCost
                    prev = minutes // 10
                cost += pushCost

            # second digit
            if minutes > 0:
                if minutes % 10 != prev:
                    cost += moveCost
                    prev = minutes % 10
                cost += pushCost

            # 3rd digit
            if minutes > 0 or seconds > 9:
                if seconds // 10 != prev:
                    cost += moveCost
                    prev = seconds // 10
                cost += pushCost

            if minutes > 0 or seconds > 0:
                if seconds % 10 != prev:
                    cost += moveCost
                cost += pushCost
            
            return cost

        # seconds under 60
        minutes = targetSeconds // 60
        seconds = targetSeconds % 60

        minCost = float('inf')
        if minutes < 100:
            min_cost = helper(minutes, seconds)
        
        # seconds >= 60
        minutes = targetSeconds // 60 - 1
        seconds = 60 + targetSeconds % 60
        if minutes >= 0 and minutes < 100 and seconds < 100:
            min_cost = min(min_cost, helper(minutes, seconds))
            return min_cost
        
        # doesn't have this test case
        if minutes > 99:
            return helper(99, 99)
        
        return min_cost


