# link: https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class UnionFind:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = list(range(n))

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
            self.rank[p1] += 1
            self.parent[p2] = p1
        return True

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        answer = [False] * len(queries)
        edgeList.sort(key=lambda x: x[2], reverse=True)
        queries = sorted(((i, query) for (i, query) in enumerate(queries)), key=lambda x: x[1][2])
        uf = UnionFind(n)
        for i, query in queries:
            u, v, limit = query
            while edgeList and edgeList[-1][2] < limit:
                n1, n2, weight = edgeList.pop()
                uf.union(n1, n2)
            answer[i] = uf.find(u) == uf.find(v)

        return answer

