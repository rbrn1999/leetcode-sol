# link: https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

import copy
class UnionFind:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = list(range(n))

    def find(self, node):
        node -= 1
        p = self.parent[node]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, n1, n2):
        n1 -= 1
        n2 -= 1
        p1, p2 = self.find(n1), self.find(n2)
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

    def isConnected(self):
        if not self.parent:
            return True
        root = self.find(0)
        for node in range(1, len(self.parent)):
            if self.find(node) != root:
                return False
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        count = 0


        # edges.sort()
        # bucket sort
        low = 0
        mid = 0
        high = len(edges)-1
        while mid <= high:
            if edges[mid][0] == 1:
                edges[low], edges[mid] = edges[mid], edges[low]
                low += 1
                mid += 1
            elif edges[mid][0] == 2:
                mid += 1
            else:
                edges[mid], edges[high] = edges[high], edges[mid]
                high -= 1


        uf = UnionFind(n)
        while edges and edges[-1][0] == 3:
            _, u, v = edges.pop()
            if not uf.union(u, v):
                count += 1

        uf_bob = copy.deepcopy(uf)
        while edges and edges[-1][0] == 2:
            _, u, v = edges.pop()
            if not uf_bob.union(u, v):
                count += 1

        if not uf_bob.isConnected():
            return -1

        while edges and edges[-1][0] == 1:
            _, u, v = edges.pop()
            if not uf.union(u, v):
                count += 1

        return count if uf.isConnected() else -1

