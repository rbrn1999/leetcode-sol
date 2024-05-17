# link: https://leetcode.com/problems/optimize-water-distribution-in-a-village/

# Prim's
from collections import defaultdict
import heapq
class Solution:
    def minCostToSupplyWater(self, n: int, wells: list[int], pipes: list[list[int]]) -> int:
        edges = defaultdict(list)
        for h1, h2, c in pipes:
            edges[h1-1].append((h2-1, c))
            edges[h2-1].append((h1-1, c))

        visited = set()
        total_cost = 0
        heap = [(wells[house], house) for house in range(n)]
        heapq.heapify(heap)

        while heap:
            cost, house = heapq.heappop(heap)
            if house in visited:
                continue
            else:
                visited.add(house)

            total_cost += cost

            for next_house, cost in edges[house]:
                if next_house in visited:
                    continue
                heapq.heappush(heap, (cost, next_house))

        return total_cost
