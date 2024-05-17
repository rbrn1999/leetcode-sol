# link: https://leetcode.com/problems/minimum-cost-to-hire-k-workers/
import heapq
class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        '''
        for each person, the wage should be the max(wage[i]/quality[i]) for i in the group
        '''
        n = len(quality)
        min_cost = float('inf')

        wage_quality = sorted(zip(wage, quality), key=lambda x: x[0] / x[1])

        quality_maxHeap = [-wage_quality[i][1] for i in range(k-1)]

        heapq.heapify(quality_maxHeap)
        total_quality = -sum(quality_maxHeap)

        for i in range(k-1, n):
            # cost = quality * max(wage per quality)
            ratio = wage_quality[i][0] / wage_quality[i][1]
            total_quality += wage_quality[i][1]
            cost = total_quality * ratio

            # update heap and sum
            if quality_maxHeap and wage_quality[i][1] < -quality_maxHeap[0]:
                total_quality += - (-heapq.heappushpop(quality_maxHeap, -wage_quality[i][1]))
            else:
                total_quality -= wage_quality[i][1]

            min_cost = min(min_cost, cost)

        return min_cost

# Kruskal's
class UnionFind:
    def __init__(self, n: int):
        self.par = list(range(n+1))
        self.rank = [0] * (n+1)

    def find(self, house: int) -> int:
        p = self.par[house]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]

        return p

    def union(self, h1: int, h2: int) -> bool:
        p1, p2 = self.find(h1), self.find(h2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1

        return True

class Solution:
    def minCostToSupplyWater(self, n: int, wells: list[int], pipes: list[list[int]]) -> int:
        # use index 0 as the initial water source (building a well)

        unionFind = UnionFind(n)

        edges = [(wells[house-1], 0, house) for house in range(1, n+1)] + [(cost, house1, house2) for house1, house2, cost in pipes]
        edges.sort()

        total_cost = 0
        for cost, h1, h2 in edges:
            if unionFind.union(h1, h2):
                total_cost += cost

        return total_cost
