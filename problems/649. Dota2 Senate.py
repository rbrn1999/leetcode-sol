# link: https://leetcode.com/problems/dota2-senate

from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = senate.count('R')
        d = len(senate) - r

        ban_r = 0
        ban_d = 0
        q = deque(senate)
        while r > 0 and d > 0:
            for _ in range(len(q)):
                c = q.popleft()
                if c == 'R':
                    if ban_r > 0:
                        ban_r -= 1
                    else:
                        ban_d += 1
                        d -= 1
                        q.append(c)
                else:
                    if ban_d > 0:
                        ban_d -= 1
                    else:
                        ban_r += 1
                        r -= 1
                        q.append(c)
        
        return "Dire" if d > 0 else "Radiant"