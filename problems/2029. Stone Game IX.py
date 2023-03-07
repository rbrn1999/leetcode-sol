# NOT SOLVED YET: wrong answer

from collections import defaultdict
from functools import cache
class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        n = len(stones)
        number_remains = defaultdict(lambda: 0)
        for stone in stones:
            number_remains[stone % 3] += 1
        @cache
        def dfs(i=0, remain=0):
            if i == n:
                return False
            if all(value == 0 for value in number_remains.values()):
                return False
            if number_remains[(3-remain+1) % 3] == 0 and number_remains[(3-remain+2) % 3] == 0:
                return i % 2 == 1
            state = i%2 == 1
            if number_remains[(3-remain+1) % 3] > 0:
                number_remains[(3-remain+1) % 3] -= 1
                state = dfs(i+1, 1)
                number_remains[(3-remain+1) % 3] += 1

            if number_remains[(3-remain+2) % 3] > 0:
                number_remains[(3-remain+2) % 3] -= 1
                state = dfs(i+1, 2)
                number_remains[(3-remain+2) % 3] += 1
    
            return state
        
        return dfs()


stones = [19,2,17,20,7,17]
print(Solution().stoneGameIX(stones))