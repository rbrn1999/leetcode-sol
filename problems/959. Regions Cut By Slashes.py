# link: https://leetcode.com/problems/regions-cut-by-slashes/

import itertools
from collections import defaultdict
class UnionFind:
    def __init__(self):
        self.par = {}
        self.rank = defaultdict(int)

    def add(self, n):
        self.par.setdefault(n, n)

    def find(self, n: tuple[int, int, int]) -> tuple[int, int, int]:
        self.add(n)
        p = self.par[n]
        while self.par[p] != p:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]

        return p

    def union(self, n1: tuple[int, int, int], n2: tuple[int, int, int]) -> bool:
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
    def regionsBySlashes(self, grid: list[str]) -> int:
        ROW, COL = len(grid), len(grid[0])
        uf = UnionFind()
        components = ROW * COL * 2

        for r, c in itertools.product(range(ROW), range(COL)):
            if grid[r][c] == ' ':
                components -= int(uf.union((r, c, 0), (r, c, 1)))
                if r > 0:
                    portion = 1 if grid[r-1][c] == '/' else 0
                    components -= int(uf.union((r, c, 0), (r-1, c, portion)))
                if r < ROW-1:
                    portion = 0 if grid[r+1][c] == '/' else 1
                    components -= int(uf.union((r, c, 0), (r+1, c, portion)))
                if c > 0:
                    portion = 1
                    components -= int(uf.union((r, c, 0), (r, c-1, portion)))
                if c < COL-1:
                    portion = 0
                    components -= int(uf.union((r, c, 0), (r, c+1, portion)))
            elif grid[r][c] == '/':
                if r > 0:
                    portion = 1 if grid[r-1][c] == '/' else 0
                    components -= int(uf.union((r, c, 0), (r-1, c, portion)))
                if r < ROW-1:
                    portion = 0 if grid[r+1][c] == '/' else 1
                    components -= int(uf.union((r, c, 1), (r+1, c, portion)))
                if c > 0:
                    portion = 1
                    components -= int(uf.union((r, c, 0), (r, c-1, portion)))
                if c < COL-1:
                    portion = 0
                    components -= int(uf.union((r, c, 1), (r, c+1, portion)))
            else:
                if r > 0:
                    portion = 1 if grid[r-1][c] == '/' else 0
                    components -= int(uf.union((r, c, 1), (r-1, c, portion)))
                if r < ROW-1:
                    portion = 0 if grid[r+1][c] == '/' else 1
                    components -= int(uf.union((r, c, 0), (r+1, c, portion)))
                if c > 0:
                    portion = 1
                    components -= int(uf.union((r, c, 0), (r, c-1, portion)))
                if c < COL-1:
                    portion = 0
                    components -= int(uf.union((r, c, 1), (r, c+1, portion)))

        return components
