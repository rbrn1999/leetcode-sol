# link: https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/

from collections import defaultdict
from functools import cache
class Solution:
    def maximumPoints(self, edges: list[list[int]], coins: list[int], k: int) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        @cache
        def dfs(node: int=0, reduces: int=0) -> int:
            if reduces > 13:
                return 0
            
            visited.add(node)
            val = coins[node]
            for _ in range(reduces):
                val //= 2
            
            total = val - k
            for child in graph[node]:
                if child in visited:
                    continue
                total += dfs(child, reduces)
            
            if val - k >= val // 2:
                visited.remove(node)
                return total
            
            total2 = val // 2
            for child in graph[node]:
                if child in visited:
                    continue
                total2 += dfs(child, reduces+1)     
                
            visited.remove(node)
            return max(total, total2)
        
        return dfs()