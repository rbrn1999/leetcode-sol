# link: https://leetcode.com/problems/network-delay-time/

from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for source, destination, cost in times:
            graph[source].append((destination, cost))
            
        queue = [(0, k)] # (cost, node)
        visited = set()
        max_cost = 0
        
        while queue:
            cost, node = heappop(queue)
            
            if node in visited:
                continue
            else:
                visited.add(node)
            
            max_cost = max(max_cost, cost)
            
            neighbors = graph[node]
            
            for neighbor in neighbors:
                new_node, new_cost = neighbor
                if new_node not in visited:
                    cur_cost = cost + new_cost
                    heappush(queue, (cur_cost, new_node))
        
        return max_cost if len(visited) == n else -1