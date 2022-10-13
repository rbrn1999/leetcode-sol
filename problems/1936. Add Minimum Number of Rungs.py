# link: https://leetcode.com/problems/add-minimum-number-of-rungs/

class Solution:
    def addRungs(self, rungs: list[int], dist: int) -> int:
        rungs.insert(0, 0)
        n = len(rungs)
        i = 1
        result = 0
        while i < n:
            if rungs[i] - rungs[i-1] <= dist:
                i += 1
                continue
            diff = rungs[i] - rungs[i-1]
            result += diff//dist - (1 if (diff % dist==0) else 0) 
            
            height = rungs[i] + (diff % dist)
            while i+j < n and height > rungs[i+j]:
                j += 1
            i += max(1, j)
                
        return result