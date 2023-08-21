# link: https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/

class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.parent = list(range(n))
        self.rank = [1] * n
    def find(self, node: int):
        p = self.parent[node]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    def union(self, n1: int, n2: int):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]

        return True
    
    def isConnected(self):
        return max(self.rank) == self.n

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]: 
        edges = sorted([(a, b, w, original_i) for original_i, (a, b, w) in enumerate(edges)], key=lambda x: x[2])

        def MST_weight(include_edge: int|None = None, exclude_edge: int|None = None) -> int:
            uf = UnionFind(n)
            weight = 0
            if include_edge is not None:
                a, b, w, _ = edges[include_edge]
                uf.union(a, b)
                weight += w

            for i, (a, b, w, _) in enumerate(edges):
                if i == include_edge or i == exclude_edge:
                    continue
                if uf.union(a, b):
                    weight += w
            return weight if uf.isConnected() else float('inf')

        min_weight = MST_weight()
        critical = []
        p_critical = []
        for i, (*_, original_i) in enumerate(edges):
            if MST_weight(exclude_edge=i) > min_weight:
                critical.append(original_i)
            elif MST_weight(include_edge=i) == min_weight: # not critical, but can be in the MST
                p_critical.append(original_i)
        
        return [critical, p_critical]
