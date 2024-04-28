# link: https://leetcode.com/problems/number-of-islands-ii/

class UnionFind:
    def __init__(self):
        self.rank = {}
        self.par = {}

    def add(self, r, c):
        self.par[(r, c)] = (r, c)
        self.rank[(r, c)] = 0

    def find(self, r, c) -> tuple[int, int]:
        p = self.par[(r, c)]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, r1, c1, r2, c2) -> bool:
        p1, p2 = self.find(r1, c1), self.find(r2, c2)
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
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        unionFind = UnionFind()
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        components = 0
        visited = set()
        result = []
        for r, c in positions:
            if (r, c) in visited:
                result.append(result[-1])
                continue
            else:
                unionFind.add(r, c)
                visited.add((r, c))

            components += 1
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if ((nr, nc) not in unionFind.par
                    or nr < 0 or nr >= m
                    or nc < 0 or nc >= n
                ):
                    continue
                if unionFind.union(r, c, nr, nc):
                    components -= 1

            result.append(components)

        return result
