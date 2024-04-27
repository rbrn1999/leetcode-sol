# link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

class UnionFind:
    def __init__(self, n: int):
        self.par = list(range(n))
        self.rank = [0] * n

    def find(self, node: int) -> int:
        p = self.par[node]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.rank[p1] += 1
            self.par[p2] = p1
        return True

class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        unionFind = UnionFind(n)
        components = n
        for a, b in edges:
            if unionFind.union(a, b):
                components -= 1

        return components
