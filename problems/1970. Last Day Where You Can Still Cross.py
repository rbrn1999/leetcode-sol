# link: https://leetcode.com/problems/last-day-where-you-can-still-cross/
class UnionFind:
    def __init__(self, m):
        self.m = m
        self.parent = {} # [node, status]
        self.rank = {}
    
    def add(self, node):
        if node not in self.parent:
            self.parent[node] = [node, [node[0]==0, node[0]==self.m-1]]
            self.rank[node] = 1

    def find(self, node):
        self.add(node)
        p = self.parent[node]
        while p != self.parent[p[0]]:
            self.parent[p[0]] = self.parent[self.parent[p[0]][0]]
            p = self.parent[p[0]]
        return p
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1[0]] > self.rank[p2[0]]:
            p1[1] = [p1[1][0] or p2[1][0], p1[1][1] or p2[1][1]]
            self.parent[p2[0]] = p1
        elif self.rank[p1[0]] < self.rank[p2[0]]:
            p2[1] = [p1[1][0] or p2[1][0], p1[1][1] or p2[1][1]]
            self.parent[p1[0]] = p2
        else:
            p1[1] = [p1[1][0] or p2[1][0], p1[1][1] or p2[1][1]]
            self.parent[p2[0]] = p1
            self.rank[p1[0]] += 1

        return True
    
    def isConnected(self, node):
        return all(self.find(node)[1])

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        uf = UnionFind(row)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(len(cells)-1, -1, -1):
            r, c = cells[i]
            r -= 1
            c -= 1
            uf.add((r, c))
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if (nr, nc) in uf.parent:
                    uf.union((r, c), (nr, nc))
            
            if uf.isConnected((r, c)):
                return i
        
        return 0
