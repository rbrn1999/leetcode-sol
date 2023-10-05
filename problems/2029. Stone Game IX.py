# link: https://leetcode.com/problems/stone-game-ix/

class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:
        count = [0] * 3
        for stone in stones:
            count[stone % 3] += 1
        
        if count[0] % 2 == 0:
            return count[1] > 0 and count[2] > 0
        else:
            return abs(count[1] - count[2]) > 2