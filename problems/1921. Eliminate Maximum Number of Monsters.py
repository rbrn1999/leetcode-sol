# link: https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        reachTime = sorted([(d//s, d%s) for d, s in zip(dist, speed)], reverse=True)
        curTime = 0
        while reachTime and (reachTime[-1][0] > curTime or \
            reachTime[-1][0] == curTime and reachTime[-1][1] > 0):
            reachTime.pop()
            curTime += 1
        
        return curTime