# link: https://leetcode.com/problems/min-cost-to-connect-all-points/solution/
class UnionFind:
    def __init__(self, size):
        self.group = [i for i in range(size)]
        self.rank = [0] * size
        
    def find(self, node: int) -> int:
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]
    
    def join(self, node1: int, node2: int) -> bool:
        group1 = self.find(node1)
        group2 = self.find(node2)
        
        if group1 == group2:
            return False
        
        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2
        else:
            self.group[group1] = group2
            self.rank[group2] += 1
        
        return True

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        def distance(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        n=len(points)
        edges = [] # (weight, node1, node2)
        for i in range(n):
            for j in range(i+1, n):
                edges.append((distance(points[i], points[j]), i, j))
                
        edges.sort()
        
        uf = UnionFind(n)
        mst_cost = 0
        edges_used = 0
        
        for weight, node1, node2 in edges:
            if uf.join(node1, node2):
                mst_cost += weight
                edges_used += 1
                if edges_used == n-1:
                    break

        return mst_cost        