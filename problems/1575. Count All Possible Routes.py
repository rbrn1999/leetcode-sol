# link: https://leetcode.com/problems/count-all-possible-routes/

from functools import cache
class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @cache
        def dfs(i, fuel):
            if fuel < 0:
                return 0
            count = 0
            if i == finish:
                count += 1
            for j in range(len(locations)):
                if i == j:
                    continue
                count += dfs(j, fuel - abs(locations[i]-locations[j]))
                count %= 10**9 + 7
            return count
        
        return dfs(start, fuel)
    