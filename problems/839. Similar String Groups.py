# link: https://leetcode.com/problems/similar-string-groups/

from collections import defaultdict

class UnionFind:
    def __init__(self):
        self.rank = defaultdict(int)
        self.parent = {}

    def add(self, node: str) -> bool:
        if node in self.parent:
            return False
        else:
            self.parent[node] = node
            return True

    def find(self, node: str) -> str:
        p = self.parent[node]
        while p != self.parent[p]:
            self.rank.pop(p, None) # slight space optimization
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, n1: str, n2: str) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
        else:
            self.rank[p1] += 1
            self.parent[p2] = p1
        return True

    def groupCount(self) -> int:
        groups = set()
        for node in self.parent:
            groups.add(self.find(node))
        return len(groups)

def isNeighbor(n1: str, n2: str) -> bool:
    diff = []
    diffCount = 0
    for i in range(len(n1)):
        if n1[i] != n2[i]:
            if diffCount == 2:
                return False
            elif diffCount == 1:
                if diff != [n2[i], n1[i]]:
                    return False
            else:
                diff = [n1[i], n2[i]]
            diffCount += 1
    return diffCount % 2 == 0

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        uf = UnionFind()
        count = 0

        for i in range(len(strs)-1):
            uf.add(strs[i])
            for j in range(i+1, len(strs)):
                uf.add(strs[j])
                if isNeighbor(strs[i], strs[j]):
                    uf.union(strs[i], strs[j])

        return uf.groupCount()

