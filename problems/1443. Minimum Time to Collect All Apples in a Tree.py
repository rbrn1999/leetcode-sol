# link: https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        graph = defaultdict(set)
        for source, dest in edges:
            graph[source].add(dest)
            graph[dest].add(source)
        
        def dfs(node: int, parent: int) -> int:
            time = 0
            for child in graph[node]:
                if child == parent:
                    continue
                child_cost = dfs(child, node) 
                time += child_cost + (2 if child_cost > 0 or hasApple[child] else 0)
            return time
        
        return dfs(0, -1)
