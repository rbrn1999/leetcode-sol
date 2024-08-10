# link: https://leetcode.com/problems/minimum-cost-to-convert-string-i/


# Dijkstra's Algorithm
from collections import defaultdict
import heapq
class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        adj = defaultdict(dict)
        for i in range(len(original)):
            adj[original[i]][changed[i]] = min(adj[original[i]].get(changed[i], float('inf')), cost[i])

        minCost = defaultdict(dict)
        for s in source:
            minCost[s][s] = 0

        for c in original:
            #shortest path
            heap = [(0, c)]
            visited = set()
            while heap:
                cur_cost, cur_c = heapq.heappop(heap)
                if cur_c in visited:
                    continue
                minCost[c][cur_c] = cur_cost
                visited.add(cur_c)
                for next_c, next_cost in adj[cur_c].items():
                    if next_c in visited:
                        continue
                    heapq.heappush(heap, (cur_cost + next_cost, next_c))

        totalCost = 0
        for s, t in zip(source, target):
            if t not in minCost[s]:
                return -1
            totalCost += minCost[s][t]

        return totalCost
