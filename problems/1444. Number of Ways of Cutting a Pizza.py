# link: https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/

from functools import cache

class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        @cache
        def hasApple(row_start, row_end, col_start, col_end) -> bool:
            for row in range(row_start, row_end+1):
                for col in range(col_start, col_end+1):
                    if pizza[row][col] == 'A':
                        return True

            return False

        @cache
        def helper(row_start=0, row_end=m-1, col_start=0, col_end=n-1, k=k) -> int:
            if k == 1:
                return 1 if hasApple(row_start, row_end, col_start, col_end) else 0
            
            combinations = 0
            for row in range(row_start, row_end):
                if hasApple(row_start, row, col_start, col_end):
                    combinations += helper(row+1, row_end, col_start, col_end, k-1)
            
            for col in range(col_start, col_end):
                if hasApple(row_start, row_end, col_start, col):
                    combinations += helper(row_start, row_end, col+1, col_end, k-1)
            
            return combinations % int(1E9 + 7)
        
        return helper()
