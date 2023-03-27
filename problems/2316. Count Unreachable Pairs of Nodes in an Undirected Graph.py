# link: https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, node):
        p = self.parent[node]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.rank[p1] += 1
        return True
    def groupSizes(self):
        groups = {}
        for node in range(self.n):
            p = self.find(node)
            groups[p] = groups.get(p, 0) + 1
        return groups

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for n1, n2 in edges:
            uf.union(n1, n2)

        sizes = list(uf.groupSizes().values())
        pairs = 0

        # O(groupSize)
        pairs = (sum(sizes) ** 2 - sum(size ** 2 for size in sizes)) // 2
        # or
        # remainingNodes = n
        # for size in sizes:
        #     remainingNodes -= size
        #     pairs += size * remainingNodes

        # O((groupSize)^2)
        # for i in range(len(sizes)):
        #     for j in range(i+1, len(sizes)):
        #         pairs += sizes[i] * sizes[j]

        return pairs

