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