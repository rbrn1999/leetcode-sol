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
