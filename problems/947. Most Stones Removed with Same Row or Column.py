# link: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
'''
Solution reference: https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/discuss
Time Complexity: O(n)
Since we don't don't revisited stones
Space Complexity: O(n)
store visited, rowOfColumns, columnOfRows
'''
from collections import defaultdict
class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        cols = defaultdict(set)
        rows = defaultdict(set)
        stone_set = set((row, col) for row, col in stones)
        for row, col in stones:
            cols[row].add(col)
            rows[col].add(row)
        
        def dfs(row, col):
            if (row, col) not in stone_set:
                return
            else:
                stone_set.remove((row, col))
            while cols[row]:
                c = cols[row].pop()
                rows[c].remove(row)
                dfs(row, c)
            while rows[col]:
                r = rows[col].pop()
                cols[r].remove(col)
                dfs(r, col)
        
        stoneGroupCount = 0        
        
        while stone_set:
            r, c = stone_set.pop()
            rows[c].remove(r)
            cols[r].remove(c)
            stone_set.add((r, c))
            dfs(r, c)
            stoneGroupCount += 1
        
        return len(stones) - stoneGroupCount

# DFS
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        cols = defaultdict(list)
        rows = defaultdict(list)
        visited = set()
        count = 0

        for r, c in stones:
            cols[c].append(r)
            rows[r].append(c)

        def dfs(row, col) -> int:
            if len(rows[row]) == 0 and len(cols[col]) == 0:
                return 0

            visited.add((row, col))
            count = 1
            for c in rows[row]:
                if (row, c) not in visited:
                    count += dfs(row, c)
            
            for r in cols[col]:
                if (r, col) not in visited:
                    count += dfs(r, col)
            
            return count
        
        for r, c in stones:
            if (r, c) not in visited:
                count += dfs(r, c) - 1
                visited.remove((r, c))
        
        return count

# Union Find
from collections import defaultdict
class UnionFind:
    def __init__(self, n: int):
        self.par = list(range(n))
        self.rank = [0] * n

    def find(self, stone: int) -> int:
        par = self.par[stone]
        while par != self.par[par]:
            self.par[par] = self.par[self.par[par]]
            par = self.par[par]
        return par

    def union(self, s1: int, s2: int) -> bool:
        p1, p2 = self.find(s1), self.find(s2)

        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.rank[p2] = self.rank[p1]
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.rank[p1] = self.rank[p2]
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        
        return True

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        cols = defaultdict(list)
        rows = defaultdict(list)
        n = len(stones)
        removes = 0
        uf = UnionFind(n)

        for i, (r, c) in enumerate(stones):
            cols[c].append(i)
            rows[r].append(i)

        for i, (r, c) in enumerate(stones):
            for j in rows[r]:
                if i != j and uf.union(i, j):
                    removes += 1
            for j in cols[c]:
                if i != j and uf.union(i, j):
                    removes += 1
        
        return removes