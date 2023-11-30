# link: https://leetcode.com/problems/knight-dialer/

# Top-Down
from functools import cache
class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        
        graph = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}

        @cache
        def dfs(cell: int, i: int) -> int:
            if i == n-1:
                return 1
            return sum(dfs(next_cell, i+1) for next_cell in graph[cell]) % (10 ** 9 + 7)
        
        ans = 0
        for num in range(5):
            ans += dfs(num, 0)
            ans %= (10 ** 9 + 7)
        for num in range(6, 10):
            ans += dfs(num, 0)
            ans %= (10 ** 9 + 7)
        
        return ans

# Bottom-Up
class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        
        graph = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6], 5: []}

        state = [1] * 10
        state[5] = 0

        for _ in range(n-1):
            new_state = [0] * 10
            for num in range(10):
                for next_num in graph[num]:
                    new_state[next_num] += state[num]
                    new_state[next_num] %= (10 ** 9 + 7)
            state = new_state

        return sum(state) % (10 ** 9 + 7)