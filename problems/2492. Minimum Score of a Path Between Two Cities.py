# link: https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)
        self.score = [float('inf')] * (n+1)

    def union(self, node1: int, node2: int, distance: int) -> bool:
        p1 = self.find(node1)
        p2 = self.find(node2)

        score = min(self.score[p1], self.score[p2], distance)
        self.score[p1] = self.score[p2] = score

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.rank[p1] += 1
            self.parent[p2] = p1

        return True

    def find(self, node: int) -> int:
        p = self.parent[node]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UnionFind(n)
        for node1, node2, distance in roads:
            uf.union(node1, node2, distance)
        return uf.score[uf.find(n)]

