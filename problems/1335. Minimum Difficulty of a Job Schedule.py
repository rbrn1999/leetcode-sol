# link: https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

from functools import cache
class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        n = len(jobDifficulty)
        @cache
        def helper(curInd, curMax, remain):
            # all remaining jobs belong to the last day
            if remain == 1:
                return max(jobDifficulty[curInd:])
            
            curMax = max(curMax, jobDifficulty[curInd])
            # if no 2nd job to distribute for the remaining days
            if n-remain == curInd:
                return curMax + sum(jobDifficulty[curInd+1:])
            
            # add to cur day
            sameDay = helper(curInd+1, curMax, remain)
            # go to the next day
            nextDay = curMax + helper(curInd+1, jobDifficulty[curInd+1], remain-1)

            return min(sameDay, nextDay)

        return helper(0, 0, d) if n >= d else -1

# Bottom-Up (optimal space)
from functools import cache
class Solution:
    def minDifficulty(self, jobDifficulty: list[int], d: int) -> int:
        @cache
        def helper(i: int, max_val: int, d: int) -> int:
            if d < 0 or i < len(jobDifficulty) and d == 0:
                return float('inf')
            if i == len(jobDifficulty):
                return 0 if d == 0 else float('inf')

            max_val = max(max_val, jobDifficulty[i])
            return min(helper(i+1, max_val, d), max_val + helper(i+1, -float('inf'), d-1))
        
        result = helper(0, -float('inf'), d)
        return result if result < float('inf') else -1