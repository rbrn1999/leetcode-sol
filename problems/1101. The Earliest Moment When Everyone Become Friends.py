# link: https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

class UnionFind:
    def __init__(self, n: int):
        self.par = list(range(n))
        self.rank = [0] * n

    def find(self, node: int) -> int: # returns parent of node
        p = self.par[node]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]

        return p

    def union(self, n1: int, n2: int) -> bool: # return True if union 2 different groups
        p1, p2 = self.find(n1), self.find(n2)
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
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        groups = n
        logs.sort()
        unionFind = UnionFind(n)

        for timestamp, x, y in logs:
            if unionFind.union(x, y):
                groups -= 1
                if groups == 1:
                    return timestamp

        return -1
