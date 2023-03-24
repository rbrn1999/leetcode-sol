# link: https://leetcode.com/problems/number-of-operations-to-make-network-connected/

class UnionFind:
    def __init__(self, n: int) -> int:
        self.n = n
        self.parents = list(range(n))
        self.rank = [0] * n

    def find(self, node: int) -> int:
        p = self.parents[node]
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p

    def union(self, node1: int, node2: int) -> int:
        p1, p2 = self.find(node1), self.find(node2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parents[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parents[p1] = p2
        else:
            self.parents[p2] = p1
            self.rank[p1] += 1

        return True

    def connectedComponents(self):
        groups = set()
        for node in range(self.n):
            groups.add(self.find(node))
        return len(groups)

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        uf = UnionFind(n)
        for node1, node2 in connections:
            uf.union(node1, node2)

        return uf.connectedComponents() - 1

