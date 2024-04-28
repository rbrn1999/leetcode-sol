# link: https://leetcode.com/problems/make-a-square-with-the-same-color/

class Solution:
    def canMakeSquare(self, grid: list[list[str]]) -> bool:
        n = 3
        w = 0
        b = 0
        
        for r in range(2):
            for c in range(2):
                if grid[r][c] == 'B':
                    b += 1
                else:
                    w += 1
        
        if b >= 3 or w >= 3:
            return True

        w = 0
        b = 0
        
        for r in range(2):
            for c in range(1, 3):
                if grid[r][c] == 'B':
                    b += 1
                else:
                    w += 1
        
        if b >= 3 or w >= 3:
            return True

        w = 0
        b = 0
        
        for r in range(1, 3):
            for c in range(2):
                if grid[r][c] == 'B':
                    b += 1
                else:
                    w += 1
        
        if b >= 3 or w >= 3:
            return True

        w = 0
        b = 0
        
        for r in range(1, 3):
            for c in range(1, 3):
                if grid[r][c] == 'B':
                    b += 1
                else:
                    w += 1
        
        if b >= 3 or w >= 3:
            return True
        
        return False
        
        
        