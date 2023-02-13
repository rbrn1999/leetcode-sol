# link: https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital

import math
from collections import defaultdict
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        edges = defaultdict(set)
        gas = 0
        for a, b in roads:
            edges[a].add(b)
            edges[b].add(a)

        def dfs(node: int, parent: int = -1) -> int:
            nonlocal gas
            total_people_count = 0
            for neighbor in edges[node]:
                if neighbor == parent:
                    continue
                people_count = dfs(neighbor, node)
                gas += math.ceil(people_count / seats)
                total_people_count += people_count
            return total_people_count + 1

        dfs(0)

        return gas

