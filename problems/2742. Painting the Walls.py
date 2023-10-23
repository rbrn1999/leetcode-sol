# link: https://leetcode.com/problems/painting-the-walls/

class Solution:
    def paintWalls(self, cost: list[int], time: list[int]) -> int:
        n = len(cost)
        dp = {n: 0}
        min_cost = float('inf')
        for i in range(n):
            temp = {}
            for k, cur_cost in dp.items():
                temp[k] = min(temp.get(k, float('inf')), cur_cost)
                if k - time[i] - 1 <= 0:
                    min_cost = min(min_cost, cur_cost + cost[i])
                else:
                    temp[k-time[i]-1] = min(temp.get(k-time[i]-1, float('inf')), cur_cost + cost[i])
            dp = temp
        
        return min_cost